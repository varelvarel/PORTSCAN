#!usr/bin/python
import os
import sys
import socket

os.system ("apt-get install figlet")
os.system ("clear")
os.system ("figlet FUXK696GHOST")

def scan():
    server = raw_input("Masukkan alamat server: ")
    ip = socket.gethostbyname(server)
    print "Alamat IP server pada:",ip
    for port in range(1,1025):
        konek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        hasil = konek.connect_ex((ip,port))
        if hasil == 0:
            print "Port terbuka pada: [{}]".format(port)
        konek.close()
           

scan()