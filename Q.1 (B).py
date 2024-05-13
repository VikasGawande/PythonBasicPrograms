def is_palindrome(num):
      real=str(num)

      reversed_str=real[::-1]

      if real==reversed_str:
            return True
      else:
            return False
value=input("Enter a String or Number--->")
if is_palindrome(value):
      print(value," Palindrome")
else:
      print(value," is not Palindrome")

print("****************************************")

def palindrome(s):
      return s==s[::-1]
value=input("Enter a String or Number--->")
if palindrome(value):
      print(value,"is Palindrome")
else:
      print(value,"is not Palindrome")
