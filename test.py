from queue import Queue
q = Queue(maxsize=(6))

class point:
    pass

aux = point()
aux.x=6
aux.y=2


q.put(aux.x)
q.put(aux.y)
print(q.qsize())
print(q.get())


