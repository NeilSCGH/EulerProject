import numpy as np

#link https://projecteuler.net/problem=[ID]

run=6

##ID 1
if run<=1:
    print("ID 1")
    sum=0
    for i in range(1000):
        if i%3==0 or i%5==0: sum+=i
    print(sum)

##ID 2
if run<=2:
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
if run<=3:
    print("\nID 3")
    n=123  #600851475143
    max=int(np.sqrt(n))
    primes=np.arange(max+1)
    for i in range(2,max):
        multiples=np.arange(i,int(max/i+1))*i
        primes[multiples]=0
    primes=primes[primes!=0]
    print("primes ok")

    max=primes[0]
    for p in primes:
        if n%p==0 and p>max: max=p
    print(max)

##ID 4
if run<=4:
    print("\nID 4")
    def isPalindromic(n):
        return n == int((str(n))[::-1])

    max=0
    for a in range(100,1000):
        for b in range(a,1000):
            n=a*b
            if isPalindromic(n) and n>max:
                max=n
    print(max)

##ID 5
if run<=5:
    print("\nID 5")
    def valid(n):
        for i in range(1,21):
            if n%i!=0: return False
        return True

    n=1
    while (not valid(n)):
        if n%10000000==0:print(n)
        n+=1
    print(n)

##ID 6
if run<=6:
    max=100
    print("\nID 6")
    squareOfSum=np.sum(range(max+1))**2
    sumOfSquare=np.sum(np.square(range(max+1)))
    print(squareOfSum-sumOfSquare)

##ID 7
if run<=7:
    print("\nID 7")
    max=150000
    primes=np.arange(max+1)
    for i in range(2,max):
        multiples=np.arange(i,int(max/i+1))*i
        primes[multiples]=0
    primes=primes[primes!=0]
    print(primes[10001])