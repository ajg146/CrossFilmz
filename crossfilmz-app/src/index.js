import React, { Component } from "react";
import ReactDOM from "react-dom";
import Drawer from "./components/Drawer";
import PermDrawer from "./components/PermDrawer"
class App extends Component {
  render() {
    return (
      <div className="App">
        <PermDrawer />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
