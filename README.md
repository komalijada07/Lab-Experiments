
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
### 🔗 Experiment 4 Output:
```text
====== ORIGINAL DATASET ======
    Name  Marks
0   Ravi     95
1   Sita     90
2  Kiran     78
3   Ravi     85
4   John    300
5    Anu     88

====== DUPLICATE ROWS ======
Empty DataFrame
Columns: [Name, Marks]
Index: []

====== DATASET AFTER REMOVING DUPLICATES ======
    Name  Marks
0   Ravi     95
1   Sita     90
2  Kiran     78
3   Ravi     85
4   John    300
5    Anu     88

====== Z-SCORES ======
    Name  Marks   Z_score
0   Ravi     95 -0.354143
1   Sita     90 -0.418714
2  Kiran     78 -0.573686
3   Ravi     85 -0.483286
4   John    300  2.288597
5    Anu     88 -0.444543

====== DETECTED OUTLIERS ======
   Name  Marks   Z_score
4  John    300  2.288597

====== DATA AFTER REMOVING OUTLIERS ======
    Name  Marks   Z_score
0   Ravi     95 -0.354143
1   Sita     90 -0.418714
2  Kiran     78 -0.573686
3   Ravi     85 -0.483286
5    Anu     88 -0.444543

====== DISTRIBUTION BEFORE REMOVING OUTLIERS ======
count      6.000000
mean     122.666667
std       86.666410
min       78.000000
25%       85.750000
50%       89.000000
75%       93.750000
max      300.000000
Name: Marks, dtype: float64

====== DISTRIBUTION AFTER REMOVING OUTLIERS ======
count     5.00000
mean     87.20000
std       6.37965
min      78.00000
25%      85.00000
50%      88.00000
75%      90.00000
max      95.00000
Name: Marks, dtype: float64
```

### 🔗 Experiment 5 Output:
```text
EXPERIMENT 5: DATA TRANSFORMATION AND SCALING

Original Data
   Age  Salary Department       City
0   18   20000         HR  Hyderabad
1   22   25000         IT    Chennai
2   25   30000    Finance  Bangalore
3   30   40000         IT  Hyderabad
4   35   50000         HR    Chennai

After Normalization
   Age  Age_Normalized
0   18        0.000000
1   22        0.235294
2   25        0.411765
3   30        0.705882
4   35        1.000000

After Standardization
   Salary  Salary_Standardized
0   20000            -1.161895
1   25000            -0.714997
2   30000            -0.268099
3   40000             0.625697
4   50000             1.519493

After Log Transformation
   Salary  Salary_Log
0   20000    9.903488
1   25000    10.126631
2   30000    10.308953
3   40000    10.596635
4   50000    10.819778

After Label Encoding
  Department  Department_Label
0         HR                 1
1         IT                 2
2    Finance                 0

After One-Hot Encoding
   Bangalore  Chennai  Hyderabad
0          0        0          1
1          0        1          0
2          1        0          0
3          0        0          1
4          0        1          0

Experiment 5 Completed Successfully!
```

