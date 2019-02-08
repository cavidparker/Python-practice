
# coding: utf-8

# Body Mass Index:

# In[1]:


height = 1.778
weight = 70
bmi = weight / height ** 2
print(bmi)
if bmi<30:
    print ("healthy")


# Switch LIST :

# 
# 

# In[2]:


x = ["apple","orange","banana"]


x[1] = "apple"
x[0] = "orange"
print(x)


# In[11]:


x = "Hello"
stive=list(x)
print (stive)


# In[22]:


car = {
    "brand":"Ford",
    "model":"mustang",
    "year":1996
}
car["year"]=2019
x = car.get("year")
for y in car:
    print(car[y])


# In[35]:


i = 1
while i<=10:
    print(i)
    if i==3:
        print("HI")
    i = i+1
    


# In[45]:


i = 0
while i<10:
    i=i+1
    if i ==3:
        print("ok")
    print(i)


# In[67]:


fruits = ["banana","apple","cherry"]
for x in fruits:
    if x == "apple":
        break
print(x) 
   
    


# In[68]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# In[80]:


for x in range(10):
    print(x)
else:
    print("Finised")


# In[82]:


fruits = ["apple","banana","cherry"]
color =["red","yellow","green"]
for x in fruits:
    for y in color:
        print(x,y)
    


# FUNCTION :

# In[6]:


def my_function ():
    print("hello function")
my_function()    
    


# In[18]:


def my_function(fname):
    print(fname +" HI")
my_function("cavid")
my_function("Tariqul")   
my_function("Parker")



# In[30]:


def my_function(country = " Norway"):
    print("i am from" + country)
my_function  (" Sweden")
my_function  (" Bangladesh")
my_function()

