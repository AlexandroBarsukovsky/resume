# Portfolio of Architectural and Analytical Projects

This repository contains three independent projects, developed to demonstrate a systematic approach to solving complex problems across different domains. Each project includes **complete architectural documentation**, and in the case of the GTM infrastructure – a **working prototype (draft implementation)**.

All projects follow a unified methodology:
- diagnosis of the current state
- formulation of principles and architecture
- detailed elaboration (models, integrations, automation)
- implementation plan and risk management
- appendices (formulas, SQL, configurations, plain‑language explanations)

**Working style:** deep immersion (12–14 hours), 3–4 days per week.

---

## 1. GTM Infrastructure for Sourcegraph (Enterprise)

**Objective:** design a scalable, event‑driven platform to transition Sourcegraph from product‑led growth to enterprise sales.

**Contents:**
- **Architectural document** – current state analysis, four‑level orchestration (1,024 analysts, 3 strategists, 96 tactical groups, 3,000 executors), Account Score and Health Score models, quarterly forecast (logistic regression + VAR + seasonality), integrations with Salesforce, Gainsight, 6sense, Tableau, financial justification (NPV $102–185M, payback <2 years), roadmap, risks.
- **Draft implementation** – backend in Python (FastAPI, Celery), frontend in React, Redis Streams queues, Kafka, Docker Compose, stubbed integrations. The prototype demonstrates architectural feasibility.

**Key technologies:** Python, Go, React, PostgreSQL, Redis, Kafka, AWS, Docker, Kubernetes.

---

## 2. AI Ecosystem for a Metal Products Manufacturer (“Iron Kit”)

**Objective:** automate operational management for a small business manufacturing metal products and selling via Wildberries.

**Contents:**
- **Architectural document** – 38 agents (6 analytical, 6 strategic, 8 tactical, 18 executive), demand forecasting models (Prophet, ARIMA), inventory management (s,S), dynamic pricing (logit model), feedback processing (NLP), new product generation (GENESIS), financial model (NPV, ROI).

**Key technologies:** Python, FastAPI, React, PostgreSQL, Redis, Docker, Wildberries API.

---

## 3. Analysis of Short‑Video Recommendation Algorithms (YouTube Shorts, TikTok, Instagram Reels)

**Objective:** systemic analysis of ranking and recommendation algorithms on short‑video platforms, development of a framework for data collection and content optimisation.

**Contents:**
- **Research report** – decomposition of the algorithm into 8 levels (from physical infrastructure to regulatory framework), mathematical models (logistic regression, multi‑target optimisation, time decay), comparative analysis of three platforms, A/B testing framework and iterative optimisation, forecast of evolution up to 2030.
- **Practical value:** the document was used by an international marketing agency as a strategic guide.

**Key topics:** ranking algorithms, retrieval, multi‑target optimisation, A/B testing, bandit algorithms.

---

## About the Projects

- All three projects were completed in a very short timeframe (architecture + documentation).
- Each project is **self‑contained** – documents and code are ready to be handed over to teams for implementation.
- The unified methodology enables rapid onboarding into new domains and the delivery of production‑ready results.

---

## Contact

Author: **Andreev Alexander Robertovich**  
Email: alisaaiclub@gmail.com
tg - @MedoedBarsuk


*All materials are provided to demonstrate competencies. For commercial use or adaptation, please contact.*
