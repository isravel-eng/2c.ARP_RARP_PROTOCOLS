import socket

server = socket.socket()
server.bind(('localhost', 9000))
server.listen(5)

print("RARP Server Waiting...")
client, addr = server.accept()
print("Connected with", addr)

address_table = {
    "6A:08:AA:C2": "192.168.1.100",
    "8A:BC:E3:FA": "192.168.1.99"
}

while True:
    mac = client.recv(1024).decode()

    if not mac:
        break

    ip = address_table.get(mac, "Not Found")
    client.send(ip.encode())
