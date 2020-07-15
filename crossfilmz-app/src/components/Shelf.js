import React from "react";
import MovieCard from "./MovieCard";
import "../basic-grid.css";

class Shelf extends React.Component {

  state = {
    loading: true,
    allmovies: []
  };   

  
  render() {
    return <div class = "basic-grid">
        <MovieCard class = "card" title = "a" tags = "Animation, Adventure" platform = "Netflix, Hulu" poster = "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"/>
        <MovieCard class = "card" title = "b" tags = "Comedy, Family" platform = "Disney+" poster = "https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwODM@._V1_SX300.jpg"/>
    </div>;
  }
}

export default Shelf;
