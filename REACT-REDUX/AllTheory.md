# What is Redux?

### Redux is a predictable state container for JavaScript applications. It helps manage the state of an application in a predictable way, making it easier to understand, debug, and maintain. Redux is commonly used with React, although it can be used with any other library or framework. The core principles of Redux include having a single source of truth (the state), state is read-only, changes are made with pure functions (reducers), and the use of actions to describe state changes.

# What is Redux Thunk used for?

### Redux Thunk is a middleware for Redux that allows you to write action creators that return functions instead of plain action objects. This is useful for handling asynchronous operations, such as API calls, within your Redux actions. By returning a function from an action creator, you can delay the dispatch of an action, perform asynchronous operations, and then dispatch another action with the results. This helps in managing side effects in a Redux application.

# What is Pure Component? When to use Pure Component over Component?

### In React, a PureComponent is a base class for components that implements a shouldComponentUpdate method with a shallow prop and state comparison. This means that a PureComponent will only re-render if the props or state have changed, preventing unnecessary renders.

### You should use PureComponent over the regular Component when you want to optimize performance by avoiding unnecessary renders. If your component's render output is purely based on props and state, and a shallow comparison is sufficient to determine if an update is needed, then using PureComponent can lead to performance improvements.

# What is the second argument that can optionally be passed to setState, and what is its purpose?

### The second argument that can be passed to the setState method in React is a callback function that will be executed once the state has been updated and the component has been re-rendered. This callback is often used to perform actions that depend on the updated state.
