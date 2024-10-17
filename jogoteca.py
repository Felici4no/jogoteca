from flask import Flask,render_template,request # render tamplate busca direto na pasta templates
app = Flask(__name__) # Se refere a própria pagina

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 =  Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('GTA', 'Gangs', 'PS2')
jogo3 = Jogo('MK', 'Luta', 'PS2') #Moral Kombat
jogo4 = Jogo('-', '-', '-')
jogo5 = Jogo('Moral Kombat', 'Luta', 'PS2')  # Moral Kombat
lista = [jogo1, jogo2,jogo3,jogo4,jogo5]

@app.route('/inicio') # http://127.0.0.1:5000/inicio
def hello_world():
    return render_template('lista.html',titulo='Jogos',jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html',titulo='Novo')


@app.route('/criar',methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo= 'Jogos', jogos=lista)

if __name__ == '__main__':
    app.run()

