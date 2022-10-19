from flask import Flask, request, jsonify, render_template, redirect
from Model import Model

app = Flask(__name__)



@app.route('/home')
def home():
    lista = Model.jsonReturn()
    return render_template('view.html', dic=lista)

@app.route('/lista', methods=['GET'])
def get():
    if request.method == 'GET':
        return jsonify(Model.jsonReturn())


@app.route('/lista/<int:lista_id>', methods=['GET'])
def get_id(lista_id):
    if request.method == 'GET':
       return jsonify(Model.visualizar_item(lista_id))



@app.route('/lista/adicionar', methods=['POST'])
def post():
    if request.method == 'POST':
        item = request.form.get('item')
        quant = request.form.get('quantidade')
        uni = request.form.get('unidade')
        Model.adicionar_item(item, quant, uni)
        return redirect('/home')


@app.route('/lista/atualizar', methods=['PUT', 'POST'])
def put():
    if request.method == 'PUT' or request.method == 'POST':
        item_id = request.form.get('id')
        item = request.form.get('item')
        quantidade = request.form.get('quantidade')
        unidade = request.form.get('unidade')
        Model.atualizar_item(item_id, item, quantidade, unidade)
        return redirect('/home')


@app.route('/lista/delete1', methods=['POST', 'DELETE'])
def deletar1():
    if request.method == 'POST' or request.method == 'DELETE':
        lista_id1 = request.form.get('id')
        Model.excluir_item(lista_id1)
        return redirect('/home')


@app.route('/lista/delete2/<int:lista_id2>', methods=['POST', 'DELETE'])
def deletar(lista_id2):
    if request.method == 'POST' or request.method == 'DELETE':
        return jsonify(Model.excluir_item(lista_id2))


if __name__ == '__main__' :
    app.run(debug=True)