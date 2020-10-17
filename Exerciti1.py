# sa vedem cate grafuri sunt
import numpy as np
f = open("C:/Users/Win/Desktop/exinput.txt", "r")
n = int(f.readline())
k1 = int(f.readline())
viz=[0]*n
c=0
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
print(viz)