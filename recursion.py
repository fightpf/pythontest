import time

def test(n):
    if n <= 1000 :
        print(n)
        n+=1
        test(n)


a=time.time()
test(0)
print(time.time()-a)
a=time.time()

for i in range(1001):
    print(i)
print(time.time()-a)