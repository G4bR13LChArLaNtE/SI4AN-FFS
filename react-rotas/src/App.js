import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';



import './App.css';
import Home from './Home/index';
import Sobre from './Sobre/index.js';
import Contato from './Contato/index';
import foto from './gabriel-foto.png';



function App() {
  return (
    <div className="page">
    <header>

    <img className="logo" src={foto} alt="Charlante"></img>
    
    <p><Link to='/home'>Início</Link></p>
    <p><Link to='/sobre'>Sobre</Link></p>
    <p><Link to='/Contato'>Contato</Link></p>

    </header>
    <main>
        <Switch>
          <Route path='/contato' component= {Contato}/>
          <Route path='/sobre' component= {Sobre}/>
          <Route path='/' component= {Home}/>
        </Switch>
      </main>
      </div>
  );
}

export default App;
