# ✨ Polymorphism ✨

# # 🔹 Method Overriding
'''it means is a scenario that during the inheritance the child class and the parent class has the same name of methods,
then when the object calls then the child class's method will execute only.'''


# # # 🔹 Method Overloading
# '''when the same class has same name method and the work is different then it is called method overloading.
# or Method overloading is a concept where inside your class uh have multiple functions with the same but their output is different
# based on input.'''
# #exampe:-
# class Shape:
#     def area(self,radius):
#         return 3.14*radius*radius
    
#     def area(self,l,b):
#         return l*b
    # this is not allow in this way in the python, but in another way we can implement.
class Shapes:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a*a
        else:
            return a*b
        
s = Shapes()

print(s.area(2))
print(s.area(3,4))
    


# # 🔹 Operator Overriding
'''it means a single operator perform different depending on the input like + "if we use + in integer it will add
if we use + in str the it will concenate and if we use it in list it will merge.'''