import React from "react";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import AllInclusiveIcon from "@material-ui/icons/AllInclusive";

class ApiButton extends React.Component {
  state = {
    movies: []
  };
  render() {
    return (
      <ListItem
        button
        key={this.props.text}
        onClick={async () => {
          const url = "http://127.0.0.1:5000/get_movies";
          const response = await fetch(url);
          const data = await response.json();
          //console.log(data);
          this.props.updateMovies(data);
        }}
      >
        <ListItemIcon>
          <AllInclusiveIcon />
        </ListItemIcon>
        <ListItemText primary={this.props.text} />
      </ListItem>
    );
  }
}

export default ApiButton;
