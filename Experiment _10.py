import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Sample Dataset with all marks
    data = {
        'Maths':,
        'Science':,
        'English': [75, 82, 90, 76, 85, 89, 68, 84, 91, 73]
    }

    # Creating DataFrame
    df = pd.DataFrame(data)

    print("Dataset:")
    print(df)

    # 2. SCATTER PLOT
    plt.figure(figsize=(6, 4))
    plt.scatter(df['Maths'], df['Science'])
    plt.title('Scatter Plot: Maths vs Science')
    plt.xlabel('Maths Marks')
    plt.ylabel('Science Marks')
    plt.show()

    # 3. CORRELATION MATRIX
    correlation = df.corr()
    print("\nCorrelation Matrix:")
    print(correlation)

    # Correlation Matrix Heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix Heatmap")
    plt.show()

    # 4. PAIR PLOT
    sns.pairplot(df)
    plt.suptitle("Pair Plot of Subject Marks", y=1.02)
    plt.show()

if __name__ == '__main__':
    main()
