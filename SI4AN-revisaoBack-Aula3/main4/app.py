import requests
from flask import Flask, render_template, request, redirect, jsonify, session as flask_session

url = "http://localhost:9009/"


def lista_alunos():
    resultado = requests.get(url)
    if resultado.status_code != 200:
        return "Deu erro!"

    alunos = resultado.json()
    return alunos


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', lista=lista_alunos())


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
