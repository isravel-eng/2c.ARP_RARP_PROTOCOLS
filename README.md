# 2c.SIMULATING ARP / RARP PROTOCOLS

## AIM
To write Python programs for simulating ARP and RARP protocols using TCP socket programming.

---

# ARP (Address Resolution Protocol)

## Algorithm

### Client Side
1. Start the program.
2. Create a socket connection.
3. Connect with the ARP server.
4. Enter the IP address.
5. Send the IP address to the server.
6. Receive the corresponding MAC address.
7. Display the MAC address.

### Server Side
1. Start the program.
2. Create a socket and wait for client connection.
3. Maintain a table of IP and MAC addresses.
4. Receive the IP address from the client.
5. Search for the corresponding MAC address.
6. Send the MAC address to the client.

---

## ARP Server Program

```python
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
```

---

## ARP Client Program

```python
import socket

client = socket.socket()
client.connect(('localhost', 8000))

while True:
    ip = input("Enter Logical Address: ")

    if ip.lower() == 'exit':
        break

    client.send(ip.encode())
    print("MAC Address:", client.recv(1024).decode())
```

---

## Sample Output - ARP

### Server

```text
ARP Server Waiting...
Connected with ('127.0.0.1', 54321)
```
<img width="602" height="86" alt="image" src="https://github.com/user-attachments/assets/0e797a0a-831d-4f15-913f-d0be56e3d9b6" />



### Client

```text
Enter Logical Address: 165.165.80.80
MAC Address: 6A:08:AA:C2

Enter Logical Address: 165.165.79.1
MAC Address: 8A:BC:E3:FA
```
<img width="655" height="111" alt="image" src="https://github.com/user-attachments/assets/8b1594a2-fe24-4610-94bd-856de8f5042e" />

---

# RARP (Reverse Address Resolution Protocol)

## Algorithm

### Client Side
1. Start the program.
2. Create a socket connection.
3. Connect with the RARP server.
4. Enter the MAC address.
5. Send the MAC address to the server.
6. Receive the corresponding IP address.
7. Display the logical address.

### Server Side
1. Start the program.
2. Create a socket and wait for client connection.
3. Maintain a table of MAC and IP addresses.
4. Receive the MAC address from the client.
5. Search for the corresponding IP address.
6. Send the IP address to the client.

---

## RARP Server Program

```python
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
```

---

## RARP Client Program

```python
import socket

client = socket.socket()
client.connect(('localhost', 9000))

while True:
    mac = input("Enter MAC Address: ")

    if mac.lower() == 'exit':
        break

    client.send(mac.encode())
    print("Logical Address:", client.recv(1024).decode())
```

---

## Sample Output - RARP

### Server

```text
RARP Server Waiting...
Connected with ('127.0.0.1', 54322)
```
<img width="468" height="88" alt="image" src="https://github.com/user-attachments/assets/7622c1bd-f09b-45cd-a1cb-7f5cdb683f82" />


### Client

```text
Enter MAC Address: 6A:08:AA:C2
Logical Address: 192.168.1.100

Enter MAC Address: 8A:BC:E3:FA
Logical Address: 192.168.1.99
```
<img width="524" height="115" alt="image" src="https://github.com/user-attachments/assets/fbd29ac0-aedd-45d8-92ae-47e547754a81" />

---

## Result
Thus, the Python programs for simulating ARP and RARP protocols using TCP sockets were successfully executed.
