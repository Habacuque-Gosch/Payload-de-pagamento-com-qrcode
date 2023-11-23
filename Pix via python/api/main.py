from flask import Flask, render_template, request, flash
from pixqrcodegen import Payload

app = Flask(__name__)

app.secret_key = "Pix"
@app.route('/robots.txt', methods=['POST', 'GET'])
def robots():
    return render_template('robots.txt')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/gerar', methods=['POST', 'GET'])
def gerar():

    payload = Payload('Habacuque Gosch', '13012155970', '10', 'palhoça', 'LOJA01')

    payload.gerarPayload()

    return render_template('gerada.html')


if __name__ == "__main__":
    app.run(debug=True)