class student:
      def __init__(self,name):
            print("Constructor Created")
            self.name=name
            print("Object Initialize")
      def show(self):
            print("My name is ",self.name)

      def __del__(self):
            print("Constructor deleted")

s1=student("SHreysh")
s1.show()
del s1