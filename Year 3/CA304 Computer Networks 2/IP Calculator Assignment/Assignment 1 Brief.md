# Assignment 1 - IP Calcuator

This assignment is broken into 4 parts + any extra additions (se below) to make a total of 100 The assignment

is due on the **26 th** of October 2020. As we cannot be sure of the status of Loop, submission details will be
sent out this week pending any updates from ISS.

Your code can span multiple files if you wish. The assignments ask you to create some functions, however you
may have to create your own _helper_ functions to complete them.

## Part 1 - IP Address Calculator [30 Marks]

Create a file called ip_calculator.py and inside it create a function called get_class_stats(ip_addr)
where ip_addr is a string representing an IPv4 address in decimal dot notation e.g. ("136.206.18.7")

When called the function should output:

```
The class of the address
The number of networks for the class of the address
The number of hosts for the class of the address
The first IP address for the class
The last IP address for the class
```
```
> get_class_stats("136.206.18.7")
Class: B
Network: 16384
Host: 65536
First address: 128.0.0.
Last address: 191.255.255.
```
For Class D and Class E addresses the program should output N/A for the number of networks and hosts.

```
> get_class_stats("224.192.16.5")
Class: D
Network: N/A
Host: N/A
First address: 224.0.0.
Last address: 239.255.255.
>
```
## Part 2 - Subnet (Class C) calculator [30 Marks]

Within the file ip_calculator.py create another function called get_subnet_stats(ip_addr,
subnet_mask) which takes in a **class C** ip address in decimal dot notation as a string and a subnet mask. It
should then print out:


```
The ip address in CIDR notation e.g. 192.168.10.0/
The number of subnets on the network
The number of addressable hosts per subnet
The valid subnets
The broadcast address of each subnet
The valid hosts on each subnet
```
```
> get_subnet_stats("192.168.10.0","255.255.255.192")
Address: 192.168.10.0/ 26
Subnets: 4
Addressable hosts per subnet: 62
Valid subnets: ["192.168.10.0", "192.168.10.64", "192.168.10.128",
"192.168.10.192"]
Broadcast addresses:
["192.168.10.63","192.168.10.127","192.168.10.191","192.168.10.255"]
First addresses:
["192.168.10.1","192.168.10.65","192.168.10.129","192.168.10.193"]
Last addresses:
["192.168.10.62","192.168.10.126","192.168.10.190","192.168.10.254"]
>
```
## Part 3 - Subnet (Class B) calculator [10 Marks]

Extend the functiionality of the get_subnet_stats function above to accomodate subnets from class B
addresses.

```
> get_subnet_stats("172.16.0.0","255.255.192.0")
Address: 172.16.0.0/ 18
Subnets: 4
Addressable hosts per subnet: 16382
Valid subnets: ["172.16.0.0", "172.16.64.0", "172.16.128.0", "172.16.192.0"]
Broadcast addresses:
["172.16.63.255","172.16.127.255","172.16.191.255","172.16.255.255"]
First addresses: ["172.16.0.1","172.16.64.1","172.16.128.1","172.16.192.1"]
Last addresses:
["172.16.63.254","172.16.127.254","172.16.191.254","172.16.255.254"]
>
```
## Part 4 - Supernet calculator [20 Marks]

Create a function called get_supernet_stats which takes in a list of contigous **class C** addresses which are
to become a supernet. The function should then print out

```
The network using CIDR notation e.g. 205.100.0.0/22 (the format is the first network number, folloed
by a / followed by the number of network bits).
The network mask
```

```
> get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0"])
Address: 205.100.0.0/ 22
Network Mask: 255.255.252.
>
```
## Nice little extras [10 Marks]

The remaining 10 marks are reserved for extra functionality for those who go above and beyond. Some
examples of extra functionality may be:

```
A GUI (e.g tkinter )
Full help documentation (e.g. pydoc)
Completed unit tests e.g. pyunit
Calculating subnets for Class A addresses
Supernetting Class B addresses
```
This is by no means an exhaustive list and if you think of something suitable, go ahead and try it out!

# Important notes / tips/ tricks etc..

```
How to test your code/logic
To test each part of your code works as intended I would recommend using an online IP address
calculator e.g http://jodies.de/ipcalc.
```
This assignment asks you to create some functions, however you may have to create some more functions
yourselves to accomplish these tasks. In addition I would recommend brushing up on your list comprehension
skills in python, there will be a lot of iterating over arrays.

