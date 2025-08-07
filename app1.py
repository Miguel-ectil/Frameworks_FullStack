from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
  return "Api rodando!!"

@app.route('/saudacao/<nome>', methods=['GET', 'POST'])
def saudacao(nome):
  return f"Olá {nome}"

@app.route('/soma', methods=['POST'])
def soma():
  dados = request.get_json()
  a = dados.get("n1", 0)
  b = dados.get("n2", 0)

  return jsonify("Resultado", a + b)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8000', debug=True)