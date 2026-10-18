
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    # Creating Sample Data
    np.random.seed(42)
    marks = np.random.normal(200, 25, 20)
    age = np.random.normal(25, 15, 20)

    df = pd.DataFrame({
        'Marks': marks,
        'Age': age
    })

    # Statistical Summary
    print("Statistical Summary of Marks")
    print(df['Marks'].describe())

    # 1. Histogram with Mean and Median
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Marks'], kde=True)

    mean = df['Marks'].mean()
    median = df['Marks'].median()

    plt.axvline(mean, color='red', linestyle='--', label='Mean')
    plt.axvline(median, color='blue', linestyle=':', label='Median')

    plt.title("Histogram with Mean and Median")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

    # 2. Boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(y=df['Age'])

    plt.title("Boxplot of Age")
    plt.show()

    # 3. Violin Plot
    plt.figure(figsize=(8, 5))
    sns.violinplot(x=df['Age'])

    plt.title("Violin Plot of Age")
    plt.xlabel("Age")
    plt.show()


if __name__ == "__main__":
    main()
  
