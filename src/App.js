import React, { Component } from 'react';
import {BrowserRouter as Router, Route} from "react-router-dom";
import Balao from './Balao'

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
            <Route exact path="/balao" component={Balao}/>
        </div>
      </Router>
    );
  }
}

export default App;