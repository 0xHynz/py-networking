import socket,sys
from contextlib import suppress


     

host = socket.gethostname()
port = int(sys.argv[1])
print(f"server started at {host}:{port}")

def stringed(data):
    return str(data,'utf-8')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   # AF_INET = Family Address
   # SOCK_STREAM = jenis socket untuk TCP


   s.bind((host,port)) # karena menggunakan AF_INET harus tuple, (host,port)
                       # host harus ipv4, sedang port bilangan bulat dari 1-65535
   s.listen() # menerima koneksi dengan mendengarkan/menunggu

   conn, addr = s.accept() #data of family address
   print (s.accept)

   with conn:
       print (f"Got connection from {addr}")
       while True:
           data = conn.recv(5)
           if not data:
              break
           if stringed(data) == "exit":
              conn.send(b'exit')
           else:
              conn.sendall(data)

