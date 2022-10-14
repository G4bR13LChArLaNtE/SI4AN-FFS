import React from 'react';
import {Routes, Route, Link} from 'react-router-dom';
import Home from './Home';
import Sobre from './Sobre';
import Usuario from './Usuario';
import './App.css'


export default function App() {
   return (
       <div className="App">
     <header className="App-header">
     <p><Link to='/home'>Home</Link></p>
     <p><Link to='/sobre/aula'>Sobre</Link></p>
     <p><Link to='/usuario'>Usuario</Link></p>
     </header>
     <main>
         <Routes>
           <Route path='/usuario' component= {Usuario}/>
           <Route path='/sobre/:id?' component= {Sobre}/>
           <Route path='/home' component= {Home}/>
         </Routes>
       </main>
       </div>
   );
}
