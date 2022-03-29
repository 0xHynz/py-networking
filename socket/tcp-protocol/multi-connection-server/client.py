import sys
import socket
import types
import selectors

sel = selectors.DefaultSelector()
messages = [b"message 1 from client", b"message 2 from client"]


def start_connections(host,port,num_conns):
    server_addr = (host,port)
    for i in range(0,num_conns):
        connid = i+1
        print(f"starting connection from {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
                connid=connid,
                msg_total=sum(len(m) for m in messages),
                recv_total=0,
                messages=messages.copy(),
                outb=b'',
                )
        sel.register(sock,events,data=data)

def service_connection(key,mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
       recv_data = sock.recv(1024)
       if recv_data:
          print(f"received {recv_data!r} from connection {data.connid}")
          data.recv_total += len(recv_data)
          if not recv_data or data.recv_total == data.msg_total:
             print(f"closing connection from {connid}")
             sel.unregister(sock)
             sock.close()

    if mask & selectors.EVENT_WRITE:
       if not data.outb and data.messages:
          data.outb = data.messages.pop(0)
          if data.outb:
              print(f"sending {data.outb!r} to connection {connid}")
              sent = sock.send(data.outb)
              data.outb = data.outb[sent:]

