from math import *
from random import randint
MIN_VALUE = 1
MAX_VALUE = 10


print("Helloworld")
random_a = randint(MIN_VALUE,MAX_VALUE)
random_b = randint(MIN_VALUE,MAX_VALUE)
random_c = randint(MIN_VALUE,MAX_VALUE)
d = random_b*random_b-(4*random_a*random_c)
print(f"Pour a = {random_a} \nPour b = {random_b} \nPour c = {random_c}\nLe discrimiant d = {d}")
if d > 0:
   x1 = (-random_b-sqrt(d))/(2*random_a)
   x2 = (-random_b+sqrt(d))/(2*random_a)
   print(f"La solution admet deux reponses x1 : {round(x1,2)} et X2 : {round(x2,2)}")

elif d == 0:
   x0 = (-random_b-d)/(2*random_a)
   print(f"La solution admet une reponse x0 : {x0}")
else :
   print("Au secours")
        
