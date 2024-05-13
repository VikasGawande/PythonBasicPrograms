import pandas as pd

# Define the two-dimensional list
two_dim_list = [
    [1, 'John', 25],
    [2, 'Alice', 30],
    [3, 'Bob', 28],
    [4, 'Emily', 27]
]

# Create DataFrame
df = pd.DataFrame(two_dim_list)

# Print the DataFrame
print(df)
print("Number of Row is:",df.shape[0])

