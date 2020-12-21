# Assignment 2 - Routing

This assignment is broken into 4 parts + any extra additions (se below) to make a total of 100 The assignment

is due on the **9 th** of November 2020.

Code should be upload in a zip file along with a README.txt which details any fancy little extras you added to
the assignment.

The purpose of this assignment is to build a pseudo router connected to a network graph.

## Part 1 - Setup and calculating cost of a packet [30 Marks]

Create a file called router.py and inside it create two classes. One class called Router. This class will
represent a router. A router has a name and a connection to a network graph.

And another class called Graph. A graph is made up of nodes and edges. Each node represents a router. Each
edge represents a link between two routers and has an associated cost. This is an integer which is used to
represent the travel time between two routers.

The Graph class should have the following function

```
add_router(self, router_name, cost) - Adds an edge to the network graph from the current
Router (name) to another router router name, cost is an integer representing the distance between
the two routers.
```
The Router class should have the following function

```
get_path(self, router_name): - This method performs Dijkstra's Algorithm to return the distance
and the path between the router and the router specified by router_name. When called this function
sohuld output:
```
```
The start and end node
```
```
The path taken
```
```
The cost
```
An example of the output would be

```
> graph = Graph()
> graph.add_router("a", "b", 7 )
> graph.add_router("a", "c", 9 )
> graph.add_router("a", "f", 14 )
> graph.add_router("b", "c", 10 )
> graph.add_router("b", "d", 15 )
> graph.add_router("c", "d", 11 )
> graph.add_router("c", "f", 2 )
> graph.add_router("d", "e", 6 )
> graph.add_router("e", "f", 9 )
> router = Router("a", graph)
```

```
> router.get_path("f")
Start: a
End: f
Path: a->c->f
Cost: 11
```
Note: The arrows are made using the join method

```
> a = [ 1 , 2 , 3 , 4 , 5 ]
> "->".join(a)
1 -> 2 -> 3 -> 4 -> 5
>
```
## Part 2 - Print routing table for router [30 Marks]

Add a function to the Router class called print_routing_table(). This function should generate and print
out the routing table for the router. The routing table is a table which details the routers most effecient path
to **every** other node on the network and the associated cost. A sample of the output would be:

```
> router.print_routing_table()
from to cost path
0 a b 7 a->b
1 a e 26 a->c->d->e
2 a c 9 a->c
3 a f 11 a->c->f
4 a d 20 a->c->d
>
```
Note: In the above example, I created the table as a pandas dataframe using the from_dict method and just
called print on the output.

## Part 3 - Remove router [10 Marks]

From time to time routers on the network can go down. If a router goes down this means that

```
our path to the router is dead
any other paths we had that passed through that router must be recalculated.
```
Create a function called remove_router(router_name). router_name is the name of the router to mark as
dead. The program should recalculate all necessary routes and produce a new routing table.

```
> router.remove_router(c)
from to cost path
0 a e 28 a->b->d->e
1 a b 7 a->b
2 a f 14 a->f
```

```
3 a d 22 a->b->d
>
```
Note: To remove a router, the node (and all associated edges) must be removed from the graph.

## Part 4 - Multiple Routers [20 Marks]

Up to this point we have a single router and a graph. The purpose of this part is to construct multiple routers
each producing a different routing table. Using a shared graph. Each router has their own calculated routing
table. If a router is marked as dead, all routers connected to the graph should produce new routing tables.

```
> graph = Graph()
> graph.add_router("a", "b", 7 )
....
graph setup
....
> graph.add_router("e", "f", 9 )
> router = Router("a", graph)
> router_two = Router("b", graph)
> router.print_routing_table()
from to cost path
0 a b 7 a->b
1 a e 26 a->c->d->e
2 a c 9 a->c
3 a f 11 a->c->f
4 a d 20 a->c->d
> router_two.print_routing_table()
from to cost path
0 b d 15 b->d
1 b e 21 b->d->e
2 b f 12 b->c->f
3 b c 10 b->c
4 b a 19 b->c->a
> router.remove_router(c)
from to cost path
0 a e 28 a->b->d->e
1 a b 7 a->b
2 a f 14 a->f
3 a d 22 a->b->d
> router_two.print_routing_table()
from to cost path
0 b e 21 b->d->e
1 b d 15 b->d
2 b f 30 b->d->e->f
3 b a 0
```
Note: see how when we removed the router "c" router_two now has no path to router "a".

## Nice little extras [10 Marks]


The remaining 10 marks are reserved for extra functionality for those who go above and beyond. Some
examples of extra functionality may be:

```
A GUI (e.g tkinter )
Full help documentation (e.g. pydoc)
Completed unit tests e.g. pyunit
Visualising the network graph e.g. NetworkX
Multithreading the Routers
```
This is by no means an exhaustive list and if you think of something suitable, go ahead and try it out!

# Important notes / tips/ tricks etc..

```
Graphs in python
A graph is a very common data structure with multiple ways of representing it. See here , here and here
you are free to choose whatever implementation you feel is best.
```
## Extra libraries / functions / classes etc..

You may use extra libraries to help with iterating over lists e.g. itertools, and you can use NetworkX to _visualise_
a graph. but you sohuld not use libraries to construct or manage the grpah, this should be your own
implementation. In terms of your own custom classes, functions etc.. You can create as many as you like, as
long as the classes and functions specified above are implemented.

## One more hint


# Marking scheme

Here is a breakdown of marks for each task by component

```
Component Marks
Setup and calculating cost of a packet 30
Print routing table for router 30
Remove router 10
Multiple Routers 20
Additions (UI, help pages, flags etc...) 10
Total 100
```
## Code assessment Rubric

The marks for each individual task will be assessed using the following rubric

```
Assessment Quality
```

**Assessment Quality**

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
>40% Weak or no evidence of basic knowledge of networking concepts and constructs, codedoes not run, insufficient for progression.


