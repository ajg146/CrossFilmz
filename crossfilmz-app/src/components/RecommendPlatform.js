import React from "react";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import AllInclusiveIcon from "@material-ui/icons/AllInclusive";

class RecommendPlatform extends React.Component {
  state = {
    movies: []
  };

  render() {
    return (
      <ListItem
        button
        key={this.props.text}
        onClick={async () => {
          const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              platform: [this.props.platform]
            })
          };
          console.log(requestOptions);
          const url = "http://127.0.0.1:5000/filter_recs";
          const response = await fetch(url, requestOptions);
          const data = await response.json();
          const finalEntry = data.map(x => x[0]);
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

export default RecommendPlatform;
