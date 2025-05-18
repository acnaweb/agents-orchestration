import time
from agente_explorador_fsm_advanced import AgenteExplorador

def simular_agente_diariamente(dias=3, ciclos_por_dia=5):
    for dia in range(dias):
        print(f"Execução do dia {dia+1}")
        agente = AgenteExplorador(log_file=f"log_agente_dia{dia+1}.json")
        agente.executar(ciclos=ciclos_por_dia)
        time.sleep(2)

if __name__ == "__main__":
    simular_agente_diariamente()