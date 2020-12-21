#!/usr/bin/env python3

import threading
import socket
import argparse
import os
import sys
import tkinter as tk

class Server(threading.Thread):

    def __init__(self, host, port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen(1)
        print('Listening at', sock.getsockname())
        while True:
            # Accept new connection
            sc, sockname = sock.accept()
            print('Accepted a new connection from {} to {}'.format(sc.getpeername(), sc.getsockname()))
            # Create new thread
            server_socket = ServerSocket(sc, sockname, self)
            # Start new thread
            server_socket.start()
            # Add thread to active connections
            self.connections.append(server_socket)
            print('Ready to receive messages from', sc.getpeername())

    def broadcast(self, message, source):
        for connection in self.connections:
            # Send to all connected clients except the source client
            if connection.sockname != source:
                connection.send(message)
    
    def remove_connection(self, connection):
        self.connections.remove(connection)


class ServerSocket(threading.Thread):
    def __init__(self, sc, sockname, server):
        super().__init__()
        self.sc = sc
        self.sockname = sockname
        self.server = server
    
    def run(self):
        while True:
            message = self.sc.recv(1024).decode('ascii')
            if message:
                print('{} says {!r}'.format(self.sockname, message))
                self.server.broadcast(message, self.sockname)
            else:
                # Client has closed the socket, exit the thread
                print('{} has closed the connection'.format(self.sockname))
                self.sc.close()
                server.remove_connection(self)
                return
    
    def send(self, message):
        self.sc.sendall(message.encode('ascii'))



def take_details():
    server = Server(hostinput.get(), int(portinput.get()))
    server.start()

def close_server():
    print('Closing all connections...')
    print('Shutting down the server...')
    os._exit(0)

if __name__ == '__main__':
    #if len(sys.argv) > 1:
      #  host = sys.argv[1]
      #  port = int(sys.argv[2])
      #  server = Server(host, port)
      #  server.start()
    # Create and start server thread
    #else:
      #  host = '0.0.0.0'
      #  port = 8080
       # server = Server(host, port)
       # server.start()
    serversetup = tk.Tk()
    serversetup.title("Server")
    serversetup.geometry('450x600+720+200')
    serversetup.configure(background='#0F0268')

    pixelVirtual = tk.PhotoImage(width=1, height=1)
    tk.Label(serversetup, bg="#C82323", image=pixelVirtual, width=303, height=88, compound="c").place(x=72, y=48)
    tk.Label(serversetup, text="Create Server", font=("Segoe UI Bold", 34), bg="#FF1717", fg="white", image=pixelVirtual, width=293, height=78, compound="c").place(x=76, y=52)
    tk.Label(serversetup, text="Host:", bg="#0F0268", fg="white", image=pixelVirtual, width=174, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=13,y=230)
    tk.Label(serversetup, text="Port:", bg="#0F0268", fg="white", image=pixelVirtual, width=174, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=13,y=276)
    
    hostinput = tk.Entry(serversetup, width=30)
    hostinput.place(x=240,y=245)
    tk.Button(serversetup, font=("Segoe UI Bold", 19), image=pixelVirtual, borderwidth=5, height=68, width=201, text="Launch Server", compound="c", command=take_details).place(x=121, y=350)
    tk.Button(serversetup, font=("Segoe UI Bold", 19), image=pixelVirtual, borderwidth=5, height=68, width=201, text="Close Server", compound="c", command=close_server).place(x=121, y=450)
    portinput = tk.Entry(serversetup, width=30)
    portinput.place(x=240,y=290)
    serversetup.mainloop()


    