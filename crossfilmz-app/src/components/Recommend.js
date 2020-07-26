import React from "react";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import AllInclusiveIcon from "@material-ui/icons/AllInclusive";

class Recommend extends React.Component {
  state = {
    movies: []
  };
  render() {
    return (
      <ListItem
        button
        key={this.props.text}
        onClick={async () => {
          const url = "http://127.0.0.1:5000/get_recs";
          const response = await fetch(url);
          const data = await response.json();
          var finalEntry = [];
          console.log(data);

          for (const [key, value] of Object.entries(data)) {
            finalEntry = finalEntry.concat(data[key].map(x => x[0]));
          }
          console.log(finalEntry);
          this.props.updateMovies(finalEntry);
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

export default Recommend;
