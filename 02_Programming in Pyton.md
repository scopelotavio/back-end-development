# Module 01 - Getting started with python





## Visual Studio Code
In this course, you will use Visual Studio Code (VSCode), an Integrated Development Environment (IDE) provided by Microsoft for free. VSCode has a wealth of plugins and extensions to make your life easier as a developer. By the end of this reading, you will be able to install and set up Visual Studio Code on your devices.

You have two options for using Visual Studio Code to complete your course activities:



### Option 1: In-Browser Visual Studio Code via Coursera Labs

Coursera's platform features an integrated, browser-based version of VS Code, eliminating the need for local installation. This environment is preconfigured to align with course requirements and is accessible through designated "Lab" items within your course. Your work and files are saved within this lab environment and remain accessible as long as you have course access. 

https://www.coursera.support/s/article/learner-000001860-Using-web-development-labs-in-Visual-Studio-Code?language=en_US 



### Option 2: Local Installation of Visual Studio Code
Alternatively, you can install VS Code directly on your local device. To do so, download the appropriate version for your operating system from Microsoft's official website: 

https://code.visualstudio.com/download    

This approach allows for a personalized setup and the flexibility to work offline.

Both options facilitate a seamless coding experience, enabling you to choose the environment that best suits your learning preferences and technical needs.



### Windows
1. Download the 64-bit or 32-bit files, depending on your OS.
2. Once the download is complete, please open the file to install it.
3. Use the default directory location when prompted where to install.
4. Make sure the Add to Path option is selected in the Select Additional Tasks view.

![A screen showing the select additional tasks screen][img010101]

5.   Click Next, and the installer will begin.
6.   Once complete, load the application, and you should see something similar to this:

![The graphic shows what your screen should look like once VS Code has been installed][img010102]



### Mac
1. Download the application based on your chipset. M1 Macs use Apple Silicon, and older versions use Intel. If you are not sure, just choose the Universal option.
2. Once the download has been completed, go to the folder where the file was downloaded (the default is usually the Downloads folder).
3. Double-click the zip file to extract the contents.
4. Drag and drop the .app file to the Applications link in the File Explorer, as displayed below.

![The graphic shows the Downloads folder where you will find the Visual Studio Code.app file][img010103]



### Python Extension
Visual Studio Code offers a Python extension from its Extension Marketplace. You can add it directly from the IDE by completing the following steps.

1. Click on the Extensions icon

![The graphic displays where you can find the Extensions icon for Python][img010104]

2.   In the search bar, type in Python. A few different extensions will return, but the one you want is the extension provided by Microsoft.

![The graphic shows where you must type in Python in the search bar][img010105]

3.   Click the install button. You may need to restart your IDE after the installation is complete.





## Installing Python paths (Optional for Windows Users)
If you want to work on your local device and have a Windows machine you will need to install Python. To install Python on Windows you first need to download the latest version from the python.org website.

1. Go to https://www.python.org/downloads/ 

![Phyton.org website landing page on browserPhyton website with the link displayed on browser][img010106]

2. Select the latest release.
3. Depending on what best suits your operating system, select either the 32-bit or 64-bit offering.

![List of Installer files with information about Operating System, Size and DescriptionCompressed files as windows installers and tarball][img010107]

4. Click the link to download the file from the Windows Installer - Recommended.
5. Once downloaded, open the file.
6. In the installation window, check the following boxes:
- Install Launcher for all users
- Add Python 3.10 to PATH

![Phyton Environment SetupInstall Phyton display][img010108]

7. Select Install Now.
8. Select Yes in the next window to allow the app to make changes to your device.
9. The installation process will begin. Wait for it to finish and then select Close once it's successful.
10. You should now be able to access the latest release of Python from the Windows menu.






## Python syntax cheat sheet
This reading provides a cheat sheet that can be used for quick reference.

### Spacing

#### Correct
```python
#any ammount of whitespace on a single line is ok
x     =        1        +        2
```

#### Incorrect
```python
x = 1
+ 2
```


### Indentation

#### Functions
In the code below, we will use some basic functions. Understanding some of the key terms and concepts while we use them is helpful. 

Functions allow you to group code into reusable blocks.

```def``` keyword: In Python, the ```def``` keyword defines a function. 

Syntax: 
```python
def function_name(parameters):

    # This is inside the function body

    return result
```

Understand the terminology of the code above:

**function_name**: The name you give to the function.

**return**: Optional statement to send back a result from the function.

**parameters**: Optional values passed to the function. It can be one or more.

Note also how no curly or round brackets are used in Python to define the scope of the function. 

#### Correct
```python
def say_hello():
    print("Hello there!")

print(say_hello())
```

```python
def say_hello(): print("Hello there!")

print(say_hello())
```

#### Incorrect
```python
def say_hello():
print("Hello there!")
```

```python
    def say_hello():
print("Hello there")
```






## Commenting code
On completion of this reading, you will be able to explain why and where to use comments in coding.

Adding comments to code not only helps you as a developer but also helps other members of your team. Comments are great for refreshing your memory of code you may have written months ago and you may have forgotten what it was intended to do. There are multiple reasons why you need to add comments to a code file. They can range from the following:

* Explaining what the code is intended to do.
* Let developers know that code is deprecated.
* Add TODO comments for work to be completed at a later time.

Below are examples of the different types of comments that can be used.


### Single-line comments
The use of a ```#``` symbol tells Python to ignore everything after this point until the end of the current line.

```python
# Don't try to Run Me, I'm a comment
x = 10
```


### Multi-line comments
Triple Quotes (`'''` or `"""`): Python uses triple single or double quotes to create multi-line comments. These are typically used for docstrings or comments spanning multiple lines.

```python
'''
This is a multi-line comment
that spans multiple lines.
'''

"""
This one as well, 
will span multiple lines
"""
```


### Inline comments
The `#` symbol tells Python to ignore everything after this point until the end of the current line, this allows the placement of comments within the code itself. Inline comments should be used to supply important information about the code they deal with.

```python
x = 1  # Resetting buffer size
```

Remember to always have a reason for a comment, they should supply information to the reader and not be a distracting nuisance





## Basic Data type and Function Cheatsheet
Here's a quick reference for data types in Python.


### Data types
| Data type | Meaning | Example |
| -- | -- | -- |
| string | Text | 'Hello', 'Testing 123' |
| integer | Numbers | -5, 4, 3, 2, 0 |
| float | Decimals | 2.4, 5.2, 1000.00 |


### Flow Control

#### Comparison operators
| Operator | Meaning | Example |
| -- | -- | -- |
| == | Equals | a == b |
| != | Not Equal | a != b |
| < | Less than | a < b |
| > | Greater than | a > b |
| <= | Less than or Equal to | a <= b |
| >= | Greater than or Equal to | a >= b |


## Indentation

Indentation is used to define code blocks in Python. Unlike many programming languages that use braces `{}` to group code, Python uses indentation.

Indentation is mandatory in Python and is used to indicate which statements belong to loops, functions, conditionals, and other structures.

```python
if x > 0:  # Colon indicates the start of the block
    print("Positive")  # Indented 
else:
    print("Non-positive") # Indented
```


### Comments

#### Single-line comments
Placing a `#` symbol in front of the text you want to be a comment causes Python to ignore everything from that point until the end of the current line.

```python
# Single Line comment
```


#### Multi-line comments
Triple Quotes (`'''` or `"""`): Python uses triple single or double quotes to create multi-line comments. These are typically used for docstrings or comments spanning multiple lines.

```python
# This is a multiline comment
# which can be used for long comments
```

#### Inline/code comments
The `#`symbol will cause Python to ignore everything from that point until the end of the current line, so inline comments can be created in this way.

```python
x = 1 # assigns value of 1 to x
```


### Colon (:)
Used to indicate the start of a code block, such as in loops, conditionals, and function definitions.

```python
if x > 0:  # Colon starts the block
    print("Positive")
```


### Built-in Functions


#### print()
This function looks for the default output device, your terminal, and displays the value passed to it.

```python
print("Hello")
```

#### input()
This function looks for the default input device, your keyboard, and captures the value. This value can then be assigned or used.

```python
print("Where do you live?")
location = input()
print("So you live in " + location)
```

**Note:** The code block above will create a prompt for the user asking "Where do you live?". The user will then enter the response and press the Return key to continue execution of the remaining code. The response entered by the user is stored, returned as an output, or can be assigned to some variable depending on the context of usage. 


#### len()
This function returns the length or the count of the elements contained within the structure it is applied on. This may be a string, array, list, tuple, dictionary or any sequence.
```python
len("Hello")
5
```


#### str()
This function can be used to convert the provided value into a String
```python
str(55)
'55'
```

#### int()
This function can be used to convert the provided value into an int
```python
int('75')
75
```

#### float()
This function can be used to convert the provided value into a float
```python
some_int = 10
float(some_int)
10.0
```


### Creating Functions
Functions in Python require a keyword to define them : `def`   followed by an identifier (a name) this forms the function signature. The body of the function contains the code to run when the function is called.

```python
def say_hello():
    return "Hello there!"

# With parameters
def say_hello(you):
    return "Hello " +  you

```










## Type casting, a deeper look
There are some scenarios in which a given value's data type needs to be changed to some other data type.

This process is known as type casting.

Another, more informal way to refer to it is "data type conversion".

The simplest example of converting data could be the following comparison:

```python
print(10 == 10)
```

In the above piece of code, I'm asking Python if the number 10 is equal to the number 10, and I'll get the boolean value of `True` printed, confirming that indeed, they are the same.

What if I do this?

```python
print(10 == 10.00)
```

Again, the boolean value of `True` is output on the screen.

Now, you might complain that, well, `10` is not technically equal to `10.0` - because, one might argue, the first number is an integer, and the second number is a float. You would be right - although these are the same numbers, they are not the same data types.

However, Python here perfoms what's known as **"implicit type conversion"**.

To understand how this works, I'll slightly tweak the previous example. Instead of asking Python to compare the two numbers and return if they are the same or not, I'll ask Python to print the result of adding these two numbers together.

```python
print(10 + 10.0)
```

The printed result is `20.0`.

This output allows me to conclude that **when Python runs operations involving integers and floats, it implicitly converts the integers type to a float, and then completes the operation.**

To really drive this point home, I can extend my previous example, using the `type()` function:

```python
print(type(10 + 10.0))
```

The output is `<class 'float'>`, so this confirms my conclusion.

Let me now show you a small program in Python, working with numbers:

```python
user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = user_num_1 + user_num_2
print(user_sum)
```

When I run this program, I could, for example, provide the first number's value as `5`, and the second number's value also as `5`, expecting that the printed `user_sum` value will be `10`.

However, when I do exactly that, the number `55` gets printed instead.

Why was this not working?

Well, the answer is pretty simple: everything that a user types in, is converted, by Python, to the `string` data type.

This means that, although I typed numbers into these two inputs, what was saved in `user_num_1` and `user_num_2` were actually strings.

Effectively, it's exactly the same as if I just did this:

```python
user_num_1 = "5"
user_num_2 = "5"
user_sum = user_num_1 + user_num_2
print(user_sum)
```
This time, the output of printing `user_sum` is still "55", but this comes at no surprise.

In order to have my Python code work as I intended, I need to perform **explicit type conversion**.

In other words, I have to convert the value of `"5"` to the value of `5`.

Here's my updated code:

```python
user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = float(user_num_1) + float(user_num_2)
print(user_sum)
```

What I'm doing here is, I'm making sure that my program can handle even accepting floats as inputs, and still work correctly.

In other words, I'm making sure that if a user provided, say, the float value of `5.5` as both the first and second numbers when running the above code, the output would not throw an error. Instead, it will be the expected `11.0`.

What if I decide to output some words to the user, telling them what happened?

Here's an attempt at doing that:

```python
num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum)
```

If I run the above code, it will throw the following error:
```python
Traceback (most recent call last):
  File "<string>", line 4, in <module>
TypeError: can only concatenate str (not "float") to str
```

What this means is, I cannot concatenate a string and a float like that. In other words, although **Python's implicit type conversion** works when I use the + operator on strings and integers, it does not work on strings and floats unless you explicitly convert the float to a string.

