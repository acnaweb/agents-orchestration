import time
from agente_explorador_fsm_advanced import AgenteExplorador

def test_benchmark_execucao_rapida():
    agente = AgenteExplorador(log_file="/tmp/log.json")
    start = time.time()
    agente.executar(ciclos=10)
    duration = time.time() - start
    assert duration < 10, "Execução demorando mais que o esperado"