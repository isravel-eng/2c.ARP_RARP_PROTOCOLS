import socket

server = socket.socket()
server.bind(('localhost', 8000))
server.listen(5)

print("ARP Server Waiting...")
client, addr = server.accept()
print("Connected with", addr)

address_table = {
    "165.165.80.80": "6A:08:AA:C2",
    "165.165.79.1": "8A:BC:E3:FA"
}

while True:
    ip = client.recv(1024).decode()

    if not ip:
        break

    mac = address_table.get(ip, "Not Found")
    client.send(mac.encode())
