import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Caminho do arquivo CSV válido
caminho_csv_validas = r"C:\Users\vitor\OneDrive\Desktop\ADS\entradas_validas.csv"

def carregar_dados(caminho_csv):
    """
    Carrega o CSV em um DataFrame do pandas.

    :param caminho_csv: Caminho para o arquivo CSV.
    :return: DataFrame com os dados.
    """
    return pd.read_csv(caminho_csv)

def calcular_ocupacao_por_dia(df):
    """
    Calcula a ocupação das salas por dia.

    :param df: DataFrame contendo as entradas válidas.
    :return: DataFrame com a ocupação das salas por dia.
    """
    # Criar uma coluna com a data extraída da coluna "Data e Hora"
    df['Data'] = pd.to_datetime(df['Data e Hora'], format="%d/%m/%Y %H:%M:%S").dt.date
    
    # Contar a ocupação por dia e sala
    ocupacao = df.groupby(['Data', 'Sala']).size().reset_index(name='Ocupação')
    return ocupacao

def plot_ocupacao_por_dia(ocupacao_df):
    """
    Plota a ocupação das salas por dia.

    :param ocupacao_df: DataFrame com a ocupação das salas por dia.
    """
    # Preparar os dados para o plot
    dias = sorted(ocupacao_df['Data'].unique())
    salas = ocupacao_df['Sala'].unique()

    ocupacao_por_sala = {sala: [] for sala in salas}

    for dia in dias:
        dia_data = ocupacao_df[ocupacao_df['Data'] == dia]
        for sala in salas:
            # Obter a ocupação da sala no dia ou preencher com 0
            ocupacao = dia_data[dia_data['Sala'] == sala]['Ocupação'].sum()
            ocupacao_por_sala[sala].append(ocupacao)

    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    for sala, ocupacao in ocupacao_por_sala.items():
        plt.plot(dias, ocupacao, marker='o', label=sala)

    plt.title('Ocupação das Salas por Dia')
    plt.xlabel('Data')
    plt.ylabel('Ocupação')
    plt.xticks(rotation=45)
    plt.legend(title="Salas")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Carregar os dados
    df = carregar_dados(caminho_csv_validas)

    # Calcular a ocupação por dia
    ocupacao_df = calcular_ocupacao_por_dia(df)

    # Plotar a ocupação das salas por dia
    plot_ocupacao_por_dia(ocupacao_df)
