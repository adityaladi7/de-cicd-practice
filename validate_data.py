import pandas as pd


def validate():
    df = pd.read_csv("data/sample.csv")

    # Rule 1: No null values
    assert df["value"].isnull().sum() == 0, "Null values found!"

    # Rule 2: Values should be positive
    assert (df["value"] > 0).all(), "Negative values found!"


if __name__ == "__main__":
    validate()
