#!/usr/bin/env python3
import socket,sys

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}
""".format(HOST=HOST)


def connect_socket(addr):
    (family, socketype, proto, cannoname, sockaddr) = addr
    print(family)
    print(socketype)
    print(proto)
    print("asdfasf")
    print(cannoname)
    
    try:
        print("entered the try")
        s = socket.socket(family,socketype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        full_data = b""
        while True:
            print("entered the while loop")
            print(s.recv(BUFFER_SIZE))
            data = s.recv(BUFFER_SIZE)
            print(data)
            if not data:
               break
            full_data += data
        print(full_data)
        
    except:
        print("DID NOT CONNECT")
        pass

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)

if __name__ == "__main__":
    main()
