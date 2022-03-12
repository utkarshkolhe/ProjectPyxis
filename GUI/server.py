import socket
import threading

HEADER=64 
PORT=5050

SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn,addr):
    print(f'[NEW CONNECTION] {addr}connected')
    connected=True
    while connected:
        msg_len=conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len=int(msg_len)
            msg=conn.recv(msg_len).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False

            print(f'[{addr}] {msg}')
            conn.send('Message received'.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f'[LISTENING] Server is listening {SERVER}')
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[ACTIVE Connections]{threading.activeCount()-1}')



print('[Starting] server is starting...')
start()
