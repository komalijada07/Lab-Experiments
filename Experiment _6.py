
import pandas as pd


def main():

    # Creating DataFrame
    data = {
        'RollNo': [101, 102, 103, 104, 105],
        'Name': ['Arun', 'Bhanu', 'Charan', 'Divya', 'Esha'],
        'Marks': [85, 72, 90, 65, 88],
        'Department': ['CSE', 'ECE', 'CSE', 'EEE', 'ECE']
    }

    df = pd.DataFrame(data)

    print("Original DataFrame")
    print(df)

    # 1. Selecting Specific Columns
    print("\nSelecting Name and Marks Columns")
    print(df[['Name', 'Marks']])

    # 2. Selecting Specific Row using Index
    print("\nSelecting Row with Index 2")
    print(df.loc[2])

    # 3. Slicing Rows
    print("\nSlicing Rows from Index 1 to 3")
    print(df[1:4])

    # 4. Boolean Filtering
    print("\nStudents with Marks Greater than 80")
    print(df[df['Marks'] > 80])

    # 5. Conditional Selection using Multiple Conditions
    print("\nCSE Students with Marks Greater than 80")
    print(df[(df['Department'] == 'CSE') & (df['Marks'] > 80)])

    # 6. Advanced Slicing using loc
    print("\nAdvanced Slicing using loc")
    print(df.loc[1:3, ['Name', 'Marks']])

    # 7. Advanced Slicing using iloc
    print("\nAdvanced Slicing using iloc")
    print(df.iloc[0:3, 1:4])


if __name__ == "__main__":
    main()
  
