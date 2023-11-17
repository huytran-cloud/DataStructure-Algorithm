class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parent = None


class Tree:
    def __init__(self):
        self.nodes = {}

    def make_root(self, id):
        self.nodes[id] = Node(id)

    def insert(self, u, v):
        if v not in self.nodes or u in self.nodes:
            return
        node = Node(u)
        node.parent = self.nodes[v]
        self.nodes[v].children.append(node)
        self.nodes[u] = node

    def height(self, id):
        if id not in self.nodes:
            return -1
        node = self.nodes[id]
        if not node.children:
            return 1
        return 1 + max(self.height(child.id) for child in node.children)

    def depth(self, id):
        if id not in self.nodes:
            return -1
        depth = 1
        node = self.nodes[id]
        while node.parent is not None:
            depth += 1
            node = node.parent
        return depth


def process_commands():
    tree = Tree()
    while True:
        command = input().split()
        if command[0] == '*':
            break
        elif command[0] == 'MakeRoot':
            tree.make_root(int(command[1]))
        elif command[0] == 'Insert':
            tree.insert(int(command[1]), int(command[2]))
        elif command[0] == 'Height':
            print(tree.height(int(command[1])))
        elif command[0] == 'Depth':
            print(tree.depth(int(command[1])))


process_commands()
