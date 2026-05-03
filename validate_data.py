# No nulls
assert df["value"].isnull().sum() == 0, "Null values found!"

# Positive values
assert (df["value"] > 0).all(), "Negative values found!"

# Unique IDs
assert df["id"].is_unique, "Duplicate IDs found!"
