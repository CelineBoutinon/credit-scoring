# credit-scoring

!(C:\Users\celin\DS Projets Python\OCDS-repos-all\credit-scoring\logo.png)

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

OpenClassrooms Data Scientist Project 7 - Implement a Credit Scoring Model

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         credit_scoring and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── credit_scoring   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes credit_scoring a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

# REQUIREMENTS

- **Data drift notebook**
python 3.10.7
numpy 2.0.2
pandas 2.2.3
evidently 0.6.6

- **Other notebooks**
imbalanced-learn 0.13.0
joblib 1.4.2
lightGBM 4.5.0
matplotlib 3.10.1
missingno 0.5.2
mlflow 2.21.0
numpy 2.0.2
pandas 2.2.3
plotly-express 0.4.1
python 3.13.2
scikit-learn 1.6.1
seaborn 0.13.2
shap 0.47.0
sklearn 1.6.1
streamlit 1.44.0
streamlit-shap 1.0.2
XGBoost= 2.1.4

- **Local environment set-up**
Windows 11 professional
awscli 2.25.5
black 25.1.0
cookiecutter 2.6.0
flake8 7.1.2
isort 6.0.1
jupyterlab 4.3.6
pytest 8.3.5
