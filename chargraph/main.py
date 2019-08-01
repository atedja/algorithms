import pprint

class Node:
    def __init__(self, c):
        self.next = {}
        self.prev = {}
        self.c = c
        self.occurs = set()

    def add_next(self, c, index):
        """ Add next character 'c' at the given 'index' """
        if not c in self.next:
            self.next[c] = []
        self.next[c].append(index)
        self.occurs.add(index)


    def add_prev(self, c, index):
        """ Add previous character 'c' at the given 'index' """
        if not c in self.prev:
            self.prev[c] = []
        self.prev[c].append(index)
        self.occurs.add(index)


    def get_indices(self, c):
        """ Gets a list of nodes for character 'c' """
        if c in self.next:
            return self.next[c].keys()
        return None


    def __repr__(self):
        return "node char: {}, next: {}, prev: {}, occurs: {}".format(self.c, self.next, self.prev, self.occurs)



def create_nodes(data):
    """ Create node structure given the data """
    nodes = [None] * 26
    base = ord('a')
    prv = -1
    for i, c in enumerate(data):
        b = ord(c)-base
        if nodes[b] == None:
            nodes[b] = Node(b)

        if prv >= 0:
            n = nodes[b]
            n.add_prev(prv, i)
            nodes[prv].add_next(b, i-1)
        prv = b

    return nodes

data = "ballad"
nodes = create_nodes(data)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)
pp.pprint(nodes)
