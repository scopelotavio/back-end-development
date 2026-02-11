








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