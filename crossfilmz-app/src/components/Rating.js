import React from "react";
import Rating from "@material-ui/lab/Rating";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
  root: {
    display: "flex",
    flexDirection: "column",
    "& > * + *": {
      marginTop: theme.spacing(1)
    }
  }
}));

export default function HalfRating(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  return (
    <div className={classes.root}>
      <Rating
        value={value}
        onChange={async (event, newValue) => {
          setValue(newValue);
          const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              title: props.title,
              genre: props.tags,
              platform: props.platform,
              score: newValue
            })
          };
          console.log(requestOptions);
          const url = "http://127.0.0.1:5000/add_rating";
          const response = await fetch(url, requestOptions);
          const data = await response.json();
          console.log(data);
        }}
      ></Rating>
    </div>
  );
}
