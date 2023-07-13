from flask import Flask, render_template, request
import random
import string
import mysql.connector

app = Flask(__name__)

import mysql.connector

# Configurações de conexão com o banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = 'Casella21@'
db_name = 'gerador_senhas'

# Conexão com o banco de dados
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    auth_plugin='mysql_native_password'
)


# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar senhas
@app.route('/gerar_senha', methods=['POST'])
def gerar_senha():
    tamanho = int(request.form['tamanho'])

    # Gerar a senha aleatória
    senha = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

    # Salvar a senha no banco de dados
    cursor = db.cursor()
    cursor.execute("INSERT INTO senhas (senha) VALUES (%s)", (senha,))
    db.commit()

    return render_template('senha.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True)
