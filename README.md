# 🦟 Malaria Prevalence Prediction Across Nigerian States

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-Academic-green?style=for-the-badge" />
</p>

---

## 📌 Overview

This project builds a machine learning pipeline to predict malaria prevalence across all 36 Nigerian states and the Federal Capital Territory using household-level survey data from the **Nigeria Malaria Indicator Survey (NMIS) 2021**. Nigeria bears approximately 27% of the global malaria burden — making data-driven, state-level risk prediction a critical tool for equitable resource allocation by national health programs. The pipeline compares three supervised classifiers — Logistic Regression, Decision Tree, and Random Forest — across a curated set of demographic, socioeconomic, and household features drawn from the NMIS dataset, ultimately identifying the strongest predictor of individual-level malaria RDT outcomes. This work is intended for public health researchers, data scientists, and policymakers interested in evidence-based malaria control in low- and middle-income country settings.

---

## 🗂️ Project Structure

```
malaria-prediction/
│
├── data/
│   ├── processed/                 # Cleaned, encoded, pipeline-ready data
│   └── raw/                       # ⚠️ Not tracked by Git — place dataset here
│       └── NGPR81FL.DTA           # NMIS 2021 household member recode (Stata format)
│
├── models/                        # Serialised trained model artefacts (.pkl)
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
├── tests/
│   ├── test_data_loader.py        # Unit tests for data loading module
│   ├── test_evaluator.py          # Unit tests for evaluation functions
│   └── test_preprocessor.py      # Unit tests for preprocessing pipeline
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Data Source

This project uses the **Nigeria Malaria Indicator Survey (NMIS) 2021** — a nationally representative household survey conducted by the National Population Commission (NPC) in partnership with the National Malaria Elimination Programme (NMEP) and USAID. The dataset covers all 37 administrative units of Nigeria. The **Household Member Recode** file (`NGPR81FL.DTA`) was used, containing **70,428 individual-level records**, of which **10,717 had a valid malaria RDT result** and form the analytical dataset.

Features used in this project:

- Malaria rapid diagnostic test (RDT) outcome *(target variable: `rdt_result`)*
- Individual demographics — age, sex
- Household characteristics — wealth index, floor material, wall material, roof material, household size, children under 5
- WASH indicators — drinking water source
- Malaria prevention — type of mosquito net slept under, electricity access
- Geographic context — state of residence, geopolitical zone, residence type, education level

**Accessing the dataset:**
The NMIS 2021 dataset is publicly available through the [DHS Program data repository](https://dhsprogram.com/data/available-datasets.cfm). Access requires free registration and submission of a brief data request describing intended use. The specific file used in this project is `NGPR81FL.DTA` (Household Member Recode, Stata format).

> ⚠️ The raw dataset is **not included** in this repository in compliance with the DHS Program data sharing policy. Please request access directly from the DHS Program and place the file in `data/raw/` before running the pipeline.

---

## 🤖 Models Used

| Model | Rationale |
|---|---|
| **Logistic Regression** | Serves as the interpretable baseline; its coefficients map directly to odds ratios, making it transparent for public health audiences unfamiliar with machine learning. |
| **Decision Tree** | Captures non-linear relationships and generates human-readable decision rules that can be communicated to non-technical stakeholders and policy makers. |
| **Random Forest** | Ensemble of decision trees that reduces overfitting and variance through majority voting, consistently the strongest performer on high-dimensional health survey data. |

All three models are trained under a unified evaluation framework using **10-fold stratified cross-validation** with **SMOTE oversampling** to address class imbalance (38% positive, 62% negative).

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

After receiving approval from the [DHS Program](https://dhsprogram.com/data/available-datasets.cfm), download the NMIS 2021 Household Member Recode file and place it at:

```
data/raw/NGPR81FL.DTA
```

The pipeline will load this file at runtime. Do **not** commit the dataset to version control — it is already listed in `.gitignore`.

### 5. Run the pipeline

```bash
python -m src.pipeline
```

---

## 📈 Results

The pipeline was fully executed on the NMIS 2021 Household Member Recode dataset. All metrics are empirical results from **10-fold stratified cross-validation** on the SMOTE-resampled dataset of 10,717 records.

### Model Performance — 10-Fold Stratified Cross-Validation

| Model | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|---|:---:|:---:|:---:|:---:|:---:|
| Logistic Regression | 0.6582 | 0.6527 | 0.6767 | 0.6643 | 0.7155 |
| Decision Tree | 0.6745 | 0.6687 | 0.6921 | 0.6801 | 0.6795 |
| **Random Forest** ✅ | **0.7213** | **0.7099** | **0.7487** | **0.7287** | **0.7989** |

**Random Forest** achieves the best performance across all five metrics, with an F1 Score of **0.7287** and AUC-ROC of **0.7989**.

### Dataset Summary

| Metric | Value |
|---|---|
| Total records loaded | 70,428 |
| Records with valid RDT result | 10,717 |
| Malaria positive (target = 1) | 4,108 (38.3%) |
| Malaria negative (target = 0) | 6,609 (61.7%) |
| Features after selection | 19 out of 102 |
| States represented | 37 (all 36 + FCT) |

### Top Predictors (Feature Importance — Random Forest)

The Random Forest feature selector retained **19 features** out of 102 one-hot encoded columns (importance threshold > 0.01). The most informative variables in order are:

1. **State of residence** — reflects well-documented spatial heterogeneity in malaria burden across Nigerian states
2. **Geopolitical zone** — North-West and South-South zones consistently record the highest prevalence
3. **Wealth index** — lower socioeconomic status strongly associated with higher malaria positivity
4. **Age** — older individuals have developed partial immunity; younger individuals carry higher risk
5. **Net type** — sleeping under an insecticide-treated net is a strong protective predictor

---

## 👨🏽‍💻 Author

**Christianah Adekunle** 

---

## 🙏 Acknowledgements

- **The DHS Program** — for making the NMIS 2021 dataset publicly accessible to researchers upon request, enabling nationally representative, state-level analysis of malaria in Nigeria.
- **The Scikit-learn community** — for maintaining the open-source machine learning library that powers the entire modeling pipeline (Pedregosa et al., 2011).

---

<p align="center">
  <sub>Built with 🐍 Python · 🌍 Made in Nigeria</sub>
</p>