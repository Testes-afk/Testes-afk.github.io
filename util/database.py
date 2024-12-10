import dateutil.utils
import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
import dateutil

#class database:

# Conexão com o banco de dados MySQL
def get_db_connection():
    try:
        # Conexão com a base de dados
        connection = mysql.connector.connect(
            host="localhost",
            user="app_user",  # Substitua por seu usuário MySQL
            password="password4321",  # Substitua por sua senha MySQL
            database="schedule_app",
            port = 3306
        )
        if connection.is_connected():
            print("Conexão com a base de dados bem-sucedida!")
        return connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

# Guardar presenca
def guardar_presenca(conn, num_aluno, sala, ip):
    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    # Inserindo os dados no banco de dados
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO entradas (create_time, num_aluno, sala, ip_address) VALUES (%s, %s, %s, %s)', (dateutil.utils.today, num_aluno, sala, ip))
        conn.commit()
        cursor.close()
        return jsonify({"message": "Presença marcada com sucesso!"}), 200
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        return jsonify({"message": "Erro ao inserir dados no banco"}), 500
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()
