class teacher:
      def show(self):
            print(f"Techer name is Shreyash")
class student(teacher):
      def show(self):
            #super().show() for method overloading
            print(f"Student name is vikas")

# s1=student()
# s1.show()

teacher().show()