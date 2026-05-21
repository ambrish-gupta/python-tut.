### ✨ File Handling ✨
## Some Theory
# 🔹Text - '12345' as a sequence of unicode chars
# 🔹Binary - 12345 as a sequence of bytes of its binary equivalent

# --> Hence there are 2 file types to deal with <--

# 🔹Text files - All program files are text files
# 🔹Binary Files - Images, music, video, exe files



# # ------------------------------------''------------------------


# how File I/O is done in most programming languages

# 🔹Open a file
# 🔹 Read/Write data
# 🔹Close the file





# ### 👉 case 1:- if the file is not present

# f = open('sample.txt','w')
# f.write('Hello World!')
# f.close()
# ##since the file is closed hence this will not work
# # f.write('jsj')



# ### write multiline strings
# f = open('sample1.txt','w')
# f.write("Hii")
# f.write('\nkaise ho?')
# f.close()


# ### 👉 case 2- if the fileis already present
# '''agr hum phle se exist file pr write krenge to purana content replace ho jayega.'''
# f = open('sample1.txt','w')
# f.write("Kya haal hai bhai??")
# f.close()



#### How exactly open() works?


# ## ✅ Problem with w mode 
# ## Introducing append mode
# '''this is for if we want to add more line in our file.'''
# f = open('sample1.txt','a')
# f.write('\nI am fine\n')
# f.close()




# ## ✅ write lines
# L = ['Heloo\n','Hii\n','where are uh from\n','I am from Mumbai']

# f = open('sample1.txt','a')
# f.writelines(L)
# f.close()






# ### 👉 Reading from files
# ##-->  using reads()
# f = open('C:\data analytics playground\sample1.txt','r')
# s = f.read()
# print(s)
# f.close()


# f = open('C:\data analytics playground\sample.txt','r')
# d = f.read()
# print(d)
# f.close()


# #### for the limited character read
# # if we want to read limited character the we can give the parameter inside the read()
# f = open('C:\data analytics playground\sample1.txt','r')
# s = f.read(10)
# print(s)
# f.close()



# # ### 👉 Reading from files by one by one lines
# f = open('C:\data analytics playground\sample1.txt','r')
# print(f.readline(),end = '')
# print(f.readline(),end = '')
# ## this is the gonnea be long code so we have to improve with loop
# f.close()



# # ### 👉 Reading from fiiles line by line using loops
# f = open('C:\data analytics playground\sample1.txt','r')

# while True:
#     data = f.readline()

#     if data == '':
#       break
#     else:
#       print(data, end='')

# f.close()




### 💡 Using Context Manager (With)
# ▪ --> It is a good idea to clase a file after usage as it will free up the resources.
# ▪ --> If we don't close it, garbage collector would close it.
# ▪ --> with keyword closes the file as soon as the usage is over.

 ## 1.
# with open('C:\data analytics playground\sample.txt','a') as f:
#  f.write('\nHello Solomn Bhai')


# ## 2. 
# with open('C:\data analytics playground\sample.txt','a') as f:
#  f.write('\nKya hai ye yarrr')
#  f.write('\ndimag kharab ho gya!')
 
# with open('C:\data analytics playground\sample.txt','r') as f:

#  while True:
#   data = f.readline()
#   if data == '':
#    break
#   else:
#     print(data, end='')




# ### 💡 moving within a file --> 10 char then 10 char
# with open('sample.txt','r') as f:
#     print(f.read(10))
#     print(f.read(10))




# ### 💡 Benefits? --> to load a big file in memory
# ## by help of these we can print in chunks.
# big_L = ['hello world!\n' for i in range(250)]

# with open('sample_big.txt','w') as f:
#     f.writelines(big_L)


# with open('sample_big.txt','r') as f:
    
#     chunk_size = 100

#     while len(f.read(chunk_size))>0:
#         print(f.read(chunk_size),end='')
#         f.read(chunk_size)  # this is for next remaining strings






### 💡 Seek and tell function
##👉 --> tell <--is denote that how much charcter we pront and where we are

# with open('sample.txt','r') as f:
#     print(f.read(10))
#     print(f.tell())

#     f.seek(4) # it says that from which char uh want to perform.
#     print(f.read(10))
#     print(f.tell())





###👉 Seek during write
with open('sample.txt','w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('XA')

# c = f.write()
# print(c)




### ⚠ 👉  Problem with working in text mode
# can't work with binary files like images
# not good for other data types like int/float/list/tuples
## 📌 in those case we use read binary(rb) and write binary(wb)



# ## working with binary file
# with open('C:\data analytics playground\Screenshot 2025-03-01 171056.png','r') as f:
#     f.read()


###✅ working with binary file
# with open('C:\data analytics playground\Screenshot 2025-03-01 171056.png','rb') as f:
#     with open('screenshot_new_copy.png','wb') as wf:
#         wf.write(f.read())

## 📌 in those case we use read binary(rb) and write binary(wb)

# with open('ooo.jpg','rb') as ff:
#     with open('new_ooo.png','wb') as wff:
#         wff.write(ff.read())





###✅ working with a big binary file
'''in the textual data it can take unicode char, it means it has to be a string '''
with open('sample.txt','w') as f:
    f.write('5')
    # if we want to show in int then we have to use the type conversion method.



with open('sample.txt','r') as fu:
    print(fu.)