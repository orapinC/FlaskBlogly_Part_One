### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
   
   JavaScript is used mainly for web development (both front- and back-end) and mobile app. However, Python, although can be used for web development (back-end), it has a wide range of use, particulary for data science, machine learning, making servers, etc.
   ***

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  1. using if-else condition to check if the key is present or not:
    ```
    dic = {"a":1, "b":2}
    if "c" in dic:
      print(dic["c"])
    else:
      print("Key not found")
    ```
  
  2. using get(key,def_val) method
    ```
    dic = {"a":1, "b":2}
    print(dic.get("c","Not found"))
    ```
  ---

- What is a unit test?
  
  Unit test tests one "unit" of functionality, typically, one function or method. It does not test the integration of components.
  ***

- What is an integration test?
  
  Integration test tests the whole software modules, or multiple software modules are combined and then tested as a group.
  ***

- What is the role of web application framework, like Flask?
  
  WAF is a software framework that makes the tasks of building and deploying web applications much easier than working without it. WAF handle web services, web resources, and web APIs. 
  ***

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  - Use URL parameter when it is the subject or main point of the page. It is something that integral to the content.
  - Use URL query parameter when it is an extra information about the page or a modifier for the information that we are going to view.
  ***
- How do you collect data from a URL placeholder parameter using Flask?
  Use the placeholder parameter to access the data from the database that match the paramenter.
  For example: we can access peter profile by use peter inplace of placeholder parameter <username> in th router and access peter's profile from the database (USERS).
  ```
  USERS = {
    "peter": "Peter the cool dog.",
    "pop": "pop the favorite soda",
  }
  @app.route("/user/<username>)
  def user_profile(username):
    name = USERS[username]
    return f"<h1>{name"}</h1>
  ***

- How do you collect data from the query string using Flask?
  
  By import request from flask and using request.args.
  For example: for a url like /search?term=fun
  1. import request from flask
  2. use request.args
  ```
  from flask import Flask, request
  @app.route("/search")
  def search():
    term = request.args["term"]
    return f'<h3>Searching for {term}</h3>'
  ```
  Then, we use term to search in database to find info that matches term.
  ***
- How do you collect data from the body of the request using Flask?
  We can access data by frist .json(), then, look for data we want and collect it.
  for example:
  ```
  response = requests.get(url)
  data = response.json()
  result = data["result"]
  ```
  ***
- What is a cookie and what kinds of things are they commonly used for?
  Cookies are name/string-value pair stored by the browser. 
  The server tells browser to store them.
  Browser sends cookies to the server with each request.
  Cookies are used for security purpose. They are used to authenticate users and help to ensure that only the actual ower of an account can access that account.
  ***
- What is the session object in Flask?
  Flask sessions are a "majic dictionary." Users can treat session as a dictionary. Sessions contain information for the current browser. They are "serialized" and "signed," so that users cannot modified data. Flask stored sessions in the browser as cookie. By default, Flask uses the Werkzeug to provide "sedure cookie" as session system. It works by serializing the session data, compressing it, and base64 encoding it.
  ***
- What does Flask's `jsonify()` do?
    Flask's jsonify() funcation automatically sets the response headers and content type for JSON responses, and allows us to return JSON-formatted data from our route handlers.
    
  ***
