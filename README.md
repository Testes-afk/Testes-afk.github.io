# Testes-afk.github.io
frontend.py -> pede o num de aluno e escaneia o QR code com a sala <br/>
landingpage -> inicia com os dados do py e confirma<br/>
confirmacao -> o utilizador é redirecionado pra essa pg dps de confirmar<br/>
index -> lista de presenças <br/>
backend.py -> pega um csv, ordena e separa em entradas validas e invalidas (um IP só pode ter uma entrada por intervalo, por dia) <br/>
app.py -> aplicação que faz o papel do frontend.py<br/>
QRcodeGenerator.py -> gera uma lista de qr codes de salas a partir do csv disponibilizado pelo prof<br/>
