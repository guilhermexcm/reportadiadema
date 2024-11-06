from flask import Flask, request, render_template, redirect, session
import requests


app = Flask(__name__)


@app.route('/Paginainicial', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def reportincident():
    return render_template('PaginaInicialAPI.html')

@app.route('/quemSomos', methods=['GET'])
def quemSomos():
    return render_template('quemSomos.html')

@app.route('/consulta', methods=['GET'])
def consulta():
    return render_template('filtrarConsulta.html')


if __name__ == '__main__':
    app.run(debug=True)
