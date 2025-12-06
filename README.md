# pca-food-consumption-pipeline
A small Python data pipeline that cleans, normalizes, and transforms a messy food-consumption dataset before running PCA for exploratory analysis.

# 🥗 PCA Food Consumption Pipeline  
A small end-to-end Python project demonstrating how to ingest, clean, transform, and analyze a messy public food-consumption dataset. The workflow standardizes units, handles missing values, scales features, and produces a reproducible PCA analysis for exploring global dietary patterns.

---

## 📁 Project Structure
```
pca-food-consumption-pipeline/
│
├── data/
│   └── food_consumption.csv        # Raw dataset
│
├── notebooks/
│   └── pca_analysis.ipynb          # PCA workflow + visualizations
│
├── src/
│   └── clean_transform.py          # Data cleaning + transformation functions
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Pipeline Overview

This project implements a simple data-engineering pipeline:

1. **Ingest raw CSV data**  
2. **Validate schema** (expected columns, dtypes, null checks)  
3. **Clean & normalize**  
   - fix inconsistent column names  
   - deduplicate country entries  
   - handle missing values  
   - convert units where needed  
   - scale features for PCA  
4. **Produce clean feature matrix** ready for modeling  
5. **Run PCA** and generate visualizations to highlight clustering patterns between countries

The cleaning logic is encapsulated in **`src/clean_transform.py`** so the pipeline can be reused on new datasets.

---

## 🔧 Installation

```bash
git clone https://github.com/ihsrohan2020/pca-food-consumption-pipeline
cd pca-food-consumption-pipeline
pip install -r requirements.txt
```

Place the dataset in the `data/` folder as:

```
data/food_consumption.csv
```

---

## 📊 Running the Notebook

Open the PCA notebook:

```bash
jupyter notebook notebooks/pca_analysis.ipynb
```

The notebook will:

- load the cleaned dataset  
- run PCA  
- generate scatterplots of country clusters  
- visualize component loadings  

---

## 🧹 Data Cleaning Functions

Located in `src/clean_transform.py`, including:

- `load_data(path)`  
- `validate_schema(df)`  
- `normalize_columns(df)`  
- `dedupe_countries(df)`  
- `handle_missing(df)`  
- `scale_features(df)`  

This modular structure makes the pipeline reproducible and easy to extend.

---

## 🎯 Why This Project

I built this project to practice structuring a reproducible data workflow—clean separation between ingestion, cleaning logic, transformations, and analysis—similar to how data engineers prepare datasets for downstream machine learning and analytics.

---

## 📎 License  
MIT License.
