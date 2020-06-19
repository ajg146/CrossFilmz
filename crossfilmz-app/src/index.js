import React, { Component } from "react";
import ReactDOM from "react-dom";
import Hello from "./components/Hello";
import Search from "./components/Search";
import MovieCard from "./components/MovieCard";
import Recomend from "./components/Recomend";
import Rating from "./components/Rating";
import Drawer from "./components/Drawer";
import Avatar from "./components/Avatar";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Drawer />

        {/* <Search></Search>
        <div>
          <MovieCard></MovieCard>
          <MovieCard></MovieCard>
          <MovieCard></MovieCard>
        </div>
        <Recomend></Recomend> */}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
