����������� �������� ������� � ����� ����, ������� ����� ������������ ��� ������.
	netstat -rn  ������ route
	netstat -at - ��� �������� ����� TCP
	netstat -lt - �� TCP ��������������
	netstst -anp - ����� ������������ ����������
	
	nmap -sT -O localhost - ������� ����� ��� ���� ����. �� ���
	lsof -i :<port> ����. ���������� � ������
	ss -p;  ss -l
	ethtool eth0 - ����������

	host <name> - ��������� � ip

	ifstat - ����� ���������� ��� ip
	iftop

time netstat -an|wc -l
time ss -ant|wc -l

������ mac
	ping <ip>
	arp -a

lsof -i:8081

�������� ����������� ��� ����������� ��������� Linux
atop, htop, iftop, iotop (� ����� �� lsof)

������ 5� ����� ��������� ������������ ����������               
	iostat -d -t 5

����� �������� � ���� ������ 10� 60���
	atop -w /tmp/atop.raw 10 60

����� ����������� ��� ��� (������� �  ������)
	echo 1 > /proc/sys/net/ipv4/tcp_tw_recycle

�����������
	������������ ����� ������������ ����������� ������:
		cat /proc/sys/fs/file-max

	��� ��������� "�� ����"
		echo "104854" > /proc/sys/fs/file-max
	
	���������� ������� ���. �������� ������������
	        cat /proc/sys/fs/file-nr
		lsof | wc -l

		lsof | grep <PID> ���������� ���. ������������ �������� ���������� �����������.
		ls -l /proc/<PID>/fd/


���������� �� ���� FreeBSD
	https://habrahabr.ru/sandbox/31010/

��� ��������� ����
	https://romantelychko.com/blog/1300/

��� ���������� ������������������ �� ������ ������ ��� Linux
	bpf - perform a command on an extended BPF map or program