from flask import Flask, jsonify # Importa a biblioteca

aluno1 = {
  'nome' : 'João',
  'idade': '27',
  'Profissão':'Técnico Hospitalar',
  'RA':'17234567'
}

aluno2 = {
  'nome' : 'Mateus',
  'idade': '21',
  'Profissão':'Auxiliar administrativo',
  'RA':'15566232'
}

aluno3 = {
  'nome' : 'Marina',
  'idade': '23',
  'Profissão':'Vendedora',
  'RA':'11653465'
}

aluno4 = {
  'nome' : 'Fernanda',
  'idade': '29',
  'Profissão':'Veterinária',
  'RA':'544816551'
}

aluno5 = {
  'nome' : 'José',
  'idade': '22',
  'Profissão': 'Motorista',
  'RA':'4653211351'
}

aluno6 = {
  'nome' : 'Sergio',
  'idade': '28',
  'Profissão': 'Mecânico',
  'RA':'4653213201'
}

aluno7 = {
  'nome' : 'Michelle',
  'idade': '23',
  'Profissão': 'Analista de sistemas',
  'RA':'4561651565'
}

lista = (aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7)

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
   return jsonify(lista)
  #return 'Meu site em Flask :D'

if __name__ == '__main__':
  app.run(host= 'localhost', port= 9009, debug=True) # Executa a aplicação
