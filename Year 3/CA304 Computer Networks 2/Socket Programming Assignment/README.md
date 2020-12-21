# Assignment 3 - Socket Programming

This assignment is broken into 4 parts + any extra additions (se below) to make a total of 100

The purpose of this assignment is to demonstrate your knowledge of networking concepts and socket
programmign to create your own discord-like application.

## Submission

```
The assignment is due on the 29 th of November 2020.
A part of this submissions is a short video (not more than 5 minutes) showing the working applicaion.
Code should be upload in a zip file along with a README.txt which details any fancy little extras you
added to the assignment.
In the readme.txt file you sohuld include the link to view the video you can host it on youtube, google
drive , or anywhere else you feel. As long as I can view the video when I click on the link I don't mind.
```
## Part 1 - Server [30 Marks]

The first part of this assignmetn is to construct a working server which can recieve text messages. Server code
should be written in a file called server.py.

Its usage is server.py <ip_address>, <port>

A server needs to inputs an ip address to run off and a port to listen on. When the server is started it
should take these parameters in as command line arguments.

```
ip address is a string
port is an int
```
If there are no command-line arugments specified it should default to

```
ip address - "0.0.0.0"
port - 8080
```
A sample output is provided below

```
> python server.py 127.0.0.1 8000
Server started on 127.0.0.1:
```
The server should contain

```
a list of clients connected to the server (and the clients display names)
a broadcast method.
```
When the server recieves data from a client, it should use the broadacst method to forward on that data to
all other connected clients.

## Part 2 - Client [30 Marks]


## [ ]

Write a file called client.py which is used to connect to the server. The client takes in three command line
arguments: your username and the servers ip address and port.

Once connected it should wait for the user to type in text. When the user hits enter, the text should be sent to
the server and broadcast to all other connected clients. If a message is recieved from the server it should be
displayed to the user.

Here is a sample output

```
> python client.py Michael 127.0.0.1 8000
Connected to 127.0.0.1:
```
```
Hello
Paul: Hi Mike!
```
## Part 3 - Two way chat [10 Marks]

At this stage you sohuld have enough to have a simple chatroom working. Demonstrate this by recording a
short video.

In the video show the following

```
Start the server
Connect client 1
Connect client 2
Send a message from client 1 to client 2
Send a message from client 2 to client 1
```
You do not have to speak or go on camera, simply start a zoom recording (or other recording software), and
record your screen showing this functionality. Upload it to a platform of your choice (e.g. google drive,
youtube etc..) and place a link to the file in the readme.txt

## Part 4 - Chatrooms [20 Marks]

Finally extend the server and client files to add int eh ability to have multiple chatrooms.

A client will now have to enter their

```
name
the ip address of the server
the port of the server
The chatroom name
```
If no chatroom of that name exists on the server, one sohuld be created. Now when a client connects they can
send/recieve message for that chatroom only.

Record a short video demonstrating this functionality showing:

```
The server starting
Client 1 entering chatroom A
```

```
Client 2 entering chatroom A
Client 1 & two talking
Client 3 entering chatroom B
Client 4 entering chatroom B
Clients 3 & 4 talking
```
## Nice little extras [10 Marks]

The remaining 10 marks are reserved for extra functionality for those who go above and beyond. Some
examples of extra functionality may be:

```
A GUI (e.g tkinter )
Full help documentation (e.g. pydoc)
Completed unit tests e.g. pyunit
Dockerize the server
```
This is by no means an exhaustive list and if you think of something suitable, go ahead and try it out!

# Important notes / tips/ tricks etc..

### A note on chat apps

This assignment is very general in it's specficiation. That is because there are multiple ways in which it can be
implemented and I am interested in seeing which one is right for you. Some may go full OO and have class
defitions, others may simply list functions and loops.

Some of you may opt for a multithreaded approach where each client spaws a separate thread on the server
and others may opt to work more iteratively. There is no right or wrong answer here, the only requirement is
to build a working apoplication using sockets and networking.

That being said, here are a few guides on the subject:

```
https://medium.com/python-in-plain-english/build-a-chatroom-app-with-python-458fc435025a
https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac
https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
https://towardsdatascience.com/build-a-simple-real-life-chat-app-with-python-a3ce8aebccb
https://www.geeksforgeeks.org/simple-chat-room-using-python/
```
### Command line arguments in python

I would recommend looking at the guide here to see how to read command-line arguments in python. (it's
not too hard).

### Running a python file vs libraries

It is good practice to run your _main_ python code under the following heading

#### .....


```
# class definitions, functions, imports and libraries
.....
```
```
if __name__ == "__main__":
# code I want to run
```
If you do not do this, if you ever need to import the file into another project, when the import statement is
read, all code outside of that if block will run.

## One more hint

# Marking scheme

Here is a breakdown of marks for each task by component

```
Component Marks
Server Setup 30
Client Setup 30
Two way chat 10
Chatrooms 20
Additions (UI, help pages, flags etc...) 10
Total 100
```
## Code assessment Rubric

The marks for each individual task will be assessed using the following rubric

```
Assessment Quality
```
#### 80%+

```
Demonstrates exceptional comprehension and engages with the lecture slides and
evidence of reading beyond the literature outlined in the module. Code runs without
errors, variables are well named, code is well formatted and commented.
```
#### 70%-79%

```
Shows sound knowledge and clear understanding of networking concepts and constructs.
Has engaged with the lecture slides. Personal learning experience is supported by
references to the slides. Code is well formatted and commented.
```
#### 60%-69%

```
Shows evidence of relevant and sound knowledge and understanding of programming
concepts and constructs Has partially engaged with the lecture slides. Personal learning
experience somewhat is partially supported by relevant references to the lecture material.
Code runs without errors however is poorly formatted, some comments are provided.
Variables are poorly named.
```

```
Assessment Quality
```
#### 50%-59%

```
Reproduces basic knowledge of networking concepts and constructs covered in the
module. Some engagement with the lecture material. Code is not well formatted, poor
variable naming, little or no comments.
```
#### 40%-49%

```
Signs of emerging knowledge of basic networking concepts and constructs. Some
engagement with the lecture content. Weak or little attempt to support with references to
the lecture material. Code partially runs. Code is not well formatted. No comments and
poor variable naming.
```
```
>40% Weak or no evidence of basic knowledge of networking concepts and constructs, codedoes not run, insufficient for progression.
```
Good Luck!


