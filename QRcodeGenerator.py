import csv
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

caminho_csv = r'C:\Users\vitor\Downloads\Projeto 1 - Gestao de Horarios do ISCTE - HorarioDeExemplo (1).csv'
caminho_output = r'C:\Users\vitor\OneDrive\Desktop\QR codes'


def listar_salas_unicas(caminho_csv):
    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo, delimiter=';')
            
            salas = set()  # Usamos um conjunto para evitar duplicações

            for linha in leitor_csv:
                sala = linha['Sala da aula']  # Obtém o valor da coluna "Sala da aula"
                salas.add(sala)

            print("Salas de aula (sem repetições):")

            # Define o caminho para salvar os QR Codes
            os.makedirs(caminho_output, exist_ok=True)

            for sala in sorted(salas):
                print(sala)
                criar_qr_code(sala, caminho_output)

    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")
    except KeyError:
        print("Erro: O arquivo CSV não contém a coluna 'Sala da aula'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def criar_qr_code(sala, caminho_output):
    try:
        # Cria o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(sala)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Adiciona o texto abaixo do QR Code
        largura, altura = qr_img.size
        nova_altura = altura + 50
        img_com_texto = Image.new("RGB", (largura, nova_altura), "white")
        img_com_texto.paste(qr_img, (0, 0))

        draw = ImageDraw.Draw(img_com_texto)
        fonte = ImageFont.load_default()
        texto_bbox = draw.textbbox((0, 0), sala, font=fonte)  # Usa textbbox para calcular o tamanho do texto
        texto_largura = texto_bbox[2] - texto_bbox[0]
        texto_x = (largura - texto_largura) // 2
        draw.text((texto_x, altura + 10), sala, fill="black", font=fonte)

        # Salva a imagem
        caminho_arquivo = os.path.join(caminho_output, f"{sala}.png")
        img_com_texto.save(caminho_arquivo)

    except Exception as e:
        print(f"Erro ao criar QR Code para a sala '{sala}': {e}")


# Substitua 'caminho_para_seu_arquivo.csv' pelo caminho do arquivo CSV.
listar_salas_unicas(caminho_csv)

