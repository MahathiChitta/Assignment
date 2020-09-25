#!/usr/bin/env python
# coding: utf-8

# In[70]:


#ANSWER 1.1
def myreduce(func,I):
    m = func(I[0],I[1])
    for i in range(2,len(I)):
        m = func(I[i],m)
        i+=1 
    return(m)
    


# In[77]:


###Checking the above code using mult and sum
def mult(a,b):
    return(a*b)

print('product of first 4 numbers',myreduce(mult,[1,2,3,4]))
def s(a,b):
    return(a+b)
for i in range (5,10):
   
    print(f'sum of first {i} numbers',myreduce(s,range(i+1)))


# In[96]:


#ANSWER 1.2
def myfilter(func,P):
    m =[]
    for i in range(len(P)):
        if func(P[i])== True:
            m.append(P[i])
        i+=1
    return(m)
            
            


# In[112]:


###Checking the above code using odd, multiple of 7 and string in a string
def oddfilter(m):
    if m%2 == 0:
        return False
    else:
        return True
def multipleof7(n):
    if n%7==0:
        return True
    else:
        return False

    
def testerfora(n):
 
    for i in range(len(n)): 
        if 'a' in n[i]:
            return True
        else:
            return False
        i+=1

a = [1,2,3,4,4,5,7,7,14,14,21,49,35,70]

print(list(filter(oddfilter,a)))
print(myfilter(oddfilter,a))
print(list(filter(multipleof7,a)))
print(myfilter(multipleof7,a))
b =['aaa','ade','bhdd','acvv','jhgga','tefj','ubvv']

print(list(filter(testerfora,b)))
print(myfilter(testerfora,b))


# In[134]:


#ANSWER 2['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
#[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

m =['x','y','z']
n =[1,2,3,4]
p=[1,2,3]
list1 = [a*b for a in m for b in n]
print(list1)
list2 = [a*b for b in n for a in m]
print(list2)
list3 = [[a+b] for a in p for b in p]
print(list3)
list4 = [[a+b for a in n] for b in n]
print(list4)
list5 = [(b,a) for a in p for b in p]
print(list5)


# In[ ]:




