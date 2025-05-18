# Makefile para orquestração de agentes de IA

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