import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import database

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
def guardar_presenca(num_aluno, sala, ip):
    conn = database.get_db_connection()

    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    
    if not confirmar_registo_unico(conn, num_aluno, ip):
        return jsonify({"message": "Aluno ja registado para a aula"}), 200

    # Inserindo os dados no banco de dados
    try:
        cursor = conn.cursor()
        instruction = "INSERT INTO entradas (create_time, num_aluno, sala, ip_address) VALUES ('{current_date}', '{num_aluno}', '{sala}', '{ip}')".format(current_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num_aluno=num_aluno, sala=sala, ip=str(ip))
        cursor.execute(instruction)
        conn.commit()
        cursor.close()
        return jsonify({"message": "Presença marcada com sucesso!"}), 200
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        return jsonify({"message": "Erro ao inserir dados no banco"}), 500
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Ler presenca
def total_presencas_em_sala(sala, inicio_horario : datetime, fim_horario : datetime) :
    conn = database.get_db_connection()
    total_presencas = None

    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    # Inserindo os dados no banco de dados
    try:
        cursor = conn.cursor()
        instruction = "SELECT COUNT(*) FROM entradas WHERE sala = '{sala}' AND create_time BETWEEN '{begin_time}' AND '{end_time}'".format(sala=str(sala), begin_time=inicio_horario.strftime('%Y-%m-%d %H:%M:%S'), end_time=fim_horario.strftime('%Y-%m-%d %H:%M:%S'))
        total_presencas = cursor.execute(instruction)
        cursor.close()
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        return jsonify({"message": "Erro ao inserir dados no banco"}), 500
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

    return total_presencas


def confirmar_registo_unico(conn, num_aluno, ip):
    now = datetime.now()
    begin_time = now.strftime('%Y-%m-%d %H:00:00')
    end_time = (now + timedelta(hours=1)).strftime('%Y-%m-%d %H:00:00')
    cursor = conn.cursor()
    instruction = "SELECT COUNT(*) FROM entradas WHERE create_time BETWEEN '{begin_time}' AND '{end_time}' AND (ip_address = '{ip}' OR num_aluno = '{num_aluno}')".format(begin_time=begin_time, end_time=end_time, ip=str(ip), num_aluno=num_aluno)
    cursor.execute(instruction)
    registos = cursor.fetchone()[0]
    return registos == 0