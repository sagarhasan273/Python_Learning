import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), 1234))

s.listen(2)
print("Socket is listening!")
while True:
    clinetsocket, address = s.accept()
    clinetsocket.send(bytes("Welcome to the server!", "utf-8"))
    clinetsocket.close()