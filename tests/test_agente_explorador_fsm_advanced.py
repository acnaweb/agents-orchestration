from pathlib import Path
import sys
import json

# Adiciona o caminho do módulo
sys.path.append(str(Path(__file__).resolve().parents[1] / "05_desafios"))

from agente_explorador_fsm_advanced import AgenteExplorador, Estado

def test_logging_executa_e_gera_arquivo(tmp_path):
    log_path = tmp_path / "log.json"
    agente = AgenteExplorador(log_file=str(log_path))
    agente.executar(ciclos=3)

    assert log_path.exists()
    with open(log_path, "r") as f:
        dados = json.load(f)
        assert isinstance(dados, list)
        assert len(dados) == 3
        assert "estado_atual" in dados[0]