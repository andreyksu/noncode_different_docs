;##############################################################################
;#	Программа мигания светодиодами.
;#	Простая обычная программа. 
;#	2а светодиода. Мигаем поочередно (один зажигаем, второй гасим) здесь используется таймер для мигания.
;#-----------------
;#	Работа с оперативкой. Обмен значениями делаем уже не через Стек а через оперативку.
;#	Резервируем байты в памяти и потом обращаемся к ним.
;#	
;#	
;##############################################################################

;-------------------------------Команды управления
.include "m8Adef.inc"
.list

.def	temp=R16
.def	temp1=R17
;-------------------------------RAM
.DSEG							; Сегмент ОЗУ

;.ORG SRAM_START+100			; можно сделать так, тогда наши байты/переменные будут находиться на 100 байт после начала ОЗУ
Var1:	.byte	1				; В озу выделили по байту.
Var2:	.byte	1

;-------------------------------Начало программного кода
.CSEG

;-------------------------------Таблица векторов прерываний
.ORG 0x0000
	RJMP 	Inital_Restart
.ORG INT0addr
	RETI
.ORG INT1addr
	RETI
.ORG OC2addr
	RETI
.ORG OVF2addr
	RETI
.ORG ICP1addr
	RETI
.ORG OC1Aaddr				;equal A; У 16ти разрядного счетчика ТС1 - два 16ти разрядных регистра сравнний/совпадений. По сути 4ре 8и разрядных. Пары РЕГИСТРОВ с именами OCR1A(OCR1AL и OCR1AH) и OCR1B(OCR1BL и OCR1BH). Прерывание по ним будет когда включен режим CTC
	RJMP	Equal_A_Register
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

;-------------------------------Инициализация стека
Inital_Restart:
	
	ldi		temp, low(RAMEND)	;load immediate
	out		SPL, temp			;SPL - stack pointer low; SPH - high

	ldi		temp, high(RAMEND)
	out		SPH, temp			;SPH - high

;-------------------------------Разрешаем глобальные прерывания

;	SEI							;Вероятно - это должно быть не здесь а в конце прямо перед преходом на основной цикл
;-------------------------------Разрешаем прерывания для таймера

	ldi		temp, 0x10			;разврешили перрывание от таймера (прерывание произойдет когда значение регистров OCR1A/OCR1B и TCNT1 совпадет. OCR1A/OCR1B - регистры сравенения, TCNT1 - счетный регистр.  Устанавливается битом OCIE1A в регистре TIMSK.
	out		TIMSK, temp			;TIFR1 в этом регистре можно узнать какое прерывание произошло. Т.е. видимо его можно не только записать но и прочитать.

;-------------------------------Настраиваем сам таймер. Настройка состоит из 2х регистров. TCCR1A и TCCR1B и TCCR1С (здесь используется A и B - но здесь было бы логично испльзовать L и H так как это по сути это один файл).

	ldi		temp, 0x00			;Здесь в рамках этой задачи нас ничего не интересует. Оставляем все выключиным. Здесь связано с ШИМ
	out		TCCR1A, temp

	ldi		temp, 0x0d			;А здесь задаем через биты  CS12, CS11, CS10 задём пределитель 1024
	out		TCCR1B, temp
;-------------------------------Устанавливаем регистры сравнения OCR1A(OCR1AH и OCR1AL). На самом деле их два таких регистра. Есть еще OCR1B. И можно их обоих задать. И прерывание будет идти от них двоих. Может быть удобно.
	ldi		temp, 0x1e			;Пусть частота 4.000.000ГЦ имеем 4.000.000/1024=3906 => т.е. на таймер будет 3906 приходить импульсов в секунду. Т.е. если мы досчитаем до 3906(0x0f42) - то это будет секунда; 2сек ~7812  =>0x1E84
	out		OCR1AH, temp

	ldi		temp, 0x84
	out		OCR1AL, temp
;-------------------------------	
	ldi		temp, 0<<FOC2 | 1<<WGM20 | 1<<COM21 | 0<<COM20 | 1<<WGM21 | 1<<CS22 | 1<<CS21 | 1<<CS20	;исходим из того что частота 16МГц. Делитель берем на 1024 (CS = 111). Делаем Fast PWM (WGM = 11). Ну и (COM = 10) - говорит когда падать к 0 при переполнении или наоборот. Пока считаем.
	out		TCCR2, temp			;0<<FOC2 - разерезрвирован т.е. не используется. 16.000.000/1024 = 15.625 будет приходить тиков в 1сек. Т.к. регистр сравнения 8и разрядный т.е. считаем до 255 то получаем 15,625/255 = 61 раз за 1 скунду таймер подсчитает до конца (т.е. частота будет 61Гц с таймера и длительность подсчета 1с/61=16мс).

	ldi		temp, 0xF7			;записываем в счетный регистр. Для примера сделаем 50% т.е. мы должны досчитать до половины т.е. до 127.
	;ldi	temp, 0x20			;а так 2ms импульса для 16MHz (255/16мс)*2=32 => 0x20
	out		OCR2, temp
;-------------------------------Инициализация портов

	ldi		temp, 0x0B			;PortB НУЛЕВОЙ и ПЕРВЫЙ на выход для светодиодов. Еще третий на выход т.к. OC2 на нем. Остальные на вход.
	out		DDRB, temp

	ldi		temp, 0xf8			;Все что на вход, подтягиваем внутренним реистором. На НУЛЕВОМ и ПЕРВОМ порту, гасим светодиоды fc=1111 0100.
	out		PORTB, temp
				
						
	ldi		temp, 0xfe			;;наверное даже не так. Лучше изначально сорханить их в оперативке. А не держать их в регистрах. Тем более, что далее по коду могу в temp что то положить, используя его для других нужд.
	ldi		temp1, 0xfd
;-------------------------------Уходим на основной цикл
	SEI
	rjmp main


;-------------------------------Основной цилк программы

swp:							;подпрограмма обмена значений между регистрами. Через Стек.
	sts		Var1, temp
	mov		temp, temp1
	lds		temp1, Var1
	ret

Equal_A_Register:
	rcall swp			;для этих целей нужно использовать не rjmp а rcall или call
	reti				;здесь нельзя использовать rjmp - для возврата к main иначе флаг I так и не поднимется.

main:
	out	PORTB, temp
	rjmp main
