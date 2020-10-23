import numpy as np
from queue import Queue
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, 1]
q = Queue(maxsize=100)

f = open("C:/Users/Win/Desktop/linput.txt", "r")
l = int(f.readline())
# numaru de linii
c = int(f.readline())
# numaru de coloane
v = np.zeros((l, c))
d = np.zeros(((l, c)))
print(l)
print(c)
#v = [line.split() for line in f]
#v=np.loadtxt("C:/Users/Win/Desktop/linput.txt", dtype='i', delimiter=' ')

for i in range(l):
    for j in range(c):
        v[i][j] = int(f.readline())

print(v)

# acuma starting pointu si finishu
xs = int(f.readline())
ys = int(f.readline())
xf = int(f.readline())
yf = int(f.readline())


class aux:
    pass


class nou:
    pass


nou = nou()
aux = point()
aux.x = xs
aux.y = ys
q.put(aux.x, aux.y)
d[xs][ys] = 1
print()
while not q.empty():
    
    for i in range(4):
        nou.x = aux.x + dx[i]
        nou.y = aux.y + dy[i]

        if(v[nou.x][nou.y] == 1 and d[nou.x][nou.y] == 0):
            d[nou.x][nou.y] = d[aux.x][aux.y]+1
            q.put(nou.x, nou.y)

    q.get()
    
print(d)
