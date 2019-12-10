def calculate_average(*arg):
    a=arg
    sum=0
    a=list(a)[0]
    number_list=len(a)
    for i in a:  
        sum+=i #sum=sum+i
    average=sum/number_list
    return average 
a=[1,2,3,4,5,6,7,8,9,20]
a=calculate_average(a)
print(a)

for i in [0,1,2,3,'4',5]:
    try :
        a=3
        b=i
        print(a+b)
    except:
        continue

