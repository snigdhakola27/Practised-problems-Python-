class person():
    def _init_(self,name,age):
        self.name=name
        self.age=age
p1=person('john',36)
print(p1.name)
print(p1.age)'''


#string representation of an object with _str_() function
'''class person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def _str_(self):
        return f"{self.name}({self.age})"
p1=person('john',36)
print(p1)'''


#creating a method in the class
'''class person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print('hello my name is '+self.name)
p1=person('john',36)
p1.fun()