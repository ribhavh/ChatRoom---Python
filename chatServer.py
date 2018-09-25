import socket
import sys
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



if len(sys.argv) != 2:
    print('Arguments are incorrect - Please use script Port Number')
    exit()


port = int(sys.argv[1])

sock.bind(("0.0.0.0", port))

sock.listen(10)

clients = []



def thread(connect, add):
    connect.send("Welcome to this interesting chatroom!")
    while True:
        try:
            message = connection.recv(1024)
            if message:
                print (add[0] + " " + message)
                message_to_send = add[0] + " " + message
                broadcast(message_to_send, connect)
            else:
                remove(connect)
        except ValueError:
            continue

def broadcast(message, connect):
    for client in clients:
        if client != connect:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(client):
    if client in clients:
        clients.remove(client)

while True:
    connection, address = sock.accept()
    clients.append(connection)

    print (address[0] + " has been connected!")

    thread = threading.Thread(target = thread, args = (connection, address))
    thread.daemon = True
    thread.start()

connection.close()
sock.close()