from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'daniel'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


usuario1 = Usuario('daniel', 'Daniel Akio Teixeira', 'dat')
usuario2 = Usuario('shodi', 'Henrique Shodi Maeta', 'hsm')
usuario3 = Usuario('harikoi', 'Gabriel Lourenço Nicolini', 'gln')
usuario4 = Usuario('matias', 'Matheus Pinto Teixeira', 'mpt')
usuarios = {
    usuario1.id: usuario1,
    usuario2.id: usuario2,
    usuario3.id: usuario3,
    usuario4.id: usuario4
}

jogo1 = Jogo('clash royale', 'Carta', 'Celular')
jogo2 = Jogo('pokemon gold', 'RPG', 'Game Boy')
jogo3 = Jogo('monster hunter', 'RPG', 'Multiplataforma')
jogo4 = Jogo('mortal kombat', 'Luta', 'Multiplataforma')
jogos = [jogo1, jogo2, jogo3, jogo4]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima = request.form['proxima']
            return redirect(proxima)
    flash(request.form['usuario'] + ' não logado, tente novamente!')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flash(session['usuario_logado'] + ' foi deslogado!')
    session['usuario_logado'] = None
    return redirect(url_for('index'))


app.run(debug=True, port=8080)
