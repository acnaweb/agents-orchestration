import json
import pandas as pd
import streamlit as st
import os

st.set_page_config(page_title="Dashboard Agente FSM", layout="centered")

st.title("📊 Dashboard do Agente Explorador (FSM com Logs)")

# Seção para logs
st.header("🔍 Análise de Logs do Agente")

uploaded_file = st.file_uploader("Selecione o arquivo de log JSON gerado pelo agente", type="json")

if uploaded_file is not None:
    data = json.load(uploaded_file)
    df = pd.DataFrame(data)
    
    st.subheader("📋 Dados do Agente")
    st.dataframe(df)
    
    st.subheader("📈 Energia por ciclo")
    st.line_chart(df["nova_energia"])
    
    st.subheader("🔁 Transições de Estado")
    st.bar_chart(df["novo_estado"].value_counts())

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Baixar como CSV", csv, "log_agente.csv", "text/csv")

# Seção para diagramas
st.header("🧠 Diagramas de Arquiteturas de Orquestração")

diagramas = {
    "Centralizada": "plantuml_diagramas/centralizada.puml",
    "Descentralizada (P2P)": "plantuml_diagramas/descentralizada_p2p.puml",
    "Hierárquica": "plantuml_diagramas/hierarquica.puml",
    "Federada / Broker-based": "plantuml_diagramas/federada_broker.puml"
}

escolha = st.selectbox("Selecione a arquitetura:", list(diagramas.keys()))

if escolha:
    st.code(Path(diagramas[escolha]).read_text(), language="plantuml")
    st.markdown("🔍 Copie este código para um visualizador PlantUML para renderizar o diagrama.")