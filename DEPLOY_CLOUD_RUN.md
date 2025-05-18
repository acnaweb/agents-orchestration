# 🚀 Deploy no Google Cloud Run

## Etapas

1. **Build da imagem Docker localmente (ou via Cloud Build):**
```bash
gcloud builds submit --tag gcr.io/SEU-PROJETO/agente-dashboard
```

2. **Deploy no Cloud Run (região, projeto e nome ajustáveis):**
```bash
gcloud run deploy agente-dashboard   --image gcr.io/SEU-PROJETO/agente-dashboard   --platform managed   --region us-central1   --allow-unauthenticated
```

> Obs: Certifique-se que o `Dockerfile` inicia o dashboard Streamlit.