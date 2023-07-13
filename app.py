from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS musicas")
    cursor.execute("CREATE TABLE musicas(titulo text, banda text, album text, ano text)")
    con.commit()
    con.close()
    
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def tabela():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()

    data = request.form

    titulo = data['titulo']
    banda = data['banda']
    album = data['album']
    ano = data['ano']

    sql = '''
    INSERT INTO musicas (titulo, banda, album, ano)
    VALUES (?, ?, ?, ?)
    '''

    cursor.execute(sql,[titulo, banda, album, ano])
    cursor.execute('SELECT * FROM musicas')

    con.commit()

    musicArray = cursor.fetchall()
    
    con.close()

    return render_template('index.html', musicArray=musicArray)

if __name__ == "__main__":
    app.run(debug=True)