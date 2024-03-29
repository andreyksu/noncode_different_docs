;##############################################################################
;#	Программа мигания светодиодами.
;#	Простая обычная программа. 
;#	2а светодиода. Мигаем поочередно (один зажигаем, второй гасим) здесь используется таймер для мигания. Таймер 1.
;#	Добавил сюда Таймер 2 - для генерации импульсов на катушку. Время накопления 2мс. Ну и частота оборотов двигателя.
;#	800об/мин => 800/60=13.3об/с
;#
;#	Пусть частота процессора 1.000.000Гц. Далее раота с пределителем для 8битного таймера 2.
;#	1МГц/256=3906; 3906/255=15.31;		15.31*60=918 - Пределитель в 256 - соответствует 918 оборотам двигателя.		1с/15.31=62.32 - длительность 1го периода т.е. за какое время при таком пределителе частоты таймер досчитает до 255
;#	1МГц/128=7812; 7812/255=30.64;		30.64*60=1838 - Пределитель в 128 - соответствует 1838 оборотам двигателя.		1с/30.64=32.64
;#	1МГц/64=15625; 15628/255=61.27;		61.27*60=3676 - Пределитель в 64 - соответствует 3676 оборотам двигателя.		1с/61.27=16.32
;#	1МГц/32=31250; 31250/255=122.55;	122.55*60=7353 - Пределитель в 32 - соответствует 7353 оборотам двигателя.		1с/122.55=8.16 
;#
;#-----------------
;#	Работа с оперативкой. Обмен значениями делаем уже не через Стек а через оперативку.
;#	Резервируем байты в памяти и потом обращаемся к ним.
;#	
;#	
;##############################################################################

;-------------------------------Команды управления
.include "m8Adef.inc"
;-------------------------------Предварительный расчет для времени задержки и скорости вращения двигателя.
;.equ 	XTAL = 1000000

;.equ	count = 255

;.equ 	prescale_1 = 256									;пределитель 110; весь регистр 0b01101 110; 0x6E
;.equ 	amount_per_second_1 = (XTAL/prescale_1)/count		;какое количество раз счетчик с данным пределителем досчитает до 255 за 1сек.
;.equ	time_one_teriod_1 = 1000/amount_per_second_1		;время одного периода ШИМ - т.е. время за которое счетчки досчитает до 255.
;.equ	amount_per_2ms_1 = (count/time_one_teriod_1)*2		;ищем до скольки нужно считать таймеру, чтобы получить 2ms ;15=0x08
;.equ	amount_per_1_5ms_1 = (count/time_one_teriod_1)*1.5
;.equ	amount_per_2_5ms_1 = (count/time_one_teriod_1)*2.5

;.equ 	prescale_2 = 128									;пределитель 101; весь регистр 0b01101 101;  0x6D
;.equ 	amount_per_second_2 = (XTAL/prescale_2)/count
;.equ	time_one_teriod_2 = 1000/amount_per_second_2
;.equ	amount_per_2ms_2 = (count/time_one_teriod_2)*2		;30=0x21
;.equ	amount_per_1_5ms_2 = (count/time_one_teriod_2)*1.5
;.equ	amount_per_2_5ms_2 = (count/time_one_teriod_2)*2.5

;.equ 	prescale_3 = 64										;пределитель 100; весь регистр 0b01101 100; 0x6C
;.equ 	amount_per_second_3 = (XTAL/prescale_3)/count
;.equ	time_one_teriod_3 = 1000/amount_per_second_3
;.equ	amount_per_2ms_3 = (count/time_one_teriod_3)*2		;61=0x3D
;.equ	amount_per_1_5ms_3 = (count/time_one_teriod_3)*1.5
;.equ	amount_per_2_5ms_3 = (count/time_one_teriod_3)*2.5

;.equ 	prescale_4 = 32										;пределитель 011; весь регистр 0b01101 011; 0x6B
;.equ 	amount_per_second_4 = (XTAL/prescale_4)/count
;.equ	time_one_teriod_4 = 1000/amount_per_second_4
;.equ	amount_per_2ms_4 = (count/time_one_teriod_4)*2		;122=0x7A
;.equ	amount_per_1_5ms_4 = (count/time_one_teriod_4)*1.5
;.equ	amount_per_2_5ms_4 = (count/time_one_teriod_4)*2.5

.list

.def	temp=R16
.def	temp1=R17				;for Swap; Так же используется для вывода в порт для зажигания свето-диода.
.def	temp2=R18				;for Swap
.def	FuseReg=R19				;Здесь будем хранить предохранитель. Этот предохранитель будет нас держать мужде 0 и 3 т.е. между делителями 32 и 256

;-------------------------------
;RAM
;-------------------------------
.DSEG							; Сегмент ОЗУ

