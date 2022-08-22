from flask import Flask, request # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Nova rota
def main():
  resultado = 'Entre com as notas na URL'

  primeira = request.args.get('primeira')
  segunda = request.args.get('segunda')

  if primeira and segunda:
        
    primeira = float(primeira)
    segunda = float(segunda)

    media = (primeira + segunda) / 2
    if media >= 7:
        resultado = 'Aprovado'
    elif media >= 4:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'

  return resultado

if __name__ == '__main__':
    app.run(host='localhost', port= 9001, debug=True)