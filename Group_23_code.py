import random
import sys
 

x = random.randint(1,200)
y = random.randint(1,200)

e=5
N=101

Y = pow(y,e,N)
X = pow(x,e,N)

def gcd(a,b):
   while b > 0:
       a, b = b, a % b
   return a

if (gcd(x,N)>1):
  print("x and N has a common factor")
 
if (gcd(y,N)>1):
  print("y and N has a common factor")
 
print("Alice's values:")
print("--------------")
print("x [secret]: ",x)
print("N= ",N)
print("X= ",X)
 
print("\nAlice generates a random value (y):")
print("y= ",y)
print("\nAlice computes Y = y^e (mod N) and passes to Bob:")
 
print("Y= ",Y)
 
print("\nBob generates a random value (c) and passes to Alice:")
 
c = random.randint(1,100)
print("c= ",c)
print("\nAlice calculates z = y.x^c (mod N) and send to Bob:")
 
z = (y* x**c) % N
 
print("\nBob now computes val=z^e (mod N) and (y x^c (mod N)) and determines if they are the same\n")
val1= (z**e) % N
val2= (Y* X**c) % N
 
print("op1= ",val1)
print("op2= ",val2)
 
if (val1==val2):
  print("Alice has proven that he knows x")
else:
  print("Failure to prove")

