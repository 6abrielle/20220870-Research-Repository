# Python Fundamentals (Dr. Samrad Soomo
## *08/08*

## Programming Language: Python

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:
* web development (server-side)
* software development
* mathematics
* system scripting

## What can Python do?
* can be used on a server to create web applications
* can be used alonside software to create workflows
* can connect to database systems and read and modify files
* can be used to handle big fata and perform complex mathematics
* can be used for rapid prototypling, or for production-ready software development

## Why Python?
* works across platforms without problem (Windows, Linux, Raspberry Pi, etc.)
* has a simple syntax similar to the English language
* has syntax that allows developers to write programs with fewer lines than some other programming languages
* python runs on an interpreter system, meaning that code can be executed as soon as it is written, meaning prototyping can be very quick
  *  interpreter systems execute code line-by-line and will only stop at an error
  *  compiler systems convert high level language to low level language and then execute code as a whole block
* python can be treated in a **procecural** way, an **object-oriented** way or a **functional** way



**pros** | **cons** 
--- | --- 
designed to be intuitive and easy to program in (without sacrificing power)<br />open source, with a large community of packages and resources<br />one of the most commonly used prgogramming languages in the world<br />"tried and true" language that has been in development for decades<br />high quality visualisations<br />runs on most operating systems and platforms | slower than "pure" (i.e. **compiled**) languages like C++<br />smaller/specialised packages might not be well tested/maintained

## How to use Python
### 1. Install python 3 distribution for your system
*Note: Python 2.7 is no longer maintained and you should do your best to transition all old code to python 3.*

### 2. Download an IDE of your choice OR use VS Code
* [Visual Studio Code](https://code.visualstudio.com/)
* [What IDE to use for Python](https://stackoverflow.com/questions/81584/what-ide-to-use-for-python)

### 3. Install useful dependencies (you may not need this for this course)
* numpty, matplotlib, scipy, nibabel, pandas, sklearn, pygame etc.
* different libraries exist for different purposes and applications

## Hello World in Python

`print("Hello, World!")`

### Hello World in C#
Namespace MyFirstCode{

Class System{
  public static void main(String[]args){
  Console.WriteLine("Hello World");
}
}
}
 
 By comparing Hello World in Python to C#, we can see how simple it can be.
 
 ## Visual Studio Code
 [Getting Started with VS Code](https://code.visualstudio.com/docs/?dv=osx) 
 
 ### Useful Extensions for VS Code
 Python
 Python for VS Code
 Python Indent
 autoDocstring
 Python Extension Pack
 
 ### Other IDEs
 [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) 

## Built-in data types
?

## Python Data Types
?

## Variables in Python
A **variable** is a name given to a storage area that our programs can manipulate (i.e. the data can be changed).

In a **constant** data cannot be changed (during execution).

Each variable in Python has a specific type which determines:
* the size and layout of the variable's memory
* the range of values that can be stored within that memory, and
* the set of operations that can be applied to the variable

A **constant** cannot be changed (during execution)

### Variable Names
A variable can have a short name (like x or y) or a more descriptive name (age, carname, total_volume).

Rules for Python Variable names:
* a variable name must start with a letter or underscore character
* a variable name cannot start with a number
* a variable name can only contain alpha-numeric characters and underscores (a-z, 0-9 and _ )
* variable names are case-sensitive (Age, age, AGE)

Valid variable examples:
`myvar = "anything"`

`my_var = "anything"`

`_my_var = "anything"`

`myVar = "anything"`

`MYVAR = "anything"`

`myvar2 = "anything"`

## Control Structures: Conditions

Decision making structures requires one or more conditions to be evaluated by the program.

Such structures also need:
* statement(s) to be executed if the condition is determined to be true, and 
* statement(s) to be executed if the condition is determined to be false
