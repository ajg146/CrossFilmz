import React, { Component } from "react";
import ReactDOM from "react-dom";
import Hello from "./components/Hello";
import Search from "./components/Search";
import MovieCard from "./components/MovieCard";
class App extends Component {
  render() {
    return (
      <div className="App">
        <Search></Search>
        <MovieCard></MovieCard>
        <h1>Hello, React!</h1>
        <Hello></Hello>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
