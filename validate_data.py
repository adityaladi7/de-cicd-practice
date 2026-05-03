import pandas as pd


def validate():
    df = pd.read_csv("data/sample.csv")

    # No null values
    assert df["value"].isnull().sum() == 0, "Null values found!"

    # Positive values
    assert (df["value"] > 0).all(), "Negative values found!"

    # Unique IDs
    assert df["id"].is_unique, "Duplicate IDs found!"


if __name__ == "__main__":
    validate()
