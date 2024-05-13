def palindrome(k):
    return k==k[::-1]
v=input("Enter string or number")
if palindrome(v):
    print("palindrome")
else:
    print("not palindrome")