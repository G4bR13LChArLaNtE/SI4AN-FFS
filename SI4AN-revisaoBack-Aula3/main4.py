from flask import Flask, jsonify # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
   return jsonify(hello='world')
  #return 'Meu site em Flask :D'

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação
