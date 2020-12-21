# Assignment 4 - Web applications

This assignment is broken into 4 parts + any extra additions (se below) to make a total of 100

The purpose of this assignment is to demonstrate your knowledge of networking concepts to construct a web
application.

For this assignment we will be using flask. To install flask, open a and type pip install flask.

## Submission

```
The assignment is due on the 18 th of December 2020.
A part of this submissions is a short video (not more than 5 minutes) showing the working applicaion.
Code should be upload in a zip file along with a README.txt which details any fancy little extras you
added to the assignment.
In the readme.txt file you sohuld include the link to view the video you can host it on youtube, google
drive , or anywhere else you feel. As long as I can view the video when I click on the link I don't mind.
```
## Part 1 - Display static page [10 Marks]

The first part of this assignment is to develop a static homepage for your application. When I go to
localhost or 127.0.0.1 on your server it sohuld display this static html homepage. The staic page can be as
in-depth or as minimal as you like.

## Part 2 - Forms and redirection [30 Marks]

A common use of web frameworks is to capture data entered from web forms. For this task create an
endpoint /formtest in your application which will.

```
Display a web form asking a user for their name
The form should be submitted (via POST back to the server)
The user sohuld be redirected to a new page which displays the name of the user using flask templates
```
## Part 3 - Returning JSON [20 Marks]

One common task of web applications is endpoints which do not return html pages, but return JSON data.
Create an endpoint called /allegiances which, when called will read the file allegiances.csv and reutrn it
in the broswer as json.

**N.B.** Make sure the return type for this call is set to return JSON (see important notes)

## Part 4 - REST Calls in HTML [30 Marks]

Another common use of web application is for the client to make a request using javascript and convert the
response into HTML.

Create a new endpoint /allegiancedashboard which when called returns a static html page. The static html
page contains javascript which will make a call to /allegiances. This call will return the JSON data and


construct a html table of the information on the fly.

## Nice little extras [10 Marks]

The remaining 10 marks are reserved for extra functionality for those who go above and beyond. Some
examples of extra functionality may be:

```
HTML properly formatted with CSS (e.g. using bootstrap, materialui).
Reading data from an sqlite database and returning that as JSON.
Full help documentation (e.g. pydoc)
Completed unit tests e.g. pyunit
Dockerize the server
```
This is by no means an exhaustive list and if you think of something suitable, go ahead and try it out!

# Important notes / tips/ tricks etc..

## Javascript Libraries

There s an uncountable amount of javasciprt libraries which offer to make things easier. For this assignment I
would recommend using JQuery only because it offers the get function. This is a really handy way of
requesting data from a remote location.

## converting a dict to json in python

There are any ways to convert a python dictionary into json before it can be returned. One way is to use the
python json library.

Another possible solution is to use Flasks in built json encoder jsonify.


## Response types

When a server sends back a response it also sends back in the header a string denoting what _kind_ of data it is
returning, this is called the Content Type or mimetype. There are many psosible types for JSON the type
should be application/json.

You can see a list of possible content types here

Here is a stackoverflow quesiton asking how to set the content type of a response in Flask

```
flask content-types question
```
# Marking scheme

Here is a breakdown of marks for each task by component

```
Component Marks
Display Static Page 10
Forms and Redirection 30
Returning JSON 20
REST Calls in HTML 30
Additions (help pages, flags etc...) 10
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

```
Assessment Quality
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
```
>40% Weak or no evidence of basic knowledge of networking concepts and constructs, codedoes not run, insufficient for progression.
```
Good Luck!


