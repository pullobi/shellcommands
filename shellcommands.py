import os
import time as tm
tmsleep = 1.5




while True:
   command = input("command:")
   os.system(command)
   em = input("1 more command?")

   if em == "yes":
      command = input("command:")
      os.system(command)
   else:
      if em == "no":
         print("Quit...")
         tm.sleep(tmsleep)
         exit()
          
      else:
         print("Please type Yes/No")