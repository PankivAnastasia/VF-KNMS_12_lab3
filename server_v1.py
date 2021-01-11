import socket, time

port = 4040

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))

shutdown = False
print("[ Server Started ]")

while not shutdown:
    try:
        (data, addr) = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)

        time_now = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + time_now + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        shutdown = True

s.close()

