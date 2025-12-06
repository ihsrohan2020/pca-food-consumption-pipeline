import pandas as pd
from sklearn.preprocessing import StandardScaler

# Data Loading

def load_data(path: str) -> pd.DataFrame:
    """Load CSV data into a pandas DataFrame."""
    return pd.read_csv(path)



# Schema Validation

EXPECTED_COLUMNS = ["country", "food_category", "consumption", "co2_emission"]

def validate_schema(df: pd.DataFrame) -> None:
    """Check for missing expected columns and raise an error if any are missing."""
    missing = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


# Cleaning Functions
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names: lowercase and underscores."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def dedupe_countries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deduplicate entries where countries appear with slight variations.
    For demo purposes, normalize common inconsistencies.
    """
    df["country"] = df["country"].str.strip().str.title()
    df = df.drop_duplicates()
    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing numeric values with the median."""
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    return df



# Scaling for PCA

def scale_features(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """
    Scale selected feature columns using StandardScaler.
    Returns a DataFrame with scaled features.
    """
    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(df[cols])
    scaled_df = pd.DataFrame(scaled_array, columns=cols)
    return scaled_df



# Full Pipeline

def run_pipeline(path: str) -> pd.DataFrame:
    """
    Execute full cleaning pipeline and return clean, scaled dataframe.
    """
    df = load_data(path)
    df = normalize_columns(df)
    validate_schema(df)
    df = dedupe_countries(df)
    df = handle_missing(df)

    # Select numeric columns for PCA
    feature_cols = ["consumption", "co2_emission"]

    scaled_df = scale_features(df, feature_cols)
    df_scaled = pd.concat([df["country"], df["food_category"], scaled_df], axis=1)

    return df_scaled


if __name__ == "__main__":
    cleaned = run_pipeline("data/food_consumption.csv")
    print(cleaned.head())
