import socket
s = socket.socket()
host = socket.gethostname()

port = 1010
s.connect((host,port))
dil = s.recv(1024).decode()
print(dil)