����������� ������� ����������� (��) �� ����������� ������� (��):
CERTIFICATE_PATH=/etc/app-server-certificates/identity.cer
HOSTNAME=
SERVER_IP_ADDRESS=
CENTRAL_SERVER_USER=
CENTRAL_SERVER_USER_PWD=
CENTRAL_SERVER=
UPDATE= # update or ""
       curl \
           -F "uuid=$GEN_UUID" \
           -F "file=@$CERTIFICATE_PATH" \
           -F "ip=$SERVER_IP_ADDRESS" \
           -F "description=$HOSTNAME" \
           -F "active=on" \
           --user $CENTRAL_SERVER_USER:$CENTRAL_SERVER_USER_PWD http://$CENTRAL_SERVER:8081/msa-configuration/$UPDATE 

�������� �� �� �� ��:
CENTRAL_SERVER=
CENTRAL_SERVER_USER=
CENTRAL_SERVER_USER_PWD=
        curl -H 'Content-type: application/xml' -d @addres.xml --user $CENTRAL_SERVER_USER:$CENTRAL_SERVER_USER_PWD http://$CENTRAL_SERVER:8081/akws/send   
��� ���� addres.xml ������ ���������� � ����� ������� �������.

��� ���� ����� ������������ ������ ��� ������ � curl, ��������� � ������� ������� --proxy <SERVER_IP>. �.�. ������� ����� ��������� �������� ���:
CENTRAL_SERVER=
CENTRAL_SERVER_USER=
CENTRAL_SERVER_USER_PWD=
        curl --proxy 127.0.0.1:8090 -H 'Content-type: application/xml' -d @addres.xml --user $CENTRAL_SERVER_USER:$CENTRAL_SERVER_USER_PWD http://$CENTRAL_SERVER:8081/akws/send  