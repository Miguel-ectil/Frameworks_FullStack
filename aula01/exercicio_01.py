from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/amostra', methods=['POST'])
def amostra():
    dados = request.get_json()
    idade = dados.get("idade", 0)

    if 5 < idade < 7:
        categoria = "Infantil"
    elif 8 < idade < 10:
        categoria = "Iniciando"
    elif 11 < idade < 13:
        categoria = "Juvenil"
    elif 14 < idade < 17:
        categoria = "Júnior"
    else:
        categoria = "Maior de idade"

    return jsonify({"resultado": categoria})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
