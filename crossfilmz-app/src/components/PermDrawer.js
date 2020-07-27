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
import RecommendPlatform from "./RecommendPlatform";
const drawerWidth = 240;
const styles = theme => ({
  root: {
    display: "flex"
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0
  },
  drawerPaper: {
    width: drawerWidth
  },
  drawerContainer: {
    overflow: "auto"
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3)
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
          <Toolbar />
          <div className={classes.drawerContainer} />
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
            <RecommendPlatform
              text="Suggest Netflix"
              platform = "Netflix"
              updateMovies={this.updateMovies}
            />
            <RecommendPlatform
              text="Suggest Amazon"
              platform = "Amazon Instant Video"
              updateMovies={this.updateMovies}
            />
            <RecommendPlatform
              text="Suggest Hulu"
              platform = "Hulu"
              updateMovies={this.updateMovies}
            />
            <RecommendPlatform
              text="Suggest Disney+"
              platform = "Disney+"
              updateMovies={this.updateMovies}
            />            
          </List>
        </Drawer>
        <main className={classes.content}>
          <Toolbar />
          <Shelf movies_to_render={this.state.movies} />
        </main>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(PermDrawer);
