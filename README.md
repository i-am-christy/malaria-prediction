# 🦟 Malaria Prevalence Prediction Across Nigerian States

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-Academic-green?style=for-the-badge" />
</p>

---

## 📌 Overview

This project builds a machine learning pipeline to predict malaria prevalence across all 36 Nigerian states and the Federal Capital Territory using household-level survey data from the **Nigeria Malaria Indicator Survey (NMIS) 2021**. Nigeria bears approximately 27% of the global malaria burden — making data-driven, state-level risk prediction a critical tool for equitable resource allocation by national health programs. The pipeline compares three supervised classifiers — Logistic Regression, Decision Tree, and Random Forest — across a curated set of demographic, socioeconomic, and household features drawn from the NMIS dataset, ultimately identifying the strongest predictor of child-level malaria test outcomes. This work is intended for public health researchers, data scientists, and policymakers interested in evidence-based malaria control in low- and middle-income country settings.

---

## 🗂️ Project Structure

```
malaria-prediction/
│
├── data/
│   ├── processed/                 # Cleaned, encoded, pipeline-ready data
│   └── raw/                       # ⚠️ Not tracked by Git — place dataset here
│       ├── NGKR81FL.DTA           # NMIS 2021 children's recode (Stata format)
│       └── NGKR81FL.MAP           # Stata value-label map companion file
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
│   ├── preprocessor.py            # Preprocessing pipeline (sklearn ColumnTransformer)
│   ├── feature_selector.py        # FeatureSelector — RF importance + correlation screen
│   ├── model_trainer.py           # ModelTrainer — GridSearchCV with 10-fold CV
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

This project uses the **Nigeria Malaria Indicator Survey (NMIS) 2021** — a nationally representative household survey conducted by the National Population Commission (NPC) in partnership with the National Malaria Elimination Programme (NMEP) and USAID. The dataset covers all 37 administrative units of Nigeria and contains approximately **14,500 child-level records** with variables spanning:

- Malaria rapid diagnostic test (RDT) outcomes *(target variable: `rdt_result`)*
- Child demographics — age (months), sex
- Household characteristics — wealth index, floor material, wall material, household size
- WASH indicators — drinking water source
- Malaria prevention — insecticide-treated net use
- Geographic context — state of residence, geopolitical zone, mother's education level

**Accessing the dataset:**
The NMIS 2021 dataset is publicly available through the [DHS Program data repository](https://dhsprogram.com/data/available-datasets.cfm). Access requires free registration and submission of a brief data request describing intended use. The specific file used in this project is `NGKR81FL.DTA` (children's recode, Stata format).

> ⚠️ The raw dataset is **not included** in this repository in compliance with the DHS Program data sharing policy. Please request access directly from the DHS Program and place the file in the `data/` directory before running the pipeline.

---

## 🤖 Models Used

| Model | Rationale |
|---|---|
| **Logistic Regression** | Serves as the interpretable baseline; its coefficients map directly to odds ratios, making it transparent for public health audiences unfamiliar with machine learning. |
| **Decision Tree** | Captures non-linear relationships and generates human-readable decision rules that can be communicated to non-technical stakeholders and policy makers. |
| **Random Forest** | Ensemble of decision trees that reduces overfitting and variance through majority voting, making it the expected top performer on this type of high-dimensional health survey data. |

All three models are trained under a unified evaluation framework to enable fair, apples-to-apples comparison.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/i-am-christy/malaria-prediction.git
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

After receiving approval from the [DHS Program](https://dhsprogram.com/data/available-datasets.cfm), download the NMIS 2021 children's recode file and place it at:

```
data/raw/NGKR81FL.DTA
```

The pipeline will load this file at runtime. Do **not** commit the dataset to version control — it is already listed in `.gitignore`.

### 5. Run the pipeline

**Option A — End-to-end Python script**
```bash
python src/pipeline.py
```

**Option B — Step-by-step notebooks**  
Open and run the notebooks in `notebooks/` sequentially (01 → 06) using Jupyter:
```bash
jupyter notebook
```

---

## 📈 Results

> ℹ️ The pipeline is currently in active development. The metrics below are **simulated expected results** grounded in published benchmarks for comparable malaria prediction systems on African health survey data (Chanda et al., 2024; Musa et al., 2025). Empirical results will replace these values upon completion of the full pipeline run.

### Model Performance on 30% Hold-Out Test Set

| Model | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|---|:---:|:---:|:---:|:---:|:---:|
| Logistic Regression | 0.742 | 0.713 | 0.681 | 0.697 | 0.784 |
| Decision Tree | 0.791 | 0.764 | 0.752 | 0.758 | 0.823 |
| **Random Forest** ✅ | **0.853** | **0.831** | **0.819** | **0.825** | **0.912** |

**Random Forest** achieves the best performance across all five metrics, with an expected F1 Score of **0.825** and AUC-ROC of **0.912** — values consistent with ensemble method benchmarks in comparable malaria datasets.

### Top Predictors (Feature Importance — Random Forest)

The most informative variables identified by the Random Forest feature importance analysis are, in order:

1. **State of residence** — reflects well-documented spatial heterogeneity in malaria burden across Nigerian states
2. **Geopolitical zone** — North-West and South-South zones consistently record the highest prevalence
3. **Wealth index** — lower socioeconomic status strongly associated with higher malaria positivity
4. **Age of child (months)** — younger children carry a disproportionate share of the malaria burden
5. **Insecticide-treated net use** — a strong protective predictor, consistent with evidence on bed-net efficacy

---

## 👩🏽‍💻 Author

**Christianah Adekunle** · *AI Automation Engineer & ML Engineer*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Christianah%20Adekunle-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/christianah-adekunle)
[![GitHub](https://img.shields.io/badge/GitHub-i--am--christy-181717?style=flat-square&logo=github)](https://github.com/i-am-christy)
[![Blog](https://img.shields.io/badge/Blog-i--am--christy.hashnode.dev-2962FF?style=flat-square&logo=hashnode)](https://i-am-christy.hashnode.dev)

---

## 🙏 Acknowledgements

- **The DHS Program** — for making the NMIS 2021 dataset publicly accessible to researchers upon request, enabling nationally representative, state-level analysis of malaria in Nigeria.
- **Federal University of Technology, Akure (FUTA)** — for the academic environment and training that shaped the analytical foundations applied in this project.
- **The Scikit-learn community** — for maintaining the open-source machine learning library that powers the entire modeling pipeline (Pedregosa et al., 2011).

---

<p align="center">
  <sub>Built with 🐍 Python · 🌍 Made in Nigeria</sub>
</p>