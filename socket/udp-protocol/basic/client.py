import socket


IP,PORT = "127.0.0.1",1337



def client():
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
         BUFFER = 1024
         s.sendto("HELO".encode(),(IP,PORT))
         r = str(s.recvfrom(BUFFER)[0],'utf-8')
         print(f"[?] {r}")
         return s.close()

if __name__=="__main__":
   client()
