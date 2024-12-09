// Função chamada quando o botão "Marcar Presença" é clicado
function marcarPresenca() {
    // Captura os valores dos campos
  
    // Conectar ao banco de dados
    db.connect((err) => {
        if (err) {
            console.error('Erro ao conectar ao banco de dados:', err);
            return;
        }
        console.log('Conectado ao banco de dados.');
    });
    
   

    // Verifica se os campos não estão vazios
    if (!numAluno || !sala) {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    // Dados a serem enviados
    const data = {
        numAluno: numAluno,
        sala: sala
    };

     //aqui se conecta com a base de dados e faz o insert
    
}

// Função que será chamada quando a página carregar
window.onload = function() {
    const params = new URLSearchParams(window.location.search);
    const numAluno = params.get('numAluno');
    const sala = params.get('sala');
    const presenca = params.get('presenca');

    // Preenche os campos com os valores passados na URL
    if (numAluno) {
        document.getElementById('numAluno').value = numAluno;
    }
    if (sala) {
        document.getElementById('sala').value = sala;
    }
    if (presenca) {
        document.getElementById('attendance').value = presenca;
    }
};
