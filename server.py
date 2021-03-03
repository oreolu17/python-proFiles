import socket

s = socket.socket()
host = socket.gethostname()
print(host)

port = 1010
s.bind((host, port))
s.listen(5)
while True:
    client,address = s.accept()
    response = 'client wassup'
    client.send(response.encode())
    s.close()

