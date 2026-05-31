# 🦟 Malaria Prevalence Prediction Across Nigerian States

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-Academic-green?style=for-the-badge" />
</p>

---

## 📌 Overview

This project builds a machine learning pipeline to predict malaria prevalence across all 36 Nigerian states and the Federal Capital Territory using household-level survey data from the **Nigeria Malaria Indicator Survey (NMIS) 2021**. Nigeria bears approximately 27% of the global malaria burden — making data-driven, state-level risk prediction a critical tool for equitable resource allocation by national health programs. The pipeline compares three supervised classifiers — Logistic Regression, Decision Tree, and Random Forest — and is deployed as an interactive Streamlit web application.

---

## 🗂️ Project Structure

```
malaria-prediction/
│
├── app/
│   ├── main.py                    # Streamlit entry point
│   ├── pages/
│   │   ├── 1_Prediction.py        # Household form → malaria risk prediction
│   │   └── 2_Risk_Map.py          # Nigeria state-level choropleth risk map
│   └── utils/
│       ├── predictor.py           # MalariaPredictor — loads model, runs inference
│       └── map_data.py            # State coordinates + positivity rates
│
├── data/
│   ├── processed/                 # Cleaned, encoded, pipeline-ready data
│   └── raw/                       # ⚠️ Not tracked by Git — place dataset here
│       └── NGPR81FL.DTA           # NMIS 2021 household member recode (Stata format)
│
├── models/                        # Serialised trained model artefacts (.pkl)
│   ├── Random_Forest.pkl
│   ├── Decision_Tree.pkl
│   └── Logistic_Regression.pkl
│
├── notebooks/                     # Exploratory and step-by-step analysis notebooks
│
├── outputs/                       # Generated figures, reports, and evaluation results
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # DataLoader class — dataset ingestion & inspection
│   ├── preprocessor.py            # Preprocessor — filter, encode, binary target
│   ├── feature_selector.py        # FeatureSelector — RF importance screening
│   ├── model_trainer.py           # ModelTrainer — SMOTE + 10-fold stratified CV
│   ├── evaluator.py               # ModelEvaluator — all five metrics + plots
│   └── pipeline.py                # MalariaPipeline orchestrator (end-to-end)
│
│── test_data_loader.py
│── test_evaluator.py
│── test_preprocessor.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Data Source

This project uses the **Nigeria Malaria Indicator Survey (NMIS) 2021** — a nationally representative household survey conducted by the National Population Commission (NPC) in partnership with the National Malaria Elimination Programme (NMEP) and USAID. The **Household Member Recode** file (`NGPR81FL.DTA`) was used, containing **70,428 individual-level records**, of which **10,717 had a valid malaria RDT result**.

> ⚠️ The raw dataset is **not included** in this repository in compliance with the DHS Program data sharing policy. Please request access at [dhsprogram.com](https://dhsprogram.com/data/available-datasets.cfm) and place the file in `data/raw/` before running the pipeline or the map page.

---

## 🤖 Models Used

| Model | Rationale |
|---|---|
| **Logistic Regression** | Interpretable baseline; coefficients map to odds ratios for public health audiences |
| **Decision Tree** | Captures non-linear relationships; generates human-readable decision rules |
| **Random Forest** | Ensemble method; best performer — reduces overfitting via majority voting |

All models trained with **10-fold stratified cross-validation** and **SMOTE oversampling** (38% positive, 62% negative class imbalance).

---

## 📈 Results

| Model | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|---|:---:|:---:|:---:|:---:|:---:|
| Logistic Regression | 0.6582 | 0.6527 | 0.6767 | 0.6643 | 0.7155 |
| Decision Tree | 0.6745 | 0.6687 | 0.6921 | 0.6801 | 0.6795 |
| **Random Forest** ✅ | **0.7213** | **0.7099** | **0.7487** | **0.7287** | **0.7989** |

---

## 🖥️ Streamlit App

The trained Random Forest model is deployed as an interactive web application with two pages:

- **🔬 Prediction** — User fills in household details (geopolitical zone, wealth index, net type, age, etc.) and receives an instant malaria risk assessment (Low / Moderate / High) with probability score
- **🗺️ Risk Map** — Interactive choropleth map showing malaria positivity rates across all 37 Nigerian states derived from NMIS 2021 data

### Run Locally

```bash
streamlit run app/main.py
```

### Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repo, set **Main file path** to `app/main.py`
5. Click **Deploy**

> ⚠️ The Risk Map page requires `data/raw/NGPR81FL.DTA` to be present. On Streamlit Cloud, upload it via the file uploader or use the cached version if already computed.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/peteridowu/malaria-prediction.git
cd malaria-prediction
```

### 2. Create and activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place `NGPR81FL.DTA` at `data/raw/NGPR81FL.DTA`.

### 5. Run the ML pipeline

```bash
python -m src.pipeline
```

### 6. Run the Streamlit app

```bash
streamlit run app/main.py
```

---

## 👩🏽‍💻 Author

**Christianah Adekunle**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Christianah%20Adekunle-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/christianah-adekunle)
[![GitHub](https://img.shields.io/badge/GitHub-i--am--christy-181717?style=flat-square&logo=github)](https://github.com/i-am-christy)
[![Blog](https://img.shields.io/badge/Blog-i--am--christy.hashnode.dev-2962FF?style=flat-square&logo=hashnode)](https://i-am-christy.hashnode.dev)

---

## 🙏 Acknowledgements

- **The DHS Program** — for making the NMIS 2021 dataset publicly accessible to researchers upon request
- **The Scikit-learn community** — for the open-source ML library powering the pipeline (Pedregosa et al., 2011)

---

<p align="center">
  <sub>Built with 🐍 Python · 🌍 Made in Nigeria</sub>
</p>