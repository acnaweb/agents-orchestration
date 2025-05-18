.PHONY: render clean install-pre-commit

# Arquivos PlantUML
PUML_FILES := $(shell find . -name '*.puml')

# Comando PlantUML com Docker
PLANTUML_DOCKER := docker run --rm -v $(PWD):/workspace plantuml/plantuml

render:
	@echo "Renderizando diagramas .puml para .png via Docker..."
	@for file in $(PUML_FILES); do \
		echo "Renderizando $$file..."; \
		$(PLANTUML_DOCKER) -tpng /workspace/$$file; \
	done
	@echo "Diagramas renderizados com sucesso."

clean:
	@echo "Removendo arquivos .png..."
	@find . -name '*.png' -type f -delete
	@echo "Arquivos removidos."

install:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt; \

test:
	pytest tests

dashboard:
	streamlit run 05_desafios/dashboard_agente_streamlit.py

simulate:
	python 05_desafios/agente_execucao_agendada.py

analyze:
	jupyter notebook 05_desafios/analise_logs_agente_fsm.ipynb

crewlog:
	python 05_desafios/crewai_logger.py

fsm:
	python 05_desafios/agente_explorador_fsm_advanced.py