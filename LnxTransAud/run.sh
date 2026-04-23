#!/bin/bash

# Navega até o diretório
cd /home/kayronn/.LnxTransAud/

# Inicia o Helvum via Flatpak em segundo plano
# O '&' é crucial para o script continuar a execução
flatpak run org.pipewire.Helvum & 

# Aguarda 2 segundos (opcional) para garantir que o Helvum carregue 
# antes de abrir a interface do tradutor
sleep 2

# Verifica se o ambiente virtual existe, se não, cria
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Ativa o ambiente e executa o app
source venv/bin/activate
python LnxTransAud.py
