;##############################################################################
;#	Программа мигания светодиодами.
;#	Простая обычная программа. 
;#	2а светодиода. Мигаем поочередно (один зажигаем, второй гасим). Мигание идет поочередно, задержка чере вычетание в трех циклах.
;#	-------------------------------
;#	Целенаправленно не делал через стек. Просто для примера сдела обмен через регистры.
;#	Переход к подпрограммам выполняется целенаправленно через rjmp а не через rcall и ret
;#	Вообще подсчет таким образом ооочень неточный
;##############################################################################

;-------------------------------Команды управления
.include "m8Adef.inc"
.list

.def	temp=R16
;-------------------------------Временный регистр, через который будем менять местами значения см. метку swp
.def	tempR1=R0			
.def	tempR2=R1
;-------------------------------Переменные, которые будем использовать в циклах, для задержки
.def	first=R18			
.def	second=R19
.def	third=R20

;-------------------------------Начало программного кода
.equ	const=0xff				;значение из которого будет производиться вычитание в циклах задержки

;-------------------------------Начало программного кода
.cseg

.org	0

;-------------------------------Инициализация стека
	
	ldi		temp, low(RAMEND)	;load immediate
	out		SPL, temp			;SPL - stack pointer low; SPH - high

	ldi		temp, high(RAMEND)
	out		SPH, temp			;SPH - high

;-------------------------------Инициализация портов

	ldi		temp, 0x03			;PortB НУЛЕВОЙ и ПЕРВЫЙ на выход. Остальные на вход.
	out		DDRB, temp

	ldi		temp, 0xfc			;Все что на вход, подтягиваем внутренним реистором. На НУЛЕВОМ и ПЕРВОМ порту, гасим светодиоды fc=1111 1100.
	out		PORTB, temp

;-------------------------------Инициализация временных переменных
	ldi		temp, 0xfd
	mov		tempR1, temp
	ldi		temp, 0xfe
	mov		tempR2, temp
;-------------------------------Уходим на основной цикл
	rjmp 	main

;-------------------------------Основной цилк программы
firstLoop:						;(n*4)-1
	dec		first				;subi	temp, 0x01
	breq	secondLoop + 2		;проверили, а не ноль ли в флаге. Если 0 то выходим из вложенного цикла.
	rjmp	firstLoop			;сюда приходим, если до 0 не дошли, и тем самым уходем на новую итерацию.

secondLoop:						;n*{8+[(n*4)-1]}-1
	ldi		first, const		
	rjmp	firstLoop
	clz
	dec		second
	breq	sleepp + 2
	rjmp	secondLoop

sleepp:							;n*<8+[n*{8+[(n*4)-1]}-1]>-1
	ldi		second, const		;n*(8+(n*(8+((n*4)-1))-1))-1 - сравнил на 10 и на 20 в переменной const - вроде совпадает расчетные и то что выдала программа
	rjmp	secondLoop
	clz
	dec		third
	breq	main
	rjmp	sleepp

swp:							;подпрограмма обмена значений между регистрами
	mov		temp, tempR1
	mov 	tempR1, tempR2
	mov		tempR2, temp
	rjmp	main + 1

main:	
	rjmp 	swp					;для этих целей нужно использовать не rjmp а rcall или call и возврат уже будет через ret
	out		PORTB, temp
;-------------------------------
	ldi		third, const
	rjmp	sleepp				;при подсчете тактов не забываем прибавить эти два такта ;для этих целей нужно использовать не rjmp а rcall или call. А возврат использовать ret. Оставил целенаправленно для примера.
;-------------------------------
	rjmp	main
