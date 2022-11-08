from flask import Flask, jsonify, request, redirect
from Model import Model


app = Flask(__name__)

@app.route('/tabela1')
def tab1():
    return jsonify('Tabela 1')

@app.route('/tabela2')
def tab2():
    return jsonify('Tabela 2')

@app.route('/tabela/<int:id>', methods=['GET'])
def get(id):
    if request.method == 'GET':
        tabela = Model.tab_get(id)
        return redirect(f'{tabela}')


if __name__ == '__main__' :
    app.run(debug=True)