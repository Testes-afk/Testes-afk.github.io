CREATE DATABASE `schedule_app` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- schedule_app.aluno definition

CREATE TABLE `aluno` (
  `numeroAluno` int NOT NULL,
  `nome` char(50) DEFAULT NULL,
  `curso` char(50) DEFAULT NULL,
  PRIMARY KEY (`numeroAluno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- schedule_app.entradas definition

CREATE TABLE `entradas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `num_aluno` varchar(10) NOT NULL,
  `sala` varchar(10) NOT NULL,
  `ip_address` varchar(32) DEFAULT NULL,
  UNIQUE KEY `entradas_unique` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- schedule_app.horario definition

CREATE TABLE `horario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Curso` varchar(100) NOT NULL,
  `UnidadeCurricular` varchar(100) NOT NULL,
  `Turno` varchar(100) NOT NULL,
  `Turma` varchar(100) NOT NULL,
  `InscritosTurno` int NOT NULL,
  `DiaSemana` varchar(10) NOT NULL,
  `HoraInicio` time NOT NULL,
  `HoraFim` time NOT NULL,
  `DataAula` date NOT NULL,
  `CaracteristicasSala` varchar(100) NOT NULL,
  `SalaAula` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- schedule_app.sala definition

CREATE TABLE `sala` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Edificio` varchar(100) NOT NULL,
  `NomeSala` varchar(100) NOT NULL,
  `CapacidadeNormal` int NOT NULL,
  `CapacidadeExame` int NOT NULL,
  `NoCaracteristicas` int NOT NULL,
  `AnfiteatroAulas` varchar(1) DEFAULT NULL,
  `ApoioTecnicoEventos` varchar(1) DEFAULT NULL,
  `Arq1` varchar(1) DEFAULT NULL,
  `Arq2` varchar(1) DEFAULT NULL,
  `Arq3` varchar(1) DEFAULT NULL,
  `Arq4` varchar(1) DEFAULT NULL,
  `Arq5` varchar(1) DEFAULT NULL,
  `Arq6` varchar(1) DEFAULT NULL,
  `Arq9` varchar(1) DEFAULT NULL,
  `BYOD` varchar(1) DEFAULT NULL,
  `FocusGroup` varchar(1) DEFAULT NULL,
  `HorarioVisivelPublico` varchar(1) DEFAULT NULL,
  `LabArqCompI` varchar(1) DEFAULT NULL,
  `LabArqCompII` varchar(1) DEFAULT NULL,
  `LabBasesEng` varchar(1) DEFAULT NULL,
  `LabEletronica` varchar(1) DEFAULT NULL,
  `LabInformatica` varchar(1) DEFAULT NULL,
  `LabJornalismo` varchar(1) DEFAULT NULL,
  `LabRedesCompI` varchar(1) DEFAULT NULL,
  `LabRedesCompII` varchar(1) DEFAULT NULL,
  `LabTelecom` varchar(1) DEFAULT NULL,
  `SalaAulasMest` varchar(1) DEFAULT NULL,
  `SalaAulasMestPlus` varchar(1) DEFAULT NULL,
  `SalaNEE` varchar(1) DEFAULT NULL,
  `SalaProvas` varchar(1) DEFAULT NULL,
  `SalaReuniao` varchar(1) DEFAULT NULL,
  `SalaArquitetura` varchar(1) DEFAULT NULL,
  `SalaAulasNormal` varchar(1) DEFAULT NULL,
  `Videoconferencia` varchar(1) DEFAULT NULL,
  `Atrio` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;