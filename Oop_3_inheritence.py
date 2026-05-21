# # ✨ Class Relationships

# # 🔹 Aggregation
# # 🔹 Inheritence


# #  ✅👉 Aggregation
# '''--> Relationship between Classes <-- when any class is part of another class, like a resturent has menu or customer info has 
# details like ,neme, gender, age , address so here we cannot define the address in the same class that's
# why we have to use another class foe the address and that is called aggregation which is thw 
# part of another class
# in simple words --> when any class is part of another class or relate with another class then 
# it will said to be aggregation.'''
# #example
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address

#     def print_address(self):
#         print(self.address.get_city(),self.address.pin,self.address.state)
    
#     def edit_profile(self,name,new_city,new_pin,new_state):
#         self.name = name
#         self.address.edit_address(new_city,new_pin,new_state)


# class Address:
#     def __init__(self,city,pin,state):
#         self.__city = city
#         self.pin = pin
#         self.state = state

#     def get_city(self):
#         return self.__city
    
#     def edit_address(self,new_city,new_pin,new_state):
#         self.__city = new_city
#         self.pin = new_pin
#         self.state = new_state

    
# '''if there's a diamond symbol in the diagram that means it is a symbol of aggregation
# '''
# add1 = Address('GKP',273152,'UP')
# cust = Customer('Amb','male',add1)
# cust.print_address()


# cust.edit_profile('Amb','Vadodra',391760,'Gujrat')
# cust.print_address()

 







# ### ✅ 👉  Inheritence
# '''Inheritence means redundency means once if fefine something then use it for multiple times.
# it means resusability, once make the class and use that other neccessary place, if two classes
# has same method there we can use inheritence to make our code smooth and easy to usable multiple time.'''
 

# #parent class
# class User:
#     def __init__(self):
#         self.name = 'Amb'

#     def login(self):
#         print('login')


# #child class
# class Student(User):
#     pass
# ## once we use the constructor in the parent class then we shouldn't have to use it in the child class.

#     def enroll(self):
#         print('enroll into the course')

# u = User()
# s = Student()

# '''if there is triangle in the diagramm it means it is a symbol of inheritence.'''

# print(s.name)
# print(s.login())
# print(s.enroll())


##✅#--> What is inherited? <--
# 🔹 Constructor
# 🔹 Non Private Attributes
# 🔹 Non Private Methods


# ###<> Constructor example
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     pass

# s = Smartphone(20000,"Apple",13)
# s.buy




### If it is alredy defined in the children class then the object will not goes for the parent class that;s why attribute will not intitalize
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print("Inside Smartphone constructor")

# s = Smartphone("Android",4)
# s.buy
# s.brand








# ## Child can't access private member of the class

# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

        ##getter
#     def show(self):
#         print(self.__price)

# class Smartphone(Phone):
#     def check(self):
#         print(self.__price)


# s = Smartphone(20000,"Apple",13)
# print(s.brand)
# # s.check()
 # s.show()






# #### <> <> <> .
# class Parent:
#     def __init__(self,num):
#         self.__num = num

#     def get_num(self):
#         return self.__num
    
# class Child(Parent):
    
#     def show(self):
#         print('This is in child class')


# son = Child(100)
# print(son.get_num())
# son.show()





# # #### <> <> <> .
# class Parent:
#     def __init__(self,num):
#         self.__num = num

#     def get_num(self):
#         return self.__num
    
# class Child(Parent):

#     def __init__(self,val,num):
#         self.__val = val
#         self.__num = num
        
#     def get_val(self):
#         return self.__val

        
    
# son = Child(100,10)
# # print('parent: Num:',son.get_num())
# print('Childs: val:',son.get_val())









# # # #### <> <> <> .
# class A:
#     def __init__(self):
#         self.var1 = 100

#     def display1(self,val1):
#         print('class A :',self.var1)


# class B(A):
#     def deisplay2(self,var2):
#         print('class B :',self.var2)

# obj = B()
# obj.display1(200)








# # # #### <> <> <> .
# # ✅ Method Overriding-->
# '''it means if the parent and child both have the same method then the method which have the child is excute only not parent's method.'''
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside the contructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     def buy(self):
#         print('Buying a smartphone')

# s = Smartphone(20000,'OPPO',40)
# s.buy()













# ## ✅ Super Keyword
### ⚠️ Important Keypoints----
###1. Super cannot access variable
###2. Super cannot use from outside the class
###3. Super is used inside the class
###4. Super cannot access the attribute

# '''we can call the parent class's method from the child class mathod using super keyword..'''

# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside the contructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     def buy(self):
#         print('Buying a smartphone')
#         # Syntax to call paarent ka buy method
#         super().buy()


# s = Smartphone(20000,'OPPO',40)
# s.buy()















# # ## ✅ Super Keyword for thr call the both constructor
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside the contructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     def __init__(self, price, brand, camera,os,ram):
#         print('Inside smartphone constructor')
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print('inside smartphone constructor')

