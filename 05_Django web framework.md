# DJANGO WEB FRAMEWORK



## Course syllabus
This is a beginner course for learners who would like to prepare themselves for a career in Django development.

### Prerequisites 
To succeed in this course, you are required to have a fundamental knowledge of the following:
- HTML and CSS
- Python
- MySQL

You also require basic internet navigation skills and an eagerness to get started with coding in `Django`!

By the end of the course you will be able to:
- Design a Django web application using Python, HTML and CSS.
- Describe and implement the HTTP request response cycle by creating views, routes and templates.
- Describe and build a data model to create database tables and dynamic web forms.
- Explore the Django Template Language to create dynamic webpages that display data stored in a database.
- Create, share and test your web application by using industry standard best practice and guidelines.  


### Course background
The course is structured around the fictional Little Lemon restaurant. 

The website was designed and coded with HTML and CSS and is currently presented as a single page.

The restaurant owners Mario and Adrian want to explore the possibility of creating a database driven web application using the Django framework. 

The owners would like to store the menu information in a database that can be updated by managers as the menu changes seasonally.

They have asked you to create a prototype of this website using the Django framework.

### Course content 
Each module intends to equip you with the knowledge and skills needed to guide you through the process of creating a web application with the Django framework. 

During this course, you’ll cover everything you need to begin web development with  Django. What to expect in the four modules is outlined below.


### Module 1
In this first module, you will get an introduction to the course where you’ll begin with an overview of what Django is and its uses. You’ll explore examples of how Django is used in the real world. Before embarking on any coding, you’ll be guided through the process to ensure your computer is set up correctly with Visual Studio Code and the appropriate Python installation for your operating system. There are also some tips on how to take this course successfully. Next, you’ll be introduced to how to create a Django web application and its two components, projects, and apps. Here, you will acquire and exercise skills using specific command line tools with the commands "Django admin" and "manage.py" through the correct structure. You will conclude this module by expanding upon web frameworks to show the MVT pattern, code reusability, and how Django’s project structure is set up to suit this.

After completing the lesson items, you will be able to:
- Differentiate between an app and project structure
- Learn to use basic commands with django-admin and manage.py.	
- Create an app inside an existing project using the correct structure.	
- Use the MVT framework to ensure reusability of code.	
- Use the DRY principles to organize your code.


### Module 2
Views are an important component when creating projects and apps in `Django`.In Module 2, you’ll learn about what a view is and how to process basic `HTTP requests`. Then, you will discover how `Django` developers use the request and response objects for common operations and how parameters associate with `HTTP` methods such as `GET`, `PUT`, `POST` and `DELETE`. Next, you’ll explore the use of regular expressions to create different `URL` patterns and map `URLs` to views. As a developer, it is essential to handle unforeseen errors throughout your development process. So, you'll learn to handle common `HTTP` errors at the HTTP, View logic and View levels. Lastly, you will unpack class-based views in Django and how to reuse them across a project.

After completing the lesson items, you will be able to:
- Create views and view logic that can process basic HTTP requests.
- Use the request and response objects for common operations.
- Differentiate parameters and how they associate with `HTTP` methods such as `GET`, `PUT`, `POST` and `DELETE`.
- Use regular expressions to create different URL patterns.
- Map URLs to views.
- Handle errors at the HTTP , View logic and View levels.
- Use class-based views in Django and reuse them across a project.


### Module 3
In the third module, you’ll cover Models. Here, you’ll learn how to use the `Django` admin panel to add and control the permissions of users and groups. Then, in order to interact with the database, you’ll explore how to use the `QuerySet API` to do this. Next, you’ll create forms and use the `Form API` to bind data to objects. You’ll conclude this module by learning how to set up a MySQL database and apply migrations to keep your data up to date.

