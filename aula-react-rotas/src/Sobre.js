import React from 'react';
import { Link, useNavigate, useLocation, useParams } from 'react-router-dom';

export default function Sobre (){
    const location = useLocation();
    // eslint-disable-next-line no-unused-vars
    const navigate = useNavigate();
    const { id } = useParams();
    return (
        <div>
            <h1>Sobre: {id} </h1>
            <h1>Path: {location.pathname}</h1>
            <Link to="/">retornar a página inicial</Link>
        </div>
    );
}
