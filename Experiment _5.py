
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


def main():

    # Sample Data
    data = {
        'Age': [18, 22, 25, 30, 35],
        'Salary': [20000, 25000, 30000, 40000, 50000],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
        'City': ['Hyderabad', 'Chennai', 'Bangalore',
                 'Hyderabad', 'Chennai']
    }

    df = pd.DataFrame(data)

    print("Original Data")
    print(df)

    # 1. Normalization
    minmax = MinMaxScaler()
    df['Age_Normalized'] = minmax.fit_transform(
        df[['Age']]
    )

    print("\nAfter Normalization")
    print(df[['Age', 'Age_Normalized']])

    # 2. Standardization
    standard = StandardScaler()
    df['Salary_Standardized'] = standard.fit_transform(
        df[['Salary']]
    )

    print("\nAfter Standardization")
    print(df[['Salary', 'Salary_Standardized']])

    # 3. Log Transformation
    df['Salary_Log'] = np.log(df['Salary'])

    print("\nAfter Log Transformation")
    print(df[['Salary', 'Salary_Log']])

    # 4. Label Encoding
    label = LabelEncoder()
    df['Department_Label'] = label.fit_transform(
        df['Department']
    )

    print("\nAfter Label Encoding")
    print(df[['Department', 'Department_Label']])

    # 5. One-Hot Encoding
    one_hot = pd.get_dummies(df['City'], dtype=int)

    print("\nAfter One-Hot Encoding")
    print(one_hot)


if __name__ == "__main__":
    main()
  
