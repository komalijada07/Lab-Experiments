
import pandas as pd


def main():

    # ------------------------------
    # 1. Creating Sample Dataset
    # ------------------------------

    data = {
        "Student": ["Ravi", "Sita", "Kiran", "Anu", "John"],
        "Marks": [85, 90, 78, 92, 88],
        "Age": [20, 21, 19, 22, 20]
    }

    df = pd.DataFrame(data)

    # ------------------------------
    # 2. Saving Dataset into
    #    CSV, Excel, and JSON files
    # ------------------------------

    df.to_csv("students.csv", index=False)
    df.to_excel("students.xlsx", index=False)
    df.to_json("students.json", orient="records")

    # ------------------------------
    # 3. Importing Data
    # ------------------------------

    csv_data = pd.read_csv("students.csv")
    excel_data = pd.read_excel("students.xlsx")
    json_data = pd.read_json("students.json")

    # ------------------------------
    # 4. Basic Exploration
    # ------------------------------

    print("\n===== CSV DATA =====")
    print(csv_data)

    print("\n===== head() =====")
    print(csv_data.head())

    print("\n===== info() =====")
    csv_data.info()

    print("\n===== describe() =====")
    print(csv_data.describe())

    print("\n===== shape =====")
    print(csv_data.shape)


if __name__ == "__main__":
    main()
### 🔗 Experiment 1 Output:
```text
========== CSV DATA ==========
  Student  Marks  Age
0    Ravi     85   20
1    Sita     90   21
2   Kiran     78   19
3     Anu     92   22
4    John     88   20

========== head() ==========
  Student  Marks  Age
0    Ravi     85   20
1    Sita     90   21
2   Kiran     78   19
3     Anu     92   22
4    John     88   20

========== info() ==========
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Student  5 non-null      object
 1   Marks    5 non-null      int64 
 2   Age      5 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 252.0+ bytes
None

========== describe() ==========
           Marks        Age
count   5.000000   5.000000
mean   86.600000  20.400000
std     5.412948   1.140175
min    78.000000  19.000000
25%    85.000000  20.000000
50%    88.000000  20.000000
75%    90.000000  21.000000
max    92.000000  22.000000

========== shape ==========
(5, 3)
```
### 🔗 Experiment 2 Output:
```text
========== DATASET ==========
    Name   Age  Marks        City
0   Ravi  20.0   85.0      Guntur
1   Sita  21.0   90.0  Vijayawada
2  Kiran   NaN   78.0        None
3    Anu  22.0    NaN   Hyderabad
4   John  20.0   88.0     Chennai

========== DATA TYPES ==========
Name      object
Age      float64
Marks    float64
City      object
dtype: object

========== MISSING VALUES USING isnull() ==========
    Name    Age  Marks   City
0  False  False  False  False
1  False  False  False  False
2  False   True  False   True
3  False  False   True  False
4  False  False  False  False

========== TOTAL MISSING VALUES USING sum() ==========
Name     0
Age      1
Marks    1
City     1
dtype: int64
```
### 🔗 Experiment 3 Output:
```text
===== ORIGINAL DATASET =====
    Age  Marks       City
0  20.0   85.0     Guntur
1  21.0    NaN       None
2   NaN   78.0  Hyderabad
3  22.0    NaN       None
4  20.0   88.0    Chennai

===== MEAN IMPUTATION =====
     Age      Marks       City
0  20.75  85.000000     Guntur
1  21.00  83.666667       None
2  20.75  78.000000  Hyderabad
3  22.00  83.666667       None
4  20.00  88.000000    Chennai

===== MEDIAN IMPUTATION =====
    Age  Marks       City
0  20.5   85.0     Guntur
1  21.0   85.0       None
2  20.5   78.0  Hyderabad
3  22.0   85.0       None
4  20.0   88.0    Chennai

===== MODE IMPUTATION =====
    Age  Marks       City
0  20.0   85.0     Guntur
1  21.0    NaN    Chennai
2   NaN   78.0  Hyderabad
3  22.0    NaN    Chennai
4  20.0   88.0    Chennai

===== FORWARD FILL =====
    Age  Marks       City
0  20.0   85.0     Guntur
1  21.0   85.0     Guntur
2  21.0   78.0  Hyderabad
3  22.0   78.0  Hyderabad
4  20.0   88.0    Chennai

===== BACKWARD FILL =====
    Age  Marks       City
0  20.0   85.0     Guntur
1  21.0   78.0  Hyderabad
2  22.0   78.0  Hyderabad
3  22.0   88.0    Chennai
4  20.0   88.0    Chennai

===== DROP ROWS =====
    Age  Marks     City
0  20.0   85.0   Guntur
4  20.0   88.0  Chennai

===== DROP COLUMNS =====
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]
```


