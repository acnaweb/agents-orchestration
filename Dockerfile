# Dockerfile para orquestração de agentes e visualização de logs

FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install streamlit jupyter crewai

EXPOSE 8501

CMD ["streamlit", "run", "05_desafios/dashboard_agente_streamlit.py"]