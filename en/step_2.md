## Get set up

If you've never written Python on your computer before, you may need to install a programmer's text editor first.

--- collapse ---
---
title: Install a programmer's text editor
---
There are lots of different text editors; they are usually free, so most programmers try different editors before they find their favourite one. As you become more experienced, you should try different editors to see if you find one that you enjoy more than the others. For now, try one of the following:

+ If you do all your text-based programming in Python, use [Thonny](https://thonny.org/). It has a lot of helpful features that work with Python to help you program correctly, and to investigate if your program does not work as expected.

+ If you use a few different languages — for example, if you create web pages with HTML and CSS as well as Python applications — then [Visual Studio Code](https://code.visualstudio.com/) is a good choice. It offers less help for any particular language, but supports a lot of different languages.

--- /collapse ---

For this project, you also need some library code. This is code written by other people that you can use so you don’t have to build all the parts of a program on your own. Python comes with lots of libraries, but you also need some extra ones. Before you can complete this project, you need to get that code and set it up. Select your operating system below to find out how to set up your library code. 

--- collapse ---
---
title: Windows
---

The command to install the libraries you need uses `pip`, a tool to fetch Python code written by other people from the internet and set up so you can use it in your projects. It is important to use `pip` to install libraries and not to just download them. This is because some libraries need other libraries to work (these libraries are called their **dependencies**) and `pip` automatically installs those too.

Conveniently, `pip` can be given a list of all the libraries a project needs, and told to install them all at once. These are usually included in a file called `requirements.txt`.

--- task ---
Download the [requirements.txt file for this project](#) to somewhere memorable on your computer. If you can't think of a location, just put it on your desktop. This isn't the best place to keep things in the long term, but it's OK to keep files here while you work on them.
--- /task ---

To install the libraries for this project, and later to run the project, you need to use the **command line interface** (CLI) — a program to control your computer by typing text commands into a window. The command line interface is called 'command prompt' in Windows.

In the CLI, you do not click to open and access files or the directories (folders) they live in. Instead, you need to know the **path** to the file. This is like a set of directions, either from where you are currently located on the computer — called a **relative path** — or from the root of the computer's hard drive — called an **absolute path**. You need to find the path to the directory that contains your `requirements.txt` file for this next step. If you saved it to your desktop, this is just a directory that the computer displays for you.


#### How to find the path to a directory on Windows

The easiest method is to open the folder in File Explorer and click into the navigation bar at the top of the window. The full path for the folder should become visible and you can then copy it.

![The File Explorer navigation bar for a folder, with the path highlighted in blue.](images/windows_path.png)

--- task ---

In the CLI, navigate to the directory you just unzipped by entering the following command — replace `[directory_path]` with the path to your directory. Then press the Enter key to run the command.

```batch
cd [directory_path]
```

--- /task ---

Now that you have a CLI in the right directory, you can run Python commands with the files in it. 

--- task ---

Run this command on your CLI to install the libraries you need. It may take a while to run, as it has to download the libraries from the internet and some of them are quite large.

```bash
pip install -r requirements.txt 
```

--- /task ---

--- /collapse ---


--- collapse ---
---
title: macOS
---

To install the libraries for this project, you need to use the **command line interface** (CLI) — a program to control your computer by typing text commands into a window. The command line interface is called 'Terminal' in macOS. So your first step is to open 'Terminal', which you can find in the 'Applications' folder of your Mac.

It can be a complex process to install libraries, so a program to handle the installation for you has been created. Here are the [details of this program](http://rpf.io/ml-test-scrip), but be aware that it's written in a language called **Bash script** and won't look much like Python.

--- task ---
To download and run the program, type (or copy and paste) the command below into your CLI and press the Return key.

```bash
sudo curl -L http://rpf.io/ml-test-scrip | sudo bash -s $USER
```

--- /task ---

The script may take several minutes, or more, to complete the setup, as this process depends on the speed of your computer and your internet connection. While this happens, lots of messages appear in the program. You don't need to read them, this is just the program's way to let you know its actions. When the program has completed its work, you should see a new line on which you can enter commands in your terminal. Then you can move on with the rest of the project.

--- /collapse ---

--- collapse ---
---
title: Linux (includes Raspberry Pi)
---

To install the libraries for this project, you need to use the **command line interface** (CLI) — a program to control your computer by typing text commands into a window. The command line interface is called 'Terminal' in Linux.

It can be a complex process to install libraries, so a program to handle the installation for you has been created. Here are the [details of this program](http://rpf.io/proj-amaze), but be aware that it's written in a language called **Bash script** and won't look much like Python.

--- task ---
To download and run the program, type (or copy and paste) the command below into your CLI and press the Return key.

```bash
curl -L http://rpf.io/proj-amaze | sudo bash -s $USER
```

--- /task ---

The script may take several minutes, or more, to complete the setup, as this process depends on the speed of your computer and your internet connection. While this happens, lots of messages appear in the program. You don't need to read them, this is just the program's way to let you know its actions. When the program has completed its work, you should see a new line on which you can enter commands in your terminal. Then you can move on with the rest of the project.

--- /collapse ---

While you wait for the libraries to install — it may take quite some time — check out the next step, 'Get inspiration', to think about what you can build. You can also create your model in Teachable Machine while you wait.
