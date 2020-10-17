# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:12:48 2020

@author: Win
"""

import numpy as np

f=open("C:/Users/Win/Desktop/dinput.txt","r")
n= int(f.readline())

k= int(f.readline())

A=np.zeros((n,n))

for i in range (k):
    x=int(f.readline())
    y=int(f.readline())
    A[x-1][y-1]=1
    A[y-1][x-1]=1
    
print(A)
print()
print("Daca exista drum direct intre x si y")
print()
k1=int(f.readline())

for i in range (k1):
    x=int(f.readline())
    y=int(f.readline())
    if(A[x-1][y-1]==1):
        print("Este pt x=%d si y=%d"%(x,y))
    else:
        print("NU este pt x=%d si y=%d"%(x,y))
        
print()
print("Daca exista drum direct intre x si y sau drum printr-un nod intermediar z")
k2= int(f.readline())
for i in range(k2):
    x=int(f.readline())
    y=int(f.readline())
    ok=0
    for z in range (n):
        if(A[x-1][z]==1 and A[z][y-1]==1):
            if(z==y-1):
                   print("Pentru x= %d si y= %d este drum direct"%(x,y))
            else:
                   print("Pentru x= %d si y= %d exista z= %d"%(x,y,z+1))
         
            ok=1
            break
    if(ok==0):
        print("NU exista drum")    
                
print("--------------DFS---------------")
viz=[0]*n
def dfs(h):
    viz[h]=1
    
    for i in range (n):
        if (viz[i]==0 and A[h][i]==1):
            dfs(i)
k3=int(f.readline())
for i in range(k3):
    x=int(f.readline())
    y=int(f.readline())
    dfs(x-1)
    print("viz: %d",viz)
    print("viz[%d]=%d"%(y,viz[y-1]))
    for i in range (n):
        viz[i]=0
