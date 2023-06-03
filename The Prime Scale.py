#this is a code which tests whether a number is a prime or not much faster than a conventional method
#I'll explain what is happening at each step

from numpy import *

n=input("Enter number:") #enter a number that you would like to prime test
n=int(n)
sqr=sqrt(n) #reducing the number of values to check against. If the number has a factor, it will have to be less than its square-root

P=0.5615*sqr**(0.829) #gives you the number of primes below your number. Equation derived from data interpolation and interval study
P=int(P)

prime = zeros((1,P))
prime[0][0]=2
cnt=1
i=3
while cnt!=P: #creating the list of primes to test the number against
    p=1  #assuming it is a prime
    for j in range(cnt-1):
        if i%prime[0][j]==0:
            p=0
            continue
    if p==1:
        prime[0][cnt]=i
        cnt+=1
    i+=1

l=1 #conditional for being a prime or not

for k in range(P): #testing the input against the primes
    if n%prime[0][k]==0:
        l=0
        print("It is divisible by",prime[0][k])  #lists all the prime numbers that the input is divisible by
        continue

if(l==1):
    print("It is a prime number")
else:
    print("It is not a prime number")

#what this algorithm does, is take the exercise of checking for primes a step further
#instead of checking for all numbers less than the square root of the number, you only check for all the primes less than the square root

#the total checks for a number is decreased significantly through this algorithm.
#you can determine whether a large number is a prime or not much faster

#through this simple exercise, I have a created code that can do the following:
# 1. Find an nth prime
# 2. Find the number of primes under a certain number (For Eg. How many primes are there under 1000?)
# 3. Finally, find whether a number is prime or not

#next step, create an algorithm that finds the closest primes to any input number