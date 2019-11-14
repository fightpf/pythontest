n0=0
n1=1
n=3
while n <= 20:
    ntemp=n1
    n1=n0+n1
    n0=ntemp
    n+=1
    print(n1)