Area of Rectangle
'''length=int(input('enter length: '))
breadth=int(input('enter breadth: '))
area = length*breadth
print(area)
print("Area of Rectangle is",area)
print("length is {0} ,breadth is {1} and area is {2}".format(length,breadth,area))
print("length is %0.1f, breadth is %0.1f and area is %0.1f"%(length,breadth,area))'''

'''length,breadth=int(input("enter length")),int(input("enter breadth"))
area=length*breadth
print(area)
print("Area of Rectangle is",area)
print("length is {0} ,breadth is {1} and area is {2}".format(length,breadth,area))
print("length is %0.1f, breadth is %0.1f and area is %0.1f"%(length,breadth,area))'''


#Perimeter of Rectangle
'''length=int(input('enter length: '))
breadth=int(input('enter breadth: '))
#length,breadth2=int(input("enter length")),int(input("enter breadth"))
perimeter =2*(length+breadth)
print(perimeter)
print("perimeter of Rectangle is",perimeter)
print("length is {0} ,breadth is {1} and area is {2}".format(length,breadth,perimeter))
print("length is %0.1f, breadth is %0.1f and area is %0.1f"%(length,breadth,perimeter))'''


#Area of Triangle
'''base=int(input('enter the base: '))
height=int(input('enter the height: '))
area=0.5*(base*height)
print(area)
print("perimeter of Rectangle is",area)
print("length is {0} ,breadth is {1} and area is {2}".format(base,height,area))
print("length is %0.1f, breadth is %0.1f and area is %0.1f"%(base,height,area))'''


#Simple interest
'''p=int(input('enter the principle: '))
t=int(input('enter the time period: '))
r=int(input('enter the rate: '))
si=(p*t*r)/100
print(si)
print("perimeter of Rectangle is",si)
print("principle is {0} ,time period is {1}, rate is {2} and si is {3}".format(p,t,r,si))
print("principle is %0.1f, time period is %0.1f, rate is %0.1f and si is %0.1f"%(p,t,r,si))'''


#Find Celsius for given Fahrenheit
'''fahrenheit=int(input('enter a number: '))
celsius=(5/9)*(fahrenheit-32)
print('celsius is',celsius)
print('%0.1f degree of fahrenheit is equal to %0.1f degree of celsius'%(fahrenheit,celsius))
print('{0} degree of fahrenheit is equal to {1} degree of celsius'.format(fahrenheit,celsius))'''

fahrenheit=float(input('enter a number: '))
celsius=(5/9)*(fahrenheit-32)
print('celsius is',celsius)
print('%0.1f degree of fahrenheit is equal to %0.1f degree of celsius'%(fahrenheit,celsius))
print('{0} degree of fahrenheit is equal to {1} degree of celsius'.format(fahrenheit,celsius))