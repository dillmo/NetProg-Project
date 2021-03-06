# NetProg-Project

Our project has two parts:
1. A server that hosts a mock e-commerce website
2. A client that can monitor that site for items and automatically buy the items
   as they come into stock

Together, these components form a demonstration of how an e-commerce
purchases can be automated.

## Running this Project

Dependencies for this project are listed in the file, "dependencies." We
recommend installing them using pip: `pip install -r dependencies`.

The server needs to be running for the client to interact with it. Before
running the server, the databases need to be created. Navigate to the
"src/server" folder, then run `python manage.py migrate`. After making
migrations, start the server by running `python manage.py runserver`. This
will host a server on "localhost:8000" which can be shut down with "Ctrl+C."

Now that the server is running, a Selenium server with the Gecko backend
needs be run in the background. The client will interface with this server to
remotely control Mozilla Firefox. Download Selenium Standalone Server from
https://www.seleniumhq.org/download/, then download geckodriver from
https://github.com/mozilla/geckodriver/releases. Put both files in the same
folder, then run the Selenium server.

Note: If the account you create on the server uses a username/password
combination other than "iamausername"/"iamapassword," please update the dummy
username and password stored in src/client/main.py

Finally, the client can be run from "src/client/main.py" like a typical
Python program. To begin with, it will run in a loop and wait for any product
named "Cat food" to show up on the server website. Once you create a product
named "Cat food" using the website's interface, the client will go through
the complete process of buying the product within 3-5 seconds.