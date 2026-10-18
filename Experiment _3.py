import pandas as pd
import numpy as np

def main():

    # Creating Sample Dataset
    data = {
        "Age": [20, 21, np.nan, 22, 20],
        "Marks": [85, np.nan, 78, np.nan, 88],
        "City": ["Guntur", None, "Hyderabad", None, "Chennai"]
    }

    df = pd.DataFrame(data)

    print("===== ORIGINAL DATASET =====")
    print(df)

    # Mean Imputation
    mean_fill = df.copy()
    mean_fill["Age"] = mean_fill["Age"].fillna(mean_fill["Age"].mean())
    mean_fill["Marks"] = mean_fill["Marks"].fillna(mean_fill["Marks"].mean())

    print("\n===== MEAN IMPUTATION =====")
    print(mean_fill)

    # Median Imputation
    median_fill = df.copy()
    median_fill["Age"] = median_fill["Age"].fillna(median_fill["Age"].median())
    median_fill["Marks"] = median_fill["Marks"].fillna(median_fill["Marks"].median())

    print("\n===== MEDIAN IMPUTATION =====")
    print(median_fill)

    # Mode Imputation
    mode_fill = df.copy()
    mode_fill["City"] = mode_fill["City"].fillna(mode_fill["City"].mode()[0])

    print("\n===== MODE IMPUTATION =====")
    print(mode_fill)

    # Forward Fill
    forward_fill = df.ffill()

    print("\n===== FORWARD FILL =====")
    print(forward_fill)

    # Backward Fill
    backward_fill = df.bfill()

    print("\n===== BACKWARD FILL =====")
    print(backward_fill)

    # Drop Rows with Missing Values
    drop_rows = df.dropna()

    print("\n===== DROP ROWS =====")
    print(drop_rows)

    # Drop Columns with Missing Values
    drop_columns = df.dropna(axis=1)

    print("\n===== DROP COLUMNS =====")
    print(drop_columns)


if __name__ == "__main__":
    main()
