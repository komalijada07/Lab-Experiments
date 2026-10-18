
import pandas as pd


def main():

    # Creating First DataFrame
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Name': ['Arun', 'Bala', 'Charan', 'David'],
        'Marks': [85, 90, 78, 88]
    })

    # Creating Second DataFrame
    df2 = pd.DataFrame({
        'ID': [3, 4, 5, 6],
        'Department': ['CSE', 'ECE', 'EEE', 'MECH'],
        'City': ['Hyderabad', 'Chennai', 'Delhi', 'Mumbai']
    })

    # Creating Third DataFrame
    df3 = pd.DataFrame({
        'ID': [7, 8],
        'Name': ['Eswar', 'Farhan'],
        'Marks': [92, 81]
    })

    print("DataFrame 1")
    print(df1)

    print("\nDataFrame 2")
    print(df2)

    print("\nDataFrame 3")
    print(df3)

    # MERGING DATAFRAMES

    # Inner Merge
    inner_merge = pd.merge(df1, df2, on='ID', how='inner')
    print("\nInner Merge")
    print(inner_merge)

    # Left Merge
    left_merge = pd.merge(df1, df2, on='ID', how='left')
    print("\nLeft Merge")
    print(left_merge)

    # Right Merge
    right_merge = pd.merge(df1, df2, on='ID', how='right')
    print("\nRight Merge")
    print(right_merge)

    # Outer Merge
    outer_merge = pd.merge(df1, df2, on='ID', how='outer')
    print("\nOuter Merge")
    print(outer_merge)

    # CONCATENATING DATAFRAMES

    # Row-wise Concatenation
    concat_rows = pd.concat([df1, df3], ignore_index=True)
    print("\nRow-wise Concatenation")
    print(concat_rows)

    # Column-wise Concatenation
    concat_columns = pd.concat([df1, df2], axis=1)
    print("\nColumn-wise Concatenation")
    print(concat_columns)

    # HANDLING MISSING VALUES AFTER MERGING

    print("\nOuter Merge with Missing Values")
    print(outer_merge)

    # Fill missing values
    filled_data = outer_merge.fillna("Not Available")
    print("\nAfter Handling Missing Values")
    print(filled_data)


if __name__ == "__main__":
    main()
  
