from pathlib import Path
import sys
import pytest

# Adiciona o caminho do módulo de desafios
sys.path.append(str(Path(__file__).resolve().parents[1] / "05_desafios"))

from agente_explorador_fsm import AgenteExplorador, Estado

def test_estado_inicial():
    agente = AgenteExplorador()
    assert agente.estado == Estado.PARADO
    assert agente.energia == 100

def test_transicao_explorando_para_parado():
    agente = AgenteExplorador()
    agente.estado = Estado.EXPLORANDO
    agente.energia = 10
    agente.perceber_obstaculo = lambda: True  # força obstáculo
    agente.tomar_decisao()
    assert agente.estado == Estado.PARADO

def test_carregando_ate_full():
    agente = AgenteExplorador()
    agente.estado = Estado.CARREGANDO
    agente.energia = 90
    agente.tomar_decisao()
    assert agente.energia == 100 or agente.estado == Estado.EXPLORANDO