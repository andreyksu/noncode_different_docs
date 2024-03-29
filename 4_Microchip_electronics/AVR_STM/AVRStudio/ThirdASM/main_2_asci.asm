;##############################################################################
;#	��������� ������� ������������.
;#	������� ������� ���������. 
;#	2� ����������. ������ ���������� (���� ��������, ������ �����) ����� ������������ ������ ��� �������.
;#-----------------
;#	����� ������� ���� ����� ����.
;#	������� � ������������ ���� ����� rcall � ret.
;##############################################################################

;-------------------------------������� ����������
.include "m8Adef.inc"
.list

.def	temp=R16
.def	temp1=R17

;-------------------------------������ ������������ ����
.CSEG

;-------------------------------������� �������� ����������
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
.ORG OC1Aaddr				;equal A; � 16�� ���������� �������� ��1 - ��� 16�� ��������� �������� ��������/����������. �� ���� 4�� 8� ���������. ���� ��������� � ������� OCR1A(OCR1AL � OCR1AH) � OCR1B(OCR1BL � OCR1BH). ���������� �� ��� ����� ����� ������� ����� CTC
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

;-------------------------------������������� �����
Inital_Restart:
	
	ldi		temp, low(RAMEND)	;load immediate
	out		SPL, temp			;SPL - stack pointer low; SPH - high

	ldi		temp, high(RAMEND)
	out		SPH, temp			;SPH - high

;-------------------------------��������� ���������� ����������

	SEI							;��� ������ ���� �� ����� � � ����� ����� ����� �������� �� �������� ����
;-------------------------------��������� ���������� ��� �������

	ldi		temp, 0x10			;���������� ���������� �� ������� (���������� ���������� ����� �������� ��������� OCR1A/OCR1B � TCNT1 ��������. OCR1A/OCR1B - �������� ����������, TCNT1 - ������� �������.  ��������������� ����� OCIE1A � �������� TIMSK.
	out		TIMSK, temp			;TIFR1 � ���� �������� ����� ������ ����� ���������� ���������. �.�. ������ ��� ����� �� ������ �������� �� � ���������.

;-------------------------------����������� ��� ������. ��������� ������� �� 2� ���������. TCCR1A � TCCR1B � TCCR1� (����� ������������ A � B - �� ����� ���� �� ������� ����������� L � H ��� ��� ��� �� ���� ��� ���� ����).

	ldi		temp, 0x00			;����� � ������ ���� ������ ��� ������ �� ����������. ��������� ��� ����������. ����� ������� � ���
	out		TCCR1A, temp

	ldi		temp, 0x0d			;� ����� ������ ����� ����  CS12, CS11, CS10 ���� ����������� 1024
	out		TCCR1B, temp
;-------------------------------������������� �������� ��������� OCR1A(OCR1AH � OCR1AL). �� ����� ���� �� ��� ����� ��������. ���� ��� OCR1B. � ����� �� ����� ������. � ���������� ����� ���� �� ��� �����. ����� ���� ������.
	ldi		temp, 0x1e		;����� ������� 4.000.000�� ����� 4.000.000/1024=3906 => 0x0f42 ��� ����� �������; 2��� ~7812  =>0x1E84
	out		OCR1AH, temp

	ldi		temp, 0x84
	out		OCR1AL, temp
;-------------------------------������������� ������

	ldi		temp, 0x03			;PortB ������� � ������ �� �����. ��������� �� ����.
	out		DDRB, temp

	ldi		temp, 0xfc			;��� ��� �� ����, ����������� ���������� ���������. �� ������� � ������ �����, ����� ���������� fc=1111 1100.
	out		PORTB, temp
				
						
	ldi temp, 0xfe
	ldi temp1, 0xfd
;-------------------------------������ �� �������� ����
	rjmp main


;-------------------------------�������� ���� ���������

swp:							;������������ ������ �������� ����� ����������. ����� ����.
	push	temp
	push 	temp1
	pop		temp
	pop		temp1
	ret

Equal_A_Register:
	nop
	rcall swp			;��� ���� ����� ����� ������������ �� rjmp � rcall ��� call
	reti				;����� ������ ������������ rjmp - ��� �������� � main ����� ���� I ��� � �� ����������.

main:
	nop
	out	PORTB, temp
	rjmp main
