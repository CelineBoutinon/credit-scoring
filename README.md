# credit-scoring

![](logo.png)

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Projet realisé en mars 2025 dans le cadre de ma formation Data Scientist avec OpenClassrooms.

## Contexte
"Prêt à dépenser" est une société financière qui propose des crédits à la consommation pour
des personnes ayant peu ou pas d'historique de prêt. L’entreprise souhaite mettre en œuvre
un outil de “scoring crédit” pour calculer la probabilité qu’un client fasse défaut sur son crédit, 
puis classifier la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme
de classification en s’appuyant sur des sources de données variées (données comportementales,
données provenant d'autres institutions financières, etc...). Il s'agira donc de :  

- Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un
 client de façon automatique;
- Analyser les features qui contribuent le plus au modèle, d’une manière générale (feature
 importance globale) et au niveau d’un client (feature importance locale), afin de permettre
 à un chargé d’études de mieux comprendre le score attribué par le modèle et l'action qui
 lui est suggérée ("decline application" ou "grant loan");
- Mettre en production le modèle de scoring de prédiction à l’aide d’une API dans le cloud et réaliser
au préalable une interface locale de test de cette API;
- Mettre en œuvre une approche MLOps end-to-end, du tracking des expérimentations
à l’analyse en production du data drift.

Les données brutes sont disponibles ici: https://www.kaggle.com/c/home-credit-default-risk/data

## Objectif du projet

- Définir et mettre en œuvre un pipeline d’entraînement des modèles  
- Définir la stratégie d’élaboration d’un modèle d’apprentissage supervisé  
- Évaluer les performances des modèles d’apprentissage supervisé  
- Mettre en œuvre un logiciel de version de code  
- Suivre la performance d’un modèle en production et en assurer la maintenance  
- Concevoir un déploiement continu d'un moteur d’inférence sur une plateforme Cloud  

## Organisation du projet

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

## Requirements

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
boto3 1.37.22  
black 25.1.0  
cookiecutter 2.6.0  
flake8 7.1.2  
isort 6.0.1  
jupyterlab 4.3.6  
pytest 8.3.5  