# '''if we want to call the both constructor and have to give the value from the child constructor then we use the super keyword.'''

# s = Smartphone(2000,"Samsung",12,"Android",2)
# print(s.os)
# print(s.brand)










# # ## ✅ Super Keyword for using outside the class (we cannot call fromt he outside with a super key)

# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside the contructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     def buy(self):
#         print('Buying a smartphone')
#         # Syntax to call paarent ka buy method
#         # super().buy()


# s = Smartphone(20000,'OPPO',40)
# s.super().buy()







# ## ✅🧠 Inheritence in Summary
#1.--> A class can inherit frim another class.
#2.--> Inheritance improves code reuse
#3.--> Constructor, attribute, methods get inherited to the child class
#4.--> The parent has no access to the child class
#5.--> Private prperties of parent are not accessible directly in child class
#6.--> child class can override the attributes or methods. This is called method overriding
#7.--> super() is an inbuilt function which is used to invoke the parent class methods and constructor


# ## practice 1:-
# class Parent:
#     def __init__(self,num):
#         self.__num = num
#         print('inside the parent constructor')
#     def get_num(self):
#         return self.__num
    
# class Child(Parent):
#     def __init__(self, num, val):
#         super().__init__(num)

#         self.__val = val

#     def get_val(self):
#         print('inside the child constructor')

#         return self.__val
    

# son = Child(100,200)
# print(son.get_num())
# print(son.get_val())




# ## practice 2:-
# class Parent:
#     def __init__(self):
#         self.num = 100

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.var = 200
#     def show(self):

#         # here self is work as object son it means it will carry the value of num which is 100
#         print(self.num)
#         print(self.var)

# son = Child()
# son.show()





# ## practice 3:-
# class Parent:
#     def __init__(self):
#         self.__num = 100

#     def show(self):
#         print("parent:",self.__num)
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var = 10

#     def show(self):
#             print("Child:",self.__var)

# obj= Child()
# obj.show()





# ## ✅🧠 Types of Inheritance
#🔹# 1:- Single Inheritance
'''it has a parent and a child ,, and the child inhetis the parent.'''

#🔹# 2:- Multilevel Inheritance
'''it means it has many classes where multiple grandpa parent child classess, here is a chahin
in both side and the last one child can inherit all the above classes'''

#🔹# 3:- Hierechical Inheritance
'''in these case a parent class can have multiple child classes and every child classes can acces the parent class or 
inherit the parent class.'''

#🔹# 4:- Multiple inheritance(Diamond Problem)
'''in these case a children class have many parent classes.  it means a single class is inheriting from multiple
classes'''

#🔹# 5:- Hybrid Inheritance
'''in the case we use the single , hierechical , multiple inheritances.'''



# #🔹# 1:- Single Inheritance
# class Phone:
#     def __init__(self,price, brand, camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     pass

# Smartphone(1000,'Redmi','13px').buy()






# #🔹# 2:- Multilevel Inheritance
# class Product:
#     def review(self):
#         print('Product customer review')

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Inside the Phone')

# class Smartphone(Phone):
#     pass
        
# s = Smartphone(2000,'POCO','40mpx')
# s.buy()

# s.review()








# #🔹# 3:- Hierechical Inheritance
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside the constructor')
#         self.__price = price
#         self.brand = brand 
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class SmartPhone(Phone):
#     pass

# class FeaturePhone(SmartPhone):
#     pass

# SmartPhone(10000,'IQ','40mpx').buy()
# FeaturePhone(15000,'Apple','45mpx').buy()







# #🔹# 4:- Multiple inheritance(Diamond Problem)
# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand =  brand
#         self.camera = camera

#     def buy(self):
#         print('buying a phone')

# class Product:
#     def buy(self):
#         print('Product buy method')

# class Smartphone(Product,Phone):
#     # whatever we inherit the first inside smartphone clas will access first. it is called method resolution order (mro).
#     pass

# s = Smartphone(200000,'Apple','44mpx')
# s.buy()








# # ## practice que.1:-
# class A:
#     def m1(self):
#         return 20
    
# class B(A):
#     def m1(self):
#         return 30
#     def m2(self):
#         return 40

# class C(B):
#     def m2(self):
#         return 50
    
# obj1 = A()
# obj2 = B()
# obj3 = C()
# print(obj1.m1() + obj3.m1() + obj3.m2())






# # ## practice que.2:-
# class A:
#     def m1(self):
#         return 20
    
# class B(A):
#     def m1(self):
#         val = super().m1()+30
#         return val

# class C(B):
#     def m1(self):
#         val = self.m1()+20
#         return val
#     # this code will give the error because of lot of executions. it means it is call itself again and again.
# obj = C()
# print(obj.m1())









# ## practice que.3:-
class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        val = super().m1()+30
        return val

class C(B):
    def m1(self):
        val = super().m1()+20
        return val
    

obj = C()

print(obj.m1())

