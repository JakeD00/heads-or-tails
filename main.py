import os
import random	 
coinflip = random.randint(0,1)
if coinflip == 1:
    print("Heads")
    os.system('pause')
else:
    print("Tails")
    os.system('pause')