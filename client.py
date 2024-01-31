import socket 
from threading import Thread

import setuptools


SERVER = None
PORT = None
IP_ADDRESS = None

clients = {}


def setup():
    print("\n")


    global SERVER
    global PORT
    global IP_ADDRESS


    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
                                                           

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((IP_ADDRESS, PORT))


SERVER.listen(10)
print("\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS !!!! ") 
print("\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS !!!! ") 