## Classes, networks and hosts

I would recommend hard coding the number of network and host bits. A suitable data structure like a dict
would work for this (however you are free to choose whatever implementation suits you).

```
>classes={
'A':{
'network_bits': 7 ,
'host_bits': 24
},
'B':{
'network_bits': 14 ,
'host_bits': 16
},
'C':{
'network_bits': 21 ,
'host_bits': 8
},
'D':{
'network_bits':'N/A',
```

```
'host_bits':'N/A'
},
'E':{
'network_bits':'N/A',
'host_bits':'N/A'
},
}
> classes['A']['network_bits']
7
>
```
## Powers of n

For some formulas you will have to calculate xy. To do this in python we can use the power operator x**y (it's
literally the multiplication symbol twice).

### > 2 ** 2

### 4

### > 2 ** 3

### 8

### >

## Helper functions

Here are some helper functions to aid you on your quest, feel free to copy/paste.

```
Converting decimal dot into binary
```
```
def to_binary_string(ip_addr):
"""
Converts an ip address represented as a string in decimal dot
```

```
notation into a list of
four binary strings
each representing one byte of the address
:param ip_addr: The ip address as a string in decimal dot notation
e.g. "132.206.19.7"
:return: An array of four binary strings each representing one byte
of ip_addr e.g.
['10000100', '11001110', '00010011', '00000111']
"""
#split into array of four ["136","206","19","9"]
byte_split = ip_addr.split(".")
# convert each number into a int, format it as binary, turn it back into
a stirng
# and return it as an array, isn't python great!
return ['{0:08b}'.format(int(x)) for x in byte_split]
```
```
Converting a list of binary strings back into decimal dot notation
```
```
def to_decimal_dot(ip_addr_list):
"""
Take in an array of four strings represting the bytes of an ip address
and convert it back into decimal dot notation
:param ip_addr_list: An array of four binary strings each
representing one byte of ip_addr e.g. ['10000100', '11001110',
'00010011', '00000111']
:return: The ip address as a string in decimal dot notation e.g.
'132.206.19.7'
"""
# for each string in the list
# use str(int(x,2)) to convert it into a decimal number
# and then turn that number into a string e.g. '10000100' -> '132'
# put all converted numbers into a list ["132","206","19","7"]
# call ".".join on the list to merge them into a string separated by "."
return ".".join([str(int(x, 2 )) for x in ip_addr_list])
```
# Marking scheme

Here is a breakdown of marks for each task by component

```
Component Marks
```
```
Which Class Calculator 30
```
```
Subnet Class C addresses 30
Subnet Class B addresses 10
```
```
Supernet Calculator 20
```
```
Additions (UI, help pages, flags etc...) 10
```

```
Component Marks
```
```
Total 100
```
## Code assessment Rubric

The marks for each individual task will be assessed using the following rubric

```
Assessment Quality
```
### 80%+

```
Demonstrates exceptional comprehension and engages with the lecture slides and
evidence of reading beyond the literature outlined in the module. Code runs without
errors, variables are well named, code is well formatted and commented.
```
### 70%-79%

```
Shows sound knowledge and clear understanding of networking concepts and constructs.
Has engaged with the lecture slides. Personal learning experience is supported by
references to the slides. Code is well formatted and commented.
```
### 60%-69%

```
Shows evidence of relevant and sound knowledge and understanding of programming
concepts and constructs Has partially engaged with the lecture slides. Personal learning
experience somewhat is partially supported by relevant references to the lecture material.
Code runs without errors however is poorly formatted, some comments are provided.
Variables are poorly named.
```
### 50%-59%

```
Reproduces basic knowledge of networking concepts and constructs covered in the
module. Some engagement with the lecture material. Code is not well formatted, poor
variable naming, little or no comments.
```
### 40%-49%

```
Signs of emerging knowledge of basic networking concepts and constructs. Some
engagement with the lecture content. Weak or little attempt to support with references to
the lecture material. Code partially runs. Code is not well formatted. No comments and
poor variable naming.
```
### >40%

```
Weak or no evidence of basic knowledge of networking concepts and constructs, code
does not run, insufficient for progression.
```

