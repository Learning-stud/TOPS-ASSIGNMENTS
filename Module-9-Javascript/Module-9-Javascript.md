# JavaScript Interview  Questions and Answers

##  Q-1: What is JavaScript?

JavaScript is a lightweight programming language that web developers commonly use to create more dynamic interactions when developing web pages, applications, servers, and even games. Developers generally use JavaScript alongside HTML and CSS. The scripting language works well with CSS in formatting HTML elements. However, JavaScript still maintains user interaction, something that CSS cannot do by itself. JavaScript's implementations within web, mobile application, and game development make the scripting language worth learning.

##  Q-2: What is the use of isNaN function?

In JavaScript, `NaN` is short for "Not-a-Number." The `isNaN()` function is used to determine if a value is `NaN` (Not-a-Number) or not. It returns `true` if the value is `NaN`, otherwise, it returns `false`. The `isNaN()` function converts the value to a Number before testing it.

**Examples:**
```javascript
console.log(isNaN(12));           // Output: false
console.log(isNaN(0 / 0));        // Output: true
console.log(isNaN(12.3));         // Output: false
console.log(isNaN("Devanshu"));   // Output: true
console.log(isNaN("25/05/2023")); // Output: true
console.log(isNaN(-46));          // Output: false
console.log(isNaN(NaN));          // Output: true

##  Q-3: What is negative Infinity?
Negative Infinity in JavaScript is a constant value that represents a value that is the lowest available. This means that no other number is lesser than this value. It can be generated using a self-made function or by an arithmetic operation. JavaScript shows the NEGATIVE_INFINITY value as -Infinity.

Example:

javascript
let x = Number.NEGATIVE_INFINITY;
console.log(x); // Output: -Infinity
Negative infinity behaves differently from mathematical infinity in various arithmetic operations. For example, when divided by any other number, it results in -0, and when divided by itself or positive infinity, it returns NaN.

## Q 4: Which company developed JavaScript?
JavaScript was invented by Brendan Eich in 1995. It was developed for Netscape 2 and became the ECMA-262 standard in 1997. After Netscape handed JavaScript over to ECMA, the Mozilla foundation continued to develop JavaScript for the Firefox browser.

## Q 5: What are undeclared and undefined variables?
Undefined:
Undefined occurs when a variable has been declared but has not been assigned any value. It is not a keyword.

##Example of Undefined:

javascript
let a;
console.log(a); // Console gives Error like 'a' is undefined.
Undeclared:
Undeclared variables occur when we try to access any variable that is not initialized or declared earlier using the var or const keyword. If we use the 'typeof' operator to get the value of an undeclared variable, we will face a runtime error with the return value as "undefined." The scope of undeclared variables is always global.

Example of Undeclared:

javascript
console.log(a); // ReferenceError: a is not declared

## Q-6: Write the code for adding new elements dynamically?
JavaScript allows us to dynamically create new elements and add them to the DOM using the createElement() method.

Example:

javascript
// Create a new div element
let newDiv = document.createElement("div");

// Add text content to the new element
newDiv.textContent = "This is a new div element";

// Append the new element to an existing element in the DOM
document.body.appendChild(newDiv);

## Q-7: Differences between ViewState and SessionState:
ViewState	SessionState
Maintained at page level only.	Maintained at session level.
View state can only be visible from a single page and not multiple pages.	Session state value availability is across all pages available in a user session.
It will retain values in the event of a postback operation occurring.	In session state, user data remains in the server. Data is available to the user until the browser is closed or there is session expiration.
Information is stored on the client’s end only.	Information is stored on the server.
Used to allow the persistence of page-instance-specific data.	Used for the persistence of user-specific data on the server’s end.
ViewState values are lost/cleared when a new page is loaded.	SessionState can be cleared by a programmer or user or in case of timeouts.

## Q-8: What is the === operator?
The === operator is a strict e quality comparison operator in JavaScript. It compares both the value and the data type of two operands and returns true only if they are both of the same type and have the same value.

Example:

javascript
console.log(5 === "5"); // Output: false
console.log(5 === 5);   // Output: true

## Q-9: How can the style/class of an element be changed?
We can change, add, or remove any CSS property from an HTML element using JavaScript. There are two common approaches to achieve this task:

Changing Style Properties:
We can directly access the style property of an HTML element and change its CSS properties.

Example:

html
<button id="myButton">Click Me</button>
javascript
// Change the background color of the button when clicked
document.getElementById("myButton").onclick = function() {
  this.style.backgroundColor = "red";
};
Changing Classes:
By changing the class attribute of an element, we can apply pre-defined CSS styles to it.

Example:

html
<div id="myDiv">This is a div element</div>
javascript
// Change the class of the div to apply different styles
document.getElementById("myDiv").onclick = function() {
  this.className = "newStyle";
};

## Q-10: What is a bootstrap card and how would you create one?
A Bootstrap card is a flexible and extensible content container that includes options for headers, footers, and other styles. To create a basic Bootstrap card, you need to follow these steps:

Add the .card class to a <div> element.
Inside the <div> element, add another element with the .card-body class.
Add text or other content inside the .card-body element.
Example:

html
<div class="card" style="width: 18rem;">
  <img src="profile-logo.jpg" alt="Profile Image">
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">This is some text inside the card body.</p>
    <a href="#" class="btn btn-primary">Click Me</a>
  </div>
</div>

## Q-11: How to read and write a file using JavaScript?
Write operation on a file:
After importing the File System module, you can use the writeFile() operation to write into a file in JavaScript.

Syntax:

javascript
writeFile(path, inputData, callBackFunction);
path: The path of the file or the name of the file into which the input data is to be written.
inputData: The data to be written in the file.
callBackFunction: The callback function that handles errors if the write operation fails.
Reading from the file:
After importing the File System module, you can use the readFile() function to read from a file in JavaScript.

Syntax:

javascript
readFile(path, format, callBackFunc);
path: The path of the file from which the contents are to be read.
format: The optional parameter representing the format of the text file (e.g., ASCII, utf-8).
callBackFunc: The callback function that handles errors and displays the file content.

## Q-12: What are all the looping structures in JavaScript?
JavaScript mainly provides three ways for executing loops:

while loop:
A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. It can be thought of as a repeating if statement.

Syntax:

javascript
while (condition) {
  // loop statements...
}
for loop:
The for loop provides a concise way of writing the loop structure. It consumes the initialization, condition, and increment/decrement in one line, providing a shorter and easy-to-debug structure of looping.

Syntax:

javascript
for (initialization; condition; increment/decrement) {
  // statements...
}
do-while loop:
The do-while loop is similar to the while loop, but it checks for the condition after executing the statements, making it an example of an Exit Control Loop.

Syntax:

javascript
do {
  // Statements...
} while (condition);

## Q-13: How can you convert the string of any base to an integer in JavaScript?
JavaScript provides the parseInt() function to convert a string of any base to an integer.

Syntax:

javascript
parseInt(string, radix);
string: The value to parse. If this argument is not a string, it is converted to one using the ToString method. Leading whitespace in this argument is ignored.
radix: An integer between 2 and 36 that represents the radix (the base in mathematical numeral systems) of the string.
Examples:

javascript
console.log(parseInt("100", 10));  // Output: 100
console.log(parseInt("10", 8));    // Output: 8
console.log(parseInt("101", 2));   // Output: 5
console.log(parseInt("2FF3", 16)); // Output: 12275
console.log(parseInt("ZZ", 36));   // Output: 1295

## Q-14: What is the function of the delete operator?
The delete operator in JavaScript is used to delete an object or a property from an object.

Syntax:

javascript
Copy code
delete object;
delete object.property;
delete object['property'];
object: The object from which you want to delete a property.
property: The specific property you want to delete.
The delete operator behaves differently depending on whether the object is in strict mode or not.


## Q-15: What are all the types of Pop up boxes available in JavaScript?
In JavaScript, popup boxes are used to display messages or notifications to the user. There are three types of popup boxes:

Alert Box:
It is used when a warning message is needed to be displayed. The user needs to press "OK" to proceed.

Syntax:

javascript
alert("Your Alert here");
Confirm Box:
It is used to get authorization or permission from the user. The user has to press "OK" or "Cancel" to proceed.

Syntax:

javascript
confirm("Confirm This...");
Prompt Box:
It is used to get user input for further use. The user can enter the re quired details and click "OK" to proceed or click "Cancel" to return a null value.

Syntax:

javascript
prompt("Your Prompt here");

## Q-16: What is the use of Void (0)?
The void keyword in JavaScript is a unary operator that evaluates its operand and always returns the undefined primitive value. Its primary purpose is to create an expression that performs an action without returning a value or to create a shortcut for returning undefined from a function.

Example:

html
<a href="#" onclick="doSomething(); void 0;">Click me</a>
In this example, doSomething() function is called, and then void 0 is used to create an expression that evaluates to undefined. The use of void prevents the browser from navigating to a new page when the link is clicked.

## Q-17: How can a page be forced to load another page in JavaScript?
In JavaScript, you can use the window.location object to force a page to load another page.

Using window.location.href property:
This property contains information about the current URL of the page, and you can set it to the URL of the new page to force the redirection.

Example:

## javascript
// Redirect the user to a new page immediately
window.location.href = "https://www.example.com";
Using window.location.assign() method:
The assign() method performs the same action as setting window.location.href.

Example:

javascript
// Redirect the user to a new page after a specified amount of time
setTimeout(function() {
  window.location.assign("https://www.example.com");
}, 2000);
Using window.location.replace() method:
The replace() method also redirects the user to a new page, but it replaces the current page in the browser history.

Example:

javascript
// Replace the current page with a new page
window.location.replace("https://www.example.com");
These are the different ways to force a page to load another page in JavaScript.

##  Q:18 Disadvantages of using innerHTML in JavaScript

## When working with JavaScript and manipulating the DOM, the innerHTML property is often used to dynamically update or create elements within an HTML document. While innerHTML can be convenient and easy to use, it also comes with several disadvantages that developers should be aware of:

Security Vulnerabilities: One of the most significant drawbacks of using innerHTML is the potential for introducing security vulnerabilities, specifically related to Cross-Site Scripting (XSS). If the content assigned to innerHTML is not properly sanitized or validated, it could lead to the injection of malicious scripts into the page, posing a serious security risk.

Overwriting Existing Event Listeners: When you set innerHTML on an element, any existing event listeners attached to its child elements get removed. This can lead to unexpected behavior or loss of functionality if you're not careful when manipulating the content.

Performance Impact: Using innerHTML to modify the DOM can cause significant performance issues, especially when dealing with large or nested structures. When you set innerHTML, the browser must reparse and rebuild the entire content, which can be time-consuming and lead to reduced performance.

Memory Leaks: Frequent usage of innerHTML can lead to memory leaks in certain browsers, particularly in older versions of Internet Explorer. The browser may fail to release memory associated with the replaced elements, causing potential performance degradation.

Loss of Event Binding: If you dynamically replace or update elements using innerHTML, any event handlers previously attached to those elements will be lost. You'll need to rebind the events after updating the content, which can lead to additional complexity and potential bugs.

Incompatibility with SVG and MathML: While innerHTML is suitable for working with HTML content, it may not behave as expected when used with SVG or MathML elements. For these specialized types of content, other DOM manipulation methods are more appropriate.

Accessibility Concerns: By using innerHTML, you risk creating content that is not accessible to all users, particularly those relying on screen readers or assistive technologies. Properly appending or modifying elements using the DOM API can ensure better accessibility.

Code Maintainability: As innerHTML allows for easy string concatenation, it can lead to less structured and maintainable code compared to using DOM manipulation methods like createElement and appendChild.

In conclusion, while innerHTML can be a quick solution for some DOM manipulation tasks, it's essential to be aware of its drawbacks and

