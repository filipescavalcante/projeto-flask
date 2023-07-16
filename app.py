from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# con = sqlite3.connect('musicas.db')
# cursor = con.cursor()

# con.commit()
# con.close()
    
@app.route("/")
def index():
    con = sqlite3.connect('musicas.db')
    cursor = con.cursor()

    cursor.execute('SELECT * FROM musicas')
    musicArray = cursor.fetchall()

    return render_template('index.html', musicArray=musicArray)

@app.route("/tabela", methods=['POST'])
def tabela():
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

    cursor.execute(sql,[titulo, banda, album, ano])
    cursor.execute('SELECT * FROM musicas')

    musicArray = cursor.fetchall()
    
    con.commit()
    con.close()

    return render_template('tabela.html', musicArray=musicArray)

if __name__ == "__main__":
    app.run(debug=True)