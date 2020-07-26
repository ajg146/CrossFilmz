import React from "react";
import { withStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import CssBaseline from "@material-ui/core/CssBaseline";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import List from "@material-ui/core/List";
import Divider from "@material-ui/core/Divider";
import Search from "./Search";
import Shelf from "./Shelf";
import LoginIcon from "./LoginIcon";
import ApiButton from "./ApiButton";
import Recommend from "./Recommend";

const drawerWidth = 240;
const styles = theme => ({
  root: {
    display: "flex"
  },
  appBar: {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0
  },
  drawerPaper: {
    width: drawerWidth
  },
  // necessary for content to be below app bar
  toolbar: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
    padding: theme.spacing(5)
  }
});
class PermDrawer extends React.Component {
  state = {
    movies: []
  };
  updateMovies = dataFromChild => {
    console.log(dataFromChild);
    this.setState({ movies: dataFromChild });
  };
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <CssBaseline />
        <AppBar position="fixed" className={classes.appBar}>
          <Toolbar>
            <Search></Search>
            <LoginIcon></LoginIcon>
          </Toolbar>
        </AppBar>
        <Drawer
          className={classes.drawer}
          variant="permanent"
          classes={{
            paper: classes.drawerPaper
          }}
          anchor="left"
        >
          <div className={classes.toolbar} />
          <Divider />
          <List>
            <ApiButton text="Netflix" updateMovies={this.updateMovies} />
            <ApiButton text="Amazon" updateMovies={this.updateMovies} />
            <ApiButton text="Hulu" updateMovies={this.updateMovies} />
            <ApiButton text="Disney" updateMovies={this.updateMovies} />
          </List>
          <Divider />
          <List>
            <Recommend text="Recommend" updateMovies={this.updateMovies} />
            {/* <Recommend text="Netflix" updateMovies={this.updateMovies} />
            <Recommend text="Amazon" updateMovies={this.updateMovies} />
            <Recommend text="Hulu" updateMovies={this.updateMovies} />
            <Recommend text="Disney" updateMovies={this.updateMovies} /> */}
          </List>
        </Drawer>
        <main className={classes.content}>
          <div className={classes.toolbar} />
          <Shelf movies_to_render={this.state.movies} />
        </main>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(PermDrawer);
