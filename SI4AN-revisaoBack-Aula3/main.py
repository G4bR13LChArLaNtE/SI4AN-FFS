from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Meu site em Flask :) "

if __name__ == '__main__':
    app.run(host= 'localhost', port= 9000, debug=True)

