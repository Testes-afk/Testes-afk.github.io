import cv2
from pyzbar.pyzbar import decode
import webbrowser
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty


KV = '''
MDScreen:
    name: "main_screen"
    MDLabel:
        id: instruction_label
        text: "Insira o número de aluno"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        font_size: "20sp"

    MDTextField:
        id: student_number_field
        hint_text: "Número de aluno"
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        mode: "rectangle"

    MDRaisedButton:
        id: submit_button
        text: "Confirmar"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.on_submit()

    MDRaisedButton:
        id: scan_qr_button
        text: "Escanear QR Code"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        opacity: 0
        disabled: True
        on_release: app.scan_qr()
'''

class MainApp(MDApp):
    numAluno = StringProperty("0")  # Variável para armazenar o número do aluno

    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    def on_submit(self):
        # Obtém o texto inserido pelo usuário e salva na variável
        student_number = self.kvs.ids.student_number_field.text
        if student_number.isdigit():  # Verifica se o número é válido
            self.numAluno = student_number
            print(f"Número de aluno registrado: {self.numAluno}")

            # Esconde os elementos iniciais
            self.kvs.ids.instruction_label.opacity = 0
            self.kvs.ids.student_number_field.opacity = 0
            self.kvs.ids.student_number_field.disabled = True
            self.kvs.ids.submit_button.opacity = 0
            self.kvs.ids.submit_button.disabled = True

            # Mostra o botão de escanear QR Code
            self.kvs.ids.scan_qr_button.opacity = 1
            self.kvs.ids.scan_qr_button.disabled = False
        else:
            print("Insira um número válido!")

    def scan_qr(self):
        print("Iniciando escaneamento de QR Code...")
        cap = cv2.VideoCapture(0)  # Abre a câmera

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Falha ao capturar imagem.")
                break

            qr_codes = decode(frame)  # Decodifica os QR Codes no frame
            for qr_code in qr_codes:
                qr_texto = qr_code.data.decode('utf-8')  # Decodifica o QR Code
                print("QR Code Detectado:", qr_texto)

                # Abre a página web com os dados do aluno e da sala
                webbrowser.open(
                    f'http://127.0.0.1:5500/landingpage.html?numAluno={self.numAluno}&sala={qr_texto}'
                )
                
                return  # Sai da função após processar o QR Code

            # Exibe o vídeo ao vivo
            cv2.imshow('Escaneando QR Code', frame)

            # Pressione 'q' para sair manualmente
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    

ma = MainApp()
ma.run()
