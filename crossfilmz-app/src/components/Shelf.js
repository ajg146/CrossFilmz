import React from "react";
import MovieCard from "./MovieCard";
import "../styles/basic-grid.css";
import shortid from "shortid";

class Shelf extends React.Component {
  state = {
    loading: true,
    allmovies: []
  };

  async componentDidUpdate(prevProps, prevState) {
    const movies = this.props.movies_to_render;
    if (movies.length !== prevProps.movies_to_render.length) {
      this.setState({ allmovies: movies, loading: false });
    }
  }

  render() {
    if (this.state.loading) {
      return <h1>Click button to load movies</h1>;
    }
    return (
      <div className="basic-grid">
        {this.state.allmovies.map(eachMovie => (
          <MovieCard
            class="card"
            key={shortid.generate()}
            title={eachMovie[0]}
            tags={eachMovie[1]}
            platform={eachMovie[2]}
            poster={eachMovie[3]}
          />
        ))}
      </div>
    );
  }
}

export default Shelf;
