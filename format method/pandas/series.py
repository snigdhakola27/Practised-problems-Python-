a=[1,7,2]
b=pd.Series(a)
print(b)
print(a[0])'''
from pandas import read_json
from pandas._testing import loc

'''a=[1,7,2]
b=pd.Series(a,index=['x','y','z'])
print(b)
print(a[2])'''

'''k={'day1':421,'day2':390,'day3':333}
l=pd.Series(k)
print(l)
m=pd.Series(k,index=['day1','day2'])
print(m)