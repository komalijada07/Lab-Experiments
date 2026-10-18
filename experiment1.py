import pandas as pd

def main():
# Experiment 1: Creating Sample Dataset
data = {
"Student": ["Ravi", "Sita", "Kiran", "Anu", "John"],
"Marks": [85, 90, 78, 92, 88],
"Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)  

print("===== DATASET =====")  
print(df)  

# Saving Dataset  
df.to_csv("students.csv", index=False)  
df.to_excel("students.xlsx", index=False)  
df.to_json("students.json", orient="records")  

# Reading CSV Data  
csv_data = pd.read_csv("students.csv")  

print("\n===== CSV DATA =====")  
print(csv_data)  

print("\n===== FIRST 5 ROWS =====")  
print(csv_data.head())  

print("\n===== DATA INFORMATION =====")  
print(csv_data.info())  

print("\n===== DATA DESCRIPTION =====")  
print(csv_data.describe())  

print("\n===== DATA SHAPE =====")  
print(csv_data.shape)

if name == "main":
main()output text
