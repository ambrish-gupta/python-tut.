# ### previous class
# #<> Write OOp classes to handle the following scenarios:
# # 🔹A user can create and view 2D coordinates
# # 🔹A user can find out the distance between 2 coordinates
# # 🔹A user can find the distance of a coordinate from origin
# # 🔹A user can check if a point lies on a fiven line
# # 🔹A user can find the distance between a given 2D point and a given line.

# class point:
#     def __init__(self,x,y):
#         self.x_cord = x
#         self.y_cord = y
    
#     def __str__(self):
#         return '<{},{}>'.format(self.x_cord,self.y_cord)


#     def euclidean_distance(self,other):
#         return ((other.x_cord - self.x_cord)**2 + (other.y_cord - self.y_cord)**2)**0.5
    
#     def distance_from_origin(self):
#         return self.euclidean_distance(point(0,0))
    
# class line:
#     def __init__(self,A,B,C):
#         self.A = A
#         self.B = B
#         self.C = C

#     def __str__(self):
#         return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    
#     def point_on_line(line,point):
#         if line.A*point.x_cord + line.B*point.y_cord + line.C == 0:
#             return 'point lies on the line'
#         else:
#             return 'point does not lies on the line'
        
#     def sortest_distance(line,point):
#         return abs(line.A*point.x_cord + line.B*point.y_cord + line.C)/(line.A**2 + line.B**2)**0.5


    

# # p1 = point(2,2)
# # p2 = point(0,0)
# # print(p1.euclidean_distance(p2))
# # print(p1.distance_from_origin())
# # print(p1)

# l1 = line(1,1,5)
# p1 = point(1,4)
# print(l1)
# print(p1)
# print(l1.point_on_line(p1))
# print('ghjgjg',l1.sortest_distance(p1))















# class person:

#     def __init__(self,name_input,country_input):
#       self.name = name_input
#       self.country = country_input
      
#     def greet(self):
#        if self.country == 'India':
#           print('Namaste',self.name)
#        else:
#           print('Hello',self.name)
       
# p1 = person('Amb','India')
# o = p1.greet()
# print(o)











# ✨ Reference Variables-->

# 👉 Refernce variables hold the objects
# 👉 We can create onjects without reference variable as well
# 👉 An object can have multiple reference variables
# 👉 Assigning a new reference variable to an existing objects does not create a new object


# # Object without a reference variable
# '''we can create the object without reference variable but if we want to find then it will hard to find thet's why we use the refence variable'''
# class Person:
#     def __init__(self):
#         self.name = 'Amb'
#         self.gender = 'male'

# p = print(Person())




# # ✨ Pass by Reference -->
# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# # Outside the class so it is a function
# '''here we can give object as a input to the function and also a function can return the object of any class'''
# def greet(personn):
#     print('Hii my name is',personn.name,'and I am a',personn.gender)
#     p1 = Person('Ambb','male')
#     return p1
# p = Person('Amb','male')
# x = greet(p)
# print(x.name)
# print(x.gender)




# # ✨ Encepsulation
'''When we make the methods then we have to keep it private and that's why the otther people can't change it easily
because if they change through the object then the code will be crash and we have to face the problems, that's why we use the 
encaptulation method (getter or get and setter or set), by using this method we can give the limited permission to cange and modify 
from the and we also can use if else conditions. Then if anyone want to cahnge it in wrong way it will show
the humble msg.'''



# # dict of objects
# # list of objects
# class Person:

#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# p1 = Person('Amb','male')
# p2 = Person('Mitthii','female')
# p3 = Person('Siddhii','female')
# '''objects can store in list,dictionary,and sets and if it store then we can do the operation whatever we do in conditional operation'''
# L = [p1,p2,p3]
# for i in L:
#     print(i.name)  
    


# <> 👉 --> Static Variables VS Instance variables <--
'''1️⃣ Instance Variables

Definition:
Instance variables are variables that belong to an object (instance), of a class.

🔹 Key Points

Defined using self

Each object has its own copy

Changes affect only that object

✅ Example
class Student:
    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks    # instance variable

s1 = Student("Amit", 80)
s2 = Student("Riya", 90)

s1.marks = 85

print(s1.marks)  # 85
print(s2.marks)  # 90


👉 s1 and s2 have separate values

2️⃣ Static Variables (Class Variables)

Definition:
Static variables are variables that belong to the class, not to any single object.

🔹 Key Points

Defined inside class but outside methods

Shared by all objects

Only one copy exists

✅ Example
class Student:
    school = "ABC School"   # static variable

    def __init__(self, name):
        self.name = name

s1 = Student("Amit")
s2 = Student("Riya")

print(s1.school)
print(s2.school)


👉 Both objects share the same school

🔁 Modifying Static Variable
Student.school = "XYZ School"

print(s1.school)  # XYZ School
print(s2.school)  # XYZ School

⚠️ Important Difference

If you modify static variable using an object:

s1.school = "New School"


➡️ It creates an instance variable, not changes static variable.
'''