from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/amostra', methods=['POST'])
def amostra():
  dados = request.get_json()
  idade = dados.get("idade", 0)

  if idade > 5 and idade < 7:
    categoria = "Infantil"
#   elif idade > 8 < 10:
#     categoria = "Iniciando"
#   elif idade > 11 < 13:
#     categoria = "Juvenil"
#   elif idade > 14 < 17:
#     categoria = "Júnior"
  else:  
    categoria = "Maior de idade"
    print(categoria)

    return jsonify("Resultado", categoria)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8000', debug=True)