def Fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(10))

def Fibonacci2(n):
    a,b=1,1
    answer=a
    for i in range(n-2):
        answer=a+b
        a,b=b,answer
    return answer
print(Fibonacci2(10))