;.ORG SRAM_START+100			; можно сделать так, тогда наши байты/переменные будут находиться на 100 байт после начала ОЗУ
;.org	0x60					; 0x60 - это начало ОЗУ (собственно в файле "m8Adef.inc" есть строчка: SRAM_START = 0x0060)
Var1:	.byte	1				; В озу выделили по байту.
Fuse1:	.byte	1				; Здесь будем хранить предохранитель. Этот предохранитель будет нас держать между 0 и 3 т.е. между делителями 32 и 256

;-------------------------------
;Начало программного кода
;-------------------------------
.CSEG

;-------------------------------
;Таблица векторов прерываний
;В mega8 все прерывания имеют одинаковый приоритет. В случае одновременного возникновения нескольких прерываний первым будет обрабатываться прерывание с меньшим номером вектора.
;-------------------------------
.ORG 0x0000
	RJMP 	Inital_Restart
.ORG INT0addr
	RJMP	INT_0_interrapt
.ORG INT1addr
	RJMP	INT_1_interrapt
.ORG OC2addr
	RETI
.ORG OVF2addr
	RETI
.ORG ICP1addr
	RETI
.ORG OC1Aaddr				;equal A; У 16ти разрядного счетчика ТС1 - два 16ти разрядных регистра сравнений/совпадений. По сути 4ре 8и разрядных регистра. Пары РЕГИСТРОВ с именами OCR1A(OCR1AL и OCR1AH) и OCR1B(OCR1BL и OCR1BH). Прерывание по ним будет когда включен режим CTC
	RJMP	Equal_A_Reg_int
.ORG OC1Baddr
	RETI		
.ORG OVF1addr
	RETI
.ORG OVF0addr
	RETI
.ORG SPIaddr
	RETI
.ORG URXCaddr
	RETI
.ORG UDREaddr
	RETI
.ORG UTXCaddr
	RETI
.ORG ADCCaddr
	RETI
.ORG ERDYaddr
	RETI
.ORG ACIaddr
	RETI
.ORG TWIaddr
	RETI
.ORG SPMRaddr
	RETI

;-------------------------------
;Инициализация стека
;-------------------------------
Inital_Restart:
	SEI

	LDI		temp, low(RAMEND)	;load immediate
	OUT		SPL, temp			;SPL - stack pointer low; SPH - high

	LDI		temp, high(RAMEND)
	OUT		SPH, temp			;SPH - high

