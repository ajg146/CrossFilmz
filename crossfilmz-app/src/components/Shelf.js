import React from "react";
import MovieCard from "./MovieCard";
import "../basic-grid.css";
import sample from "./sample_response.json";
import shortid from "shortid";

class Shelf extends React.Component {
  state = {
    loading: true,
    allmovies: []
  };

  async componentDidUpdate(prevProps, prevState) {
    const movies = this.props.movies_to_render;
    if (movies.length != prevProps.movies_to_render.length) {
      this.setState({ allmovies: movies, loading: false });
    }
  }

  render() {
    if (this.state.loading) {
      return <h1>CLick button to load movies</h1>;
    }
    return (
      <div class="basic-grid">
        {this.state.allmovies.map(eachMovie => (
          <MovieCard
            class="card"
            key={shortid.generate()}
            title={eachMovie[0]}
            tags={eachMovie[1]}
            platform={eachMovie[2]}
            poster="https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
          />
        ))}
      </div>
      // <div class="basic-grid">
      //   <MovieCard
      //     class="card"
      //     title={this.state.allmovies[0][0]}
      //     tags={this.state.allmovies[0][1]}
      //     platform={this.state.allmovies[0][2]}
      //     poster="https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
      //   />
      //   <MovieCard
      //     class="card"
      //     title={this.state.allmovies[1]}
      //     tags="Comedy, Family"
      //     platform="Disney+"
      //     poster="https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwODM@._V1_SX300.jpg"
      //   />
    );
  }
}

export default Shelf;
