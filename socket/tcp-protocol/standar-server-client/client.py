import socket
import sys
HOST, PORT = socket.gethostname(),int(sys.argv[1])


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
     s.connect((HOST,PORT))
     while True:
        msg = bytes(str(input('message: ')), 'utf-8')
        s.sendall(msg)
        data = s.recv(5)

        if data == b'exit':
           s.close()
           sys.exit('bye!')

        print("Received: ",data)
