# Telco Churn Intelligence — TCi 📶

**End-to-end interview-ready Data Science project** focused on customer churn for a telecom provider.
This repo contains EDA, feature engineering, modelling, explainability, and an ultra-polished Streamlit dashboard demo.

**Project tagline:** Why customers leave — a data-driven investigation with actionable retention strategies.

---

## 🚀 What you'll find
- `data/` — synthetic "Secret" telco dataset (Indonesia-inspired) + processed samples  
- `notebooks/` — step-by-step Jupyter notebooks: EDA, feature engineering, modelling  
- `app/` — Streamlit multi-page dashboard (`streamlit_app.py`) with dark theme  
- `assets/` — images, logos, screenshots  
- `requirements.txt` — environment deps  
- `run.sh` — quick start script  
- `Dockerfile` — optional containerization (starter)

---

## 🎯 Objectives
1. Identify key drivers of churn and segment high-risk customers  
2. Build predictive model (baseline → tuned) with explainability (SHAP)  
3. Present findings with an interactive dashboard for stakeholders  
4. Provide reproducible pipeline and clear next steps for productionisation

---

## ✅ How to run (local)
```bash
# create venv (recommended)
python3 -m venv venv
source venv/bin/activate

# install
pip install -r requirements.txt

# generate synthetic dataset (optional; data is included)
python scripts/generate_synthetic_telco.py --out data/raw/telco_secret.csv

# run the Streamlit app
streamlit run app/streamlit_app.py
```

---

## 📂 Project structure (final)
```
📦 telco-churn-tci
 ┣ 📜 README.md
 ┣ 📜 requirements.txt
 ┣ 📜 LICENSE
 ┣ 📜 .gitignore
 ┣ 📂 data
 ┃ ┣ 📂 raw
 ┃ ┗ 📂 processed
 ┣ 📂 notebooks
 ┃ ┣ 01_eda.ipynb
 ┃ ┣ 02_feature_engineering.ipynb
 ┃ ┗ 03_modeling.ipynb
 ┣ 📂 app
 ┃ ┗ streamlit_app.py
 ┣ 📂 scripts
 ┃ ┗ generate_synthetic_telco.py
 ┣ 📂 assets
 ┃ ┗ logo.png
 ┗ 📜 run.sh
```

---

## 🧾 Notes (quick)
- This skeleton uses a synthetic dataset to keep the repo unique and recruiter-friendly.
- Notebooks include narrative cells: hypothesis, methods, results, and business interpretation.
- The Streamlit app uses a dark premium theme and includes EDA, Model Prediction, and Insights pages.
- Fill the notebooks with your analysis code; they are pre-populated with sections to guide you.

---

## License
This project is licensed under the MIT License.
