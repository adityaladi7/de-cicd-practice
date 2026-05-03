import pandas as pd


def extract():
    return pd.read_csv("data/sample.csv")


def transform(df):
    # Example transformation
    df["value"] = df["value"] * 10
    return df


def load(df):
    df.to_csv("data/output.csv", index=False)


def run_etl():
    df = extract()
    df = transform(df)
    load(df)


if __name__ == "__main__":
    run_etl()
