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

  async componentDidMount() {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        platforms: [""]
      })
    };
    console.log(requestOptions);
    const url = "http://127.0.0.1:5000/get_movies";
    const response = await fetch(url, requestOptions);
    const data = await response.json();
    console.log(data);
    this.setState({ allmovies: data, loading: false });
  }

  render() {
    if (this.state.loading) {
      return <h1>Loading movies....</h1>;
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