After completing the lesson items, you will be able to:
- Create Models.
- Apply migrations to appropriate use cases using a best practice approach.
- Use the `QuerySet API` to interact with the database.
- Create a form and use the Form API to bind data to objects.
- Use the `Django` admin panel to add and control the permissions of users and groups.
- Set up a `MySQL` database for your Django app.


### Module 4 
The last module focuses on Templates in `Django`. You’ll start off by learning to create templates and use the template language to create markup. Then, you’ll explore how to use templating to generate `HTML`. Next, you will learn how to integrate third-party libraries into your `Django app`. You will end off by exploring debugging and testing in `Django`.

After completing the lesson items, you will be able to:
- Create templates and use the template language to create markup.
- Use templating to generate `HTML`.
- Work with Templates.	


### Module 5: Graded Assessment
In the final week, you'll apply the skills you gained from the course to complete the prototype for the Little Lemon website designed with `Django`. You will then move on to complete the final graded assessment. Finally, you will have the opportunity to reflect on the course content and review the learning path. 

After completing the project exercises, you will be able to:  
- Synthesize your new `Django` skills to create a website for a local restaurant.
- Reflect on what you learned in this course and explore the next steps in your journey.










# MODULE 01 - INTRODUCTION TO DJANGO

## Course Introduction

### Installing Python (optional for Windows users)
To install `python` on Windows, you first need to download the latest version from the python.org website.

1. Go to https://www.python.org/downloads/windows
2. Select the latest release.

![Phyton Download page displaying the phyton versions][img050101]

3. Depending on what best suits your operating system, select either the 32-bit or 64-bit offering.
4. Click the link to download the file.
5. Open the file, once downloaded.
6. On the installation window, check the following boxes:
    - Install Launcher for all users. 
    - Add Python 3.10 to PATH. 

![Phyton Installation options][img050102]

7. Select Install Now.   

![Phyton installation advanced options and path to folder selection][img050103]

8. Select Yes on the next window to allow the app to make changes to your device.
9.  Once the installation process has begun, allow it to finish. 
10.  Select Close once it's successful.
11. You should now be able to access the latest release of Python from the Windows menu.



### Setting up a project in VS Code
In this reading you’ll learn how to install Visual Studio Code and add a Python extension to it.


#### Features of VS Code
A Python program is a text file with a `.py` extension. Therefore, it is possible to write the code using any text editor. However, an editor familiar with Python syntax helps avoid syntactical errors. Throughout this course, you will use Visual Code to develop your programs. 

Visual Studio Code (`VS Code`) is Microsoft's popular source code editor. It is a desktop application for Windows, Linux, and Mac. It is lightweight but speedy and includes essential features such as debugging support, auto-completion and syntax highlighting. 


#### Install VS Code
VS Code is available to download for free at https://code.visualstudio.com/Download. Choose the downloader that is appropriate for your operating system.

![Visual Studio Code download page screenshot][img050101]

This reading focuses on the Windows platform installation. For other operating systems, follow the instructions on the above page.

The Windows installer is an executable (VSCodeUserSetup-x64-1.71.2.exe). Execute it from the downloads folder. You may need admin credentials to do this, then follow the installation wizard.

It will help if, during the installation, you specify the installation folder with a short path that is easy to navigate instead of the default path suggested by the installer.

Selection of destination location for the navigation of the program folder
Also, ensure that it is added to the system’s PATH environment variable.   

Additional tasks selection during the installation of visual studio code
You are ready to launch VS Code from the start menu or the desktop shortcut if you have created it. 

It opens to the Getting Started page. Play around with the Appearance and Layout settings according to your liking. 

Get Started view
Python Extension for VS Code
VS Code doesn’t support Python as is. So, you need to enable it by adding Python Extension.

Click the Extensions button on the left sidebar (use the ctrl+shift+x shortcut) to open the Extensions Marketplace. Type Python in the lookup box and select the Python extension from the list shown.

Phyton extension installation to Visual Code Studio from the marketplace
Go ahead and click on Install.

