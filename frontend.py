import cv2
from pyzbar.pyzbar import decode
import webbrowser

# Função para processar o QR Code
def processar_qr_code(imagem):
    qr_codes = decode(imagem)
    for qr_code in qr_codes:
        # Decodifica o QR Code e extrai o texto
        qr_texto = qr_code.data.decode('utf-8')
        print("QR Code Detectado:", qr_texto)
        # Retorna o texto do QR code
        return qr_texto
    return None

# Pergunta para o usuário o número de aluno
num_aluno = input("Digite o número de aluno: ")



# Abrir a câmera
cap = cv2.VideoCapture(0)  # 0 normalmente é a webcam padrão

while True:
    # Captura frame a frame
    ret, frame = cap.read()
    
    if not ret:
        print("Falha ao capturar imagem.")
        break
    
    # Processa o QR Code no frame
    qr_code_texto = processar_qr_code(frame)
    
    # Exibe o vídeo ao vivo com a indicação de que foi detectado o QR Code
    cv2.imshow('Escaneando QR Code', frame)
    
    if qr_code_texto:
        # Redireciona para a página, preenchendo os campos "numAluno", "sala" e "attendance"
        webbrowser.open(f'http://127.0.0.1:5500/landingpage.html?numAluno={num_aluno}&sala={qr_code_texto}')
        break  # Interrompe após encontrar o primeiro QR code

    # Se pressionar 'q', o loop será interrompido
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
