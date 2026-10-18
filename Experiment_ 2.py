    # Experiment 2: Identifying Data Types and Missing Values

    import numpy as np

    # Creating Sample Dataset
    data = {
        "Name": ["Ravi", "Sita", "Kiran", "Anu", "John"],
        "Age": [20, 21, np.nan, 22, 20],
        "Marks": [85, 90, 78, np.nan, 88],
        "City": ["Guntur", "Vijayawada", None, "Hyderabad", "Chennai"]
    }

    df = pd.DataFrame(data)

    # Display Dataset
    print("\n========== DATASET ==========")
    print(df)

    # Identifying Data Types
    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    # Detecting Missing Values
    print("\n========== MISSING VALUES USING isnull() ==========")
    print(df.isnull())

    # Counting Missing Values
    print("\n========== TOTAL MISSING VALUES USING sum() ==========")
    print(df.isnull().sum())
