# # from pymongo import MongoClient
# # client=MongoClient('localhost',27017)
# # db=client['warje']
# # collection=db.Student

# # collection.insert_many([
# #     {'Name':'Sanak','RollNbr':12,'Dept':'MCA','MobileNbr':8275790604},
# #     {'Name':'Shreyash','RollNbr':13,'Dept':'MCA','MobileNbr':8275790605},
# #     {'Name':'mihir','RollNbr':14,'Dept':'IT','MobileNbr':8275790606},
# #     {'Name':'vikas','RollNbr':15,'Dept':'Mech','MobileNbr':8275790607},
# #     {'Name':'vivek','RollNbr':16,'Dept':'MCA','MobileNbr':8275790608},
# #     {'Name':'push','RollNbr':17,'Dept':'MCA','MobileNbr':8275790609}, 
# # ])
# # Read
# # for i in collection.find({'Dept':'MCA'}):
#     # print(i)
    
# # update
# # print("data is updated",collection.update_one({'Name':'vikas'},{'$set':{'MobileNbr':9359078831}}))

# # print(collection.delete_one({'Name':'Shreyash'}))

# # with open("vikas.txt","r+") as file:
# #     BookTitle=input("Enter Book Title--->")
# #     BookAuthor=input("Enter BookAuthor---->")
# #     file.writelines(f"BookTitle is {BookTitle}\nBookAuthor is {BookAuthor}")

# # import pandas as pd
# # data={
# #     'ID':[1001,1002,1003],
# #     'Name':['Mohan','Sachin','Rohit'],
# #     'HRA':[12000,13000,11000],
# #     'TA':[6000,9000,4000],
# #     'DA':[10000,9000,8000]
# # }
# # df=pd.DataFrame(data)
# # print(df)
# # print("----------------------------")
# # print("sum of every column\n",df.sum())
# # print("----------------------------")
# # print(df.select_dtypes(include='int64').mean())
# # print(df.select_dtypes(include='int64').median())
# # print(df['HRA'].median())

# # import numpy as np
# # arr=np.array([
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9],
# #     [6,2,9]
# # ])
# # print(arr)
# # print(np.mean(arr,axis=1))
# # print(np.sum(arr,axis=0))

# import pandas as pd
# import numpy as np
# s = np.array([12, 65, 35, 12, 65, 89])
# arr = pd.Series(s)
# # dj = arr.unique()
# fre = pd.Series(arr).value_counts()
# # print(dj)
# print(fre)

# # print(k.max())
# # print(k.min())


import pandas as pd
df = pd.read_csv("C:\\python\\practicals\\sample.csv")
# for i in df['City']:
#     print(df['City']=="Pune")
# print(df['Age']>21)
# print(df[['ID','Age']].max())
# # print(df.describe())
print(df.columns)
print(df.head(6))



# # import pandas as pd
# # data={
# #     'ID':[1001,1002,1003],
# #     'Name':['Mohan','Sachin','virat'],
# #     'HRA':[12000,13000,11000],
# #     'TA':[6000,5000,4000],
# #     'DA':[10000,9000,8000]
# # }
# # df=pd.DataFrame(data)
# # print(df)
# # print(df.sum())
# # print(df.select_dtypes(include='int64').mean())
# # print("HRA sum is: ",df['HRA'].mean())
# # print(df.select_dtypes(include='int64').median())
# # print(df.head(2))
# # print(df.tail(1))
# # v=df['Name'].isnull()
# # print(v)
# # print(df.columns)

