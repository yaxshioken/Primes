if __name__ == '__main__':
    x=int(input("Enter a number: "))
    primes=[]
    for i in range(2,x+1):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
            if is_prime:
                primes.append(i)
    print(*primes)