;-------------------------------
;Разрешаем прерывания для таймера
;-------------------------------

	LDI		temp, 0x10			;разврешили перрывание от таймера (прерывание произойдет когда значение регистров OCR1A/OCR1B и TCNT1 совпадет. OCR1A/OCR1B - регистры сравенения, TCNT1 - счетный регистр.  Устанавливается битом OCIE1A в регистре TIMSK.
	OUT		TIMSK, temp			;TIFR1 в этом регистре можно узнать какое прерывание произошло. Т.е. видимо его можно не только записать но и прочитать.
								;Так же используется Timer2 - но он в режиме ШИМ - а в этом режим прерываний от него нет.

;-------------------------------
;Настраиваем сам таймер. Настройка состоит из 2х регистров. TCCR1A и TCCR1B и TCCR1С (здесь используется A и B - но здесь было бы логично испльзовать L и H так как это по сути это один файл).
;-------------------------------

	LDI		temp, 0x00			;Здесь в рамках этой задачи нас ничего не интересует. Оставляем все выключеным. Здесь настойка касается ШИМ - нам это не интересно в этом таймере. Оставляем как есть.
	OUT		TCCR1A, temp

	LDI		temp, 0x0d		;0x0d здесь задаем через биты  CS12, CS11, CS10 задём пределитель 1024
	OUT		TCCR1B, temp
;-------------------------------
;Устанавливаем регистры сравнения OCR1A(OCR1AH и OCR1AL). На самом деле их два таких регистра. Есть еще OCR1B. И можно их обоих задать, если есть задача. И прерывание будет идти от них двоих. Может быть удобно.
;-------------------------------
	LDI		temp, 0x07			;Пусть частота 1.000.000ГЦ имеем 1.000.000/1024=976 => 0x03DO это будет секунда; 2сек ~1953  =>0x07 A1
	OUT		OCR1AH, temp

	LDI		temp, 0xA1
	OUT		OCR1AL, temp
;-------------------------------
;Настройка таймера Timer2 - здесь настройка на ШИМ + пределитель
;Установка по умолчанию для пределителя 256 (0b0110 1110; 0x6E) и 2ms - для счета.
;-------------------------------
	LDI		temp, 0<<FOC2 | 1<<WGM20 | 1<<COM21 | 0<<COM20 | 1<<WGM21 | 1<<CS22 | 1<<CS21 | 0<<CS20
	OUT		TCCR2, temp

	LDI		temp, 0x0F
	OUT		OCR2, temp
;-------------------------------
;Настройка прерываний по внешним входам.
;-------------------------------
	LDI		temp, 1<<ISC11 | 0<<ISC10 | 1<<ISC01 | 0<<ISC00		;прерывания будут срабатывать при спадающем фронте. (При прерывании по постоянному нулю или постоянной единице - нужно быть внимательно - на входе всегда 0 или 1 и может быть зависание - постоянно будет прерывание)
	OUT		MCUCR, temp

	LDI		temp, 1<<INT1 | 1<<INT0								;разрешаем прерывания от INT1 и от INT0;
	OUT		GIMSK, temp											;GIFR - это регистр флагов, с них можно считать от куда пришло прерывание. При входе в подпрограмму обработки прерывания автоматов сбарсывается в 0.
;-------------------------------
;Инициализация портов
;-------------------------------
	LDI		temp, 0x0B			;PortB НУЛЕВОЙ и ПЕРВЫЙ на выход для светодиодов. Еще ТРЕТИЙ на выход т.к. OC2 на нем. Остальные на вход.
	OUT		DDRB, temp			;0x0b=0000 1011

	LDI		temp, 0xf8			;Все что на вход, подтягиваем внутренним реистором. На НУЛЕВОМ и ПЕРВОМ порту, гасим светодиоды 
	OUT		PORTB, temp			;0хf8=1111 1000
;-------------------------------
	LDI		temp, 0x00			;Все на вход на порту D.
	OUT		DDRD, temp			;На этом порту сидит INT0 и INT1

	LDI		temp, 0xff			;Все на выход подтягивающй резистор
	OUT		PORTD, temp			;0хf8=1111 1111
;-------------------------------							
	LDI		temp1, 0xfe			;Устанавливаем изначальные значения значения для Swap; 0xfe = 1111 1110
	LDI		temp2, 0xfd			;0xfd = 1111 1101

	LDI		FuseReg, 0x01		;Предохранитель устанавливаем в 0

	LDI		ZL, low(coefficients*2)		;Записываем первый байт массива коэффициентов.
	LDI		ZH, high(coefficients*2)	;Записываем второй байт массива коэффициентов.
;-------------------------------
;Разрешаем глобальные прерывания
;-------------------------------
	SEI
;-------------------------------
;Уходим на основной цикл
;-------------------------------
	RJMP	main

;-------------------------------
;Набор прерываний
;-------------------------------
Equal_A_Reg_int:
	PUSH	temp
	IN		temp, SREG			;Речь про эти три строчки.
	PUSH	temp				;Вот здесь нельзя использовать подпрограмму типа Save - по аналогии Exit - причина банальная. Если использовать RJMP для перехода и возврата - то в Save для RJMP - как то для каждого возврата нужно знать куда вернуться (В Equal_A_Reg_int или INT_0_interrapt) - Т.е. от куда выполнен прыжек.
								;По этой причине стоит использовать RCALL - но RCALL сама записывает в стек текущий адрес - адрес перехода к Save - соответственно когда будем возвращаться, по RET возникают проблемы с адресацией (нужно подумать - но по факту из Save возвращался в Save).

	RCALL	swp					;для этих целей нужно использовать не rjmp а rcall или call
	RJMP	Exit

INT_0_interrapt:
	PUSH	temp
	IN		temp, SREG
	PUSH	temp

	CPI		FuseReg, 4
	BREQ	Exit

	INC		FuseReg

	LPM		YL, Z+
	LPM		YH, Z+

	OUT		OCR2, YL
	OUT		TCCR2, YH

	RJMP	Exit

INT_1_interrapt:
	PUSH	temp
	IN		temp, SREG
	PUSH	temp

	CPI		FuseReg, 1
	BREQ	Exit

	DEC		FuseReg

	SUBI	ZL, 4
	LPM		YL, Z+
	LPM		YH, Z+

	OUT		OCR2, YL
	OUT		TCCR2, YH

	RJMP	Exit


;-------------------------------
;Набор подпрограмм
;-------------------------------

swp:							;подпрограмма обмена значений между регистрами. Через OЗУ.
	STS		Var1, temp1
	MOV		temp1, temp2
	LDS		temp2, Var1
	RET

Exit:
	POP		temp
	OUT		SREG, temp
	POP		temp
	RETI					;здесь нельзя использовать rjmp - для возврата к main иначе флаг I так и не поднимется

;-------------------------------
;Основной цилк программы
;-------------------------------
main:
	out		PORTB, temp1
	rjmp	main

;-------------------------------
;Хранение коэффициентов
;-------------------------------

coefficients:	
;	.dw		0x6E0F, 0x6D21, 0x6C3D, 0x6B7A
	.dw		0x6E08, 0x6D10, 0x6C1E, 0x6B3D
;Осталась проблема связанная с перемещением вперед и назад (предохранитель перевел к 1 так как если 0 - то ошибка) - но проблема так и осталась.