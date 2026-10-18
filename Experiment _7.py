
import pandas as pd


def main():

    # Creating Simple DataFrame
    data = {
        'Department': ['CSE', 'CSE', 'ECE', 'ECE', 'EEE', 'EEE'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Marks': [85, 90, 78, 88, 70, 95],
        'Salary': [50000, 52000, 48000, 51000, 45000, 55000]
    }

    df = pd.DataFrame(data)

    print("Original DataFrame")
    print(df)

    # 1. Grouping Data using groupby()
    print("\n1. Grouping Data using groupby()")
    dept_group = df.groupby('Department')['Marks'].mean()
    print(dept_group)

    # 2. Multiple Aggregate Statistics
    print("\n2. Multiple Aggregate Statistics")
    aggregate_stats = df.groupby('Department')['Salary'].agg(
        ['sum', 'mean', 'max', 'min']
    )
    print(aggregate_stats)

    # 3. Grouping by Multiple Columns
    print("\n3. Grouping by Multiple Columns")
    multi_group = df.groupby(['Department', 'Gender'])['Marks'].mean()
    print(multi_group)

    # 4. Creating Pivot Table
    print("\n4. Creating Pivot Table for Average Marks")
    pivot_table = pd.pivot_table(
        df,
        values='Marks',
        index='Department',
        columns='Gender',
        aggfunc='mean'
    )
    print(pivot_table)

    # 5. Pivot Table with Multiple Aggregates
    print("\n5. Pivot Table for Salary Statistics")
    pivot_salary = pd.pivot_table(
        df,
        values='Salary',
        index='Department',
        columns='Gender',
        aggfunc=['mean', 'sum']
    )
    print(pivot_salary)


if __name__ == "__main__":
    main()
  