Next up, you need to inform VS Code about the Python interpreter you want it to use while providing highlighting, auto code completion, and debugging support.

Press ctrl+shift+P to open the Command Palette. Type Python: Select Interpreter in the search box. 

Selection of Phyton Interpreter from the command palette
A list of available Python interpreter installations displays. 

You may have more than one version of Python on your system or none at all. So, you’ll need to install Python before continuing.   

Selection of Phyton version from command palette
Hello World in VS Code
It is now time to see how VS Code helps write Python programs.

Open a folder from the File menu and add an empty Python code file (name it hello.py). Enter a print statement in it and save.

Demonstration of writing Phyton programs on VS Code with an example of "Hello World" text and print statement
VS Code provides a visual indication of different elements of the code, such as keywords, functions and strings by coloring them appropriately per the chosen scheme.   

Command terminal menu display to run the code
To run this code, open the command terminal from the Terminal menu. 

Execute hello.py with Python by entering the following line in the terminal:   

1
python hello.py 
So, you have successfully installed VS Code, enabled Python and test-run a sample code.

Python recommends using a virtual environment to build Python applications. 

A virtual environment is an isolated environment having its copy of the interpreter and libraries so that there’s no clash with the global installation of Python.

Python’s virtual environment is set-up with the help of a built-in module named venv. For example:

12
python -m venv c:\Django 
C:\django>scripts\activate 
After the virtual environment is activated, install the Django framework with the following command:

1
(django) c:\django> pip3 install django
The VS Code software can be launched from within this folder as follows:   

1
(django) C:\django>code . 
This is a handy shortcut to start VS Code.



#### SQLite Extension for VS Code
During this course, you will be learning a lot about `SQLite` databases. Hence, it will be convenient, if possible, to browse the database from within the VS Code environment. VS Code Marketplace has helpful extensions like **SQLite Viewer** or **SQLite**. Please find it in the Marketplace on VSCode and install it.

![Display of SQLite Viewer extension from VS Code Marketplace][img050113]

To test, add an `SQLite` database in the folder and double-click on it. The database tables will be shown on the main panel. 

It's important to know that `Django` enables the use of SQLite database by default and VS Code Extensions for SQLite help in viewing the tables. 

##### Note:
No sample database tables are added by default. Database tables are added using a process known as migrations and will learn about them later in this course. When database tables are added, they will be empty until you populate them with data. 

The image below is thus illustrative and will vary according to the tables present in your Django application.  

![SQLite database tables on main panel][img050114]

This reading taught you how to install VS Code on Windows OS, add a Python extension and run a Python program. You also added the SQLite Viewer extension to browse the SQLite database.


## Working with virtual environments on your local machine

While working with Django, you must first go to the local directory where you want to create your project and setup a virtual environment. 

Ensure pip in installed on your device. The latest version can be installed and upgraded by using the command:

### Windows
```python
py -m pip install --upgrade pip
```

### MacOS
```python
python3 -m pip install --user --upgrade pip
```

Python uses `venv` as the preferred module to create and manage virtual environments. `venv` is also included in the Python standard library and does not require any additional installation. 

