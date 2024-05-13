# class TextTooShortError(Exception):
#     def __init__(self, message="Text entered is too short (less than 10 characters)."):
#         self.message = message
#         super().__init__(self.message)

# def process_text(text):
#     if len(text) < 10:
#         raise TextTooShortError
#     else:
#         print("Text processing can proceed.")

# # Example usage
# try:
#     user_text = input("Enter some text: ")
#     process_text(user_text)
# except TextTooShortError as e:
#     print(e)



class TextTooShortError(Exception):
      def __init__(self,message="Text entered is too short(less than to character)"):
            self.message=message
            super().__init__(self.message)

def process_text(text):
      if len(text)<10:
            raise TextTooShortError
      else:
            print("Correct Text")

try:
      t=input("Enter a Text--->")
      process_text(t)
except TextTooShortError as e:
      print(e)  