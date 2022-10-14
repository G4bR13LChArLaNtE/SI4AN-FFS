import React from 'react';
import { Link } from "react-router-dom";



import '../Contato/index'

export default function Dados(){

    const nome = document.getElementById('nome');


    return(
        <div className="pagedados">
                <div className="container">

                        <p>Nome:{nome}</p>
                        <p>E-mail:</p>
                        <p>Assunto:</p>
                        <p>Mensagem:</p>

                        </div><br /><br /><br /><br />



<Link to="/Home">retornar a página inicial</Link>
<br /><br /><br /><br /><br /><br />

       </div>
    );
}