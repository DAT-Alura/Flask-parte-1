from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('super mario', 'Ação', 'Super Nintendo')
jogo2 = Jogo('pokemon gold', 'RPG', 'Game Boy')
jogo3 = Jogo('monster hunter', 'RPG', 'Multiplataforma')
jogo4 = Jogo('mortal kombat', 'Luta', 'Multiplataforma')
lista = [jogo1, jogo2, jogo3, jogo4]

@app.route("/")
def inicio():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo')

@app.route("/criar", methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True, port=8080)