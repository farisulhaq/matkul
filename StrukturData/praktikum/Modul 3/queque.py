def createQueue():
    q = []
    return q
def enQueue(q,data):
    q.insert(0,data)
    return q
def deQueue(q):
    data = q.pop()
    return data
def isEmpty(q):
    return (q == [])
def size(q):
    return (len(q))