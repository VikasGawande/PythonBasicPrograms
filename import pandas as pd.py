# import  pandas as pd
# data={
#      'name':['vikas','shreyash','shubham','avinash','pratik'],
#       'marks':[70,80,90,45,60],
#       'age':[20,25,23,45,19]
# }
# df=pd.DataFrame(data)
# print(df)
# # print(df.select_dtypes(include='int64').sum())
# print(df.select_dtypes(include='int64').mean())
# print(df.select_dtypes(include='int64').median())
# # print(df.dtypes())
# print(df.head(3))
# # print("---------")
# print (len(df))
# print(df.columns)
# print(df.sum())
# print(df['marks'].mean())
# print(df['age'].median())


# import pandas as pd
# data={
#     'ID':[1001,1002,1003],
#     'Name':['Mohan','Sachin','Virat'],
#     'HRA':[12000,13000,11000],
#     'TA':[6000,5000,4000],
#     'DA':[10000,9000,8000]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.sum())
# print(df.select_dtypes(include='int64').mean())
# print("HRA sum is: ",df['HRA'].mean())
# print(df.select_dtypes(include='int64').median())
# print(df.head(2))
# print(df.tail(1))



# import numpy as np
# arr=np.array([
#   [1,2,3],
#   [4,7,8],
#   [7,2,9],
#   [7,3,9]
#   ])
# print(arr)
# print(np.mean(arr,axis=0))  #if axis=0 then column wise and if axis=1 then row wise


# import numpy as np
# arr = np.array(
#     [
#         [1, 2, 3, 5, 7],
#         [4, 7, 8, 6, 8],
#         [7, 2, 9, 7, 5],
#         [7, 3, 9, 7, 5],
#         [7, 4, 9, 6, 5],
#     ]
# )
# print(arr)
# print("-----------")
# print(np.mean(arr,axis=0))
# print("---------")
# print(np.median(arr, axis=0))
# print(arr[:2, -2:])  # 1):2,:2 ghetla tr top left corner yenar #2)-2:,-2: ghetla tr Bottum right yenar
                       # 3)3:,:2 ghetla tr bottom left che 1,2 index print honar. #4):2,-2: ghetla tr top right yenar 

# import numpy as np
# import pandas as pd
# array = np.array([55,65,22,55])
# arr= pd.Series(array)
# ts=arr.unique()
# print(ts.max())
# print(ts.mean())

# import pandas as pd
# import numpy as np

# l=np.array([12,99,56,55,56])
# arr=pd.Series(l)
# ts=arr.unique()
# print(ts)
# print(ts.max())
# print(ts.min())

import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
print(arr)
print(np.mean(arr,axis=0))




# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client['emp']
# collection= db.employee
# # Inserting multiple documents
# collection.insert_many([
#     {"Id":123 ,"name":"Vikas","address":"Pune","phone":9359078831,"email":"vikas@","dept":"it"},
#     {"Id":124 ,"name":"sam","address":"amt","phone":9359078831,"email":"sam@","dept":"Account"},
#     {"Id":125 ,"name":"dj","address":"mumbai","phone":9359078831,"email":"dj@","dept":"Mech"},
# ])
# for i in collection.find({"dept":"Account"}):
#     print(i)
# # print(collection.find_one({"dept":"Account"}))
# print(collection.delete_one_one({"ID":123}))
# print(collection.update_one({"ID":125},{"$set":{"phone":7218795452}}))


# import pandas as pd
# df = pd.read_csv("C:\\python\\practicals\\sample.csv")
# for i in df['City']:
    # print(df['City']=="Pune")
# print(df['Age']>21)
# print(df[['ID','Age']].max())
# print(df.describe())