### 🔗 Experiment 6 Output:
```text
Original DataFrame
   RollNo    Name  Marks Department
0     101    Arun     85        CSE
1     102   Bhanu     72        ECE
2     103  Charan     90        CSE
3     104   Divya     65        EEE
4     105    Esha     88        ECE

Selecting Name and Marks Columns
     Name  Marks
0    Arun     85
1   Bhanu     72
2  Charan     90
3   Divya     65
4    Esha     88

Selecting Row with Index 2
RollNo           103
Name          Charan
Marks             90
Department       CSE
Name: 2, dtype: object

Slicing Rows from Index 1 to 3
   RollNo    Name  Marks Department
1     102   Bhanu     72        ECE
2     103  Charan     90        CSE
3     104   Divya     65        EEE

Students with Marks Greater than 80
   RollNo    Name  Marks Department
0     101    Arun     85        CSE
2     103  Charan     90        CSE
4     105    Esha     88        ECE

CSE Students with Marks Greater than 80
   RollNo    Name  Marks Department
0     101    Arun     85        CSE
2     103  Charan     90        CSE

Advanced Slicing using loc
    Name  Marks
1  Bhanu     72
2  Charan     90
3   Divya     65

Advanced Slicing using iloc
     Name  Marks Department
0    Arun     85        CSE
1   Bhanu     72        ECE
2  Charan     90        CSE
```
### 🔗 Experiment 7 Output:
```text
Original DataFrame
  Department  Gender  Marks  Salary
0        CSE    Male     85   50000
1        CSE  Female     90   52000
2        ECE    Male     78   48000
3        ECE  Female     88   51000
4        EEE    Male     70   45000
5        EEE  Female     95   55000

1. Grouping Data using groupby()
Department
CSE    87.5
ECE    83.0
EEE    82.5
Name: Marks, dtype: float64

2. Multiple Aggregate Statistics
              sum     mean    max    min
Department                              
CSE        102000  51000.0  52000  50000
ECE         99000  49500.0  51000  48000
EEE        100000  50000.0  55000  45000

3. Grouping by Multiple Columns
Department  Gender
CSE         Female    90.0
            Male      85.0
ECE         Female    88.0
            Male      78.0
EEE         Female    95.0
            Male      70.0
Name: Marks, dtype: float64

4. Creating Pivot Table for Average Marks
Gender      Female  Male
Department              
CSE           90.0  85.0
ECE           88.0  78.0
EEE           95.0  70.0

5. Pivot Table for Salary Statistics
              mean            sum       
Gender      Female     Male Female   Male
Department                              
CSE        52000.0  50000.0  52000  50000
ECE        51000.0  48000.0  51000  48000
EEE        55000.0  45000.0  55000  45000
```
### 🔗 Experiment 8 Output:
```text
DataFrame 1
   ID    Name  Marks
0   1    Arun     85
1   2    Bala     90
2   3  Charan     78
3   4   David     88

DataFrame 2
   ID Department       City
0   3        CSE  Hyderabad
1   4        ECE    Chennai
2   5        EEE      Delhi
3   6       MECH     Mumbai

DataFrame 3
   ID    Name  Marks
0   7   Eswar     92
1   8  Farhan     81

Inner Merge
   ID    Name  Marks Department       City
0   3  Charan     78        CSE  Hyderabad
1   4   David     88        ECE    Chennai

Left Merge
   ID    Name  Marks Department       City
0   1    Arun     85        NaN        NaN
1   2    Bala     90        NaN        NaN
2   3  Charan     78        CSE  Hyderabad
3   4   David     88        ECE    Chennai

Right Merge
   ID    Name  Marks Department       City
0   3  Charan   78.0        CSE  Hyderabad
1   4   David   88.0        ECE    Chennai
2   5     NaN    NaN        EEE      Delhi
3   6     NaN    NaN       MECH     Mumbai

Outer Merge
   ID    Name  Marks Department       City
0   1    Arun   85.0        NaN        NaN
1   2    Bala   90.0        NaN        NaN
2   3  Charan   78.0        CSE  Hyderabad
3   4   David   88.0        ECE    Chennai
4   5     NaN    NaN        EEE      Delhi
5   6     NaN    NaN       MECH     Mumbai

Row-wise Concatenation
   ID    Name  Marks
0   1    Arun     85
1   2    Bala     90
2   3  Charan     78
3   4   David     88
4   7   Eswar     92
5   8  Farhan     81

Column-wise Concatenation
   ID    Name  Marks  ID Department       City
0   1    Arun     85   3        CSE  Hyderabad
1   2    Bala     90   4        ECE    Chennai
2   3  Charan     78   5        EEE      Delhi
3   4   David     88   6       MECH     Mumbai

Outer Merge with Missing Values
   ID    Name  Marks Department       City
0   1    Arun   85.0        NaN        NaN
1   2    Bala   90.0        NaN        NaN
2   3  Charan   78.0        CSE  Hyderabad
3   4   David   88.0        ECE    Chennai
4   5     NaN    NaN        EEE      Delhi
5   6     NaN    NaN       MECH     Mumbai

After Handling Missing Values
   ID           Name          Marks     Department           City
0   1           Arun           85.0  Not Available  Not Available
1   2           Bala           90.0  Not Available  Not Available
2   3         Charan           78.0            CSE      Hyderabad
3   4          David           88.0            ECE        Chennai
4   5  Not Available  Not Available            EEE          Delhi
5   6  Not Available  Not Available           MECH         Mumbai
```
### 🔗 Experiment 9 Output:
```text
Statistical Summary of Marks
count     20.000000
mean     201.218335
std       22.569947
min      152.143714
25%      191.135759
50%      201.077271
75%      214.281896
max      239.120786
Name: Marks, dtype: float64
```

#### 📊 Generated Plots & Visualizations:

##### 1. Histogram Plot
Shows the continuous distribution of Marks with dashed lines indicating the Mean and Median values.
![Histogram Demo](https://wikimedia.org)

##### 2. Box Plot
Visualizes the distribution of Age, displaying the median, quartiles, and potential outliers.
![Boxplot Demo](https://wikimedia.org)

##### 3. Violin Plot
Combines box plot features with a density plot to reveal the structural symmetry of the Age distribution.
![Violin Plot Demo](https://wikimedia.org)



