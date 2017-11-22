class Doubly_Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None
        self.prevnode = None

a = Doubly_Node(1)
b = Doubly_Node(2)
c = Doubly_Node(3)

a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b

