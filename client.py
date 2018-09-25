import socket
import sys
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
    print('Arguments are incorrect - Please use script IP address Port Number')
    exit()


def send_message():
    while True:
        message = raw_input()
        sock.send(message)

Port = int(sys.argv[1])
sock.connect(("0.0.0.0", Port))
thread = threading.Thread(target = send_message)
thread.daemon = True
thread.start()






while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data)


sock.close()