`venv` (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects. 

In case you want to install virtualenv that is used for earlier versions of Python, use the command:

### Windows
```python
py -m pip install --user virtualenv
```

### MacOS
```python
python3 -m pip install --user virtualenv
```

You can **create a virtual environment** in the specific project directory by running a command:

#### Windows
```python
py -m venv env
```

#### MacOS
```python
python3 -m venv env
```

#### Note:
`env` is the name assigned to the virtual environment and this will create a virtual Python installation in the env folder.


### Activate the virtual environment
Next you need to activate the virtual environment. You will put the virtual environment-specific python and pip executables into your shell’s PATH.

You can do this by running a command such as:

#### Windows
```python
.\env\Scripts\activate
```

#### MacOS
```python
source env/bin/activate
```


### Exit the virtual environment
You can exit the virtual environment by running the command:

#### MacOS and Windows 
```python
deactivate
```

There may be OS specific difficulties you may encounter while installing and using virtual environments. 

More information can be found on the official [Python website](https://www.python.org/). 

### Note: 
`venv` is not the only option available for creating virtual environments and other options exist such as pipenv which is another variation. However, in this course, the use of `venv` is recommended. 





Working with labs in this course
NOTE: This is a reference reading in support of the labs you will encounter throughout this course. It consists of helpful information you may require while working with different labs and you can use this as a point of reference  

The labs for this course have everything installed and set-up so you can start working with Django right away.  You can get started with terminal in VScode.

Open the Terminal

New Terminal in VS code

Verify that you are in /home/coder/project/workplace/myproject directory before running the command. Here is how you can navigate to it once the lab is up:

For a directory named workplace, move inside the directory with the shell command such as:

cd workplace

 Move up the directory or outside the directory by one level, use a command such as:

cd .. 

In most cases for example, the learner will first step into the workplace directory and then again inside the myproject directory that contains the script for manage.py to run Django commands.  


Commands in Terminal
To run and view your Django app in the browser, execute the following command in terminal. (Verify you are in the directory where manage.py file resides.)

123
python3 manage.py runserver # To run the server
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database
Open the Browser
To view your code and instructions side-by-side, select the following in your VS Code toolbar:
View -> Editor Layout -> Two Columns

To view a file in Preview mode, right click on the file and click on Browser Preview (in the EXPLORER sidebar) 

Select your code file in the code tree, which will open it up in a new VS Code tab.

You can drag any file over to the second column to view the contents in that column.

Great work! You can now see instructions and code at the same time.


Open Browser preview:

Additional views to browse preview 
General Notes
You may come across some code that is not directly relevant to the lab. A line such as:

from django.shortcuts import render

Here for example, render()  is a helper function that is often required to render the template, hence Django imports it automatically. You may come across some similar auto-imports and it is safe to keep or remove them while updating the lab. 

This course recommends typing the code manually as you work through the exercises instead of copying and pasting. Typing the code will help you develop muscle memory and better your understanding of the fundamental concepts of this course.

The lab will use the Python commands that work on Linux shell. So to run any Python command, it is advisable to use python3 as the keyword for invoking Python 3+ versions instead of just using the keyword python

The commands added in the Labs/Readings/Videos are specific to the Operating System. For example, the use of Control instead of Command key in case of Windows OS and keyword python3 instead of python in case of MacOS. Learner should make the necessary adjustments in understanding  specific to the Operating System they use.  

While all the labs work on independent shell, on completion, it is a good practice to stop the server by pressing a Command on the shell such as: Ctrl/Cmd + C






Additional resources
The following resources will be helpful as additional references when dealing with different concepts related to the topics you have covered in this course introduction. 

Since this is a course exclusively about an open-source framework, there will also be a wide-scale reference to the official Django website and documentation. 

Access the links below to explore more about Django.

Django official website

Django documentation

Installing VS Code on Mac - Official

Installing VS Code on Windows - Official

Django installation - Official

Install Django on Windows

Setting up Virtual environment in Python - venv (Windows and MacOS)




## Projects and Apps



### Project Structure
When installing Django globally or in a virtual environment, Python recommends using isolated environment libraries and other dependencies required for a particular application.

Python's standard library contains the `venv` module. 

It installs a command-line utility called Django-admin in the system path and is located in the scripts folder of your current Python environment.

As the name suggests, you use the django-admin utility to perform various administrative tasks. 

These tasks include creating the project and app, performing  migrations to generate database tables, whose structure matches data models, and running a development server.


#### What is a project?
When you set out to build a modular, extensible and scalable web application, you need an arrangement that controls the standard features of its various sub-modules.

A Django project is a Python package containing the database configuration used by various sub-modules (Django calls them apps) and other Django-specific settings.

Use the `startproject` command of Django-admin as follows:   

```python
(djenv) C:\djenv>django-admin startproject demoproject 
```

The startproject is Django’s default project template. It creates the following file structure in the Python environment:   

```python
C:\djenv\demoproject 
│   manage.py 
│ 
└───demoproject 
        asgi.py 
        settings.py 
        urls.py 
        wsgi.py 
        __init__.py 
```

If you start `VS Code` in this folder, the file structure appears in its explorer as shown:

![File structure display in VS Code][img050115]

You can see a folder named `demoproject` is created in the Python environment folder. 

It contains a script  `manage.py` and another folder of the same name. 

You will learn more about the files in the inner folder later.

The `manage.py` script inside the outer demoproject has the same role as the django-admin utility. 

You can use it to perform various administrative tasks. In that sense, it is a local copy of the django-admin utility.


#### manage.py
As mentioned above, the `manage.py` script can perform everything that the django-admin utility does. However, using `manage.py` is more straightforward, especially if you are required to work on a single project. If you have multiple projects, use django-adminand specify the settings. The general usage of `manage.py` is as follows: 

```python
python manage.py <command>
```

Let's explore some of the required command options:


#### startapp
As mentioned above, a Django project folder can contain one or more apps. An app is also represented by a folder of a specific file system. The command to create an app is: 

```python
python manage.py startapp <name of app>
```

You will explore the structure of an app later. 


#### makemigrations
Django manages the database operations with the ORM technique. Migration refers to generating a database table whose structure matches the data model declared in the app.
The following command should be run whenever a new model is declared. 

```python
python manage.py makemigrations
```


#### migrate
This command option of `manage.py` synchronizes the database state with the currently declared models and migrations. 

```python
python manage.py migrate
```
![Display of manage.py migrate code on console and terminal][img050116]


#### runserver

This command starts Django’s built-in development server on the local machine with IP address 127.0.0.1 and port 8000.  

```powershell
python manage.py runserver
```

It helps if you don't use this development server in the production environment. 


#### Shell
This command opens up an interactive Python shell inside the project. This is useful when you are required to perform some quick interactive operations. 

```powershell
python manage.py shell
```

![Display of manage.py shell code on console and terminal][img050117]

Django prefers IPython if it is installed over the standard Python shell. 


#### Project package
The `startproject` command option of the Django-admin utility creates the folder of the given name, inside which there is another folder of the same name. For example, the command:

```powershell
django-admin startproject demoproject
```
This creates a demoproject folder, inside which there’s another demoproject folder.

The inner folder is a Python package. For a folder to be recognized by Python as a package, it must have a file `__init__.py`. In addition, the startproject template places four more files in the package folder.


settings.py

Django configures specific parameters with their default values and puts them in this file. 

The django-admin utility and manage.py script use these settings while performing various administrative tasks.


#### urls.py
This script contains a list of object urlpatterns. Every time the client browser requests a URL, the Django server looks to match its pattern and routes the application to the mapped view. 

The default structure of urls.py contains a view mapped to the project’s Admin site.

123456
from django.contrib import admin 
from django.urls import path 

 urlpatterns = [ 
    path('admin/', admin.site.urls), 
] 


#### asgi.py
This file is used by the application servers following the `ASGI` standard to serve asynchronous web applications.



#### wsgi.py

Many web application servers implement the WSGI standard. This script is the entry point for such WSGI-compatible servers to serve your classical web application. 


#### settings.py
This file defines the attributes that influence the function of a Django application. The startproject template assigns some default values to these attributes. They may be modified as per requirement during the use of the application.

Let us explain some critical settings.

#### INSTALLED_APPS

This is a list of strings. Each string represents the path of an app inside the parent project folder. The startproject template installs some apps by default. They appear in the INSTALLED_APPS list.

```js
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
]
```
This list must be updated by adding its name whenever a new app is installed. 

For example, if we create a demoapp with the following command:

1
python manage.py startapp demoapp
Then, add the `'demoapp'` string inside the INSTALLED_APP list.

![Display of demoapp inside the installed app list][img050118]



#### Databases
This attribute is a dictionary that specifies the configuration of one or more databases to be used by the current Django application. By default, Django uses the SQLite database. Hence, this setting has a pre-defined configuration for it.

```js
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', 
    } 
} 
```

The default name of the SQLite database is db.sqlite3, which is created in the parent project folder. 

In place of SQLite, you may choose to use any other. For example, for MySQL, the database settings could be as follows:

```js
DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'djangotest',   
        'USER': 'root',   
        'PASSWORD': 'password',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',            
    }   
}
```

Note here the default port number for MySQL is 3306 as against the default port number 8000 used with SQLite in Django. 



#### DEBUG = True
By default, the development server runs in debug mode. This helps develop the application as the server picks up changes in the code and the output can be refreshed without restarting. However, it must be disabled in the production environment.



#### ALLOWED HOSTS
This attribute is a list of strings. By default, it is empty. Each string represents the fully qualified host/domain where this Django site can be served. For example, to make the site running on localhost externally visible, you may add 0.0.0.0:8000 to this list.



#### ROOT_URLCONF
This setting is a string pointing toward the urls.py module in which the project’s URL patterns are found. In this case, it would be:
```powershell
ROOT_URLCONF = 'demoproject.urls'
```


#### STATIC_URL
This setting points to the folder where the static files, such as JavaScript code, CSS files and images, are placed. Usually, it is set to 'static/' corresponding to the folder of this name in the parent project folder.



#### Test the installation
After creating the project, to verify that it is built correctly, start the development server with the following command while remaining in the project’s parent folder:

```powershell
python manage.py runserver
```

![Development server display with runserver code][img050119]

The server starts running at port 8000 of the localhost with IP address 127.0.0.1. Open the browser and enter http://127.0.0.1:8000/.   

![Django page browser display][img050120]

If you get this output, the project has been created successfully.

In this reading, you learned how to create a Django project. The file structure of the project has also been explained here. In the end, the installation of the project has been successfully verified.


## Admin and structures
## Web Frameworks and MVT































# MODULE 02 - VIEWS





# MODULE 03 - MODELS





# MODULE 04 - TEMPLATES





# MODULE 05 - GRADED ASSESSMENT



# PUBLIC

[img050101]: /back-end-development/public/img050101_installing-python.png
[img050102]: /back-end-development/public/img050102_installing-python-2.png
[img050103]: /back-end-development/public/img050103_installing-python-3.png
[img050104]: /back-end-development/public/img050104_installing-vsCode-1.png
[img050105]: /back-end-development/public/img050105_installing-vsCode-2.png
[img050106]: /back-end-development/public/img050106_installing-vsCode-3.png
[img050107]: /back-end-development/public/img050107_installing-vsCode-4.png
[img050108]: /back-end-development/public/img050108_installing-vsCode-5.png
[img050109]: /back-end-development/public/img050109_installing-vsCode-6.png
[img050110]: /back-end-development/public/img050110_installing-vsCode-7.png
[img050111]: /back-end-development/public/img050111installing-vsCode-8.png
[img050112]: /back-end-development/public/img050112_installing-vsCode-9.png
[img050113]: /back-end-development/public/img050113_installing-vsCode-10.png
[img050114]: /back-end-development/public/img050114_installing-vsCode-11.png
[img050115]: /back-end-development/public/img050115_django-Project-Structure-01.png
[img050116]: /back-end-development/public/img050116_django-Project-Structure-02.png
[img050117]: /back-end-development/public/img050117_django-Project-Structure-03.png
[img050118]: /back-end-development/public/img050118_django-Project-Structure-04.png
[img050119]: /back-end-development/public/img050119_django-Project-Structure-05.png
[img050120]: /back-end-development/public/img050120_django-Project-Structure-06.png