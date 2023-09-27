**(Q-01): What is jQuery?**

**Answer:**

- jQuery is a lightweight, "write less, do more," JavaScript library.
- The purpose of jQuery is to make it much easier to use JavaScript on your website.
- jQuery takes a lot of common tasks that require many lines of JavaScript code to accomplish and wraps them into methods that you can call with a single line of code.
- jQuery also simplifies a lot of the complicated things from JavaScript, like AJAX calls and DOM manipulation.

The jQuery library contains the following features:
- HTML/DOM manipulation
- CSS manipulation
- HTML event methods
- Effects and animations
- AJAX
- Utilities


**(Q-02): How to Apply CSS Using jQuery, How to Add Class and Remove Class in jQuery, jQuery Animation?**

**How to Apply CSS Using jQuery:**
You can apply CSS to elements using jQuery by using the `.css()` method.

**Syntax for Applying CSS:**
- `$().css(propertyname, value);`
- `$().css(properties);`

**Adding CSS Classes to an Element:**
To add CSS classes to an element, you can use the `.addClass()` method.

**Syntax for Adding CSS Classes:**
- `$('selector').addClass(class_name);`

**Removing CSS Classes from an Element:**
To remove CSS classes from an element, you can use the `.removeClass()` method.

**Syntax for Removing CSS Classes:**
- `$('selector').removeClass(class_name);`

**jQuery Animation:**
The jQuery `animate()` method is used to create custom animations.

**Syntax for jQuery Animation:**
- `$(selector).animate({params}, speed, callback);`

**Example of jQuery Animation:**
```javascript
$("button").click(function(){
  $("div").animate({left: '250px'});
});

**(Q-03): How to create a slider with animation in jQuery?**

**Code:**

```html
<div class="container">
  <div class="slider">
    <ul class="slides">
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=120" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=70" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=50" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=170" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=190" /></li>
    </ul>
  </div>

  <div class="buttons">
    <button type="button" class="btn btn-default pause">
      <span class="glyphicon glyphicon-pause"></span>
    </button>
    <button type="button" class="btn btn-default play">
      <span class="glyphicon glyphicon-play"></span>
    </button>
  </div>
</div>
