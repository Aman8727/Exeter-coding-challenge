#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd 
import csv 
import re 
import string


# In[107]:


reader = csv.reader(open('french_dictionary.csv', 'r'))
d = {}
k= {}
for row in reader:
    key, value = row
    d[key] = value
    k[key] = 0 
# print(k)


# In[90]:


def upp(word):
    w1 = word.lower()
    nw1 = d[w1]
    return nw1.capitalize()


# In[92]:


def check(word):
    if('[' in word or ']' in word):
        return True 
    return False


# #for calculating the [] containing columns 

# In[93]:


def maketheword(word):
    flag =0 ;
    if('[' in word and ']' in word):
        nword = word[1:-1]
        flag =0
    elif('['in word):
        nword = word[1:]
        flag =1
    else:
        nword = word[:-1]
        flag =2
    
    if(nword in d):
        k[nword] += 1
        if(flag ==0):
            return word[0]+d[nword]+word[-1]
        elif(flag==1):
            return word[0]+d[nword]
        else:
            return d[nword] + word[-1]
        
    elif(nword.lower() in d):
        nnword = nword.lower()
        k[nnword] +=1 
        if(flag ==0):
            return word[0]+d[nnword].capitalize()+word[-1]
        elif(flag==1):
            return word[0]+d[nnword].capitalize()
        else:
            return d[nnword].capitalize() + word[-1]
    return word


# In[94]:


fin = open("t8.shakespeare.txt", 'rt')
fout = open("t8.shakespeare_1.txt","wt")
for line in fin:
    for word in re.split(r"[,!-.\s]\s*",line):
        if(word in d):
            line = line.replace(word, d[word])
            k[word] += 1
        elif (word.lower() in d):
            w1 =upp(word)
            line =line.replace(word,w1)
            k[word.lower()] +=1 
        elif(check(word)):
            formword = maketheword(word)
            line = line.replace(word,formword)
    fout.write(line)
fin.close()
fout.close()


# In[96]:


field= ['English word','French word','Frequency']


# In[97]:


with open('frequency.csv','w') as f:
    write=csv.writer(f)
    write.writerow(field)
    for key in d:
        if(k[key]):
            write.writerow([key,d[key],k[key]])


# In[ ]:




