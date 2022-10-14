from flask import Flask, jsonify # Importa a biblioteca

aluno1 = {
  'nome' : 'Joao',
  'idade': '27',
  'Profissao':'Tecnico Hospitalar',
  'RA':'17234567'
}

aluno2 = {
  'nome' : 'Mateus',
  'idade': '21',
  'Profissao':'Auxiliar administrativo',
  'RA':'15566232'
}

aluno3 = {
  'nome' : 'Marina',
  'idade': '23',
  'Profissao':'Vendedora',
  'RA':'11653465'
}

aluno4 = {
  'nome' : 'Fernanda',
  'idade': '29',
  'Profissao':'Veterinaria',
  'RA':'544816551'
}

aluno5 = {
  'nome' : 'Jose',
  'idade': '22',
  'Profissao': 'Motorista',
  'RA':'4653211351'
}

aluno6 = {
  'nome' : 'Sergio',
  'idade': '28',
  'Profissao': 'Mecanico',
  'RA':'4653213201'
}

aluno7 = {
  'nome' : 'Michelle',
  'idade': '23',
  'Profissao': 'Analista de sistemas',
  'RA':'4561651565'
}

lista = (aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7)


app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
@app.route('/aluno')
def main():
   return jsonify(lista)
  #return 'Meu site em Flask :D'

if __name__ == '__main__':
  app.run(host= 'localhost', port= 9009, debug=True) # Executa a aplicação
