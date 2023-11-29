import socket
import os

serverName = '127.0.0.1'
serverPort = 1200

serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverS.bind((serverName,serverPort))
print('Serveri eshte startuar ne IP adresen: %d' % (serverName, serverPort))