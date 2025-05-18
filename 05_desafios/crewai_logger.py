from crewai import Crew, Agent, Task
import json
from datetime import datetime

class Logger:
    def __init__(self, file_path="log_crewai.json"):
        self.file_path = file_path
        self.logs = []

    def log(self, etapa, conteudo):
        self.logs.append({
            "timestamp": str(datetime.utcnow()),
            "etapa": etapa,
            "conteudo": conteudo
        })

    def salvar(self):
        with open(self.file_path, "w") as f:
            json.dump(self.logs, f, indent=2)

logger = Logger()

planner = Agent(role="planner", goal="criar plano", backstory="planejador experiente")
executor = Agent(role="executor", goal="executar tarefas", backstory="operacional rápido")

logger.log("inicializacao", "Agentes inicializados")

task = Task(description="Pesquisar sobre agentes autônomos", expected_output="Resumo pesquisado", agent=planner)

crew = Crew(agents=[planner, executor], tasks=[task])
logger.log("execucao", "Crew executado")
crew.kickoff()
logger.log("finalizacao", "Execução concluída")
logger.salvar()