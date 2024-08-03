import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 8
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

msg_list = []


def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg_list.append(msg)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

            print(f"{addr}: {msg}")
            for message in msg_list:
                conn.send(message.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print("[STARTING] server is starting...")
start()