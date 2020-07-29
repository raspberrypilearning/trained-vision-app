## Get the game starter code

Your completed model now needs to be inserted into a desktop Python application to make a working game. A simple version of 'rock, paper, scissors' has been written for you to use, as you are focusing on the machnine learning aspects of the project. However, there is a lot of room to improve the game's interface. If you want to learn about how to do this, check out the [Getting started with GUIs](https://projects.raspberrypi.org/en/projects/getting-started-with-guis) project.

First, you need to download the starter file for the project.

--- task ---

Download the [starter zip file](http://rpf.io/trained-vision-app-go) and unzip it somewhere you'll remember on your computer. If you can't think of a location, just put it on your desktop. This isn't the best place to keep things in the long term, but it's fine when you're working on them.

--- /task ---

Next, you need to install the libraries you're going to be using in this project. For this, you'll need to use the **command line interace** (CLI) — a program for controlling your computer by typing text commands into a window. The command line interface is called 'command prompt' in Windows and 'terminal' in Mac OS and Linux. If you don't know how to find the path to a directory and navigate to it in your CLI, take a look at the 'Get the starter files' step of [project 4](#).

--- task ---

Open your CLI and navigate to the directory you just unzipped using the `cd` command.

--- /task ---

Now that you have a CLI in the right directory, you can start running Python commands with the files in it. 

The command to install the libraries you need uses **pip**, a tool for fetching Python code written by other people from the internet and setting it up so you can use it in your projects. It's important to use pip to install libraries rather than just downloading them: some libraries need other libraries to work (these libraries are called their **dependencies**) and pip will automatically install those too.

Conveniently, pip can be given a list of all the librarys a project needs, and told to install them all at once. These are usually included in a file called `requirements.txt`, as they have been with the starter code provided here.

--- task ---

Run this command on your CLI to install the libraries you'll need. It may take a while to run, as it will have to download the libraries from the internet and some of them are quite large.

```bash
pip install requirements.txt 
```

--- /task ---

Now that you have the libraries you need installed, it's time to open the Python file you'll be using to do this project. If you've never written Python on your computer before, you may need to install a programmer's text editor first.

--- collapse ---
---
title: Click here if you need to install a programmer's text editor
---

WHICH EDITOR ARE WE RECOMMENDING THESE DAYS? BRACKETS?

--- /collapse ---

--- task ---

Open your text editor and use it to open the `project.py` file in the directory you've been working in.

--- /task ---

There's a lot of code already provided for you, but it's all for creating the game and capturing an image from your computer's camera. First, run the program as it is to get an idea of how the game will work.

--- task ---

Go back to your CLI window and type the following command to run the program. Remember it, as you'll need to run the program several times.

### If you're using Windows or Linux

```
python project.py
```

Then press the return key to run the program.

### If you're using a Mac
```
python3 project.py
```

Then press the return key to run the program.

--- /task ---

It may take a moment, but when your program runs you should see something like the image below.

![](images/app_start.png)

Now that you have the game running, it's time to connect your model to it.