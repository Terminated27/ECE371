from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt

PORT_NUMBER = 5000
SIZE = 1024

# hostName = gethostbyname("AidanEOS")  # adi's laptop hostname
hostName = gethostbyname("192.168.1.10")  # alterra hosting

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key = ""
while True:
    (data, addr) = mySocket.recvfrom(SIZE)
    data = data.decode()
    if data.find("public_key") != -1:  # client has sent their public key\
        ###################################your code goes here#####################################
        # retrieve public key and private key from the received message (message is a string!)
        keys = re.search(
            r"public_key: (\d+) (\d+) private_key: (\d+) (\d+)", data
        )  # use regex to find message of key
        public_key_e = int(keys.group(1))
        public_key_n = int(keys.group(2))  # extract private and public keys
        private_key = (int(keys.group(3)), int(keys.group(4)))
        print("public key is : %d, %d" % (public_key_e, public_key_n))
    else:
        cipher = int(data)
        print(str(cipher) + ":")
        ###################################your code goes here#####################################
        # data_decoded is the decoded character based on the received cipher, calculate it using functions in RSA.py
        data_decoded = decrypt(private_key, cipher)  # decrypt text
        print(data_decoded)
        # python2: print data ,
sys.ext()
# What could I be doing wrong?
