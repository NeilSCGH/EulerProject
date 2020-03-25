import numpy as np

##ID 1
print("ID 1")
sum=0
for i in range(1000):
    if i%3==0 or i%5==0: sum+=i
print(sum)

##ID 2
print("\nID 2")
fibo=[1,1]
while fibo[-1]<4000000:
    fibo.append(fibo[-2]+fibo[-1])
fibo.pop(-1)

sum=0
for f in fibo:
    if f%2!=0: sum+=f
print(sum)

##ID 3
print("\nID 3")
max=100000
primes=np.arange(max+1)
n=int(np.sqrt(max))
for i in range(2,n):
    multiples=np.arange(i,int(max/i+1))*i
    primes[multiples]=0
primes=primes[primes!=0]
print("primes ok")

n=600851475143
max=primes[0]
for p in primes:
    if n%p==0 and p>max: max=p
print(max)

##ID 4
print("\nID 4")


##ID 5
print("\nID 5")
