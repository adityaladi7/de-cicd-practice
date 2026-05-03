import pandas as pd


def test_output_data():
    df = pd.read_csv("data/output.csv")

    # Check no nulls
    assert df["value"].isnull().sum() == 0

    # Check transformation worked
    assert (df["value"] % 10 == 0).all()
