import socket

client = socket.socket()
client.connect(('localhost', 8000))

while True:
    ip = input("Enter Logical Address: ")

    if ip.lower() == 'exit':
        break

    client.send(ip.encode())
    print("MAC Address:", client.recv(1024).decode())
