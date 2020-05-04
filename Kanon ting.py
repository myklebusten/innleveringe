#!/usr/bin/env python
# coding: utf-8

# ## kanon

# In[3]:


from pylab import *


def y(t, v0, theta):
    g = 9.81
    return v0 * sin(theta) * t - 0.5 * g * t**2

def yder(t, v0, theta):
    g = 9.81
    return v0 * sin(theta) - g * t

def x(t, v0, theta):
    return v0 * cos(theta) * t

def newtons(f, fder, x, v0, theta, tol = 1E-8, N = 100):
    i = 0
    while abs(f(x, v0, theta)) > tol and i <= 100:
        x = x - f(x, v0, theta)/fder(x, v0, theta)
        i+=1
    return x

stor = 0
stortid = 0
thetaverdier = [pi/6, pi/5, pi/4, pi/3]

for abc in thetaverdier:
    tid = newtons(y, yder, 10, 18, abc)
    m = x(tid, 18, abc)
    print("Tid: ", tid, 3, "Avstand: ", m, 3)
    if m > stor:
        stor = m
        stortid = tid
print("det tok", stortid,"sekunder " "og den største avstanden var", stor,"meter")


# In[ ]:




