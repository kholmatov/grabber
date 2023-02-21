The web application's functionality is to retrieve information about a specific Android application available on the Aptoide mobile application marketplace (https://en.aptoide.com/) and display it to the user.

What is inside?
===========
The application is packaged in a Docker container..

Project Structure
=================
```
scrapy
    .
    ├── Dockerfile - is a text document containing all the commands for building the image
    ├── README.md - a text file that is distributed with the software and contains information about it.
    ├── app - application directory
    │   ├── __init__.py
    │   ├── api.py - script to run FastAPI
    │   ├── spiders 
    │   │   ├── __init__.py
    │   │   ├── aptoide.py - this is a special class for parsing information from the site en.aptoide.com
    │   │   └── spider.py - file for downloading pages from sites
    │   └── test_api.py - file pytest
    ├── requirements.txt - list of external dependencies
    ├── run_app.sh - server startup script
    └── run_test.sh - test run script and check files on demand pep8
```
How to use?
=================

How to run REST API service locally on port 8000:
* We give permission to execute the script `chmod +x run_app.sh`
* Run the command `./run_app.sh`
* After running the commands, the application will start listening for requests at `0.0.0.0:8000`.
* After that, the web interface will become available at `http://0.0.0.0:8000/docs`
* Use Swagger as HTML page for demo

How to run tests?
-----------------------------
* We give permission to execute the script `chmod +x run_test.sh`
* Run the command `./run_test.sh`

Technology stack:
-----------------
* Docker - is a platform designed to help developers build, share, and run modern applications.
* asyncio - The library for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.
* AIOHTTP - asynchronous HTTP Client/Server for asyncio and Python
* Mypy - is an optional static type checker for Python that aims to combine the benefits of dynamic (or 'duck') typing and static typing.
* FastAPI - API web framework
* beautifulsoup4 - is a Python library for pulling data out of HTML and XML files
 
Test:
-----
* Pytest - the pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
* Pylama - code audit tool for python.

Logs:
-----
* Logs are collected and stored using docker logs

Summary
-------
This project was implemented on a limited time and resource basis.
What else I would  like to implement in this project:
* Separate logging level for each request and saving them to an external database for analysis and error detection
* Kubernetes setup and load balancer for scaling
* System Health Monitoring
* System caching and checking for information updates
* Stress testing
* Connecting dynamic proxy server
* Security and anti-spam system


