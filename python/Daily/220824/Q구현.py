queue = []
front = -1
rear = -1

def enQueue(item):
    global rear
    rear += 1
    queue.append(item)

def deQueue():
    global front
    front += 1
    dqqueue = queue.pop(0)
    return dqqueue

enQueue(1)
print(queue)
enQueue(2)
print(queue)
enQueue(3)
print(queue)
print(deQueue())
print(queue)