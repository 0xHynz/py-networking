
# UDP-SCANNER
#-*- coding: utf-8 -*-

import socket
import sys
import string
import random
import concurrent.futures #multiprocessing library

# main method
def main(HOST,PORT,BUFFER=1024):
    #create socket
    try:
       with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
          # create rabdom data
          alphabet = string.ascii_letters
          msg = "".join([random.choice(alphabet) for msg in range(6)])
          s.sendto(msg.encode(),(HOST, PORT))

          s.settimeout(2)

          r = s.recvfrom(BUFFER)
          print (r[0].decode(),f"{r[1][0]} | PORT {r[1][1]}")

    except TimeoutError:
       pass


def runWithThread():
   HOST = sys.argv[1]
   with concurrent.futures.ThreadPoolExecutor(max_workers=5) as cc:
        results = [cc.submit(main,HOST,PORT) for PORT in [z for z in range(0,1000)]]
        for check in results:
            print (check.result())


if __name__=="__main__":
   runWithThread()
