import socket


HOST,PORT,BUFFER = socket.gethostname(),int(1337),1024

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT));print("[*] server listening, at {}:{}".format(HOST,PORT))

while True:
    data =  s.recvfrom(BUFFER)
    if data:
       print("[+] message from client: {}".format(data[0].decode()))
       s.sendto(f"Connected to server, Hello {data[1][0]}:{data[1][1]}".encode(),data[1])
    
