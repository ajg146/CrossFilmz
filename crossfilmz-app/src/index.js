import React, { Component } from "react";
import ReactDOM from "react-dom";
import Drawer from "./components/Drawer";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Drawer />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
