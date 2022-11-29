.include "m8def.inc"

; Start macro.inc ===============================================================================================================================================
								
;= End macro.inc  ===============================================================================================================================================
 
 
; RAM ===========================================================================================================================================================
		.DSEG
; FLASH =========================================================================================================================================================
		.CSEG

.ORG 0x000
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
.ORG OC1Aaddr
	RETI
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


Inital_Restart:
		LDI		R16,Low(RAMEND)
		OUT		SPL,R16

		LDI		R16,High(RAMEND)
		OUT		SPH,R16

		SEI							; ��������� ���������� ����������
		LDI		R17, (1<<RXCIE)		; ��������� ���������� �� ������ �����.
		OUT		UCSRB, R17

		RJMP	MainLoop

MainLoop:
		LDI		R16, 3
		SBRS 	R16, 3				; ���� 3�� ��� 1 � R16 �� ������������� ����� �������. SBRC - ���������� �� ��� 0_��. ����������� ������� SBIC/SBIS �� ��� ��������� ���������. �� ��� ������ 1f ���������.									
		RCALL	None				; �� ��� ��� � ��� 3�� 0 �� �� �������� �� �������
									; � ����� � ��� ANDI	R16,1<<2 - �.�. ����������� ��������� ����� 00000100 �.�. & � ���� ������� 0 ��������, ��� � ���� �������� � R16 ��� 0, �� ���� �������� ��� z � ������� �������� BREQ.
		LDI		R17, 5
CPP:	CP		R16, R17			; ������������ ��������� �� R16 �������� R17. ��������� ������������ ������ ��� �������� �� ��������. ���� �������� Z �� ���� �� �����.
		BREQ	Plus
		RJMP MainLoop

None:
		NOP
		RET
		

Plus:
		INC		R16
		RJMP 	CPP				
									;INC 	Rd 	Increment 				Rd = Rd + 1 		Z,N,V 	
									;DEC 	Rd 	Decrement 				Rd = Rd - 1  		Z,N,V 	
									;TST 	Rd 	Test for Zero or Minus 	Rd = Rd AND Rd  	Z,N,V 	
									;CLR 	Rd 	Clear Register 			Rd = Rd XOR Rd		Z,N,V 	
									;SER 	Rd 	Set Register 			Rd = $FF 			None

; EEPROM ==================================================
			.ESEG			; ������� EEPROM
