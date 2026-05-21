# # There are two types of loops in python
# # 1. While loop -> program to print the table
# #  Program -> Sum of all digits of a given number
# #  Program -> keep accepting numbers from the user till he/she enters a 0 and then find the avg

# number = int(input('enter the number '))

# i = 1
# while i<11:
#     print(number,'*',i,'=',number *i)
#     i+=1

# #  while loop with else
# x= 1
# while x < 3:
#     print(x)
#     x+=1
# else:
#     print('Limit Cross')



# # <> Guessing game
# # generate a random integer between 1 to 100


# # import the module
# import random
# jackpot = random.randint(1,100)
# # guess with random in randint
# guess = int(input('guess a number '))
# # counter value
# counter = 1
# # take while loop and give the condition
# while guess!=jackpot:
# # then counter increment
#  if guess<jackpot:
#     print('Galat! Guess Higher ')
#  elif guess>jackpot:
#     print('Galat! Guess Lower ')

#  guess = int(input('fir se galat! sahi guess karo be thoda ladkiyon ke khyalon se niklo!! '))

#  counter += 1
# # then print the else value and print that it is the correct answer
# else:
#   print('Sahi guess kiya be! ekdm fadu(SEXY)!! ')
# # then print the attempts (how many attempts havw you took)
# print('dekho bhaiya itne attempts kiye aapne! ',counter)



# # <> For loop 

# # in that 1 says from where the value is started and 11 says that from where the value end, and the 3 is says that how much margin we want
# for i in range(1,11,3):
#   print(i)
# for i in range(10,0,-1):
#  print(i)
# for i in 'Delhi ':
#     print(i)


# cur_population = 10000

# for i in range(10,0,-1):
    
#     print('Year',i,'Population is:',cur_population)
#     cur_population = cur_population /1.10


# #  sequence sum
# # 1/1!+2/2!+3/3!+....f

# n = int(input('enter n '))
# result = 0
# fact = 1
# for i in range(1,n+1):
#     fact  = fact * i
#     result = result + i/fact
# print(result)



# # <> Nested loops
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,' ',j)



# # <> ex:- print the following pattern
# # 1
# # 121
# # 12321
# # 1234321
# # 123454321

# rows = int(input('enter the rows:- '))
# for i in range(1, rows+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     for k in range(i-1,0,-1):
#         print(k,end='')
#     print()



# # <> continue and brreak statements'
# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,10):
#     if i ==5 &  i == 4:


#         continue
#     print(i)


# lower = int(input('enter the lower value '))
# upper = int(input('enter the upper value'))
# for i in range(lower,upper+1):
#     for j in range(2,i):
#      if i%j==0:
#         break
#     else:
#         print(i)




