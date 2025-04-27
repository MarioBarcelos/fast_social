# Fast Social

**Fast Social** é uma aplicação desenvolvida com **FastAPI** que implementa autenticação baseada em tokens JWT, gerenciamento de usuários e integração com banco de dados utilizando SQLModel. O projeto é modular e segue boas práticas de desenvolvimento, incluindo suporte para migrações de banco de dados e testes automatizados.

## Funcionalidades

- **Autenticação JWT**:
  - Geração de tokens de acesso e refresh tokens.
  - Validação de tokens e autenticação de usuários.
  - Suporte a escopos de acesso.

- **Gerenciamento de Usuários**:
  - Recuperação de usuários do banco de dados.
  - Verificação de credenciais com hashing de senhas.

- **Banco de Dados**:
  - Integração com SQLModel para ORM.
  - Suporte a migrações utilizando Alembic.

- **Configuração**:
  - Arquivo `settings.toml` para gerenciar configurações sensíveis.
  - Suporte a múltiplos ambientes (desenvolvimento e produção).

- **Testes Automatizados**:
  - Scripts de teste para validação de funcionalidades.

- **Docker**:
  - Arquivos `Dockerfile.dev` e `docker-compose.yaml` para facilitar o desenvolvimento e a execução em contêineres.

## Estrutura do Projeto

- **`pamps/`**: Contém os módulos principais da aplicação, incluindo autenticação, modelos de dados e lógica de negócios.
- **`migrations/`**: Diretório gerenciado pelo Alembic para controle de versões do banco de dados.
- **`tests/`**: Contém os testes automatizados.
- **`settings.toml`**: Arquivo de configuração do projeto.
- **`Dockerfile.dev` e `docker-compose.yaml`**: Configuração para contêineres Docker.
- **`requirements.txt` e `requirements-dev.txt`**: Dependências do projeto para produção e desenvolvimento.

## Requisitos

- **Python 3.9+**
- **FastAPI**
- **SQLModel**
- **Alembic**
- **Docker** (opcional, para execução em contêineres)

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/MarioBarcelos/fast_social.git
    cd fast_social
2. Crie e ative um ambiente virtual:
    python -m venv .venv
    source .venv/bin/activate
3. Instale as dependências:
    pip install -r requirements.txt
4. Configure o arquivo settings.toml com suas credenciais.
5. Execute a aplicação:
    uvicorn pamps.main:app --reload
6. Acesse a documentação interativa da API em:
    http://127.0.0.1:8000/docs

Como Contribuir
    1.Faça um fork do repositório.
    2.Crie uma branch para sua feature:
        git checkout -b minha-feature
    3.Faça commit das suas alterações:
        git commit -m "Adiciona minha feature"
    4.Envie para o repositório remoto:
        git push origin minha-feature
    5.Abra um Pull Request.