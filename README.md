[![Live Demo](https://img.shields.io/badge/Demo-Streamlit%20Live-brightgreen?logo=streamlit)](https://agente-dashboard-abc123-uc.a.run.app)

[![CI](https://github.com/usuario/repositorio/workflows/CI%20-%20Testes%20Automatizados/badge.svg)](https://github.com/usuario/repositorio/actions)

# 📦 Repositório de Orquestração de Agentes de IA

Este repositório contém materiais estruturados para capacitação profissional em **orquestração de agentes de inteligência artificial**, com foco em aplicações práticas, padrões arquiteturais e ferramentas de mercado.

---

## 📁 Estrutura

- `01_fundamentos/` – Conceitos base sobre agentes, BDI, deliberação e comunicação.
- `02_arquiteturas/` – Exemplos e padrões arquiteturais centralizados, descentralizados, federados.
- `03_ferramentas_frameworks/` – Ferramentas práticas como LangChain, CrewAI, ROS, JADE.
- `04_padroes_projeto/` – Implementações de padrões como FSM, Observer, Chain of Responsibility.
- `05_desafios/` – Desafios práticos validados com código, incluindo um agente explorador com FSM.
- `plantuml_diagramas/` – Diagramas UML de orquestração de agentes, especialmente com LLMs.

---

## 🚀 Execução do Agente Explorador FSM

```bash
cd 05_desafios
python3 agente_explorador_fsm.py
```

---

## 🧠 Orquestração com LangChain (exemplo)
Crie um ambiente virtual e instale as dependências:

```bash
pip install langchain openai
```

Exemplo básico:

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType

llm = OpenAI(temperature=0)

tools = [
    Tool(
        name="Busca Simples",
        func=lambda x: f"Você buscou por: {x}",
        description="Busca de informações genérica."
    )
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
agent.run("Preciso buscar informações sobre agentes autônomos.")
```

---

## 🤖 Orquestração com CrewAI (exemplo)

Instale a dependência:

```bash
pip install crewai
```

Exemplo mínimo:

```python
from crewai import Crew, Agent, Task

planner = Agent(role="planner", goal="planejar tarefas", backstory="especialista em organização")
executor = Agent(role="executor", goal="executar tarefas", backstory="muito eficiente")

task = Task(description="Organizar o dia de trabalho.", expected_output="Agenda organizada", agent=planner)

crew = Crew(agents=[planner, executor], tasks=[task])
crew.kickoff()
```

---

## 📊 Diagrama de Orquestração (PlantUML)

Veja o diagrama `plantuml_diagramas/arquitetura_agentes_llm.puml` com o seguinte fluxo:

- Usuário → Planejador → Executor → Crítico → Executor → Usuário
- Interações com base de conhecimento

Utilize um visualizador PlantUML online ou extensões de VSCode para renderização.

---

## ✅ Requisitos

- Python 3.8+
- VSCode (sugestão) + Extensões PlantUML e Python
- Acesso a APIs como OpenAI (opcional para LangChain)

---

Desenvolvido para estudo profissional e aplicação de mercado.
---

📄 Para uma visão geral completa dos módulos e objetivos da capacitação, consulte o arquivo:
👉 [CAPACITACAO_COMPLETA.md](./CAPACITACAO_COMPLETA.md)
---

## 🛠️ Execução com Makefile

Este projeto já possui um `Makefile` com os principais comandos automatizados.

### ✅ Passos recomendados para execução:

```bash
# 1. Criar ambiente virtual e instalar dependências
make install

# 2. Executar os testes para garantir funcionamento
make test

# 3. Rodar o agente explorador com log estruturado
make fsm

# 4. Abrir o dashboard Streamlit com os logs
make dashboard

# 5. Analisar os dados com Jupyter Notebook
make analyze

# 6. Executar simulação diária automática
make simulate

# 7. Executar cenário de orquestração LLM com CrewAI
make crewlog
```

> 💡 Dica: use `make <alvo>` no terminal dentro da pasta do projeto.

---

## 🌐 Live Demo

> Após o deploy no Cloud Run, adicione o link abaixo ao seu README.md:

```markdown
[![Live Demo](https://img.shields.io/badge/Demo-Streamlit-blue?logo=streamlit)](https://agente-dashboard-<REGIAO>-a.run.app)
```

Substitua `<REGIAO>` pela região usada no deploy (ex: `us-central1`).
---

## 🧠 O que é Orquestração de Agentes?

Orquestração de agentes de IA envolve a coordenação entre diferentes agentes autônomos ou cognitivos (como agentes FSM, LLMs ou robôs físicos), permitindo que colaborem para atingir objetivos complexos.

### Exemplos de Orquestração
- **Agentes FSM coordenados** por uma máquina de supervisão
- **Agentes LLM** com papéis complementares: planejador, executor, crítico
- **CrewAI** como framework de orquestração de tarefas multi-etapas com feedback

### Padrões Utilizados
- Chain of Responsibility
- Command Pattern
- Federated/Broker Architectures
- Event-Driven Design

---

## 🎓 Projeto Final – Orquestrador Inteligente Multi-Agente

### 🧾 Descrição
Construir um sistema inteligente com três agentes autônomos:

1. **Planner LLM**: Cria o plano de tarefas a partir de um objetivo de negócio
2. **Executor FSM**: Realiza as ações em ambiente simulado com logging estruturado
3. **Crítico**: Avalia os resultados e realimenta o sistema com ajustes

### 🎯 Objetivo
Simular um ciclo completo de planejamento, execução e melhoria contínua com agentes orquestrados e logs acessíveis para análise.

### 📁 Entregáveis
- Código dos 3 agentes integrados
- Arquitetura em PlantUML
- Log em JSON e CSV
- Notebook com análise dos logs
- Dashboard interativo com Streamlit

### 🚀 Execução
```bash
make crewlog
make fsm
make dashboard
make analyze
```

> 💡 Combine execução do planner e executor em sequência para simular orquestração real.