def even_or_odd(n):
    if n%2==0:
        print('{} is even'.format(n))
    else:
        print('{} is odd'.format(n))
even_or_odd(90)
even_or_odd(35) '''


#Len of the string
'''def strlen(name):
    c=0
    for x in name:
        c+=1
    return c
result=strlen('rama')
print(result)'''


#Area of the rectangle
'''def rectangle(l,b):
    area=l*b
    return area
result=rectangle(10,5)
print('area of rectangle is',result)
print('area of a rectangle is {}'.format(result))