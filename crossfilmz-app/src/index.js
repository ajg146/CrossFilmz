import React, { Component } from "react";
import ReactDOM from "react-dom";
import Hello from "./components/Hello";
import Search from "./components/Search";
import MovieCard from "./components/MovieCard";
import Recomend from "./components/Recomend";
import Rating from "./components/Rating";
class App extends Component {
  render() {
    return (
      <div className="App">
        <Search></Search>
        <MovieCard></MovieCard>
        <Recomend></Recomend>
 
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
