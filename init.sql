-- init.sql

CREATE TABLE IF NOT EXISTS tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    status_conclusao BOOLEAN DEFAULT FALSE NOT NULL,
    data_criacao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    data_status_conclusao TIMESTAMPTZ
);
