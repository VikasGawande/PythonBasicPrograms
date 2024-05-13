import threading
import time

def numbers():
      for i in range(1,6):
            print("Thread", i)
            time.sleep(2)

def alphabates():
      list=['a','b','c','d','e']
      for j in list:
            print("Thread",j)
            time.sleep(2)
            
t1=threading.Thread(target=numbers)
t2=threading.Thread(target=alphabates)

t1.start()
t2.start()

t1.join()
t2.join()


            