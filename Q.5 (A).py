import pandas as pd
data={
      'ID'   :[1001,1002,1003],
      'Name' :['Mohan','Sachin','Virat'],
      'HRA'  :[12000,13000,11000],
      'TA'   :[6000,5000,4000],
      'DA'   :[10000,9000,8000]
}

df=pd.DataFrame(data)
print(df)

sum_of_column=df.sum()
print(sum_of_column)

print("Mean is:\n",df.select_dtypes(include='int64').mean())
print("Median is:\n",df.select_dtypes(include='int64').median())