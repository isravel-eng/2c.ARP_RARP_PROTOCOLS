import socket

client = socket.socket()
client.connect(('localhost', 9000))

while True:
    mac = input("Enter MAC Address: ")

    if mac.lower() == 'exit':
        break

    client.send(mac.encode())
    print("Logical Address:", client.recv(1024).decode())
