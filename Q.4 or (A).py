with open ('shreyash.txt','r') as file:
      const=file.read()
      print(const)
      
      # str1=const[::-1]

# with open('shreyash.txt','w+')as file:
#       file.write(str1)
#       print(str1)

#Output:

# my name is shreyash   
# i am from amravati    
# currently live in pune

# with open ('shreyash.txt','r') as file:
#       const=file.readline()
#       print(const)

# #Output

# # my name is shreyash  (Only first line read in file)

# with open ('shreyash.txt','r') as file:
#       const=file.readlines()
#       print(const)