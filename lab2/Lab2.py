#!/usr/bin/env python
# coding: utf-8

# # Lab 2

# Booleans

# In[2]:


#1. 
print(10>9)

#2.
print(10==9)

#3.
print(10<9)

#4
print(bool("abc"))

#5.
print(bool(0))


# Operators

# In[3]:


#1. 
print(10*5)

#2. 
print(10/2)

#3. 
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#4. 
if 5!= 10:
  print("5 and 10 is not equal")

#5. 
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


# Lists

# In[4]:


#1.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2.
fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'

#3. 
fruits = ["apple", "banana", "cherry"]
fruits.append('orange')

#4.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#5.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#6. 
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#7. 
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#8. 
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


# Tuples

# In[5]:


#1.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#2. 
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#3.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#4.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


# Sets

# In[6]:


#1.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#2. 
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4. 
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


# Dictionaries

# In[7]:


#1. 
car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model"))

#2.
car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#3. 
car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#4. 
car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


#5. 
car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


# If ... Else

# In[8]:


#1. 
a = 50
b = 10
if a>b:
    print("Hello World")
    
#2. 
a = 50
b = 10
if a!=b:
    print("Hello World")
    
#3. 
a = 50
b = 10 
if a==b:
    print("Yes")
else:
    print("No")
    
#4. 
a = 50
b = 10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")
    
#5. 
if a==b and c==d:
    print("Hello")

#6. 
if a==b or c==d:
    print("Hello")

#7. 
if 5>2:
    print("YES")
    
#8. 
a = 2
b = 5
print("YES") if a == b else print("NO")

#9. 
a = 2
b = 50
c = 2
if a == c or b ==c:
    print("YES")


# While loops

# In[9]:


#1.
i = 1
while i<6:
    print(i)
    i += 1

#2.
i = 1
while i<6:
    if i==3:
        break
    i+=1

#3. 
i=0
while i < 6:
    i+=1
    if i == 3:
        continue
    print(i)

#4. 
i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")


# Loops

# In[10]:


#1.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
#2. 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
#3. 
for x in range(6):
    print(x)

#4. 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# In[ ]:




