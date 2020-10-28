import numpy as np
from queue import Queue


class aux:
    pass


aux = aux()


class nou:
    pass


nou = nou()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = Queue(maxsize=100)
Q = Queue(maxsize=100)

f = open("C:/Users/Win/Desktop/hidrante.txt", 'r')

rows = int(f.readline())
coloumns = int(f.readline())
d = np.zeros((rows+1, coloumns+1))
v = np.zeros((rows+1, coloumns+1))

for i in range(rows):
    for j in range(coloumns):
        v[i][j] = int(f.readline())


print("---------------Orasel------------------")
print(v)

for i in range(4):
    aux.x = int(f.readline())
    
    q.put(aux.x)
    aux.y = int(f.readline())
  
    Q.put(aux.y)
    d[aux.x][aux.y] = 1


while not q.empty():
    aux.x = q.get()
    aux.y = Q.get()
    for i in range(4):
        nou.x = aux.x + dx[i]
        nou.y = aux.y + dy[i]
        if(nou.x <= rows and nou.y <= coloumns):
            if(v[nou.x][nou.y] == 1 and d[nou.x][nou.y] == 0):
                d[nou.x][nou.y] = d[aux.x][aux.y]+1
                q.put(nou.x)
                Q.put(nou.y)
print("-----------------------------------")
print(d)
aux.x=int(f.readline())
aux.y= int(f.readline())
print("Plecam din (%d,%d)"%(aux.x,aux.y))
while d[aux.x][aux.y]!=1:
    for i in range(4):
        nou.x= aux.x +dx[i]
        nou.y=aux.y+dy[i]
        if(d[nou.x][nou.y]==d[aux.x][aux.y]-1):
            if(d[aux.x][aux.y]-1==0):
                break
            else:
                aux.x=nou.x
                aux.y=nou.y
                q.put(nou.x)
                Q.put(nou.y)


print("Hidrantul (%d,%d)"%(aux.x,aux.y))