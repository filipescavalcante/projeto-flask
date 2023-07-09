from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def helloWorld():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS musicas")
    cursor.execute("CREATE TABLE musicas(titulo text, banda text, album text, ano text)")
    con.commit()
    
    res = cursor.execute("SELECT * FROM musicas")

    nome = 'Filipe'
    
    return render_template('index.html', nome=nome)

if __name__ == "__main__":
    app.run(debug=True)