def stack():
    s = []
    return s
def push(s, data):
    item = s.append(data)
    return item
def pop(s):
    item = s.pop()
    return item
def peek(s):
    item = s[len(s)-1]
    return item
def isEmpty(s):
    return s == []
def size(s):
    return len(s) 