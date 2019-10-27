a=3
b= int(a) #將b指向到a的物件
a = 5
#b=4 #建立一個新物件4
print(id(b),id(a))
print(a)
print(b)

a=[1,2,3]
b=a.copy()
#b[0]=999
print(a,b)
print(id(a),id(b))
