#!/usr/bin/env python
# coding: utf-8

# In[132]:


import numpy as np
import random
import matplotlib.pyplot as plt



P_op = 0.6                                           # transition probability to switch from pessimist to optimist
N_iter = 2500                                        # number of iterations
beta = 0.5                                           # speed of adjustment coefficient
TN = 1                                               # trading volume of speculative investors
TF = 1                                               # trading volume of fundamentalists
pf = 50                                              # fundamental value
p = 50                                               # actual price
a1 = 0.1                                             # weight factor for getting information from price 
a2 = 0.9                                             # weight factor for getting information from others behaviour
v = 0.3                                              # speed of change
#x = (1/a)*(np.log(P_op/v))
#P_po = v*np.exp(-a*x)
P_po = 0.4166666666666667                            # transition probability to switch from optimist to pessimist

n_tot = 100                                          #Total number of person

#Type = 1 for op and 0 for po
class person():
  def __init__(self,id):                           
    self.state = random.sample([0,1],1)[0]           # generating uniform random number to take an array of total number of traders
    self.id = id

#Initialize the simulation create person (GOD) 
Person_list = []
for i in range(n_tot):Person_list.append(person(i))
#print([x.state for x in Person_list])
y1 = []
y2 = []
xs = []
p_dot = []
for j in range(N_iter):                              # counting the number of each type of traders from zero in each iterations
  n_o = 0
  n_p = 0 
  for persons in Person_list:
    random_num = random.uniform(0,1)               

    if persons.state == 0:
        if random_num <= P_op:  
            persons.state = 1
    else:
        if random_num <= P_po:
            persons.state = 0
            
  for persons in Person_list:
    if persons.state == 0:
        n_p += 1
    else:
        n_o += 1
    
        
  x=0
  y1.append(n_o)
  y2.append(n_p)
  N = int((n_o + n_p)/2)
  n = (n_o - n_p)/2
  x = n/N
  xs.append(x)
  p_dot= beta*(x*TN+TF*(pf-p))
  P_op = v*np.exp((a1)*(p_dot)/v +(a2)*x)
  P_po = v*np.exp(-(a1)*(p_dot)/v -(a2)*x)
  #print(P_op,P_po)
  #print(n_o)
  #print(n_p)
  #print(x)

plt.figure()
plt.xlabel("number of iterations")
plt.ylabel("x")
plt.title("")
plt.plot(xs, linewidth = 1)
plt.savefig("plot2.jpg")
plt.show()


# In[ ]:




