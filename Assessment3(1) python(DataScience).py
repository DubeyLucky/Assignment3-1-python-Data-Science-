#!/usr/bin/env python
# coding: utf-8

# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

# In[2]:


#The def keyword is used to create, (or define) a function.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def odd():
    
    for i in l:
        if i%2 != 0:
            print(i)
    return odd


# In[3]:


odd()


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.

# #We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.

# In[5]:


def test(*args):
    x = 0
    for i in args:
        x = x+i
    return x


# In[6]:


test(2,5)


# In[7]:


test(6,8)


# In[12]:


def test1(*mul):
    x = 3
    for i in mul:
        x = x * i
    return x


# In[13]:


test1(2)


# In[14]:


def test2(**kwargs):
    return kwargs


# In[15]:


test2(Lucky=[20154])


# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].

# An iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.
# 
# Name the method used to initialise the iterator object and the method used for iteration for example:-

# In[8]:


x = "Lucky"

y = iter(x)

next(y)


# In[9]:


next(y)


# In[10]:


next(y)


# In[11]:


next(y)


# In[12]:


next(y)


# the samethings has been done by for loop

# In[13]:


for i in x:
    print(i)


# Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

# In[14]:


l = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# In[15]:


y = iter(l)


# In[16]:


next(y)


# In[17]:


next(y)


# In[18]:


next(y)


# In[19]:


next(y)


# In[20]:


next(y)


# In[ ]:


Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.


#  A Python generator function allows you to declare a function that behaves like an iterator, providing a faster and easier way to create iterators.
#     
# If you want to return multiple values from a function, you can use generator functions with yield keywords.
#     

# In[32]:


def gen(a):
    
    x,y = 0,1
    
    for i in range(a):
        
        yield x
        
        x,y = y, x+y
    return gen


# In[33]:


gen(10)


# In[34]:


for i in gen(10):
    print(i)


# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.

# In[38]:


def genprimes(limit): 
                     
    D = {}            
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

p = genprimes(100)
prms = [i for i in p]

print (prms)


# Write a python program to print the first 10 Fibonacci numbers using a while loop.

# In[39]:


def fibs(n):
    a,b = 0,1
    sum = 0
    count=1
    while(count<=n):
        count+=1
        print(a)
        a=b
        b=sum
        sum=a+b
    return fibs


# In[40]:


fibs(10)


# Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[42]:


s = "pwskills"



# In[44]:


test = []

for i in s:
    test.append(i)
    print(i)


# In[46]:


test


# In[ ]:


Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.


# In[62]:


odd_list = [x for x in range(1,100) if x % 2 != 0]
print(odd_list)


# In[ ]:





# In[ ]:





# In[ ]:




