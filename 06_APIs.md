








# Module 01 - REST APIs





## HTTP methods, status codes and response types
                     

### Introduction 
You already know that `HTTP` methods and status codes play an essential role in `REST APIs`. It is important to keep to the conventions for `HTTP` methods and status codes for two reasons. Firstly, if you follow conventions from the developing phase, it will be much easier to avoid bugs in your code and deploy the final project on the production server. Secondly, it makes it easier for other developers to use your APIs. This reading highlights the most important HTTP methods, status codes and API response types that you will use when working on API projects.


### HTTP methods
In the world of `REST APIs`, one endpoint can perform multiple tasks. It can deliver a resource, create a new resource, update or delete it. The endpoint remains the same while the action varies. When a client invokes an API, how does the API developer know which of the multiple actions should be performed?  This is where HTTP methods come in.   

HTTP methods or request types tell the API endpoint what it should do with the resources. It defines the action. The API developer makes decisions and manipulates resources appropriately based on the HTTP methods in an HTTP request. Here is a list of the most used HTTP methods and which action you should initiate for those calls. 


| HTTP method | Action |
| -- | -- |
| GET | Returns the requested resource. If not found, returns a 404 Not Found status code. |
| POST | Creates a record. The POST request always comes with an HTTP request body containing JSON or Form URL encoded data, which is also called a payload. If the data is valid, the API endpoint will create a new resource based on these data. Although you can create multiple resources with a single POST call, it is not considered a best practice to do so.
| PUT | Instructs the API to replace a resource. Like a POST request, the PUT request also comes with data. A PUT request usually supplies all data for a particular resource so that the API developer can fully replace that resource with the provided data. A PUT request deals with a single resource.  
| PATCH | Tells the API to update a part of the resource. Note the difference between a PUT and a PATCH call. A PUT call replaces the complete resource, while the PATCH call only updates some parts. A PATCH request also deals with a single record.  
| DELETE | Instructs the API to delete a resource.


### Example calls
| HTTP method | Sample endpoints | Query string / payload |
| -- | -- | -- |
| HTTP method | Sample endpoints | Query string / payload |
| :--- | :--- | :--- |
| `GET` | `/api/menu-items`<br>`/api/menu-items/1`<br>`/api/menu-items?category=appetizers`<br>`/api/menu-items?perpage=3&page=2` | A `GET` call doesn’t need a payload. However, `GET` calls can be accompanied by query string parameters and their values to filter the API output. |
| `POST` | `/api/menu-items`<br>`/api/orders` | Here’s a sample JSON payload for the `/api/menu-items` endpoint to create a new resource:<br><br>`{`<br>`"title":"Beef Steak",`<br>`"price": 5.50,`<br>`"category":"main",`<br>`}` |
| `PUT` | `/api/menu-items/1`<br>`/api/orders/1` | Here’s a sample JSON payload for this endpoint `/api/menu-items/1` to completely replace it. Note that you need to supply all data for a `PUT` request.<br><br>`{`<br>`"title":"Chicken Steak",`<br>`"price": 2.50,`<br>`"category":"main",`<br>`}` |
| `PATCH` | `/api/menu-items/1`<br>`/api/orders/1` | Here’s a sample JSON payload for this endpoint `/api/menu-items/1` to partially update this resource<br>`{`<br>`"price": 3.00`<br>`}` |
| `DELETE` | `/api/menu-items`<br>`/api/menu-items/1`<br>`/api/orders`<br>`/api/orders/1` | When the `DELETE` call is sent to a collection endpoint, like `/api/menu-items` the API developer should delete the entire collection. When it is sent to a particular resource, like this, `/api/menu-items/1`, then the API developer should delete only that resource. |


### Status codes
Sending appropriate status codes with every API response is essential. And as a developer, you should not just pick any code. Every status code has meaning, so you should choose the most appropriate one based on the situation. Here’s a list of the status code ranges and their purposes. 

| Status code range | Purpose |
| :--- | :--- |
| `100–199` | This range is mainly used to pass on some information. For example, sometimes an API needs time to process the request and it can’t instantly deliver the result. In such a case, the API developer can set it to keep returning `102 - Processing` until the result is ready. This way, the client understands that the result isn’t ready and should be checked again. |
| `200–299` | These are the success codes. If the client requests something and the API acts successfully, it should deliver the output with one of these status codes.<br><br>For example, for a `PUT`, `PATCH`, or `DELETE` call, you can return `200 - Successful` if the operation was successful. For a successful `POST` call, you can set it to return a `201 - Created` status code when the resource has been created successfully. |
| `300–399` | These are the redirection codes. Suppose as an API developer, you changed the API endpoint from `/api/items` to `/api/menu-items`. If the client makes an API call to `/api/items`, then you can redirect the client to this new endpoint `/api/menu-items` with a `301 - Permanently moved` status code so that the client can make new calls to that endpoint next time. |
| `400–499` | 4xx status codes are used in the following situation: if the client requests something that does not exist, sends an invalid payload with insufficient data, or wants to perform an action that the client is not authorized for.<br><br>For the above scenarios, the appropriate status codes will be:<br><br>• `404 - Not Found` if the client requests something that doesn’t exist,<br>• `400 - Bad Request` if a client sends an invalid payload with insufficient data,<br>• `401 - Unauthorized`,<br>• `403 - Forbidden` if the client tries to perform an action it's not authorized for. |
| `500–599` | These alarming status codes are usually automatically generated on the server side if something goes wrong in the code, and the API developer doesn't write code to deal with those errors. For example, a client requests a non-existing resource, and the API developer tries to display that resource without adequately checking if that resource exists in the database. Or if the API developer didn't validate the incoming data and attempted to create a new resource with invalid or insufficient data. You, as an API developer, should always avoid 5xx errors. |


### Response types
These days, the most common response types involved with REST APIs are `JSON`, `XML`, `plain text`, and sometimes `YAML`. Frameworks like DRF come with built-in renderer classes that can convert the data into an appropriate format and display it correctly.

There are also third-party renderers available for this job. While making an API call, the client can specify its desired response format with the Accept HTTP header. And that header should be considered to deliver the result in that format using the render classes. Here’s a list of HTTP headers for different response types.  

| Response type | Request header |
| :--- | :--- |
| HTML | `Accept: text/html` |
| JSON and JSONP | `Accept: application/json` |
| XML | `Accept: application/xml`<br>`Accept: text/xml` |
| YAML | `Accept: application/yaml`<br>`Accept: application/x-yaml`<br>`Accept: text/yaml` |


### Conclusion
In this reading, you learned about different types of `HTTP` methods, status codes, and `API` response types.





## Good routes versus bad routes



### Introduction 

Naming your `API` properly is the first step in designing a good API. When the API name follows a convention, it provides lots of information about the API and its purpose. To create a meaningful API endpoint, you need to follow some simple guidelines and rules. 

In this reading, you will learn about API naming conventions and familiarize yourself with good API endpoints vs. bad API endpoints, or good and bad routes.


### Rule 01: Everything in lowercase, with hyphens and not abridged 
The `URI` of your API should always be in **lowercase**. Do not use camelCase, PascalCase or Title case when you design your API. Also, separate multiple words using **hyphens**, not underscores. Do not keep abridged, or shortened, words in your URI; always use the full and meaningful form.

If your API accepts a `variable`, you should always represent it in **camelCase**, and wrap it inside a set of curly braces `{}`.

Let’s examine the following examples.

| URI | Status | Why |
| :--- | :--- | :--- |
| `/customers` | Good | Plural and lowercase
| `/customers/16/phone-number` | Good | Lowercase and hyphen used to separate words
| `/customers/16/address/home` | Good | Lowercase, no trailing slash, displays the hierarchical relationship with forward slashes.
| `/users/{userId}` | Good | Variable in camelCase, and no hyphen in the variable name
| `/Customers` | Bad | Title case
| `/generalMembers` | Bad | camelCase, no hyphens to separate words
| `/MenuItems` <br> `/GeneralMembers` | Bad | Pascal case
| `/customers/16/tel-no` | Bad | Abbreviation
| `/customers/16/phone_number` | Bad | Underscores
| `/customers/16/phonenumber` | Bad | No separation of words
| `/users/{user-id}` | Bad | Variable should be in camelCase, and hyphen between words


### Rule 02: Use a forward slash to indicate a hierarchical relationship
In your API URI, always use the **forward slash**  to indicate a hierarchical relationship. To understand this rule, consider the following scenarios and the relationship from the API endpoints. 

A store can have customers who have placed many orders and each of these orders can have delivery addresses, menu items and bills. 

| URI | Status |
| :--- | :--- |
| `/store/customers/{customerId}/orders` | Good |
| `/store/orders/{orderId}` | Good |
| `/store/orders/{orderId}/menu-items` | Good |

Similarly, a library can have books from many authors. Each of these books has an ISBN number.

| URI | Status |
| :--- | :--- |
| `/library/authors/books` | Good |
| `/library/book/{bookId}/isbn` | Good |

### Rule 03: Use nouns for resource names, not verbs
One of the most prominent features of REST APIs is that it uses nouns to indicate resources, not verbs. And you should always stick to this rule when designing your API. You should also use plural nouns to indicate a collection.

| URI | Expects | Status | Why |
| :--- | :--- | :--- | :--- |
| `/orders` | Collection | Good | Uses a noun, not a verb |
| `/users/{userId}` | Single user | Good | Uses a noun and proper hierarchical relationship and naming convention |
| `/order` | Collection | Bad | Uses plural nouns for collections |
| `/getOrder` | Single resource | Bad | Uses a verb, camelCase |
| `/getUser/{userId}` | Single user | Bad | Uses a verb, camelCase |

### Rule 04: Avoid special characters 
You should always avoid special characters in your API endpoints. They can be confusing and technically complex for your users. Consider the following bad examples.

| URI | Status | Why |
| :--- | :--- | :--- |
| `/users/12\|23\|23/address` | Bad | Special character \| |
| `/orders/16/menu^items` | Bad | Special character ^ |

If your API can accept multiple user ids, then they should be separated using a comma, as demonstrated below.

| URI | Status | Why |
| :--- | :--- | :--- |
| `/users/12,23,23/address` | Good | Uses a comma for separation |


### Rule 05: Avoid file extensions in URI
You should always avoid file extensions in your API names. For example, if your API can deliver an output in both JSON and XML format, it should never look like this.

| URI | Status | Why |
| :--- | :--- | :--- |
| `/sports/basketball/teams/{teamId}.json` | Bad | File extension at the end |
| `/sports/basketball/teams/{teamId}.xml` | Bad | File extension at the end |

Instead, your client should be able to indicate its expected format in a query string, just like this. 

| URI | Status | Why |
| :--- | :--- | :--- |
| `/sports/basketball/teams/{teamId}?format=json` | Good | No file extension |
| `/sports/basketball/teams/{teamId}?format=xml` | Good | No file extension |

Similarly, if your `API` is serving a static file, for example, `CSS` or `JavaScript` files, you should use endpoints like the following to deliver the minified and original source file. You can also use a query string to get the minified or original version.  Some API developers use the output format like file extension at the end of the regular API endpoints, which is also bad practice.    

| URI | Status | Why |
| :--- | :--- | :--- |
| `/assets/js/jquery/3.12/min` | Good | No file extension |
| `/assets/js/jquery/3.12/source` | Good | No file extension |
| `/assets/js/jquery/3.12/?format=min` | Good | No file extension |
| `/assets/js/jquery/3.12/?format=source` | Good | No file extension |
| `/menu-items?format=json` | Good | Perfectly named endpoint with expected output format in a query string |
| `/menu-items.json` | Bad | Uses the expected output format as the file extension |


### Rule 06: Use query parameters to filter when necessary 
When designing your `API`, you should always perform data filtering using a query string. This is the same when you expect some extra parameters, like the number of items per page and page number. 

Consider this example of a travel site. You want to find which locations a particular user has traveled to. And then you want to know which locations in the USA the user has already seen. 

| URI | Status | Why |
| :--- | :--- | :--- |
| `/users/{userId}/locations` | Good | Hierarchical |
| `/users/{userId}/locations?country=USA` | Good | camelCase, no separation of words |
| `/articles?per-page=10&page=2` | Good | Proper use of query string |
| `/users/{userId}/locations/USA` | Bad | Doesn't use a query string to filter data |
| `/articles/page/2/items-per-page/10` | Bad | Redundant and obscure |


### Rule 07: No trailing slash
When sharing your `API` endpoint with others in your team, or in public, avoid using a trailing slash `/` at the end of your API endpoints. Consider the following examples.

| URI | Status | Why |
| :--- | :--- | :--- |
| `/users/{userId}` | Good | No trailing slash |
| `/articles/{articleId}/author` | Good | No trailing slash |
| `/users/{userId}/` | Bad | Trailing slash |
| `/articles/{articleId}/author/` | Bad | Trailing slash |


### Conclusion
Now you understand how to create `REST API` endpoints with good names. Remember, a consistent naming strategy for your API is one of the most important design decisions for the whole project!






## Installing VS Code
This reading walks you through the steps to set up an Integrated Development Environment, or IDE, on a Windows and on a Mac (further down below). The IDE you'll be using in the course is `Visual Studio Code`, which Microsoft provides for free and comes with a wealth of plugins and extensions to make your life as a developer easier. You have two options for using Visual Studio Code to complete your course activities:


### Option 1: Use Visual Studio Code in-browser with Coursera Labs
Coursera’s platform offers an in-browser version of Visual Studio Code which is preconfigured and requires no local setup. You can access the Visual Studio Code environment through the “Lab” items included in this course. Your work and files will be saved and available within this in-browser lab while you have course access.


### Option 2: Work on your local device
You can also choose to complete your work on your local machine if you prefer. This will require a few steps of set up in advance. 

First, you need to download the IDE from Microsoft's website - https://code.visualstudio.com/download
. Select the download based on your operating system.


### Windows
- **Step 1:** Download the Windows installer.
- **Step 2:** Open the file to install it once the download is complete.
- **Step 3:** Review and accept the license agreement, then click Next.
![Set up Visual Studio Code on Microsoft Step 3][img060101]
- **Step 4:** Keep the default value when prompted for the destination location and click next.
![Set up Microsoft Visual Studio Code Step 4][img060102]
- **Step 5:** On the additional tasks view, make sure that Add to PATH is selected. 
![Set up Microsoft Visual Studio Code Step 5][img060103]
- **Step 6:** Click next.
- **Step 7:** Click install when the ready to install page appears.
![Set up Microsoft Visual Studio Code Step 7 ][img060104]
- **Step 8:** Click finish once completed, and the application will launch.


### Mac
- **Step 1:** Download the application based on the chipset you have. M1 macs use Apple Silicon, and older Macs use Intel. If you are not sure, choose the Universal option.
- **Step 2:** Go to your Downloads folder once the download is complete. 
- **Step 3:** Double-click the zip file to extract the contents.
- **Step 4:** Drag and drop the .app file to the application link in Finder below.
![Set up Visual Studio Code on Mac Step 4][img060105]
- **Step 5:** Open the app.


### Linux
Please refer to the [official Linux installation guide](https://code.visualstudio.com/docs/setup/linux) for Visual Studio Code.


### Selecting a working directory
Now that you have Visual Studio Code set up create a folder on your device that you'll use to do course exercises. Open Visual Studio Code, go to `File` and select `Open Folder`. Using the file browser, select the folder you just created.

Congratulations, you're set up now to begin writing some code.





## Setting up tools and environment

### Introduction
Before you can start an API project you need to have the right setup on your computer. In this reading, you will learn how to configure necessary extensions in VS Code. You will also learn how to use pipenv to manage the packages and the virtual environment for your API projects.


### Step 1: Install VS Code
The previous reading guided you through installing Visual Studio code on your computer. This is the first step in setting up your development environment. If you have not installed it yet, go back to 
Installing VS Code and follow the steps.


### Step 2: Install Python
Download and install the latest version of Python from [https://python.org](https://python.org/) or use the software manager for your operating system.


### Step 3: Install the VS Code Python extension
Open `VS code` and access the extensions panel from the view menu, the left sidebar or by pressing Command, Shift and X. Search for Python and select the first one from Microsoft. This extension provides features like syntax highlighting, autosuggestions, debugging, and linting, which makes it very useful for Python developers.


### Step 4: Install additional VS Code extensions (optional)
You can also install a few other useful `VS Code` extensions for Python development. Search for: Python Indent by Kevin Rose to correct Python indentation in VS Code, and Djaneiro by Scott Barkman for useful Django snippets.


### Step 5: Install a package manager 
Next, you need to install pipenv, a package manager for Python applications from https://pipenv.pypa.io/en/latest/. `pipenv` lets you easily create virtual environments for your projects so that you can manage your dependencies more efficiently. This allows you to install packages for your projects without conflicting with other versions of the same package used by other projects. 

To install `pipenv`, open your terminal or PowerShell and type the following command:

```python
pip3 install pipenv
```
![pipenv installation command][img060106]

Type in **pipenv** and press enter. A list of commands and options supported by pipenv will display.

![Commands and options supported by pipenv.][img060107]


### Conclusion
You should be set up to start your first `Django API` project using Python. You now know how to install the latest version of Python, the Python extension and other useful extensions in VS Code as well as the package manager pipenv.





## Creating a Django project (steps and code)
 

### Introduction
This Reading will give you an overview of the steps to be taken while working with VS Code using pipenv as your virtual environment while creating a Django project. The project structure can be variable according to the learner preferences, but the one suggested can also be used for ease. 

**Note:** The instructions in this reading may vary slightly from the instructions in the video about creating a `Django` project because the video presumes a preconfigured `Pipfile`. 

**Note:** The commands added below are specific to `MacOS`. The learner will have to make `OS` specific changes such as using keyword python instead of `python3` for Windows OS.  


### Step 1
Open `VS Code` on your computer and click on File. In the drop-down menu select Open Folder and select the folder you have created for the project. 

![Open Folder option under the File drop-down menu.][img060108]

Now click on Terminal and select `New Terminal` from the drop-down menu. This is the main folder that contains all your files for the Django project you are going to create. 


### Step 2
Create a directory for the Django project by running the following command:

`mkdir LittleLemon`


### Step 3
Step inside the LittleLemon directory with the command:

`cd LittleLemon`


### Step 4
Run the following command to create a project in this directory:

`django-admin startproject BookList .`


### Step 5
Run a command to activate pipenv:

`pipenv shell`

**Note:** It is expected that pipenv is installed using pip in your local machine. 


### Step 6
Open the file labeled **Pipfile** that was created inside the project directory. This file contains details of the dependencies for the project. Update it with the following code and save the file. 

![The Pipfile in the project directory.][img060109]

```python
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"
 
[packages]
django = "*"
djangorestframework = "*"
djangorestframework-xml = "*"
djoser = "*"
 
[dev-packages]
 
[requires]
python_version = "3.9"
```


### Step 7
Run this command to install the dependencies using the updated Pipfile: 

`pipenv install`

**Note:** Alternatively, you can also use commands such as pipenv install django to install specific packages. This will also update the Pipfile. 


### Step 8
Now run this command to create a Django app:

`python3 manage.py startapp LittleLemonDRF`


### Step 9
Run the command to start the server to test if the installation was successful.

`python3 manage.py runserver`

Stop the server by pressing **Ctrl + C** while you are in the Terminal window.


### Step 10
Create the `urls.py` file in the app-level LittleLemonDRF directory.

Paste the following code inside it:

```python
from django.urls import path
from . import views
 
urlpatterns = [
    path('ratings', views.RatingsView.as_view()),
]
```

**Note: The specific url configurations will differ according to the views created**


### Step 11
Open the **urls.py** file in the project-level directory and update the code as follow:

```python
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('LittleLemonDRF.urls')),
]
```

**Note:** The specific url configurations at the project-level will vary according to the name of the app created. 


### Concluding Thoughts
In this reading, you learnt about the initial setup you need to make on your local machine while running VS Code with pipenv for creating a Django project.      





## Exercise: Know your tools


### Introduction
In this exercise, you are going to use the `REST API` client Insomnia to make HTTP Requests so make sure you’ve installed it on your computer. You will also use the Request and Response Service 
httpbin.org. `Httpbin.org` is an open-source web service that allows you to make HTTP calls without any additional installations or dependencies. 

You will be exploring the different functionalities available in Insomnia such as:
- Creating a `GET` request
- Creating a `POST` request with Form Data
- Creating a `POST` request with JSON Data


#### Software images 
This reading contains software screengrab images. While the software's appearance often evolves with continual updates, the core functionalities and techniques covered in this reading should remain applicable.


### Instructions
To get started, open **Insomnia** on your local device and navigate to the tab labeled **DEBUG**.  
**Note:** The Debug option has now changed to Collection.

![The DEBUG tab in Insomnia][img060110]

If you haven't installed Insomnia yet, you can download the install files at https://insomnia.rest/
   

### Create a GET request
Open the https://httpbin.org/ website and click on **HTTP Methods**. A menu with different HTTP methods will expand which you can add to your endpoints.

![c1m1l2 ITEM 3 The HTTP Methods menu on the httpbin.org website includes options such as DELETE, GET, PATCH and POST.][img060111]


#### Step 1:
In Insomnia, click on the + icon on the left-hand side of the screen and select **HTTP Request** from the drop-down menu.

![The + icon in Insomnia provides access to a menu of different requests including HTTP Request.][img060112]


#### Step 2:
Double-click the request to change its title to `GET` request using Insomnia. 


#### Step 3: 
Click on the `GET` dropdown to see a list of available options and re-select `GET`. 

Update the URL endpoint with the value: https://httpbin.org/get

Press the Send button and notice the JSON output. 

**Note:** Some of the values for the `JSON` such as "origin": “76.197.210.235” will be different. At this point we care only that the JSON is returned. 


#### Step 4:
From the **Body** drop-down option, select Multipart Form. 

Add the following values under New name and New value:

- New name: title
- New value: Lord of the Rings

Press the `Send` button once again and observe the changes.  

Notice that the value of Content-Length has been updated to include the changes.


#### Step 5: 
Update a form entry with the following details:

- New name: author
- New value: JRR Tolkien            

Press the `Send` button once again. Notice that Content-Length has further been updated. 


#### Step 6: 
You can Filter your output using the Filter response body at the section in the bottom right-hand side of Insomnia as indicated in the screenshot below. 

![Filter functionality in Insomnia][img060113]    

Add the following filter inside it:

```json
$.origin
```

It should update the *Preview*. The output will appear similar to what is displayed in the screenshot below.

![Output when using the $.origin filter in Insomnia][img060114]

#### Step 7: 
Modify the filter incrementally as below which should produce the respective outputs.

```json
$.headers
```

![Output when using the  $.headers filter in Insomnia.][img060115]

```http
$.headers.Content-Type
```

![Output using the  $.headers.Content-Type filter in Insomia][img060116]

**Note:** *The dot operator is used here to explore the contents of the JSON output. Also notice the value of the Content-Type is form-data because you selected Multipart form.*

Clear the contents of the Filter response body. 


#### Step 8:
Now deselect the option for the name title and re-create the GET request.
                                        

Notice the change in the Content-Length again.

#### Additional step

Now that you know the steps to create a GET request in Insomnia, you can explore different configuration settings by following the steps discussed to get more accustomed to the tool.



### Create a POST request with Form Data


#### Step 1:
Keeping the contents of the form data the same, update the request type to POST and update the URL endpoint to:

https://httpbin.org/post
  

![POST request selected from drop-down menu in Insomnia.][img060117]

Press the **Send** button again. The output should appear as below:

![Form data output of a POST request in Insomnia][img060118]

Notice that the contents of the form are updated inside the output for the POST request. 


#### Step 2:
Explore the other tabs under the output such as Headers, Cookies and Timeline.

![Tabs in the output section of Insomnia like Headers, Cookies and Timeline][img060119]

#### Step 3:      
Since you have modified the same `HTTP request`, update the changes for the title of the request in the left-hand section to POST request using Insomnia.

![New title of the POST request in Insomnia][img060120]



### Create a POST request with JSON Data

#### Step 1:
Now further create another HTTP Request like the one at the beginning by pressing the + icon and selecting HTTP Request. 

#### Step 2:
Update the request type to POST and the request label as:

POST request using JSON object

Note: The labels are for reference and independent of the request type.

Paste the same URL endpoint that you used earlier in the URL text-box:

`https://httpbin.org/post`

The updated view should appear as below:

![Insomnia with two POST requests appearing in the left-hand pane][img060121]

#### Step 3:
Under the **Body** dropdown option, select JSON as the text input.

![JSON is an option under the text input section in the dropdown menu of the Body option.][img060122]

A text input area should appear as below.

![A text input area that appears after selecting JSON as the text input in Insomnia][img060123]

Step 4:
Enter the following content inside the text input area:

```json
{
    "title": "Lord of the Rings",
    "author": "JRR Tolkien",
    "published" : {
        "year": 1954,
        "month": "july",
        "day" : 29
    }
}
```

**Note:** When you run the code you have copied inside Insomnia, you may face a small inconsistency such as the value of JSON showing “null”. If that happens, you have to remove the extra indentations that are getting added inside the JSON data that you have added on Insomnia. The simple rule of thumb is removing all the extra space and pressing the Tab key on your keyboard. 

Press the Send button. 

The output for the JSON input should appear as below: 

![Output of a POST request with JSON set as the text input.][img060124]

Notice the contents entered as JSON object in both the data and json field inside the JSON output. 

#### Step 5:

Add the following line to Filter response body:

`$.json.published.year`

The output will be as follows:

```http
[
	1954
]
```

- **Modify the Filter response body as follow:**

`$[json][published][day]`

The output will be as follows:

```http
[
	29
]
```

### Concluding Thoughts
There are several configuration options inside Insomnia. While using a `REST API` client it is good to explore these. You can also get help from other free and open-source API services that provide options to make API calls to access public data. 





## Additional resources
The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this section.

- [Curl command line tool and library for transferring data with URLs](https://curl.se/)
- [HTTPie for web and desktop](https://httpie.io/)
- [Postman API platform for building and using APIs](https://www.postman.com/)
- [Postman Echo service to test REST clients and make sample API calls](https://postman-echo.com/)
- [Insomnia homepage](https://insomnia.rest/)
- [Getting started with Insomnia](https://docs.insomnia.rest/insomnia/get-started)
- [Httpbin HTTP request and response service](https://httpbin.org/)
- [Python homepage](https://python.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python Indent by Kevin Rose](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Djaneiro by Scott Barkman](https://marketplace.visualstudio.com/items?itemName=thebarkman.vscode-djaneiro)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [Django](https://www.djangoproject.com/)
- [List of HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)





## Authentication versus authorization


### Introduction
You need to secure your `APIs` because they provide third-party clients access to your backend data. If you don’t secure your APIs properly, anyone can tamper with the data and access sensitive information. But even if a client is allowed to access the data, you need to control who can do what. This is where `authentication` and `authorization` come in. You now know that although they sound similar, they are not the same. In this reading, you will learn about the difference between authentication and authorization and how you can use it to protect your API endpoints.


### Authentication
`Authentication` is the process of verifying the credentials of a user. Logging into websites with a username and password is a typical example of authentication. When the username and password match, the website recognizes the user and sets some cookies in the user’s browser. When the user visits another page on that website, the browser sends those cookies within the `HTTP` request header. The website recognizes the cookies as well as server-side session data and therefore doesn’t ask for credentials until the user logs out again.  

So, how does this work? `Token-based` authentication usually involves two steps in the API Architecture. First, the client identifies itself with a username and password. Then the API server gives it a `bearer token`. From there, the client includes the bearer token with every API call that it places. The API server verifies it and then allows the client to perform the action or not. This is where authorization comes in, but more on this later.

If the credentials are not valid, the client will receive a `401 - Unauthorized` HTTP status code.

This is like coming to the office on the first day, submitting all your papers and documents, and then receiving your employee card. After that, only your employee card will be sufficient to get inside. Authentication works just like that!

The two steps in the API authentication process can be represented by the following two diagrams. 

#### Authentication process: Getting an access token
![Diagram of the process of getting an access token][img060125]

#### Authenticated API calls
![Diagram of an authenticated API call][img060126]
       

### Authorization
However, even with your employee card, you will not be able to access all the rooms or spaces in the office. There are some places that are only accessible to a certain group of people who have been given that privilege. `Authorization` is exactly like that. Authentication lets you in, authorization lets you act. It checks after authentication if the user has the proper privileges to perform some tasks. 

On the server side, this is typically done by assigning the user to a group or a set of groups. Then, after verifying the token, the code checks if the user belongs to the appropriate group to perform that task. If not, the client will receive a 403 - Forbidden HTTP status code.  

#### API authorization
![Diagram of API authorization][img060127]

This extra authorization layer in the API architecture ensures that only people with proper privileges can access and modify data. An authorization system in an API project is very important because it prevents data corruption and data breaches. 


### Implementing authorization 
Privileges are the tasks that an API user performs, and they are the building blocks of an authorization layer. First, as an API developer, you identify the required privileges in your project. For example, for a bookshop, there might be the following types of privileges:

- Browse the books
- Add new books
- Edit books
- Delete books
- Place orders 

There can be many other privileges like this. And not every user will have every privilege. For instance, regular customers are not allowed to add and edit books, even if they are properly authenticated. Only managers are allowed to perform those operations. 

So, after identifying the privileges, you carefully distribute all these privileges into multiple roles. And then, the authorization check is done in the backend code of each API endpoint that requires a user role check. The developer verifies if the user belongs to the appropriate group or roles, and then makes the decision to allow or deny the action. 


### User groups in Django
The `Django` admin panel comes with excellent support for the user group system. If you log into the admin panel, you will find two distinct sections – users and groups.

![Django admin panel with two sections for users and groups][img060128]

From here, you can create groups or roles like Manager, Editor, Customer, Admin and so on and assign privileges to these groups. If you click on the Add button next to the groups, you will be taken to a screen where you can create new groups. The Django admin panel will list all the necessary privileges based on the models in your project. Here is a screen that indicates the available privileges for a bookshop.     

![Django admin panel with bookshop privileges listed][img060129]
     
On this screen, you can create an Editor role, for instance, and add privileges to it.

![Django admin panel with Editor role and privileges][img060130]

Or you can create a Customer role that will have different privileges. 

![Django admin panel with Customer role and privileges][img060131]

The Django admin panel allows you to manage groups throughout the project. You can add and remove privileges to groups as the project grows.

![Django admin panel with two user roles][img060132]

But creating groups with privileges is not enough. After creating these groups and assigning users to them, you need to write some code in the function or class-based views that determine if authenticated users belong to those groups and then make decisions based on that. But you will learn to do this later in the course.


### Conclusion
`Authentication` and `authorization` are concepts that differ in function and how they are set up in an API architecture. The knowledge you gained in this reading about user groups, roles and privileges lay the groundwork for all the steps that you will learn later on for setting up a proper security layer in your API projects. 




# PUBLIC

[img060101]: /back-end-development/public/img060101_vscode_license.png
[img060102]: /back-end-development/public/img060102_vscode_install_location.png
[img060103]: /back-end-development/public/img060103_path_selected.png
[img060104]: /back-end-development/public/img060104_vscode_ready_to_install.png
[img060105]: /back-end-development/public/img060105_mac_install_app.png
[img060106]: /back-end-development/public/img060106_Setting-up-tools-and-environment-1.png
[img060107]: /back-end-development/public/img060107_Setting-up-tools-and-environment-2.png
[img060108]: /back-end-development/public/img060108_image.png
[img060109]: /back-end-development/public/img060109_image.png
[img060110]: /back-end-development/public/img060110_image.png
[img060111]: /back-end-development/public/img060111_image.png
[img060112]: /back-end-development/public/img060112_image.png
[img060113]: /back-end-development/public/img060113_image.png
[img060114]: /back-end-development/public/img060114_image.png
[img060115]: /back-end-development/public/img060115_image.png
[img060116]: /back-end-development/public/img060116_image.png
[img060117]: /back-end-development/public/img060117_image.png
[img060118]: /back-end-development/public/img060118_image.png
[img060119]: /back-end-development/public/img060119_image.png
[img060120]: /back-end-development/public/img060120_image.png
[img060121]: /back-end-development/public/img060121_image.png
[img060122]: /back-end-development/public/img060122_image.png
[img060123]: /back-end-development/public/img060123_image.png
[img060124]: /back-end-development/public/img060124_image.png
[img060125]: /back-end-development/public/img060125_Authentication-and-authorization-1.png
[img060126]: /back-end-development/public/img060126_Authentication-and-authorization-2.png
[img060127]: /back-end-development/public/img060127_Authentication-and-authorization-3.png
[img060128]: /back-end-development/public/img060128_Authentication-and-authorization-4.png
[img060129]: /back-end-development/public/img060129_Authentication-and-authorization-5.png
[img060130]: /back-end-development/public/img060130_Authentication-and-authorization-6.png
[img060131]: /back-end-development/public/img060131_Authentication-and-authorization-7.png
[img060132]: /back-end-development/public/img060132_Authentication-and-authorization-8.png