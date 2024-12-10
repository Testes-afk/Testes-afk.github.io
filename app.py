from flask import Flask, request, jsonify
import util.database as database
import frontend

app = Flask(__name__)

conn = None

# Verificação de conexão ao banco de dados logo que o servidor iniciar
@app.before_request
def before_request():
    conn = database.get_db_connection()
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
    #conn = database.get_db_connection()
    
    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    
    # Inserindo os dados no banco de dados
    database.guardar_presenca(conn, num_aluno, sala, request.remote_addr)

if __name__ == '__main__':
    app.run(debug=True)