Also note, that you also cannot concatenate a string and integer. This happens because Python enforces type safety, meaning it requires explicit instructions on how to combine different data types in cases such as string with integer.

The solution to this is to perform explicit type conversion, as follows.

```python
n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)
print("The sum of " + n1 + " and " + n2 + " is " + str(user_sum))
```

This time, the output is: `The sum of 5.5 and 5.5 is 11.0`.

In Python, it's easy to perform explicit conversions, and sometimes they are very useful. You'll learn more about how this works as you get more experience in Python.






## Additional resources
Python allows you to do quite a lot with very little code. Compared to other languages such as Java or C#, Python has a much easier learning curve. It lends itself well to the "write less, do more philosophy". Python developers are also in high demand and learning how to program in Python makes for a good career choice.

You can access the links below to learn more about programming in Python.

Check out the Python website to find out more about built-in functions: [Python](https://docs.python.org/3/library/functions.html)

Check out W3 Schools to learn more about coding and web development: [W3Schools](https://www.w3schools.com/python/default.asp)

Check out HackerRank to practice your new acquired Python skills: [HackerRank](https://www.hackerrank.com/domains/python)







## Conditional statements
This reading introduces you to the conditional statements of `if`, `else` and `elif`.

### If
In keeping with the light switch example, the state of the switch can be stored with a Boolean value of `True` or `False`.

- On = True
- Off = False

```python

#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')
```

The code snippet above has a variable called `current` which keeps track of the state of the light - on or off. The first `if` statement will check if the light is on and if it is, the flow will go inside the condition and set the `current` variable to `False` - turning the light off. In the above code snippet, the value of the current variable is initially set to False, so this condition is not met.

The second `if` statement will check if the light is off and if it is, the flow will go inside the condition and will set the `current` variable to `True` - turning the light on. 


### If else
The above code works fine but it can be rewritten more effectively by using another condition called `else`. The following code is an example:

```python
current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')
```

The `else` statement has made your code a bit easier to read and given that the flow relates to the same condition, it makes more sense to combine them as part of a single unit.


### elif
Python also has another condition called `elif` which helps when you have multiple conditions to satisfy. The light switch example is pretty straightforward in that you only have to check for the state of on or off - `True` or `False`. In certain conditions, it may not be that easy. Thankfully `elif` is here to help.

Let's say you want to give a certain discount to customers if they spend over $100. You will also provide an extra discount if that customer is part of a loyalty program. If the customer is not part of the loyalty program and did not spend over a $100, a service charge of 5% is applied.

```python
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))
```

The above code snippet first checks to see if the customer is part of the loyalty program and if they are spending over $100. If both conditions are met, a discount of 20% is applied to the bill. The `elif` statement will only be executed if the first `if` condition is not met. The `elif` statement will only check if the bill is over $100 and if it is, it will apply a discount of 10%  to the bill.

The final `else` statement is only executed if neither of the other two conditions are met. In this case, a charge of 5% is applied to the bill.






## Looping Constructs: Practical Examples
This reading introduces you to the different looping constructs in Python.


### For loop
Looping through data is a fairly common task in any programming language. The `for` loop makes it easy to work with any type of sequence in Python.  Let's run through some examples of `for` loops and the different ways you can use them.

```python
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    print('One of my favorite desserts is', dessert)
```

In the code snippet above, the `for` loop iterates over the contents of the favorites list and prints out a sentence with the dessert name for each item in the list.

The `for` loop is based on the size or length of the elements to iterate over. 

![For Loop ProgramFor Loop Program][img020101]


### While loop
On the other hand, a `while` loop is based upon a condition being `true`. Once the condition is no longer true the loop stops. The amount of times the `while` loop is executed is not known ahead of time as it is with the for loop. 

If you take the above `for` loop example and convert that to the `while` loop alternative, you will end up with something like this:

```python
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

count = 0

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1

```

Note that you needed to declare a `counter` variable. The `counter` variable is then compared to the length of the `favorites` list. As you loop through the data the counter is incremented. Once the condition `count < len(favorites)` is no longer true the loop will stop.

![The graphic explains the flow of  a for- loop.][img020102]






## Practicing control flow and loops


### Controlling loops
So far, you have only looped over sequences based on the length of the data you wanted to iterate over. In many cases, this is not necessary and depending on the amount of the data it can also be quite costly. You'll now examine how you can control the flow of the loop and exit out when a specific condition is met. You will also look at control statements such as `break`, `continue` and `pass`. 


### If else
In many cases, you may need to search for a particular item in a list. Once the item is found, there is no need to continue looping over the other results. Using the same example as before, let's assume you only need to check if the dessert "Churros" is in the list and if it is, print a single statement. 

```python
#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)        
```

Running the above code will output the following:

`Yes! One of my favorite desserts is Churros`

But what happens if you look for a dessert and that dessert is not on the list? The code above is currently not set up to handle this. Let's look for the dessert "Pudding" which is not on the list, and also add an `else` statement to handle the case of when it's not found. If the dessert is not part of the list, you will print a new statement.

```python
#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert) 
    else:
        print('No sorry, that dessert is not on my list')
```

Running the above code will result in the following output:

`No sorry, that dessert is not on my list`

**Note:** As the code iterates through the list, it will print the statement above five times since there are five items in the list. There are more efficient ways to handle this scenario and print the message only once, such as using a `for loop` or creative applications of `if-else` statements. You will learn about these techniques soon enough as you progress in the course.


### Loop control statements

#### Break
The code works as intended but you may notice one flaw. If you change the search term to something that is on the list like `"Churros"` and run it again you will get the following output:

```
No sorry, that dessert is not on my list
No sorry, that dessert is not on my list
Yes one of my favorite desserts is Churros
No sorry, that dessert is not on my list
No sorry, that dessert is not on my list
```

This is not what you want! The dessert is on the list but it still printed out the else condition. To fix it, you need to use a control statement called break. 

Add the following:

```python
#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
    else:
        print('No sorry, not a dessert on my list')
```

Running the above code will partially resolve the issue. The break statement is used to stop the loop, which in turn also stops the else condition. Without the break the loop will continue even after the if condition is satisfied.

The output of the code will be:
```
No sorry, not a dessert on my list
No sorry, not a dessert on my list
Yes one of my favorite desserts is Churros
```

While the `break` statement did stop the execution once "Churros" was found, the first two statements are not what we want here. We resolve this by modifying the if-else statement that we learnt earlier. Try changing the code above using this code block:

```python
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes, one of my favorite desserts is', dessert)
        break
else:  # This else belongs to the for loop, not the if statement
    print('No sorry, not a dessert on my list')
```

What has changed here is the placement of the else block. The ```else``` will execute only once after the entire ```for``` loop is checked and if the dessert we want is not in the list. The else statement is used here in conjunction with the for loop, and so called the ```for-else```. You will learn little more about it as you progress. 


#### Continue
Similar to break, `continue` can be used to control the iteration of the loop. The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest. If you change your code to this, you will notice the outcome will print everything except the Churros dessert.

```python
#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

```


#### Pass
The `pass` statement in this case acts as a placeholder, allowing you to include an empty block of code without causing a syntax error. It does nothing and allows the program to continue execution normally.

```python
#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 
```






## Exercise: Use control flow and loops to solve a problem

### Introduction
In this exercise, you will practice control flow with loops to solve problems. You will be given a list of integers and you will have to add some code to find a specific number in a list and return it. 

### Instructions
1.   Under the `num_list` create a new for loop and print out each value on the list in sequential order.

2.  Inside the `for` loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition

3.  Change the print statement to `“Over 45”` and add an `else` condition with a print statement of `“Under 45”`.

4.  Update the `for` loop to use the enumerate function so you can get and use the index. Alter the condition to look for number `36` and print out the following: `‘Number found at position: ‘, index number`

5.  Next, create a new variable called `count` and assign it a value of `0` and place it outside the for loop.

6.  Inside the for loop increment the counter by `1`.

7.  Add a print statement outside the for loop to print the value of the `count` variable.

8.  Finally, add a `break` statement directly after the print statement inside the if condition for finding the number. 

```python
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)
```










# Module 02 - Basic Programming with Python






## Function and variable scope

### Functions and variables
It is essential to understand the levels of scope in Python and how things can be accessed from the four different scope levels. Below are the four scope levels and a brief explanation of where and how they are used.

1. Local scope

**LOCAL SCOPE** refers to a variable that are declared **inside a function**. For example, in the code below, the variable `total` is only available to the code within the `get_total()` function. Anything outside of this function will not have access to it.

```python
def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))


# Accessing variable outside of the function:
print(total)
NameError: name 'total' is not defined
```

When you attempt to access total outside of the function, Python raises a `NameError` because the variable is out of scope.


2. Enclosing scope

**ENCLOSING SCOPE** refers to a function inside another function or what is commonly called a **nested function**. 

In the code below, I added a nested function called `double_it` to the `get_total` function. 

As `double_it()` is inside the scope of the `get_total()` function, it can access the variable total declared in the enclosing function. However, the local variable double, defined inside double_it(), cannot be accessed from inside the get_total() function. The function double_it() is also called the inner function.

```python
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()

```

3. Global scope

**Global scope** is when a variable is declared outside of a function. This means it can be accessed from anywhere. 

In the code below, I added a global variable called `special`. This can then be accessed from both functions `get_total()` and `double_it()`:

```python

special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total

```

The global variable special is declared outside of any function and can be accessed from any part of the program, including inside both `get_total()` and `double_it()`. The variable `total` is enclosed within `get_total()`, and double is local to `double_it()`.


4. Built-in scope
**Built-in scope** includes `built-in` functions and objects (like `print()`, `len()`, etc.), but not reserved keywords (like def, for, if, etc.).





## What are data structures?
This reading introduces you to data structures. So far, you have only stored small bits of data in a variable. This was either an integer, Boolean or a string. 

But what happens if you need to work with more complex information, such as a collection of data like a list of people or a list of companies? 

Data structures are designed for this very purpose.

![Data structures in Python][img020201]

A data structure allows you to organize and arrange your data to perform operations on them. Python has the following built-in data structures: List, dictionary, tuple and set. These are all considered non-primitive data structures, meaning they are classed as objects, this will be explored later in the course. 

Along with the built-in data structures, Python allows users to create their own. Data structures such as Stacks, Queues and Trees can all be created by the user. 

Each data structure can be designed to solve a particular problem or optimize a current solution to make it much more performant.

### Mutability and Immutability
Data Structures can be mutable or immutable. The next question you may ask is, what is mutability? Mutability refers to data inside the data structure that can be modified. For example, you can either change, update, or delete the data when needed. A list is an example of a mutable data structure. The opposite of mutable is immutable. An immutable data structure will not allow modification once the data has been set. The tuple is an example of an immutable data structure.






## Additional resources
Access the links below to learn more about programming in Python.

- Explore the Python website to learn more about control flow: [Learn more about Python](https://docs.python.org/3/tutorial/controlflow.html)

- Check out W3Scools to learn more about Conditional Operators: [W3Schools](https://www.w3schools.in/what-is-conditional-operator)

- Learn more about conditional statements at the Real Python website: [realpython.com](https://realpython.com/python-conditional-statements/)
















[img010101]: /back-end-development/public/img010101_path_selected.png
[img010102]: /back-end-development/public/img010102_initial_screen.png
[img010103]: /back-end-development/public/img010103_mac_install_app.png
[img010104]: /back-end-development/public/img010104_extensions_icon.png
[img010105]: /back-end-development/public/img010105_python_extension.png
[img010106]: /back-end-development/public/img010106_Screenshot-2022-06-23-at-16.58.30.png
[img010107]: /back-end-development/public/img010107_Screenshot-2022-06-23-at-17.04.00.png
[img010108]: /back-end-development/public/img010108_Screenshot-2022-06-23-at-17.12.24.png

[img020101]: /back-end-development/public/img020101_For-Loop-Program.png
[img020102]: /back-end-development/public/img020102_BED_C2M1L3_item07-img02.png
[img020201]: /back-end-development/public/img020201_item04-img01.png