DROP TABLE IF EXISTS matricula;
DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS disciplina;


-- criação de uma tabela aluno
CREATE TABLE aluno(
  -- atributos de aluno e seus respectivos tipos
  -- tipos mais comuns de dados:
  -- INTEGER --> Int | DECIMAL --> Float | VARCHAR --> String | BOOL --> Boolean
  id_aluno INTEGER NOT NULL,-- NOT NULL é pq o id do aluno não pode ser nulo
  nome_aluno VARCHAR(80) NOT NULL, -- (80) é o tamanho que o VARCHAR vai aceitar  	nesse caso e o NOT NULL pq ele não pode ser nulo
  email_aluno VARCHAR(80) NOT NULL, 
  cidade_aluno VARCHAR (80) NULL, -- NULL pq ela pode ser nulo
  uf_aluno VARCHAR(2) NULL,

  -- Ele atribui um comando especial
  CONSTRAINT pk_aluno
    PRIMARY KEY(id_aluno),
  
  CONSTRAINT email_unico
    UNIQUE(email_aluno)
);

-- criação de uma tabela disciplina
CREATE TABLE disciplina(
  id_disciplina INTEGER NOT NULL,
  nome_disciplina VARCHAR (80) NOT NULL,
  carga_horaria_disciplina INTEGER NOT NULL,
  data_inicio_disciplina DATE NULL, -- DATE Vai mapear DATE
  modalidade_disciplina VARCHAR(20) DEFAULT 'Presencial' NOT NULL, -- A coluna     não pode ser nula, caso ela seja nula deverá ser armazenado o valor que foi     indicado, nesse   caso 'Presencial'
  
  CONSTRAINT pk_disciplina
    PRIMARY KEY (id_disciplina)
);

-- criação de uma tabela matrícula
CREATE TABLE matricula(
  id_matricula INTEGER NOT NULL,
  id_aluno INTEGER NOT NULL,
  id_disciplina INTEGER NOT NULL,
  data_matricula DATE DEFAULT (CURRENT_DATE) NOT NULL,
  status_matricula VARCHAR (20) DEFAULT 'PENDENTE' NOT NULL,
  observacao_matricula VARCHAR (250) NULL,
  
  CONSTRAINT pk_matricula
    PRIMARY KEY (id_matricula),
  
  CONSTRAINT fk_aluno
    FOREIGN KEY (id_aluno)
    REFERENCES aluno(id_aluno),
 
  CONSTRAINT fk_matricula
    FOREIGN KEY (id_disciplina)
    REFERENCES disciplina(id_disciplina)
  
);

  ALTER TABLE aluno
  ADD COLUMN telefone VARCHAR(20) NULL;
  
  ALTER TABLE disciplina
  ADD COLUMN vagas INTEGER DEFAULT 30 NOT NULL;
  
  ALTER TABLE disciplina
  MODIFY COLUMN data_inicio_disciplina DATE NOT NULL;
  
  ALTER TABLE disciplina
  ADD CONSTRAINT nome_disciplina_unico
  UNIQUE (nome_disciplina);
  
  ALTER TABLE aluno
  DROP COLUMN uf_aluno;

