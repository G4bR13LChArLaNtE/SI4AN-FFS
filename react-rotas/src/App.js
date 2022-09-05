import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';

import './App.css';
import Home from './Home';
import Sobre from './Sobre';
import Usuario from './Usuario';



function App() {
  return (
    <div className="page">
    <header>
    <p><Link to='/home'>Home</Link></p>
    <p><Link to='/usuario'>Usuario</Link></p>
    <p><Link to='/sobre'>Sobre</Link></p>
    </header>
    <main>
        <Switch>
          <Route path='/usuario' component= {Usuario}/>
          <Route path='/sobre' component= {Sobre}/>
          <Route path='/home' component= {Home}/>
        </Switch>
      </main></div>
  );
}

export default App;
