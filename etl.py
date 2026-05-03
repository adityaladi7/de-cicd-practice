import pandas as pd


def extract():
    print("Extracting data...")
    return pd.read_csv("data/sample.csv")


def transform(df):
    print("Transforming data...")
    df["value"] = df["value"] * 10
    return df


def load(df):
    print("Loading data...")
    df.to_csv("data/output.csv", index=False)


def run_etl():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL completed successfully!")


if __name__ == "__main__":
    run_etl()
