
python_questions = [
    {
        "number": 1,
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.",
        "learned": False
    },
    {
        "number": 2,
        "question": "What is the difference between Python 2 and Python 3?",
        "answer": "Python 2 and Python 3 are two major versions of the Python programming language. Python 3 introduced several improvements and backward-incompatible changes compared to Python 2, including better Unicode support, syntax enhancements, and the print function becoming a built-in function.",
        "learned": False
    },
    {
        "number": 3,
        "question": "What are the basic data types in Python?",
        "answer": "The basic data types in Python include integers, floating-point numbers, strings, booleans, and complex numbers.",
        "learned": False
    },
    {
        "number": 4,
        "question": "What is PEP 8?",
        "answer": "PEP 8 is a style guide for Python code written by Guido van Rossum, Barry Warsaw, and Nick Coghlan. It provides guidelines and best practices for writing clean, readable code.",
        "learned": False
    },
    {
        "number": 5,
        "question": "What is a Python module?",
        "answer": "A Python module is a file containing Python code that can be imported and used in other Python scripts or modules. It allows for code organization, reusability, and encapsulation.",
        "learned": False
    },
    {
        "number": 6,
        "question": "What is a Python package?",
        "answer": "A Python package is a directory containing Python modules and an optional __init__.py file. It allows for hierarchical organization of modules and facilitates namespace management.",
        "learned": False
    },
    {
        "number": 7,
        "question": "What is a Python function?",
        "answer": "A Python function is a block of reusable code that performs a specific task. It can take input arguments, perform operations, and optionally return a result.",
        "learned": False
    },
    {
        "number": 8,
        "question": "What is a Python class?",
        "answer": "A Python class is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that objects of the class will have.",
        "learned": False
    },
    {
        "number": 9,
        "question": "What is inheritance in Python?",
        "answer": "Inheritance is a mechanism in object-oriented programming where a class (subclass) inherits properties and behaviors from another class (superclass). It allows for code reuse and promotes code organization.",
        "learned": False
    },
    {
        "number": 10,
        "question": "What is encapsulation in Python?",
        "answer": "Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data within a single unit (class). It hides the internal state of an object from outside access and ensures data integrity.",
        "learned": False
    },
    {
        "number": 11,
        "question": "What is polymorphism in Python?",
        "answer": "Polymorphism is the ability of objects to take on different forms or behave differently based on the context. In Python, polymorphism can be achieved through method overriding and method overloading.",
        "learned": False
    },
    {
        "number": 12,
        "question": "What is method overriding in Python?",
        "answer": "Method overriding is the process of defining a method in a subclass that has the same name and signature as a method in the superclass. It allows the subclass to provide a specific implementation of the method while retaining the interface defined by the superclass.",
        "learned": False
    },
    {
        "number": 13,
        "question": "What is method overloading in Python?",
        "answer": "Method overloading is the ability to define multiple methods with the same name but different parameters in a class. Python does not support method overloading by default, but it can be achieved using default parameter values or variable-length argument lists.",
        "learned": False
    },
    {
        "number": 14,
        "question": "What is a constructor in Python?",
        "answer": "A constructor is a special method in a Python class that is automatically called when an object of the class is created. It is used to initialize the object's state.",
        "learned": False
    },
    {
        "number": 15,
        "question": "What is a destructor in Python?",
        "answer": "A destructor is a special method in a Python class that is automatically called when an object is destroyed or garbage-collected. It is used to release resources or perform cleanup operations.",
        "learned": False
    },
    {
        "number": 16,
        "question": "What is method resolution order (MRO) in Python?",
        "answer": "Method resolution order (MRO) is the order in which Python searches for methods and attributes in classes and their superclasses during method invocation or attribute access. It is determined by the C3 linearization algorithm.",
        "learned": False
    },
    {
        "number": 17,
        "question": "What is a class attribute in Python?",
        "answer": "A class attribute is a variable defined within a class that is shared by all instances (objects) of the class. It is accessed using the class name rather than an instance variable.",
        "learned": False
    },
    {
        "number": 18,
        "question": "What is an instance attribute in Python?",
        "answer": "An instance attribute is a variable defined within a class that is unique to each instance (object) of the class. It is accessed using the instance variable.",
        "learned": False
    },
    {
        "number": 19,
        "question": "What is the self variable in Python?",
        "answer": "The self variable is a reference to the current instance of a class. It is used to access instance variables and methods within the class.",
        "learned": False
    },
    {
        "number": 20,
        "question": "What is a static method in Python?",
        "answer": "A static method is a method defined within a class that does not access or modify instance variables. It is called using the class name rather than an instance variable.",
        "learned": False
    },
    {
        "number": 21,
        "question": "What is a class method in Python?",
        "answer": "A class method is a method defined within a class that operates on class-level variables rather than instance variables. It is decorated with the @classmethod decorator and takes the class (cls) as its first parameter.",
        "learned": False
    },
    {
        "number": 22,
        "question": "What is the difference between a class method and a static method in Python?",
        "answer": "A class method operates on class-level variables and takes the class (cls) as its first parameter, whereas a static method does not access or modify instance variables and does not take any implicit parameters.",
        "learned": False
    },
    {
        "number": 23,
        "question": "What is the __init__ method in Python?",
        "answer": "The __init__ method is a special method in a Python class that is called automatically when an object of the class is created. It is used to initialize the object's state.",
        "learned": False
    },
    {
        "number": 24,
        "question": "What is the __str__ method in Python?",
        "answer": "The __str__ method is a special method in a Python class that is called when the str() function is invoked on an object. It should return a string representation of the object.",
        "learned": False
    },
    {
        "number": 25,
        "question": "What is the __repr__ method in Python?",
        "answer": "The __repr__ method is a special method in a Python class that is called when the repr() function is invoked on an object. It should return an unambiguous string representation of the object.",
        "learned": False
    },
    {
        "number": 26,
        "question": "What is a magic method in Python?",
        "answer": "A magic method is a special method in a Python class that is invoked by the Python interpreter in response to certain operations or built-in functions. Examples include __init__, __str__, and __repr__.",
        "learned": False
    },
    {
        "number": 27,
        "question": "What is operator overloading in Python?",
        "answer": "Operator overloading is the ability to define custom behavior for operators such as +, -, *, /, and == in Python classes. It allows objects of a class to behave like built-in types.",
        "learned": False
    },
    {
        "number": 28,
        "question": "What is the purpose of the __add__ method in Python?",
        "answer": "The __add__ method is a magic method in a Python class that is called when the + operator is used with objects of the class. It should return the result of adding two objects together.",
        "learned": False
    },
    {
        "number": 29,
        "question": "What is the purpose of the __eq__ method in Python?",
        "answer": "The __eq__ method is a magic method in a Python class that is called when the == operator is used with objects of the class. It should return True if the objects are equal, and False otherwise.",
        "learned": False
    },
    {
        "number": 30,
        "question": "What is the purpose of the __lt__ method in Python?",
        "answer": "The __lt__ method is a magic method in a Python class that is called when the < operator is used with objects of the class. It should return True if the first object is less than the second object, and False otherwise.",
        "learned": False
    },
    {
        "number": 31,
        "question": "What is a generator in Python?",
        "answer": "A generator is a special type of iterator that generates values on-the-fly rather than storing them in memory. It is implemented using the yield keyword.",
        "learned": False
    },
    {
        "number": 32,
        "question": "What is the difference between range and xrange in Python 2?",
        "answer": "In Python 2, range() returns a list of numbers, while xrange() returns an xrange object, which is a generator-like object that generates numbers on-the-fly. xrange() is more memory-efficient for large ranges.",
        "learned": False
    },
    {
        "number": 33,
        "question": "What is a decorator in Python?",
        "answer": "A decorator is a function that takes another function as input and extends or modifies its behavior without modifying its source code. It is used to add functionality to functions or methods.",
        "learned": False
    },
    {
        "number": 34,
        "question": "What is the @classmethod decorator in Python?",
        "answer": "The @classmethod decorator is used to define a class method in a Python class. It takes the class (cls) as its first parameter rather than an instance of the class.",
        "learned": False
    },
    {
        "number": 35,
        "question": "What is the @staticmethod decorator in Python?",
        "answer": "The @staticmethod decorator is used to define a static method in a Python class. It does not access or modify instance variables and does not take any implicit parameters.",
        "learned": False
    },
    {
        "number": 36,
        "question": "What is a lambda function in Python?",
        "answer": "A lambda function is an anonymous function defined using the lambda keyword. It can take any number of arguments but can only have one expression.",
        "learned": False
    },
    {
        "number": 37,
        "question": "What is the purpose of the filter() function in Python?",
        "answer": "The filter() function is used to filter elements from an iterable (such as a list) based on a given predicate function. It returns an iterator containing the elements for which the predicate function returns True.",
        "learned": False
    },
    {
        "number": 38,
        "question": "What is the purpose of the map() function in Python?",
        "answer": "The map() function is used to apply a given function to each element of an iterable (such as a list) and return an iterator containing the results.",
        "learned": False
    },
    {
        "number": 39,
        "question": "What is the purpose of the reduce() function in Python?",
        "answer": "The reduce() function is used to apply a given function to the elements of an iterable (such as a list) and return a single value. It is similar to the built-in sum() function but can apply any binary function.",
        "learned": False
    },
    {
        "number": 40,
        "question": "What is a list comprehension in Python?",
        "answer": "A list comprehension is a concise way to create lists in Python by applying an expression to each item in an iterable and optionally filtering the items based on a condition.",
        "learned": False
    },
    {
        "number": 41,
        "question": "What is a dictionary comprehension in Python?",
        "answer": "A dictionary comprehension is a concise way to create dictionaries in Python by applying an expression to each key-value pair in an iterable and optionally filtering the pairs based on a condition.",
        "learned": False
    },
    {
        "number": 42,
        "question": "What is a set comprehension in Python?",
        "answer": "A set comprehension is a concise way to create sets in Python by applying an expression to each element in an iterable and optionally filtering the elements based on a condition.",
        "learned": False
    },
    {
        "number": 43,
        "question": "What is a generator comprehension in Python?",
        "answer": "A generator comprehension, also known as a generator expression, is a concise way to create generators in Python by applying an expression to each item in an iterable and optionally filtering the items based on a condition.",
        "learned": False
    },
    {
        "number": 44,
        "question": "What is a context manager in Python?",
        "answer": "A context manager is an object that is used to manage resources and perform setup and teardown operations within a Python context. It is implemented using the with statement and can be created using the __enter__ and __exit__ methods.",
        "learned": False
    },
    {
        "number": 45,
        "question": "What is the purpose of the with statement in Python?",
        "answer": "The with statement is used to manage resources and ensure cleanup operations are performed after the execution of a block of code. It is commonly used with context managers.",
        "learned": False
    },
    {
        "number": 46,
        "question": "What is the purpose of the __enter__ method in Python?",
        "answer": "The __enter__ method is called when entering a context managed by a context manager. It is used to perform setup operations and optionally return a resource.",
        "learned": False
    },
    {
        "number": 47,
        "question": "What is the purpose of the __exit__ method in Python?",
        "answer": "The __exit__ method is called when exiting a context managed by a context manager. It is used to perform cleanup operations and handle exceptions.",
        "learned": False
    },
    {
        "number": 48,
        "question": "What is the purpose of the itertools module in Python?",
        "answer": "The itertools module in Python provides a collection of functions for creating iterators for efficient looping and combining iterators. It includes functions such as count(), cycle(), and chain().",
        "learned": False
    },
    {
        "number": 49,
        "question": "What is the purpose of the functools module in Python?",
        "answer": "The functools module in Python provides a collection of higher-order functions and operations on callable objects. It includes functions such as partial(), reduce(), and wraps().",
        "learned": False
    },
    {
        "number": 50,
        "question": "What is the purpose of the operator module in Python?",
        "answer": "The operator module in Python provides a collection of functions corresponding to the built-in operators, such as arithmetic, comparison, and logical operators. It allows for functional-style programming.",
        "learned": False
    },
    {
        "number": 51,
        "question": "What is the purpose of the sys module in Python?",
        "answer": "The sys module in Python provides access to system-specific parameters and functions, such as command-line arguments, environment variables, and exit status. It is often used for system-level programming.",
        "learned": False
    },
    {
        "number": 52,
        "question": "What is the purpose of the os module in Python?",
        "answer": "The os module in Python provides functions for interacting with the operating system, such as file operations, process management, and environment variables. It allows for platform-independent programming.",
        "learned": False
    },
    {
        "number": 53,
        "question": "What is the purpose of the re module in Python?",
        "answer": "The re module in Python provides support for regular expressions, which are used for pattern matching and text manipulation. It allows for powerful string processing operations.",
        "learned": False
    },
    {
        "number": 54,
        "question": "What is the purpose of the datetime module in Python?",
        "answer": "The datetime module in Python provides classes and functions for working with dates, times, and time intervals. It allows for date and time arithmetic and formatting.",
        "learned": False
    },
    {
        "number": 55,
        "question": "What is the purpose of the logging module in Python?",
        "answer": "The logging module in Python provides a flexible framework for logging messages from Python programs. It allows for logging to files, streams, sockets, and other destinations with different levels of severity.",
        "learned": False
    },
    {
        "number": 56,
        "question": "What is the purpose of the pickle module in Python?",
        "answer": "The pickle module in Python provides functions for serializing and deserializing Python objects into a byte stream. It allows for object persistence and inter-process communication.",
        "learned": False
    },
    {
        "number": 57,
        "question": "What is the purpose of the multiprocessing module in Python?",
        "answer": "The multiprocessing module in Python provides support for parallel processing and concurrent execution of tasks using multiple processes. It allows for improved performance on multi-core systems.",
        "learned": False
    },
    {
        "number": 58,
        "question": "What is the purpose of the threading module in Python?",
        "answer": "The threading module in Python provides support for concurrent execution of tasks using multiple threads within a single process. It allows for asynchronous and parallel programming.",
        "learned": False
    },
    {
        "number": 59,
        "question": "What is the purpose of the concurrent.futures module in Python?",
        "answer": "The concurrent.futures module in Python provides a high-level interface for asynchronously executing callables (functions or methods) using threads or processes. It simplifies parallel programming.",
        "learned": False
    },
    {
        "number": 60,
        "question": "What is the purpose of the asyncio module in Python?",
        "answer": "The asyncio module in Python provides support for asynchronous I/O and event loop-based concurrency. It allows for efficient handling of I/O-bound and CPU-bound tasks.",
        "learned": False
    },
    {
        "number": 61,
        "question": "What is the purpose of the concurrent package in Python?",
        "answer": "The concurrent package in Python provides high-level abstractions for parallel programming, including futures, tasks, and executors. It simplifies concurrent and parallel programming.",
        "learned": False
    },
    {
        "number": 62,
        "question": "What is the purpose of the logging package in Python?",
        "answer": "The logging package in Python provides a flexible and extensible framework for logging messages from Python programs. It allows for fine-grained control over log messages and destinations.",
        "learned": False
    },
    {
        "number": 63,
        "question": "What is the purpose of the itertools package in Python?",
        "answer": "The itertools package in Python provides a collection of functions for creating iterators and combining iterators in efficient ways. It allows for functional-style programming and combinatorial algorithms.",
        "learned": False
    },
    {
        "number": 64,
        "question": "What is the purpose of the functools package in Python?",
        "answer": "The functools package in Python provides a collection of higher-order functions and operations on callable objects. It allows for functional-style programming and function composition.",
        "learned": False
    },
    {
        "number": 65,
        "question": "What is the purpose of the operator package in Python?",
        "answer": "The operator package in Python provides a collection of functions corresponding to the built-in operators, such as arithmetic, comparison, and logical operators. It allows for functional-style programming and operator overloading.",
        "learned": False
    },
    {
        "number": 66,
        "question": "What is the purpose of the enum package in Python?",
        "answer": "The enum package in Python provides support for creating and using enumerated types. It allows for more readable and maintainable code by providing named constants and symbolic names.",
        "learned": False
    },
    {
        "number": 67,
        "question": "What is the purpose of the typing package in Python?",
        "answer": "The typing package in Python provides support for type hints and type checking in Python code. It allows for better documentation, code understanding, and static analysis.",
        "learned": False
    },
    {
        "number": 68,
        "question": "What is the purpose of the pathlib package in Python?",
        "answer": "The pathlib package in Python provides object-oriented filesystem paths for working with files and directories. It allows for more intuitive and platform-independent file operations.",
        "learned": False
    },
    {
        "number": 69,
        "question": "What is the purpose of the zipfile package in Python?",
        "answer": "The zipfile package in Python provides support for reading and writing ZIP archives. It allows for compression, extraction, and manipulation of ZIP files.",
        "learned": False
    },
    {
        "number": 70,
        "question": "What is the purpose of the shutil package in Python?",
        "answer": "The shutil package in Python provides high-level file operations for copying, moving, and deleting files and directories. It allows for platform-independent file management.",
        "learned": False
    },
    {
        "number": 71,
        "question": "What is the purpose of the random package in Python?",
        "answer": "The random package in Python provides functions for generating random numbers and selecting random elements from sequences. It allows for simulations, games, and cryptography.",
        "learned": False
    },
    {
        "number": 72,
        "question": "What is the purpose of the time package in Python?",
        "answer": "The time package in Python provides functions for working with time-related functions, such as getting the current time, measuring time intervals, and formatting time strings.",
        "learned": False
    },
    {
        "number": 73,
        "question": "What is the purpose of the datetime package in Python?",
        "answer": "The datetime package in Python provides classes and functions for working with dates, times, and time intervals. It allows for date and time arithmetic, parsing, and formatting.",
        "learned": False
    },
    {
        "number": 74,
        "question": "What is the purpose of the calendar package in Python?",
        "answer": "The calendar package in Python provides functions for working with dates and calendars, such as determining leap years, calculating weekdays, and formatting calendars.",
        "learned": False
    },
    {
        "number": 75,
        "question": "What is the purpose of the math package in Python?",
        "answer": "The math package in Python provides functions for mathematical operations, such as trigonometry, logarithms, and exponential functions. It allows for advanced mathematical computations.",
        "learned": False
    },
    {
        "number": 76,
        "question": "What is the purpose of the cmath package in Python?",
        "answer": "The cmath package in Python provides functions for mathematical operations on complex numbers. It allows for complex arithmetic, trigonometry, and exponential functions.",
        "learned": False
    },
    {
        "number": 77,
        "question": "What is the purpose of the statistics package in Python?",
        "answer": "The statistics package in Python provides functions for statistical calculations, such as mean, median, mode, variance, and standard deviation. It allows for basic statistical analysis.",
        "learned": False
    },
    {
        "number": 78,
        "question": "What is the purpose of the numpy package in Python?",
        "answer": "The numpy package in Python provides support for multidimensional arrays and mathematical functions for array manipulation. It allows for efficient numerical computations and scientific computing.",
        "learned": False
    },
    {
        "number": 79,
        "question": "What is the purpose of the scipy package in Python?",
        "answer": "The scipy package in Python provides a collection of scientific computing functions and algorithms for optimization, interpolation, integration, linear algebra, and signal processing.",
        "learned": False
    },
    {
        "number": 80,
        "question": "What is the purpose of the pandas package in Python?",
        "answer": "The pandas package in Python provides data structures and functions for data manipulation and analysis, such as reading and writing data from various sources, reshaping data, and performing statistical analysis.",
        "learned": False
    },
    {
        "number": 81,
        "question": "What is the purpose of the matplotlib package in Python?",
        "answer": "The matplotlib package in Python provides functions for creating static, interactive, and animated visualizations and plots. It allows for data exploration, presentation, and communication.",
        "learned": False
    },
    {
        "number": 82,
        "question": "What is the purpose of the seaborn package in Python?",
        "answer": "The seaborn package in Python provides functions for creating statistical data visualizations based on matplotlib. It allows for the creation of complex, informative plots with minimal code.",
        "learned": False
    },
    {
        "number": 83,
        "question": "What is the purpose of the scikit-learn package in Python?",
        "answer": "The scikit-learn package in Python provides tools and algorithms for machine learning and data mining tasks, such as classification, regression, clustering, and dimensionality reduction.",
        "learned": False
    },
    {
        "number": 84,
        "question": "What is the purpose of the tensorflow package in Python?",
        "answer": "The tensorflow package in Python provides a deep learning framework for building and training neural networks. It allows for high-level and low-level APIs for model development and deployment.",
        "learned": False
    },
    {
        "number": 85,
        "question": "What is the purpose of the keras package in Python?",
        "answer": "The keras package in Python provides a high-level neural networks API built on top of tensorflow. It allows for easy and fast prototyping of deep learning models with minimal code.",
        "learned": False
    },
    {
        "number": 86,
        "question": "What is the purpose of the nltk package in Python?",
        "answer": "The nltk package in Python provides tools and libraries for natural language processing (NLP) tasks, such as tokenization, stemming, tagging, parsing, and classification.",
        "learned": False
    },
    {
        "number": 87,
        "question": "What is the purpose of the spaCy package in Python?",
        "answer": "The spaCy package in Python provides an industrial-strength natural language processing (NLP) library with support for advanced NLP tasks, such as named entity recognition, dependency parsing, and part-of-speech tagging.",
        "learned": False
    },
    {
        "number": 88,
        "question": "What is the purpose of the gensim package in Python?",
        "answer": "The gensim package in Python provides tools and algorithms for topic modeling, document similarity analysis, and other natural language processing (NLP) tasks. It allows for efficient processing of large text corpora.",
        "learned": False
    },
    {
        "number": 89,
        "question": "What is the purpose of the beautifulsoup4 package in Python?",
        "answer": "The beautifulsoup4 package in Python provides tools for scraping and parsing HTML and XML documents. It allows for extracting data from web pages and manipulating the document tree.",
        "learned": False
    },
    {
        "number": 90,
        "question": "What is the purpose of the requests package in Python?",
        "answer": "The requests package in Python provides tools for making HTTP requests and interacting with web services. It allows for sending and receiving HTTP requests with ease.",
        "learned": False
    },
    {
        "number": 91,
        "question": "What is the purpose of the flask package in Python?",
        "answer": "The flask package in Python provides a lightweight and extensible web framework for building web applications. It allows for routing, request handling, template rendering, and more.",
        "learned": False
    },
    {
        "number": 92,
        "question": "What is the purpose of the django package in Python?",
        "answer": "The django package in Python provides a high-level web framework for building web applications. It follows the model-view-template (MVT) architectural pattern and includes built-in features for authentication, database management, and more.",
        "learned": False
    },
    {
        "number": 93,
        "question": "What is the purpose of the sqlalchemy package in Python?",
        "answer": "The sqlalchemy package in Python provides tools and libraries for working with SQL databases. It allows for database abstraction, query building, and ORM (Object-Relational Mapping) capabilities.",
        "learned": False
    },
    {
        "number": 94,
        "question": "What is the purpose of the celery package in Python?",
        "answer": "The celery package in Python provides distributed task queueing capabilities for processing asynchronous and scheduled tasks. It allows for scaling and distributing workloads across multiple workers.",
        "learned": False
    },
    {
        "number": 95,
        "question": "What is the purpose of the redis package in Python?",
        "answer": "The redis package in Python provides a client for interacting with Redis, an in-memory data structure store used as a database, cache, and message broker. It allows for efficient data storage and retrieval.",
        "learned": False
    },
    {
        "number": 96,
        "question": "What is the purpose of the pymongo package in Python?",
        "answer": "The pymongo package in Python provides tools for interacting with MongoDB, a NoSQL document-oriented database. It allows for CRUD (Create, Read, Update, Delete) operations and data manipulation.",
        "learned": False
    },
    {
        "number": 97,
        "question": "What is the purpose of the psycopg2 package in Python?",
        "answer": "The psycopg2 package in Python provides a client for interacting with PostgreSQL, a powerful open-source relational database system. It allows for executing SQL queries and managing database connections.",
        "learned": False
    },
    {
        "number": 98,
        "question": "What is the purpose of the pymysql package in Python?",
        "answer": "The pymysql package in Python provides a client for interacting with MySQL, a popular open-source relational database system. It allows for executing SQL queries and managing database connections.",
        "learned": False
    },
    {
        "number": 99,
        "question": "What is the purpose of the sqlite3 package in Python?",
        "answer": "The sqlite3 package in Python provides a client for interacting with SQLite, a lightweight and self-contained SQL database engine. It allows for executing SQL queries and managing database connections.",
        "learned": False
    },
    {
        "number": 100,
        "question": "What is the purpose of the pytest package in Python?",
        "answer": "The pytest package in Python provides a testing framework for writing and executing automated tests in Python. It allows for easy test discovery, fixture setup, and test execution.",
        "learned": False
    },
    {
        "number": 101,
        "question": "What is Object-Oriented Programming (OOP) in Python?",
        "answer": "Object-Oriented Programming (OOP) is a programming paradigm that focuses on organizing code into objects, which encapsulate data and behavior. Python is an object-oriented programming language, meaning it supports creating and manipulating objects to build applications.",
        "learned": False
    },
    {
        "number": 102,
        "question": "What are the four pillars of Object-Oriented Programming?",
        "answer": "The four pillars of Object-Oriented Programming are encapsulation, inheritance, polymorphism, and abstraction. These principles help in designing and implementing effective object-oriented systems.",
        "learned": False
    },
    {
        "number": 103,
        "question": "What is encapsulation in Python?",
        "answer": "Encapsulation is the bundling of data and methods that operate on the data into a single unit called a class. It allows for controlling access to the data by hiding implementation details and exposing only the necessary interfaces.",
        "learned": False
    },
    {
        "number": 104,
        "question": "How do you create a class in Python?",
        "answer": "You can create a class in Python using the 'class' keyword followed by the class name. For example: 'class MyClass:'",
        "learned": False
    },
    {
        "number": 105,
        "question": "What is a constructor in Python?",
        "answer": "A constructor in Python is a special method (__init__) that is automatically called when a new instance of a class is created. It is used to initialize the object's state.",
        "learned": False
    },
    {
        "number":106,
        "question": "What is inheritance in Python?",
        "answer": "Inheritance is a mechanism in Python that allows a class to inherit properties and behavior from another class. The class that inherits is called a subclass or derived class, and the class it inherits from is called a superclass or base class.",
        "learned": False
    },
    {
        "number":107,
        "question": "How do you implement inheritance in Python?",
        "answer": "You can implement inheritance in Python by specifying the superclass in parentheses after the subclass name when defining the subclass. For example: 'class SubClass(SuperClass):'",
        "learned": False
    },
    {
        "number": 108,
        "question": "What is method overriding in Python?",
        "answer": "Method overriding is a feature of object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This allows for customization of behavior in the subclass.",
        "learned": False
    },
    {
        "number": 109,
        "question": "What is method overloading in Python?",
        "answer": "Method overloading is not directly supported in Python like in some other languages such as Java. However, Python allows for function overloading through the use of default arguments and variable-length argument lists.",
        "learned": False
    },
    {
        "number": 110,
        "question": "What is polymorphism in Python?",
        "answer": "Polymorphism is the ability of a single interface (such as a method or function) to work with objects of multiple types. In Python, polymorphism is achieved through method overriding and duck typing.",
        "learned": False
    },
    {
        "number": 111,
        "question": "What is duck typing in Python?",
        "answer": "Duck typing is a programming concept used in dynamic languages like Python, where the type or class of an object is less important than the methods it defines. If an object implements certain methods, it can be used in place of another object that expects those methods, regardless of their actual class or type.",
        "learned": False
    },
    {
        "number": 112,
        "question": "What is composition in Python?",
        "answer": "Composition is a design principle in object-oriented programming where objects are composed of other objects as parts. It allows for building complex objects by combining simpler ones.",
        "learned": False
    },
    {
        "number": 113,
        "question": "What is aggregation in Python?",
        "answer": "Aggregation is a special form of composition where objects have a 'has-a' relationship, meaning one object contains another object, but the contained object can exist independently of the container object.",
        "learned": False
    },
    {
        "number": 114,
        "question": "What is method chaining in Python?",
        "answer": "Method chaining is a programming technique where multiple methods are called sequentially on the same object, with each method returning the modified object. This allows for concise and readable code.",
        "learned": False
    },
    {
        "number": 115,
        "question": "What is a class attribute in Python?",
        "answer": "A class attribute in Python is a variable that is shared by all instances of a class. It is defined within the class but outside any method, and it is accessed using the class name rather than an instance.",
        "learned": False
    },
    {
        "number": 116,
        "question": "What is an instance attribute in Python?",
        "answer": "An instance attribute in Python is a variable that is specific to a particular instance of a class. It is defined within the class constructor (__init__) and is accessed using the instance name.",
        "learned": False
    },
    {
        "number": 117,
        "question": "What is the difference between a class attribute and an instance attribute in Python?",
        "answer": "A class attribute is shared by all instances of a class and is accessed using the class name, whereas an instance attribute is specific to a particular instance of a class and is accessed using the instance name.",
        "learned": False
    },
    {
        "number": 118,
        "question": "What is a static method in Python?",
        "answer": "A static method in Python is a method that belongs to the class rather than any particular instance. It does not have access to the instance or class state and is used primarily for utility functions that do not require access to instance or class variables.",
        "learned": False
    },
    {
        "number": 119,
        "question": "What is a class method in Python?",
        "answer": "A class method in Python is a method that operates on the class rather than any particular instance. It has access to the class variables and can be used to create factory methods or perform operations that affect the class as a whole.",
        "learned": False
    },
    {
        "number": 120,
        "question": "What is the purpose of the super() function in Python?",
        "answer": "The super() function in Python is used to call methods and access properties from the superclass within a subclass. It allows for invoking superclass methods and constructors to avoid code duplication and ensure proper initialization.",
        "learned": False
    },
    {
        "number": 121,
        "question": "What is method resolution order (MRO) in Python?",
        "answer": "Method Resolution Order (MRO) in Python defines the order in which methods are resolved in the presence of multiple inheritance. It is determined by the C3 linearization algorithm, which ensures that base classes are searched in a consistent order.",
        "learned": False
    },
    {
        "number": 122,
        "question": "What is multiple inheritance in Python?",
        "answer": "Multiple inheritance in Python refers to the ability of a class to inherit properties and behavior from more than one parent class. While Python supports multiple inheritance, it can lead to complexities such as the diamond problem and method resolution order (MRO) conflicts.",
        "learned": False
    },
    {
        "number": 123,
        "question": "What is a mixin in Python?",
        "answer": "A mixin in Python is a class that provides a set of methods that can be added to another class by inheritance, without the need to subclass the mixin directly. Mixins are often used to add common functionality to multiple classes.",
        "learned": False
    },
    {
        "number": 124,
        "question": "What is the diamond problem in multiple inheritance?",
        "answer": "The diamond problem is a common issue in multiple inheritance where a class inherits from two or more classes that have a common ancestor. This can lead to ambiguities in method resolution order and can result in unexpected behavior.",
        "learned": False
    },
    {
        "number": 125,
        "question": "How do you handle the diamond problem in Python?",
        "answer": "In Python, the diamond problem is handled using the C3 linearization algorithm, which defines the method resolution order (MRO) for classes with multiple inheritance. By following the MRO, Python ensures a consistent order for method resolution.",
        "learned": False
    },
    {
        "number": 126,
        "question": "What is method overriding in Python?",
        "answer": "Method overriding is a feature of object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This allows for customization of behavior in the subclass.",
        "learned": False
    },
    {
        "number": 127,
        "question": "What is method overloading in Python?",
        "answer": "Method overloading is not directly supported in Python like in some other languages such as Java. However, Python allows for function overloading through the use of default arguments and variable-length argument lists.",
        "learned": False
    },
    {
        "number": 128,
        "question": "What is operator overloading in Python?",
        "answer": "Operator overloading in Python refers to defining custom behavior for operators (+, -, *, /, etc.) when applied to objects of user-defined classes. It allows objects to behave like built-in types and enables a more natural syntax for working with objects.",
        "learned": False
    },
    {
        "number": 129,
        "question": "What is data hiding in Python?",
        "answer": "Data hiding in Python refers to the practice of restricting access to certain attributes or methods of a class to prevent direct modification or misuse by external code. It is achieved using access modifiers such as private and protected.",
        "learned": False
    },
    {
        "number": 130,
        "question": "What is the difference between private and protected members in Python?",
        "answer": "Private members in Python are indicated by prefixing the attribute or method name with double underscores (e.g., '__attribute'), and they can only be accessed within the class that defines them. Protected members are indicated by prefixing the attribute or method name with a single underscore (e.g., '_attribute'), and they can be accessed within the class and its subclasses.",
        "learned": False
    },
    {
        "number": 131,
        "question": "What is the purpose of the __str__ method in Python?",
        "answer": "The __str__ method in Python is used to define the string representation of an object. It is called by the str() function and the print() function to convert the object to a string.",
        "learned": False
    },
    {
        "number": 132,
        "question": "What is the purpose of the __repr__ method in Python?",
        "answer": "The __repr__ method in Python is used to define the official string representation of an object. It is called by the repr() function and is typically used for debugging and logging purposes.",
        "learned": False
    },
    {
        "number": 133,
        "question": "What is the purpose of the __init__ method in Python?",
        "answer": "The __init__ method in Python is a constructor method that is automatically called when a new instance of a class is created. It is used to initialize the object's state and can accept arguments to customize the initialization process.",
        "learned": False
    },
    {
        "number": 134,
        "question": "What is the purpose of the __del__ method in Python?",
        "answer": "The __del__ method in Python is a destructor method that is automatically called when an object is about to be destroyed. It is used to perform cleanup actions such as releasing resources or closing files.",
        "learned": False
    },
    {
        "number": 135,
        "question": "What is the purpose of the __getattr__ method in Python?",
        "answer": "The __getattr__ method in Python is called when an attribute is accessed on an object that does not exist. It allows for defining custom behavior for attribute access and can be used to implement lazy loading and dynamic attribute lookup.",
        "learned": False
    },
    {
        "number": 136,
        "question": "What is the purpose of the __setattr__ method in Python?",
        "answer": "The __setattr__ method in Python is called when an attribute is set on an object. It allows for intercepting attribute assignment and can be used to enforce data validation and encapsulation.",
        "learned": False
    },
    {
        "number": 137,
        "question": "What is the purpose of the __delattr__ method in Python?",
        "answer": "The __delattr__ method in Python is called when an attribute is deleted from an object using the 'del' keyword. It allows for defining custom behavior for attribute deletion and can be used to perform cleanup actions.",
        "learned": False
    },
    {
        "number": 138,
        "question": "What is the purpose of the @property decorator in Python?",
        "answer": "The @property decorator in Python is used to define properties on a class that behave like attributes but have custom getter, setter, and deleter methods. It allows for controlling access to and manipulation of object attributes.",
        "learned": False
    },
    {
        "number": 139,
        "question": "What is the purpose of the @staticmethod decorator in Python?",
        "answer": "The @staticmethod decorator in Python is used to define static methods within a class. Static methods do not have access to instance or class variables and are primarily used for utility functions that do not require access to object state.",
        "learned": False
    },
    {
        "number": 140,
        "question": "What is the purpose of the @classmethod decorator in Python?",
        "answer": "The @classmethod decorator in Python is used to define class methods within a class. Class methods have access to the class variables and can be used to perform operations that affect the class as a whole.",
        "learned": False
    },
    {
        "number": 141,
        "question": "What is the purpose of the isinstance() function in Python?",
        "answer": "The isinstance() function in Python is used to check if an object is an instance of a particular class or type. It returns True if the object is an instance of the specified class or a subclass, otherwise False.",
        "learned": False
    },
    {
        "number": 142,
        "question": "What is the purpose of the issubclass() function in Python?",
        "answer": "The issubclass() function in Python is used to check if a class is a subclass of another class. It returns True if the first argument is a subclass of the second argument, otherwise False.",
        "learned": False
    },
    {
        "number": 143,
        "question": "What is the purpose of the super() function in Python?",
        "answer": "The super() function in Python is used to call methods and access properties from the superclass within a subclass. It allows for invoking superclass methods and constructors to avoid code duplication and ensure proper initialization.",
        "learned": False
    },
    {
        "number": 144,
        "question": "What is the purpose of the hasattr() function in Python?",
        "answer": "The hasattr() function in Python is used to check if an object has a particular attribute. It returns True if the object has the specified attribute, otherwise False.",
        "learned": False
    },
    {
        "number": 145,
        "question": "What is the purpose of the getattr() function in Python?",
        "answer": "The getattr() function in Python is used to get the value of a named attribute of an object. If the attribute does not exist, a default value can be specified, or an AttributeError is raised.",
        "learned": False
    },
    {
        "number": 146,
        "question": "What is the purpose of the setattr() function in Python?",
        "answer": "The setattr() function in Python is used to set the value of a named attribute of an object. If the attribute does not exist, it is created. If the object is not mutable, a TypeError is raised.",
        "learned": False
    },
    {
        "number": 147,
        "question": "What is the purpose of the delattr() function in Python?",
        "answer": "The delattr() function in Python is used to delete a named attribute of an object. If the attribute does not exist, an AttributeError is raised.",
        "learned": False
    },
    {
        "number": 148,
        "question": "What is the purpose of the property() function in Python?",
        "answer": "The property() function in Python is used to create properties on a class that behave like attributes but have custom getter, setter, and deleter methods. It allows for controlling access to and manipulation of object attributes.",
        "learned": False
    },
    {
        "number":149,
        "question": "What is the purpose of the classmethod() decorator in Python?",
        "answer": "The classmethod() decorator in Python is used to define class methods within a class. Class methods have access to the class variables and can be used to perform operations that affect the class as a whole.",
        "learned": False
    },
    {
        "number": 150,
        "question": "What is the purpose of the staticmethod() decorator in Python?",
        "answer": "The staticmethod() decorator in Python is used to define static methods within a class. Static methods do not have access to instance or class variables and are primarily used for utility functions that do not require access to object state.",
        "learned": False
    }

]