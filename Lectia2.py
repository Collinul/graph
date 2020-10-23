import numpy as np
from queue import Queue
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = Queue(maxsize=100)
Q = Queue(maxsize=100)

f = open("C:/Users/Win/Desktop/linput.txt", "r")
l = int(f.readline())
# numaru de linii
c = int(f.readline())
# numaru de coloane
v = np.zeros((l+1, c))
d = np.zeros((l+1, c))
for i in range(l):
    for j in range(c):
        v[i][j] = int(f.readline())
print("------------Labirintul---------------")
print(v)
print("-------------------------------------")
# acuma starting pointu si finishu
xs = int(f.readline())-1
ys = int(f.readline())-1
xf = int(f.readline())-1
yf = int(f.readline())-1


class aux:
    pass


class nou:
    pass


nou = nou()
aux = aux()
aux.x = xs
aux.y = ys
q.put(aux.x)
Q.put(aux.y)

d[xs][ys] = 1
print("------------Parcurgerea--------------")
while not q.empty():
    aux.x = q.get()
    aux.y = Q.get()
    # print("aux.x",aux.x)
    for i in range(4):

        nou.x = aux.x + dx[i]
        nou.y = aux.y + dy[i]
        if(nou.x <= c and nou.y <= l):
            # print("nou.x",nou.x)
            if(v[nou.x][nou.y] == 1 and d[nou.x][nou.y] == 0):

                d[nou.x][nou.y] = d[aux.x][aux.y]+1
                q.put(nou.x)
                Q.put(nou.y)


print(d)
print("-------------------------------------")
aux.x = xf
aux.y = yf
q.put(aux.x)
Q.put(aux.y)
a = aux.x
b = aux.y


while d[a][b] != 1:
    aux.x = a
    aux.y = b
    for i in range(4):
        nou.x = aux.x + dx[i]
        nou.y = aux.y + dy[i]
        if(nou.x <= c and nou.y <= l):
            if(d[nou.x][nou.y] == d[aux.x][aux.y]-1):
                a = nou.x
                b = nou.y
                q.put(nou.x)
                Q.put(nou.y)
print("------------Ordinea-----------------")
while not q.empty():
    print("^(%d,%d)^" % (q.get(), Q.get()))
print("------------------------------------")