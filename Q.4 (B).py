from pymongo import MongoClient
client=MongoClient("localhost",27017)
db=client['Vikas']
collection=db['Students']

collection.insert_many([
      {"Name" : "Shreyash" ,"Rollnbr" : 101, "Dept" : "MCA"},
      {"Name" : "Vikas" ,"Rollnbr" : 102, "Dept" : "PGDM"},
      {"Name" : "Pratik" ,"Rollnbr" : 103, "Dept" : "MCA"},
      {"Name" : "Avdhut" ,"Rollnbr" : 104, "Dept" : "MCA"},
])

# collection.delete_one({"Name":"Vikas"})
# print("Deleted")

collection.update_one({"Name":"Pratik"},{'$set':{"Name":"Vikas"}})
print("Updated")

for data in collection.find({"Dept" : "MCA"}):
      print(data)


