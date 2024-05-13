with open("library.txt",'w+') as file:
      booktitle=input("Enter a Book Title--->")
      bookauthor=input("Enter a Book Author--->")

      file.write(f'Book Title name is {booktitle}\n Book Author Name is {bookauthor}')
      # file.seek()
      # file.write(bookauthor)