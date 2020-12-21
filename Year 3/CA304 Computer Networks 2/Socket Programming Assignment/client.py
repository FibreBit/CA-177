#!/usr/bin/env python3

import threading
import socket
import argparse
import os
import sys
import tkinter as tk


class Send(threading.Thread):

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name

    def run(self):

        while True:
            print('{}: '.format(self.name), end='')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

            # Type 'QUIT' to leave the chatroom
            if message == 'QUIT':
                self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
                break
            
            # Send message to server for broadcasting
            else:
                self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
        
        print('\nLeaving the chat...')
        self.sock.close()
        os._exit(0)


class Receive(threading.Thread):

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name
        self.messages = None

    def run(self):

        while True:
            message = self.sock.recv(1024).decode('ascii')

            if message:

                if self.messages:
                    self.messages.insert(tk.END, message)
                    print('\r{}\n{}: '.format(message, self.name), end = '')
                
                else:
                    # Thread has started, but client GUI is not yet ready
                    print('\r{}\n{}: '.format(message, self.name), end = '')
            
            else:
                # Server has closed the socket, exit the program
                print('\nOh no, we have lost connection to the server!')
                print('\nQuitting...')
                self.sock.close()
                os._exit(0)

class Client:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name
        self.messages = None
    
    def start(self):

        print('Trying to connect to {}:{}...'.format(self.host, self.port))
        self.sock.connect((self.host, self.port))
        print('Successfully connected to {}:{}'.format(self.host, self.port))
        
        print()
        print('Welcome, {}! Getting ready to send and receive messages...'.format(self.name))

        # Create send and receive threads
        send = Send(self.sock, self.name)
        receive = Receive(self.sock, self.name)

        # Start send and receive threads
        send.start()
        receive.start()

        self.sock.sendall('Server: {} has joined the chat. Say hi!'.format(self.name).encode('ascii'))
        print("\rAll set! Leave the chatroom anytime by typing 'QUIT'\n")
        print('{}: '.format(self.name), end = '')

        return receive

    def send(self, text_input):

        message = text_input.get()
        text_input.delete(0, tk.END)
        self.messages.insert(tk.END, '{}: {}'.format(self.name, message))
        # Type 'QUIT' to leave the chatroom
        if message == 'QUIT':
            self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
            print('\nQuitting...')
            self.sock.close()
            os._exit(0)
        # Send message to server for broadcasting
        else:
            self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))


def main(host, port, name):
    loginscreen.destroy()
    client = Client(host, port, name)
    receive = client.start()

    window = tk.Tk()
    window.title('Chatroom')
    window.configure(background='#0F0268')
    frm_messages = tk.Frame(master=window)
    scrollbar = tk.Scrollbar(master=frm_messages)
    messages = tk.Listbox(
        master=frm_messages, 
        yscrollcommand=scrollbar.set,
        fg="white"
    )
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
    messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    messages.configure(background='#0F0268')
    client.messages = messages
    receive.messages = messages

    frm_messages.grid(row=0, column=0, columnspan=2, sticky="nsew")

    frm_entry = tk.Frame(master=window)
    text_input = tk.Entry(master=frm_entry)
    text_input.pack(fill=tk.BOTH, expand=True)
    text_input.bind("<Return>", lambda x: client.send(text_input))
    text_input.insert(0, "")

    btn_send = tk.Button(window,text='Send', font=("Segoe UI Bold", 20), command=lambda: client.send(text_input))

    frm_entry.grid(row=1, column=0, padx=10, sticky="ew")
    btn_send.grid(row=1, column=1, pady=10, sticky="ew")

    window.rowconfigure(0, minsize=500, weight=1)
    window.rowconfigure(1, minsize=50, weight=0)
    window.columnconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=200, weight=0)

    window.mainloop()


def take_details():
    main(hostinput.get(), int(portinput.get()), username.get())

if __name__ == '__main__':
        
    #if len(sys.argv) > 1:
    #    host = sys.argv[1]
    #    port = int(sys.argv[2])
    ##    user = sys.argv[3]
    #    print(host, port, user)
     #   main(host, port, user)
    loginscreen = tk.Tk()
    loginscreen.title("Python Chatroom")
    loginscreen.geometry('450x600+720+200')
    loginscreen.configure(background='#0F0268')

    pixelVirtual = tk.PhotoImage(width=1, height=1)
    tk.Label(loginscreen, bg="#C82323", image=pixelVirtual, width=303, height=88, compound="c").place(x=72, y=48)
    tk.Label(loginscreen, text="Chatroom", font=("Segoe UI Bold", 38), bg="#FF1717", fg="white", image=pixelVirtual, width=293, height=78, compound="c").place(x=76, y=52)
    tk.Label(loginscreen, text="Username:", bg="#0F0268", fg="white", image=pixelVirtual, width=174, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=47,y=184)
    tk.Label(loginscreen, text="Host:", bg="#0F0268", fg="white", image=pixelVirtual, width=174, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=13,y=230)
    tk.Label(loginscreen, text="Port:", bg="#0F0268", fg="white", image=pixelVirtual, width=174, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=13,y=276)
    tk.Button(loginscreen, font=("Segoe UI Bold", 19), image=pixelVirtual, borderwidth=5, height=68, width=201, text="Enter chatroom", compound="c", command=take_details).place(x=121, y=450)

    username = tk.Entry(loginscreen, width=30)
    username.place(x=240,y=200)
    hostinput = tk.Entry(loginscreen, width=30)
    hostinput.place(x=240,y=245)
    portinput = tk.Entry(loginscreen, width=30)
    portinput.place(x=240,y=290)
    loginscreen.mainloop()
    #else:
       # print("There has been an error. Please enter the host address and port\n of the chatroom you wish to join in the arguments (python client.py '127.0.0.1' 8080)")
    # Create and start server thread
