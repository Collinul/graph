# sa vedem cate grafuri sunt
import numpy as np
f = open("C:/Users/Win/Desktop/exinput.txt", "r")
n = int(f.readline())
k1 = int(f.readline())
viz=[0]*n
c=0
v=[]
A = np.zeros((n, n))
for i in range(k1):
    x = int(f.readline())
    y = int(f.readline())
    A[x-1][y-1] = 1
    A[y-1][x-1] = 1
print(A)

def dfs(h):
    viz[h] = c 

    for i in range(n):
        if (viz[i] == 0 and A[h][i] == 1):
            dfs(i)

for i in range (n):
    if(viz[i]==0):
        c+=1
        dfs(i)
print("viz= ",viz)
sorted(v)
for i in range (len(viz)):
    c=0
    for j in range (len(viz)):
        
        if(viz[j]==viz[i] and viz[j]!=viz[i-1]):
            c+=1
        
            
    if(c!=0):
        v.append(c)
    
    
    
print("vectoru de cate noduri per grupa",v)