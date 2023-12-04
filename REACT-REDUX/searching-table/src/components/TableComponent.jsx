import React, { useState } from "react";

/* The `const data` is an array of objects that represents a collection of data. Each object in the
array represents a person with properties such as `id`, `name`, and `age`. This data can be used to
populate a table in the React component. */
const data = [
  { id: 1, name: "Tirth", age: 20 },
  { id: 2, name: "Devanshu", age: 23 },
  { id: 3, name: "abhay", age: 23 },
  { id: 4, name: "Devansh", age: 23 },
  { id: 5, name: "abhi", age: 23 },
  { id: 6, name: "namika", age: 23 },
  { id: 7, name: "abhijeet", age: 23 },
  { id: 8, name: "uday", age: 23 },
];

/* The code block is defining a React functional component called `App`. Inside the component, it is
using the `useState` hook to create a state variable called `searchTerm` and a function called
`setSearchTerm` to update the state. */
const App = () => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredData = data.filter((item) =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="App">
      <input
        type="text"
        placeholder="Search by name"
        value={searchTerm}
        onChange={handleSearch}
        className="border border-gray-300 p-2 m-2"
      />

      <table className="border-collapse border border-gray-500 m-2">
        <thead>
          <tr className="bg-gray-200">
            <th className="border border-gray-500 p-2">ID</th>
            <th className="border border-gray-500 p-2">Name</th>
            <th className="border border-gray-500 p-2">Age</th>
          </tr>
        </thead>
        <tbody>
          {/* /* /* The code block you provided is using the `map` function to iterate over the `filteredData`
        array and create a new array of React elements. */}
          {filteredData.map((item) => (
            <tr key={item.id} className="bg-white">
              <td className="border border-gray-500 p-2">{item.id}</td>
              <td className="border border-gray-500 p-2">{item.name}</td>
              <td className="border border-gray-500 p-2">{item.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;
