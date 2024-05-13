with open("library.txt",'w+') as file:
      booktitle=input("Enter a Book Title--->")
      bookauthor=input("Enter a Book Author--->")

      file.writelines([f'Book Title name is {booktitle}\n Book Author Name is {bookauthor}'])
      # file.seek()
      # file.write(bookauthor)