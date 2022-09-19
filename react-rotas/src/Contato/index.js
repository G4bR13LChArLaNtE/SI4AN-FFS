import React, { useState, createContext } from 'react';
import { Link } from "react-router-dom";


import './Contato.css';



export default function Contato() {


    const [formValues, setFormValues] = useState({});

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormValues({...formValues, [name]: value});

    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);

        console.log("Os Dados são", data);

        const Context = createContext(handleSubmit);

        console.log(Context);

        return data;

    }


    

    


   return (

       <div className="pagecontato">
           

        <form onSubmit={handleSubmit}>

            <label>
                <h5>Nome:</h5>
                <input
                onChange={handleChange}
                type="text"
                name="nome"
                placeholder="Seu nome, por favor!"
                size="53"
                value={formValues.nome}
                nome={formValues.nome}/>
            </label>
            <label>
                <h5>E-mail:</h5>
                <input
                onChange={handleChange}
                type="email"
                name="email"
                placeholder="Digite seu e-mail" 
                size="53"
                value={formValues.email}
                email={formValues.email}/>
            </label>
            <label>
                <h5>Assunto:</h5>
                <input 
                onChange={handleChange}
                type="text"
                name="assunto"
                placeholder="Sobre o quê vamos conversar?" 
                size="53"
                value={formValues.assunto}
                assunto={formValues.assunto}/>
            </label>
            <label>
            <h5>Mensagem:</h5>
                <textarea
                onChange={handleChange}
                name="mensagem"
                value={formValues.mensagen}
                mensagem={formValues.mensagem}
                placeholder="Digite a mensagem..."
                row="14"
                maxlength="750">
                </textarea>
            </label><br /><br />

            <select
            name="sexo"
            value={formValues.sex}
            onChange={handleChange}>
                <option value="M">Masculino</option>
                <option value="F">Feminino</option>
            </select><br /><br /><br /><br /><br /><br />

            <button type="submit">Enviar</button>
        </form><br /><br /><br /><br />



                        <div className="container">

                <p>Nome:{formValues.nome}</p>
                <p>E-mail:{formValues.email}</p>
                <p>Assunto:{formValues.assunto}</p>
                <p>Mensagem:{formValues.mensagem}</p>

                </div><br /><br /><br /><br />


<Link to="/Home">retornar a página inicial</Link><br /><br /><br /><br /><br /><br />
       </div>

       
   );
}

