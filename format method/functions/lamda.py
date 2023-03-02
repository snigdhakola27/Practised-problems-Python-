x=lambda a:a+10
print(x(5))
x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(5,6,2))

def fun(n):
    return lambda a:a*n
res=fun(2)
print(res(11))

def fun(n):
    return lambda a:a*n
res=fun(2)
res=fun(3)
print(res(11))
print(res(11))