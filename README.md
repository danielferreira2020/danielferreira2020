<!-- =========================================================
  README - Daniel Ferreira | Data Engineer / Analytics Engineer
  Tema: tech + moderno + interativo
========================================================== -->

<h1 align="center">Daniel Ferreira</h1>
<p align="center">
  <b>Data Engineer • Analytics Engineer • Data Science (aplicado)</b><br/>
  Conecto <b>engenharia</b>, <b>analytics</b> e <b>negócio</b> para transformar perguntas em decisões práticas.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/daniel-ferreira-201261221/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="mailto:SEU_EMAIL_AQUI">
    <img alt="Email" src="https://img.shields.io/badge/Email-1f2937?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <img alt="Location" src="https://img.shields.io/badge/Goi%C3%A2nia%2C%20BR-111827?style=for-the-badge&logo=google-maps&logoColor=white"/>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=SEU_USERNAME&style=flat-square&color=0ea5e9" alt="views" />
  <img src="https://img.shields.io/github/followers/SEU_USERNAME?style=flat-square&color=22c55e" alt="followers" />
  <img src="https://img.shields.io/github/stars/SEU_USERNAME?style=flat-square&color=f59e0b" alt="stars" />
</p>

---

## 🔥 O que eu faço (sem enrolação)

- **Engenharia de Dados ponta a ponta**: ingestão → transformação → governança → métricas → consumo (BI/Apps).
- **Pipelines e automação**: reduz retrabalho, padroniza informação e dá previsibilidade com custo sob controle.
- **Analytics pragmático**: modelos dimensionais, métricas confiáveis e narrativa executiva que o time usa no dia a dia.

> *Foco em resolver problema real: tempo, clareza, confiança e entrega incremental.*

---

## 🧠 Stack (principal)

<p>
  <img src="https://img.shields.io/badge/Python-111827?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL-111827?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-111827?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Airflow-111827?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/GCP-111827?style=for-the-badge&logo=googlecloud&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power%20BI-111827?style=for-the-badge&logo=powerbi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Looker%20Studio-111827?style=for-the-badge&logo=google&logoColor=white"/>
</p>

**Também uso no dia a dia**
- Modelagem: **Star Schema / Dimensional** (fato/dimensão), métricas e governança.
- Observabilidade: logging, validações, SLAs, “data quality checks”.
- Integração: APIs, arquivos (CSV/Parquet), jobs e automações.

---

## 🧩 Como eu penso (arquitetura de dados)

```mermaid
flowchart LR
  A["Fontes: App, ERP, API"] --> B["Ingestao"]
  B --> C["Staging / Raw"]
  C --> D["Transformacoes (ELT) - dbt"]
  D --> E["Curado - Modelo Dimensional"]
  E --> F["BI: Power BI / Looker"]
  E --> G["Produtos de Dados / ML"]
  D --> H["Qualidade + Observabilidade"]
  H --> D
