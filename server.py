import socket
import os

serverName = '127.0.0.1'
serverPort = 8888

serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverS.bind((serverName,serverPort))
print('Serveri eshte startuar ne IP adresen: %d' % (serverName, serverPort))

serverS.listen(5)
print('Serveri eshte duke pritur per ndonje kerkese')

while True:
    clientS, address = serverS.accept()
    print('---------------------------------------')
    print('Klienti u lidh me %s ne portin %s' % address)

    fjalia = clientS.recv(2048).decode('utf-8')
    print('Kerkesa nga klienti: ' + str(fjalia))

    if fjalia == "LIST_MEMBERS":
        members = ["Anetar1", "Anetar2", "Anetar3"]
        response = "\n".join(members)
        clientS.send(response.encode("utf-8"))

    elif fjalia.startswith("AUTHENTICATE"):
        commands = fjalia.split(":")
        if commands[1] == 'getuar' and commands[2] == '123':
            response = 'AUTH_SUCCESS'
            clientS.send(response.encode('utf-8'))
        else:
            response = 'AUTH_FAILED'
            clientS.send(response.encode('utf-8'))