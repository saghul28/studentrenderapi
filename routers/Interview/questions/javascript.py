javascript_questions = [
    {
        "number": 1,
        "question": "What is JavaScript?",
        "answer": "JavaScript is a high-level, interpreted programming language that is primarily used for client-side web development. It allows dynamic content to be added to web pages and enhances user interaction.",
        "learned": False
    },
    {
        "number": 2,
        "question": "What are the different data types in JavaScript?",
        "answer": "JavaScript supports several data types, including numbers, strings, booleans, objects, arrays, functions, and symbols.",
        "learned": False
    },
    {
        "number": 3,
        "question": "What is the difference between == and === operators in JavaScript?",
        "answer": "== is the equality operator and checks for equality of value, while === is the strict equality operator and checks for equality of both value and type.",
        "learned": False
    },
    {
        "number": 4,
        "question": "What is a closure in JavaScript?",
        "answer": "A closure is a function that retains access to variables from its lexical scope even after the scope has finished executing. It allows for data encapsulation and private variables in JavaScript.",
        "learned": False
    },
    {
        "number": 5,
        "question": "What is event delegation in JavaScript?",
        "answer": "Event delegation is a technique in JavaScript where a single event listener is attached to a parent element to manage events for all its descendants. It helps improve performance and reduces memory usage.",
        "learned": False
    },
    {
        "number": 6,
        "question": "What is the difference between var, let, and const in JavaScript?",
        "answer": "var is function-scoped and can be redeclared and reassigned. let is block-scoped, can be reassigned but not redeclared. const is also block-scoped but cannot be reassigned or redeclared.",
        "learned": False
    },
    {
        "number": 7,
        "question": "What is the 'this' keyword in JavaScript?",
        "answer": "The 'this' keyword refers to the context in which a function is called. Its value is determined by how a function is invoked, and it can change depending on the execution context.",
        "learned": False
    },
    {
        "number": 8,
        "question": "What is the difference between 'null' and 'undefined' in JavaScript?",
        "answer": "'null' represents the intentional absence of any object value, while 'undefined' represents the lack of a defined value. 'null' is explicitly assigned, while 'undefined' is the default value of uninitialized variables.",
        "learned": False
    },
    {
        "number": 9,
        "question": "What are arrow functions in JavaScript?",
        "answer": "Arrow functions are a concise way to write function expressions in JavaScript. They have a shorter syntax compared to traditional function expressions and inherit the 'this' value from the enclosing lexical scope.",
        "learned": False
    },
    {
        "number": 10,
        "question": "What is a promise in JavaScript?",
        "answer": "A promise is an object representing the eventual completion or failure of an asynchronous operation. It allows for better handling of asynchronous code compared to traditional callback functions.",
        "learned": False
    },
    {
        "number": 11,
        "question": "What is the difference between 'let' and 'var' in JavaScript?",
        "answer": "'let' is block-scoped, meaning it is only accessible within the block it is defined in, while 'var' is function-scoped. Additionally, 'let' does not allow redeclaration of the same variable in the same scope, while 'var' does.",
        "learned": False
    },
    {
        "number": 12,
        "question": "What is the event loop in JavaScript?",
        "answer": "The event loop is a mechanism in JavaScript that allows for asynchronous operations to be handled efficiently. It continuously checks the call stack and task queue, executing tasks in the queue when the call stack is empty.",
        "learned": False
    },
    {
        "number": 13,
        "question": "What is the difference between '==' and '===' operators in JavaScript?",
        "answer": "'==' is the equality operator and performs type coercion, while '===' is the strict equality operator and does not perform type coercion. '===' requires both value and type to be equal.",
        "learned": False
    },
    {
        "number": 14,
        "question": "What is the purpose of the 'async' and 'await' keywords in JavaScript?",
        "answer": "'async' is used to declare an asynchronous function, which returns a promise. 'await' is used inside an async function to pause the execution and wait for the promise to resolve before continuing.",
        "learned": False
    },
    {
        "number": 15,
        "question": "What are JavaScript modules?",
        "answer": "JavaScript modules are reusable pieces of code that encapsulate related functionality. They allow for better organization, maintainability, and code reuse in large-scale applications.",
        "learned": False
    },
    {
        "number": 16,
        "question": "What is the purpose of the 'prototype' property in JavaScript?",
        "answer": "The 'prototype' property is used to add methods and properties to objects in JavaScript. It allows for inheritance and the creation of object hierarchies.",
        "learned": False
    },
    {
        "number": 17,
        "question": "What are higher-order functions in JavaScript?",
        "answer": "Higher-order functions are functions that can accept other functions as arguments or return functions as output. They enable functional programming paradigms in JavaScript.",
        "learned": False
    },
    {
        "number": 18,
        "question": "What is lexical scoping in JavaScript?",
        "answer": "Lexical scoping refers to how variable names are resolved in nested functions. In JavaScript, inner functions have access to variables defined in their outer function's scope.",
        "learned": False
    },
    {
        "number": 19,
        "question": "What is the difference between 'let' and 'const' in JavaScript?",
        "answer": "'let' allows variables to be reassigned, while 'const' does not. However, both are block-scoped and cannot be accessed outside their block scope.",
        "learned": False
    },
    {
        "number": 20,
        "question": "What is the purpose of the 'use strict' directive in JavaScript?",
        "answer": "The 'use strict' directive enables strict mode in JavaScript, which imposes stricter parsing and error handling rules. It helps catch common coding mistakes and prevents certain actions.",
        "learned": False
    },
    {
        "number": 21,
        "question": "What is the difference between '==', '===', and '!=' operators in JavaScript?",
        "answer": "'==' is the equality operator and performs type coercion, '===' is the strict equality operator and does not perform type coercion, and '!=' is the inequality operator and performs type coercion.",
        "learned": False
    },
    {
        "number": 22,
        "question": "What is a callback function in JavaScript?",
        "answer": "A callback function is a function passed as an argument to another function, which is then invoked inside the outer function to complete some asynchronous task or handle an event.",
        "learned": False
    },
    {
        "number": 23,
        "question": "What are the different ways to create objects in JavaScript?",
        "answer": "Objects can be created using object literals, constructor functions, the 'Object.create()' method, or ES6 classes.",
        "learned": False
    },
    {
        "number": 24,
        "question": "What is JSON and how is it related to JavaScript?",
        "answer": "JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is derived from JavaScript object literals.",
        "learned": False
    },
    {
        "number": 25,
        "question": "What are the different types of error handling mechanisms in JavaScript?",
        "answer": "JavaScript supports error handling using try-catch blocks, the 'throw' statement, and the 'finally' block for cleanup code. It also provides built-in error objects like 'Error', 'SyntaxError', 'TypeError', etc.",
        "learned": False
    },
    {
        "number": 26,
        "question": "What is the purpose of the 'bind' method in JavaScript?",
        "answer": "The 'bind' method is used to create a new function with a specified 'this' value and initial arguments. It allows for explicit binding of 'this' in function invocation.",
        "learned": False
    },
    {
        "number": 27,
        "question": "What is the difference between 'null' and 'undefined' in JavaScript?",
        "answer": "'null' represents the intentional absence of any object value, while 'undefined' represents the lack of a defined value. 'null' is explicitly assigned, while 'undefined' is the default value of uninitialized variables.",
        "learned": False
    },
    {
        "number": 28,
        "question": "What is event bubbling and event capturing in JavaScript?",
        "answer": "Event bubbling is the default event propagation mechanism in which an event triggered on a nested element propagates to its ancestors. Event capturing is the opposite, where the event is captured from the top of the DOM tree down to the target element.",
        "learned": False
    },
    {
        "number": 29,
        "question": "What is a closure in JavaScript?",
        "answer": "A closure is a function that retains access to variables from its lexical scope even after the scope has finished executing. It allows for data encapsulation and private variables in JavaScript.",
        "learned": False
    },
    {
        "number": 30,
        "question": "What is the 'apply' method in JavaScript?",
        "answer": "The 'apply' method is used to call a function with a given 'this' value and arguments provided as an array. It is similar to the 'call' method but accepts arguments as an array.",
        "learned": False
    },
    
    {
        "number": 31,
        "question": "What is the Event Loop in JavaScript?",
        "answer": "The Event Loop is a mechanism in JavaScript that handles asynchronous tasks. It continuously checks the call stack and the callback queue, moving tasks from the queue to the stack when the stack is empty.",
        "learned": False
    },
    {
        "number": 32,
        "question": "What is the purpose of the 'this' keyword in JavaScript?",
        "answer": "The 'this' keyword refers to the context in which a function is called. Its value depends on how the function is invoked and can be determined using explicit or implicit binding rules.",
        "learned": False
    },
    {
        "number": 33,
        "question": "What are arrow functions in JavaScript?",
        "answer": "Arrow functions are a concise syntax for writing function expressions in JavaScript. They have a shorter syntax compared to traditional function expressions and do not bind their own 'this', 'arguments', 'super', or 'new.target'.",
        "learned": False
    },
    {
        "number": 34,
        "question": "What are closures in JavaScript?",
        "answer": "Closures are functions that retain access to variables from their lexical scope even after the scope has finished executing. They allow for data encapsulation and the creation of private variables in JavaScript.",
        "learned": False
    },
    {
        "number": 35,
        "question": "What is the purpose of the 'typeof' operator in JavaScript?",
        "answer": "The 'typeof' operator is used to determine the type of a variable or expression in JavaScript. It returns a string indicating the data type, such as 'number', 'string', 'boolean', 'object', 'function', or 'undefined'.",
        "learned": False
    },
    {
        "number": 36,
        "question": "What is the difference between 'null' and 'undefined' in JavaScript?",
        "answer": "'null' represents the intentional absence of any object value, while 'undefined' represents the lack of a defined value. 'null' is explicitly assigned, while 'undefined' is the default value of uninitialized variables.",
        "learned": False
    },
    {
        "number": 37,
        "question": "What is the difference between '==', '===', and '!=' operators in JavaScript?",
        "answer": "'==' is the equality operator and performs type coercion, '===' is the strict equality operator and does not perform type coercion, and '!=' is the inequality operator and performs type coercion.",
        "learned": False
    },
    {
        "number": 38,
        "question": "What is the 'let' keyword in JavaScript?",
        "answer": "'let' is a block-scoped variable declaration keyword introduced in ECMAScript 6 (ES6). It allows variables to be declared with block scope, preventing them from being accessed outside their block scope.",
        "learned": False
    },
    {
        "number": 39,
        "question": "What is the 'const' keyword in JavaScript?",
        "answer": "'const' is a variable declaration keyword introduced in ECMAScript 6 (ES6) that creates a constant variable whose value cannot be reassigned. However, the variable's properties can still be modified.",
        "learned": False
    },
    {
        "number": 40,
        "question": "What is a Promise in JavaScript?",
        "answer": "A Promise is an object representing the eventual completion or failure of an asynchronous operation. It allows for asynchronous programming and better handling of callbacks.",
        "learned": False
    },
    {
        "number": 41,
        "question": "What are the different ways to loop through arrays in JavaScript?",
        "answer": "Arrays in JavaScript can be looped through using 'for' loops, 'while' loops, 'do-while' loops, 'for...in' loops, 'for...of' loops (introduced in ES6), and array methods like 'forEach()', 'map()', 'filter()', etc.",
        "learned": False
    },
    {
        "number": 42,
        "question": "What is the purpose of the 'async' and 'await' keywords in JavaScript?",
        "answer": "The 'async' keyword is used to define asynchronous functions, which return Promises. The 'await' keyword is used to pause the execution of an async function until the Promise is resolved, allowing for synchronous-looking asynchronous code.",
        "learned": False
    },
    {
        "number": 43,
        "question": "What is the purpose of the 'NaN' value in JavaScript?",
        "answer": "'NaN' stands for 'Not-a-Number' and is a special value in JavaScript indicating an unrepresentable value resulting from an invalid arithmetic operation. It is returned when a mathematical operation fails.",
        "learned": False
    },
    {
        "number": 44,
        "question": "What are template literals in JavaScript?",
        "answer": "Template literals are string literals allowing embedded expressions. They are enclosed by backticks (`) instead of single or double quotes and can contain placeholders (interpolated expressions) using ${} syntax.",
        "learned": False
    },
    {
        "number": 45,
        "question": "What is destructuring assignment in JavaScript?",
        "answer": "Destructuring assignment is a syntax in JavaScript that allows for the extraction of values from arrays or properties from objects into distinct variables. It provides a concise way to work with arrays and objects.",
        "learned": False
    },
    {
        "number": 46,
        "question": "What are the primitive data types in JavaScript?",
        "answer": "The primitive data types in JavaScript are 'number', 'string', 'boolean', 'undefined', 'null', and 'symbol'.",
        "learned": False
    },
    {
        "number": 47,
        "question": "What is the purpose of the 'arguments' object in JavaScript?",
        "answer": "The 'arguments' object is an array-like object available within all functions that contains the values of the arguments passed to the function. It allows for accessing variable numbers of arguments.",
        "learned": False
    },
    {
        "number": 48,
        "question": "What is a rest parameter in JavaScript?",
        "answer": "A rest parameter is a syntax in JavaScript that allows a function to accept an indefinite number of arguments as an array. It is denoted by three dots (...) before the parameter name in a function declaration.",
        "learned": False
    },
    {
        "number": 49,
        "question": "What is the purpose of the 'Symbol' data type in JavaScript?",
        "answer": "The 'Symbol' data type is a new primitive data type introduced in ECMAScript 6 (ES6) that represents a unique identifier. Symbols are used to create private object properties and for defining new iteration behaviors.",
        "learned": False
    },
    {
        "number": 50,
        "question": "What is hoisting in JavaScript?",
        "answer": "Hoisting is a JavaScript mechanism where variable and function declarations are moved to the top of their containing scope during the compilation phase. This allows variables and functions to be used before they are declared.",
        "learned": False
    },
    {
        "number": 51,
        "question": "What is the 'apply' method in JavaScript?",
        "answer": "The 'apply' method is used to call a function with a given 'this' value and arguments provided as an array. It is similar to the 'call' method but accepts arguments as an array.",
        "learned": False
    },
    {
        "number": 52,
        "question": "What is a generator function in JavaScript?",
        "answer": "A generator function is a special type of function in JavaScript that can pause its execution and yield multiple values. It is defined using the function* syntax and the yield keyword.",
        "learned": False
    },
    {
        "number": 53,
        "question": "What is the 'Map' data structure in JavaScript?",
        "answer": "The 'Map' object in JavaScript is a collection of key-value pairs where keys can be of any data type. It provides an easy way to store and retrieve data with better performance than plain objects for large datasets.",
        "learned": False
    },
    {
        "number": 54,
        "question": "What is the 'Set' data structure in JavaScript?",
        "answer": "The 'Set' object in JavaScript is a collection of unique values, where each value may occur only once. It provides methods for adding, removing, and checking for the presence of elements.",
        "learned": False
    },
    {
        "number": 55,
        "question": "What is the 'parseInt' function in JavaScript?",
        "answer": "The 'parseInt' function is used to parse a string and convert it to an integer. It takes an optional second argument specifying the radix (base) of the numeral system to be used for parsing.",
        "learned": False
    },
    {
        "number": 56,
        "question": "What is the 'parseFloat' function in JavaScript?",
        "answer": "The 'parseFloat' function is used to parse a string and convert it to a floating-point number. It works similarly to 'parseInt' but parses floating-point numbers instead of integers.",
        "learned": False
    },
    {
        "number": 57,
        "question": "What is a weak set in JavaScript?",
        "answer": "A weak set is a collection of objects in JavaScript where each object may occur only once. Unlike a regular set, a weak set allows its elements to be garbage-collected if no other references to them exist outside the set.",
        "learned": False
    },
    {
        "number": 58,
        "question": "What is a weak map in JavaScript?",
        "answer": "A weak map is a collection of key-value pairs in JavaScript where keys can be objects and values can be arbitrary values. Similarly to a weak set, a weak map allows its keys to be garbage-collected if no other references to them exist outside the map.",
        "learned": False
    },
    {
        "number": 59,
        "question": "What is a decorator in JavaScript?",
        "answer": "A decorator is a design pattern in JavaScript used to dynamically add behavior to objects at runtime. It allows for the modification or extension of the behavior of individual objects without affecting other instances of the same class.",
        "learned": False
    },
    {
        "number": 60,
        "question": "What is memoization in JavaScript?",
        "answer": "Memoization is an optimization technique in JavaScript used to speed up the execution of functions by caching the results of expensive function calls and returning the cached result when the same inputs occur again.",
        "learned": False
    },
    {
        "number": 61,
        "question": "What is the 'Symbol.iterator' method in JavaScript?",
        "answer": "The 'Symbol.iterator' method is a special method in JavaScript used to define the default iterator for an object. It is used to make an object iterable, allowing it to be used in 'for...of' loops and other iterable contexts.",
        "learned": False
    },
    {
        "number": 62,
        "question": "What is the 'startsWith' method in JavaScript?",
        "answer": "The 'startsWith' method is a string method in JavaScript used to determine whether a string begins with the characters of a specified string, returning 'true' if the string starts with the specified characters, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 63,
        "question": "What is the 'endsWith' method in JavaScript?",
        "answer": "The 'endsWith' method is a string method in JavaScript used to determine whether a string ends with the characters of a specified string, returning 'true' if the string ends with the specified characters, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 64,
        "question": "What is the 'includes' method in JavaScript?",
        "answer": "The 'includes' method is an array method in JavaScript used to determine whether an array includes a certain value, returning 'true' if the array contains the value, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 65,
        "question": "What is the 'find' method in JavaScript?",
        "answer": "The 'find' method is an array method in JavaScript used to find the first element in an array that satisfies a provided testing function. It returns the value of the first element found, or 'undefined' if no matching element is found.",
        "learned": False
    },
    {
        "number": 66,
        "question": "What is the 'findIndex' method in JavaScript?",
        "answer": "The 'findIndex' method is an array method in JavaScript used to find the index of the first element in an array that satisfies a provided testing function. It returns the index of the first matching element found, or -1 if no matching element is found.",
        "learned": False
    },
    {
        "number": 67,
        "question": "What is the 'some' method in JavaScript?",
        "answer": "The 'some' method is an array method in JavaScript used to test whether at least one element in the array satisfies a provided testing function. It returns 'true' if at least one element satisfies the condition, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 68,
        "question": "What is the 'every' method in JavaScript?",
        "answer": "The 'every' method is an array method in JavaScript used to test whether all elements in the array satisfy a provided testing function. It returns 'true' if all elements satisfy the condition, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 69,
        "question": "What is the 'filter' method in JavaScript?",
        "answer": "The 'filter' method is an array method in JavaScript used to create a new array with all elements that pass a provided testing function. It returns an array containing only the elements that satisfy the condition.",
        "learned": False
    },
    {
        "number": 70,
        "question": "What is the 'reduce' method in JavaScript?",
        "answer": "The 'reduce' method is an array method in JavaScript used to apply a function to each element of the array and reduce the array to a single value. It executes the callback function once for each element, passing four arguments: accumulator, current value, current index, and the array itself.",
        "learned": False
    },
    {
        "number": 71,
        "question": "What is the 'flat' method in JavaScript?",
        "answer": "The 'flat' method is an array method in JavaScript used to create a new array with all sub-array elements concatenated into it recursively up to the specified depth. It flattens nested arrays.",
        "learned": False
    },
    {
        "number": 72,
        "question": "What is the 'flatMap' method in JavaScript?",
        "answer": "The 'flatMap' method is an array method in JavaScript used to first map each element using a mapping function, then flatten the result into a new array. It combines the 'map' and 'flat' methods into a single method call.",
        "learned": False
    },
    {
        "number": 73,
        "question": "What is the 'slice' method in JavaScript?",
        "answer": "The 'slice' method is an array method in JavaScript used to extract a section of an array and returns a new array containing the extracted elements. It takes two arguments: the start index (inclusive) and the end index (exclusive).",
        "learned": False
    },
    {
        "number": 74,
        "question": "What is the 'splice' method in JavaScript?",
        "answer": "The 'splice' method is an array method in JavaScript used to change the contents of an array by removing or replacing existing elements and/or adding new elements in place. It modifies the original array and returns an array containing the removed elements, if any.",
        "learned": False
    },
    {
        "number": 75,
        "question": "What is the 'sort' method in JavaScript?",
        "answer": "The 'sort' method is an array method in JavaScript used to sort the elements of an array in place and return the sorted array. It modifies the original array and sorts the elements according to the Unicode code point values of the elements' string representations.",
        "learned": False
    },
    {
        "number": 76,
        "question": "What is the 'concat' method in JavaScript?",
        "answer": "The 'concat' method is an array method in JavaScript used to merge two or more arrays and return a new array containing the combined elements of the original arrays. It does not modify the original arrays.",
        "learned": False
    },
    {
        "number": 77,
        "question": "What is the 'join' method in JavaScript?",
        "answer": "The 'join' method is an array method in JavaScript used to create and return a new string by concatenating all the elements of an array, separated by a specified separator string. It does not modify the original array.",
        "learned": False
    },
    {
        "number": 78,
        "question": "What is the 'toString' method in JavaScript?",
        "answer": "The 'toString' method is an array method in JavaScript used to convert an array to a string and return the resulting string. It converts each element of the array to a string and joins them together with commas.",
        "learned": False
    },
    {
        "number": 79,
        "question": "What is the 'reverse' method in JavaScript?",
        "answer": "The 'reverse' method is an array method in JavaScript used to reverse the order of the elements in an array in place and return the reversed array. It modifies the original array.",
        "learned": False
    },
    {
        "number": 80,
        "question": "What is the 'isArray' method in JavaScript?",
        "answer": "The 'isArray' method is a static method in JavaScript's 'Array' object used to determine whether a value is an array. It returns 'true' if the value is an array, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 81,
        "question": "What is event delegation in JavaScript?",
        "answer": "Event delegation is a technique in JavaScript where a single event listener is attached to a parent element instead of individual child elements. When an event occurs, it bubbles up from the child elements to the parent element, allowing the parent element to handle the event.",
        "learned": False
    },
    {
        "number": 82,
        "question": "What is event propagation in JavaScript?",
        "answer": "Event propagation refers to the flow of events through the DOM tree from the target element to its ancestors or from the document root to the target element. It consists of two phases: capturing phase and bubbling phase.",
        "learned": False
    },
    {
        "number": 83,
        "question": "What is event bubbling in JavaScript?",
        "answer": "Event bubbling is the default behavior in JavaScript where an event occurring on a child element bubbles up through its ancestors in the DOM tree until it reaches the document root. This allows event handlers attached to ancestor elements to also handle the event.",
        "learned": False
    },
    {
        "number": 84,
        "question": "What is event capturing in JavaScript?",
        "answer": "Event capturing is the phase of event propagation in JavaScript where the event travels from the document root down to the target element. During the capturing phase, event handlers attached to ancestor elements are invoked before the event reaches the target element.",
        "learned": False
    },
    {
        "number": 85,
        "question": "What is event.preventDefault() in JavaScript?",
        "answer": "The event.preventDefault() method is a function in JavaScript used to prevent the default action of an event from occurring. It is often used within event handlers to prevent the default behavior of certain elements, such as submitting a form or following a link.",
        "learned": False
    },
    {
        "number": 86,
        "question": "What is event.stopPropagation() in JavaScript?",
        "answer": "The event.stopPropagation() method is a function in JavaScript used to stop the propagation of an event through the DOM tree. It prevents the event from bubbling up to ancestor elements or capturing down to descendant elements.",
        "learned": False
    },
    {
        "number": 87,
        "question": "What is event.target in JavaScript?",
        "answer": "The event.target property in JavaScript refers to the element on which the event occurred. It is often used within event handlers to access the element that triggered the event, allowing developers to perform actions based on the target element.",
        "learned": False
    },
    {
        "number": 88,
        "question": "What is event.currentTarget in JavaScript?",
        "answer": "The event.currentTarget property in JavaScript refers to the element that currently has the event handler attached to it. Unlike event.target, which always refers to the element on which the event occurred, event.currentTarget remains constant throughout event propagation.",
        "learned": False
    },
    {
        "number": 89,
        "question": "What is the 'bind' method in JavaScript?",
        "answer": "The 'bind' method is a function in JavaScript used to create a new function with a specified 'this' value and optional arguments. It allows developers to explicitly set the context in which a function will be executed, regardless of how it is called.",
        "learned": False
    },
    {
        "number": 90,
        "question": "What is the 'call' method in JavaScript?",
        "answer": "The 'call' method is a function in JavaScript used to invoke a function with a specified 'this' value and individual arguments. It allows developers to explicitly set the context in which a function will be executed and pass arguments individually.",
        "learned": False
    },
    {
        "number": 91,
        "question": "What is the 'apply' method in JavaScript?",
        "answer": "The 'apply' method is a function in JavaScript used to invoke a function with a specified 'this' value and arguments provided as an array. It allows developers to explicitly set the context in which a function will be executed and pass arguments as an array.",
        "learned": False
    },
    {
        "number": 92,
        "question": "What is the 'bind' method in JavaScript?",
        "answer": "The 'bind' method is a function in JavaScript used to create a new function with a specified 'this' value and optional arguments. It allows developers to explicitly set the context in which a function will be executed, regardless of how it is called.",
        "learned": False
    },
    {
        "number": 93,
        "question": "What is the 'forEach' method in JavaScript?",
        "answer": "The 'forEach' method is an array method in JavaScript used to iterate over the elements of an array and execute a callback function for each element. It is often used as an alternative to traditional 'for' loops for iterating over arrays.",
        "learned": False
    },
    {
        "number": 94,
        "question": "What is the 'map' method in JavaScript?",
        "answer": "The 'map' method is an array method in JavaScript used to create a new array with the results of calling a provided function on every element in the original array. It applies the callback function to each element and returns an array of the results.",
        "learned": False
    },
    {
        "number": 95,
        "question": "What is the 'filter' method in JavaScript?",
        "answer": "The 'filter' method is an array method in JavaScript used to create a new array with all elements that pass a provided testing function. It returns an array containing only the elements that satisfy the condition.",
        "learned": False
    },
    {
        "number": 96,
        "question": "What is the 'reduce' method in JavaScript?",
        "answer": "The 'reduce' method is an array method in JavaScript used to apply a function to each element of the array and reduce the array to a single value. It executes the callback function once for each element, passing four arguments: accumulator, current value, current index, and the array itself.",
        "learned": False
    },
    {
        "number": 97,
        "question": "What is the 'some' method in JavaScript?",
        "answer": "The 'some' method is an array method in JavaScript used to test whether at least one element in the array satisfies a provided testing function. It returns 'true' if at least one element satisfies the condition, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 98,
        "question": "What is the 'every' method in JavaScript?",
        "answer": "The 'every' method is an array method in JavaScript used to test whether all elements in the array satisfy a provided testing function. It returns 'true' if all elements satisfy the condition, and 'false' otherwise.",
        "learned": False
    },
    {
        "number": 99,
        "question": "What is the 'find' method in JavaScript?",
        "answer": "The 'find' method is an array method in JavaScript used to return the first element in the array that satisfies a provided testing function. It returns 'undefined' if no such element is found.",
        "learned": False
    },
    {
        "number": 100,
        "question": "What is the 'findIndex' method in JavaScript?",
        "answer": "The 'findIndex' method is an array method in JavaScript used to return the index of the first element in the array that satisfies a provided testing function. It returns '-1' if no such element is found.",
        "learned": False
    }
    
]

   

