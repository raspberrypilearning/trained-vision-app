## Set up your game

Your completed model now needs to be inserted into a desktop Python application to make a working game. A simple version of rock, paper, scissors, where the computer will use the player's guess to cheat, has been written for you to use. You are focusing on the machine learning aspects of the project. However, there is a lot of room to improve the game's interface. If you want to learn about how to do this, check out the [Getting started with GUIs project](https://projects.raspberrypi.org/en/projects/getting-started-with-guis). You can also make changes to the computer's method of choosing whether to play 'rock', 'paper', or 'scissors', if you want to create a game where the player always wins, or where the computer chooses at random.

First, you need to download and set up the starter file for the project.

--- collapse ---
---
title: For Windows
---

--- task ---
Download the [starter zip file](http://rpf.io/trained-vision-app-go) and unzip it somewhere you'll remember on your computer. If you can't think of a location, just put it on your desktop. This isn't the best place to keep things in the long term, but it's fine when you're working on them.
--- /task ---

Next, you need to install the libraries you will use in this project. For this, you'll need to use the **command line interface** (CLI) — a program that controls your computer by typing text commands into a window. The command line interface is called 'command prompt' in Windows.

In the CLI, you don't access files by clicking to open them, or the directories (folders) they live in. You need to know the **path** to the file. It's like a set of directions, either from where you are currently located on the computer — called a **relative path** — or from the root of the computer's hard drive — called an **absolute path**. You'll need to find the path to the directory you've just unzipped for this next step.

#### Finding the path to a directory on Windows

The easiest way to find the path to a directory you know in Windows is to open the folder in Windows Explorer, as you would normally, and click into the navigation bar at the top of the window. The full path for the folder should become visible and you can then copy it.

![The Windows Explorer navigation bar for a folder, with the path highlighted.](images/windows_path.png)

--- task ---

In the CLI, navigate to the directory you just unzipped by entering the following command, and replace `[directory_path]` with the path to your directory.

```batch
cd [directory_path]
```

--- /task ---

Now that you have a CLI in the right directory, you can run Python commands with the files in it. 

The command to install the libraries you need uses **pip**, a tool to fetch Python code written by other people from the internet and set it up so you can use it in your projects. It's important to use pip to install libraries rather than just downloading them: some libraries need other libraries to work (these libraries are called their **dependencies**) and pip will automatically install those too.

Conveniently, pip can be given a list of all the libraries a project needs, and told to install them all at once. These are usually included in a file called `requirements.txt`, as they have been with the starter code provided here.

--- task ---

Run this command on your CLI to install the libraries you'll need. It may take a while to run, as it will have to download the libraries from the internet and some of them are quite large.

```bash
pip install requirements.txt 
```

--- /task ---

--- /collapse ---


--- collapse ---
---
title: For macOS
---

To install the libraries and other files you're going to be using in this project, you'll need to use the **command line interface** (CLI) — a program that controls your computer by typing text commands into a window. The command line interface is called 'terminal' in macOS.

In the CLI, you don't access files by clicking to open them, or the directories (folders) they live in. You need to know the **path** to the file. It's like a set of directions, either from where you are currently located on the computer — called a **relative path** — or from the root of the computer's hard drive — called an **absolute** path. You need to find the path to the directory you've just unzipped for this next step.

There are also some special paths, that are sorts of shortcuts in the system, and you're going to be using one of them, called the **home directory**. Every user on a computer gets their own home directory to store their files, and it is accessed using a special character called the tilde (`~`).

--- task ---

Open the CLI on your computer and type the command below in:

```bash
cd ~
```
Now press the Return key.

--- /task ---

You are now located in your home directory, and can install the files needed for this project there. Because this can be a complex process, a program to handle the installation for you has been created. Here are the [details of this program](http://rpf.io/proj-rps), but be aware that it's written in a language called **bash script**, and won't look much like Python.

--- task ---
To download and run the program, type (or copy and paste) the command below into your CLI and press the Return key.

```bash
curl -L http://rpf.io/proj-rps | sudo bash -s $USER
```

--- /task ---

The script may take several minutes, or more, to complete the setup depending on the speed of your computer and your internet connection. Once it has finished, you will have a new directory inside your home directory, called `amazing_image_identifier`. This is the directory you'll work in.

--- task ---

To change directory to the `amazing_image_identifier` directory, type the following command into your CLI and press the Return key.

```bash
cd amazing_image_identifier
```

--- /task ---

--- /collapse ---



--- collapse ---
---
title: For Linux (including Raspberry Pi)
---

To install the libraries and other files you'll use in this project, you need to use the **command line interface** (CLI) — a program that controls your computer by typing text commands into a window. The command line interface is called 'terminal' in Linux.

In the CLI, you don't access files by clicking to open them, or the directories (folders) they live in. You need to know the **path** to the file. It's like a set of directions, either from where you are currently located on the computer — called a **relative path** — or from the root of the computer's hard drive — called an **absolute** path. You need to find the path to the directory you've just unzipped for this next step.

There are also some special paths, that are sorts of shortcuts in the system, and you're going to be using one of them, called the **home directory**. Every user on a computer gets their own home directory to store their files, and it is accessed using a special character called the tilde (`~`).

--- task ---

Open the CLI on your computer and type the command below in:

```bash
cd ~
```
Now press the Return key.

--- /task ---

You are now located in your home directory, and can install the files needed for this project there. Because this can be a complex process, a program to handle the installation for you has been created. Here are the [details of this program](http://rpf.io/proj-rps), but be aware that it's written in a language called **bash script**, and won't look much like Python.

--- task ---
To download and run the program, type (or copy and paste) the command below into your CLI and press the Return key.

```bash
curl -L http://rpf.io/proj-rps | sudo bash -s $USER
```

--- /task ---

The script may take several minutes, or more, to complete the setup depending on the speed of your computer and your internet connection. Once it has finished, you will have a new directory inside your home directory, called `rps_by_hand`. This is the directory you'll work in.

--- task ---

To change directory to the `rps_by_hand` directory, type the following command into your CLI and press the Return key.

```bash
cd rps_by_hand
```

--- /task ---

--- /collapse ---

There's a lot of code already provided for you, but it's all to create the game and capture an image from your computer's camera. First, run the program as it is to get an idea of how the game will work.

--- task ---

Go back to your CLI window and type the following command to run the program. Remember it, as you'll need to run the program several times.

### If you're using Windows or Linux

```
python project.py
```

Then press the Return key to run the program.

### If you're using macOS
```
python3 project.py
```

Then press the Return key to run the program.

--- /task ---

It may take a moment, but when your program runs you should see something like the image below.

![White screen with the words 'Ready to play?' at the top of the page and a Play! button at the bottom of the page](images/app_start.png)

Now that you have the game running, it's time to connect your model to it.
