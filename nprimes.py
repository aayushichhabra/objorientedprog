def factors(n):
    factorlist=[]
    for i in range (1,n+1):
        if n%i==0:
            factorlist=factorlist+[i]
    return (factorlist)


def isprime(n):
    return (factors(n)==[1,n])

def primesupton(n):
    plist=[]
    for i in range(1,n+1):
        if isprime(i)==True:
            plist=plist+[i]
    return(plist)

def nprimes(n):
    (count,i,plist)=(0,1,[])
    while(count<n):
        if isprime(i)==True:
            (count,plist)=(count+1,plist+[i])
        i=i+1
    return(plist)

print("first3 prime nos:",nprimes(3))
print("all prime nos smaller than 15:",primesupton(15))
