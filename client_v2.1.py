import socket, threading, time

from cezar_coder.decode_cezar import decode_cezar
from cezar_coder.encode_cezar import encode_cezar


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)

                decrypt = " "
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += decode_cezar(i)

                print(decrypt)

                time.sleep(0.2)
        except:
            pass



shutdown = False
join = False

server_ip = ("192.168.3.45", 4040)
client_ip = ('192.168.3.50', 0)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(client_ip)

client_name = input("Name: ")

recvThread = threading.Thread(target=receving, args=("RecvThread", socket))
recvThread.start()

while not shutdown:
    if not join:

        socket.sendto(("[" + client_name + "] => join chat ").encode("utf-8"), server_ip)
        join = True
    else:
        try:
            message = input()

            message = encode_cezar(message)

            if message != "":
                socket.sendto(("[" + client_name + "] :: " + message).encode("utf-8"), server_ip)
                print("sent")
            time.sleep(0.2)
        except:
            socket.sendto(("[" + client_name + "] <= left chat ").encode("utf-8"), server_ip)
            shutdown = True

recvThread.join()
socket.close()
