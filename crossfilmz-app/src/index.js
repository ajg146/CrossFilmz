import React, { Component } from "react";
import ReactDOM from "react-dom";
import Hello from "./components/Hello";
import Search from "./components/Search";
class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Hello, React!</h1>
        <Hello></Hello>
        <Search></Search>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
