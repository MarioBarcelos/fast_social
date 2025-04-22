#!/usr/bin/bash

# Inicia ambiente com docker
PAMPS_DB=pamps_test docker-compose up -d

# Aguarde 5 seg para normalizar projeto
sleep 5

# Verifica banco
docker-compose exec app pamps reset-db -f
docker-compose exec app alembic stamp base

# Realizar migrações no banco
docker-compose exec app alembic upgrade head

# Executar testes
docker-compose exec app pytest -v -l --tb=short --maxfail=1 tests/

# Terminar ambiente com docker
docker-compose down