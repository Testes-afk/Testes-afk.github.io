import csv
from datetime import datetime

# Caminho do arquivo CSV
caminho_arquivo = r"C:\Users\vitor\OneDrive\Desktop\ADS\lista_presencas.csv"

# Lista de intervalos de horários
intervalos = [
    ("09:00:00", "10:00:00"), ("10:00:00", "11:00:00"), ("11:00:00", "12:00:00"),
    ("12:00:00", "13:00:00"), ("13:00:00", "14:00:00"), ("14:00:00", "15:00:00"),
    ("15:00:00", "16:00:00"), ("16:00:00", "17:00:00"), ("17:00:00", "18:00:00"),
    ("18:00:00", "19:00:00"), ("19:00:00", "20:00:00"), ("20:00:00", "21:00:00"),
    ("21:00:00", "22:00:00"), ("22:00:00", "23:00:00")
]


def ordenar_entradas(caminho_csv):
    """
    Ordena as entradas do CSV por IP, depois por dia e, por fim, por hora.

    :param caminho_csv: Caminho para o arquivo CSV contendo os dados.
    :return: Lista de dicionários ordenados por IP, dia e hora.
    """
    entradas = []

    # Ler o arquivo CSV
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        headers = next(leitor)  # Captura os cabeçalhos
        for linha in leitor:
            data_hora = f"{linha[2].strip()} {linha[3].strip()}"  # Unificar data e hora
            entradas.append({
                "Número do Aluno": linha[0],
                "Sala": linha[1],
                "Data": linha[2].strip(),
                "Hora": linha[3].strip(),
                "Data e Hora": data_hora,
                "IP": linha[4].strip()
            })

    # Ordenar por IP, depois por data e depois por hora
    entradas_ordenadas = sorted(
        entradas,
        key=lambda x: (
            x["IP"],
            datetime.strptime(x["Data"], "%d/%m/%Y") if x["Data"] else datetime.min,
            datetime.strptime(x["Hora"], "%H:%M:%S") if x["Hora"] else datetime.min
        )
    )

    return entradas_ordenadas

def separar_entradas_por_intervalo(entradas):
    """
    Separa as entradas em válidas e inválidas com base em IP, dia e intervalo de horário.
    Apenas a primeira entrada de cada intervalo, por dia, por IP, é considerada válida.

    :param entradas: Lista de dicionários ordenados por IP, dia e hora.
    :return: Duas listas: entradas válidas e entradas inválidas.
    """
    entradas_validas = []
    entradas_invalidas = []

    # Obter intervalos únicos por IP e Dia
    entradas_por_ip = {}
    for entrada in entradas:
        ip = entrada["IP"]
        dia = entrada["Data"]
        if ip not in entradas_por_ip:
            entradas_por_ip[ip] = {}
        if dia not in entradas_por_ip[ip]:
            entradas_por_ip[ip][dia] = []
        entradas_por_ip[ip][dia].append(entrada)

    # Separar por intervalo
    for ip, dias in entradas_por_ip.items():
        for dia, entradas_dia in dias.items():
            intervalos_usados = set()  # Mantém controle dos intervalos já processados
            for entrada in entradas_dia:
                hora = datetime.strptime(entrada["Hora"], "%H:%M:%S").time()
                for inicio, fim in intervalos:
                    intervalo_inicio = datetime.strptime(inicio, "%H:%M:%S").time()
                    intervalo_fim = datetime.strptime(fim, "%H:%M:%S").time()

                    if intervalo_inicio <= hora <= intervalo_fim:
                        if (dia, inicio, fim) not in intervalos_usados:
                            entradas_validas.append(entrada)
                            intervalos_usados.add((dia, inicio, fim))
                        else:
                            entradas_invalidas.append(entrada)
                        break  # Intervalo encontrado, passar para a próxima entrada

    return entradas_validas, entradas_invalidas


if __name__ == "__main__":
    caminho_arquivo = r"C:\Users\vitor\OneDrive\Desktop\ADS\lista_presencas.csv"
    entradas_ordenadas = ordenar_entradas(caminho_arquivo)

    entradas_validas, entradas_invalidas = separar_entradas_por_intervalo(entradas_ordenadas)

    print("Entradas válidas:")
    for entrada in entradas_validas:
        print(entrada)

    print("\nEntradas inválidas:")
    for entrada in entradas_invalidas:
        print(entrada)

