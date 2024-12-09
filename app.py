from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Conexão com o banco de dados MySQL
def get_db_connection():
    try:
        # Conexão com a base de dados
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Substitua por seu usuário MySQL
            password="Vitor11anos",  # Substitua por sua senha MySQL
            database="gestaohorario"
        )
        if connection.is_connected():
            print("Conexão com a base de dados bem-sucedida!")
        return connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

# Verificação de conexão ao banco de dados logo que o servidor iniciar
@app.before_first_request
def before_first_request():
    conn = get_db_connection()
    if conn:
        print("Conexão bem-sucedida ao banco de dados!")
    else:
        print("Falha na conexão com o banco de dados.")

@app.route('/marcar_presenca', methods=['POST'])
def marcar_presenca():
    # Obtendo os dados enviados pela requisição
    data = request.get_json()
    num_aluno = data['numAluno']
    sala = data['sala']
    
    # Conectar ao banco de dados
    conn = get_db_connection()
    
    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    
    # Inserindo os dados no banco de dados
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO entradas (NumAluno, Sala) VALUES (%s, %s)', (num_aluno, sala))
        conn.commit()
        cursor.close()
        return jsonify({"message": "Presença marcada com sucesso!"}), 200
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        return jsonify({"message": "Erro ao inserir dados no banco"}), 500
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
