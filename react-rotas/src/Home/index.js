import React from 'react';


import './Home.css';

export default function Home(){
   return (
       <div className="pagehome">

            <h1>A aplicação</h1>

            <h3 className="desc1">React-router-dom:</h3>
            <p> Olá, tudo bem? Me Chamo Gabriel Charlante. Aqui nessa aplicação feita em React você verá um pouco sobre a utilização da biblioteca rect-router-dom.</p>

            <p> O react-router-dom é uma biblioteca padrão para que você consiga fazer o roteamento das páginas da sua aplicação de forma dinâmica.</p>

            <p>Aqui você verá a aplicação prática dessa biblioteca de forma simples e direta. Ao apertar nos links acima você será direcionado para a página selecionada.</p>


            <h3 className="desc2">Próximas páginas:</h3>
            <p>Nas próximas páginas utilizei como base minhas informações curriculares. Na página "<b>Sobre</b>" você conhecerá um pouco mais sobre a minha pessoal e minha carreira, já na página "<b>Contato</b>" você poderá me contatar através de um formulário.</p>
       </div>
   );
}