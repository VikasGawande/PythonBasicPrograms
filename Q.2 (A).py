#Instance Variable
class student:
      def __init__(self,name,dept):
            self.name=name
            self.dept=dept

      def info(self):
            print(f"Name is :{self.name} and Departmnet is {self.dept}")
#Driver code
s1=student("Shreyash","MCA")
s1.info()

#Static Variable
class student:
      dept="MCA"
      def __init__(self,name):
            self.name=name

      def info(self):
            print(f"Name is :{self.name} and Departmnet is {self.dept}")
#Driver code
s1=student("Shreyash")
s1.info()

#Local Variable
def add():
      a=10
      b=10
      return a+b
print("Sum is :",add())

