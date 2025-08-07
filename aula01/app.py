from flask import Flask

app = Flask(__name__)


@app.route('/teste', methods=['GET', 'POST'])
def index():
  date = [
    # "title": "Seja bem vindo a minha api meu nobre meu nobre",
    {
        "nome":"Miguel",
        "idade": 21,
        "firstdai": "07/07/2005",
        "resum": "Nego das trincheiras das quebradas da zona norte, ok broth"
    },
  ]

  print(date)
  return date

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8000')