import json
from datetime import datetime

class LLMOrquestrador:
    def __init__(self, log_file="log_llm.json"):
        self.etapas = []
        self.log_file = log_file

    def executar_plano(self, tarefa):
        self.etapas.append(self._log("planejamento", f"Criando plano para: {tarefa}"))
        self.etapas.append(self._log("execucao", f"Executando plano para: {tarefa}"))
        self.etapas.append(self._log("feedback", f"Avaliando resultado de: {tarefa}"))

        with open(self.log_file, 'w') as f:
            json.dump(self.etapas, f, indent=2)

    def _log(self, etapa, descricao):
        return {
            "timestamp": str(datetime.utcnow()),
            "etapa": etapa,
            "descricao": descricao
        }

if __name__ == "__main__":
    agente = LLMOrquestrador()
    agente.executar_plano("Coletar dados sobre orquestração de agentes.")