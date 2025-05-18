#!/bin/bash

echo "🚀 Criando ambiente virtual .venv ..."
python3 -m venv .venv
source .venv/bin/activate

echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Ambiente pronto. Para ativar novamente, use:"
echo "source .venv/bin/activate"