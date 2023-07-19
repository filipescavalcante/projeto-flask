from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
    
@app.route("/")
def index():
    con = sqlite3.connect('musicas.db')
    cursor = con.cursor()

    cursor.execute('SELECT * FROM musicas')
    musicArray = cursor.fetchall()

    return render_template('index.html', musicArray=musicArray)

@app.route("/add", methods=['POST'])
def add():
    con = sqlite3.connect('musicas.db')
    cursor = con.cursor()

    data = request.form

    titulo = data['titulo']
    banda = data['banda']
    album = data['album']
    ano = data['ano']

    sql = '''
    INSERT INTO musicas (titulo, banda, album, ano)
    VALUES (?, ?, ?, ?);
    '''

    cursor.execute(sql, [titulo, banda, album, ano])

    con.commit()
    con.close()

    return redirect(url_for('index'))

@app.route("/excluir/<id>", methods=['POST', 'GET'])
def excluir(id):
    con = sqlite3.connect('musicas.db')
    cursor = con.cursor()

    sql = 'DELETE FROM musicas WHERE id = ?'

    cursor.execute(sql,[id])

    con.commit()
    con.close()

    return redirect(url_for('index'))

@app.route("/editar/<id>", methods=['POST', 'GET'])
def editar(id):
    con = sqlite3.connect('musicas.db')
    cursor = con.cursor()

    sql = 'SELECT * FROM musicas WHERE id = ?'

    cursor.execute(sql,[id])

    dados = cursor.fetchall()

    return render_template('edit.html', dados=dados)

@app.route("/update/<id>", methods=['POST', 'GET'])
def update(id):
    con = sqlite3.connect('musicas.db')
    cursor = con.cursor()

    data = request.form

    novoTitulo = data['novo-titulo']
    novoBanda = data['novo-banda']
    novoAlbum = data['novo-album']
    novoAno = data['novo-ano']

    sql = 'UPDATE musicas SET titulo = ?, banda = ?, album = ?, ano = ? WHERE id = ?'

    cursor.execute(sql,[novoTitulo, novoBanda, novoAlbum, novoAno, id])

    con.commit()
    con.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)