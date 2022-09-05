from flask import Flask, request, render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/', methods=['POST', 'GET'])# Nova rota
@app.route('/index.html', methods=['POST', 'GET'])
def main():
    resultado = None
    media = None

    if request.method == 'POST':
        primeira = request.form.get('primeira')
        segunda = request.form.get('segunda')
        terceira = request.form.get('terceira')
        quarta = request.form.get('quarta')

        if primeira and segunda and terceira and quarta:
            primeira = float(primeira)
            segunda = float(segunda)
            terceira = float(terceira)
            quarta = float(quarta)

        media = (primeira + segunda + terceira + quarta) / 4
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media, resultado=resultado)

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação