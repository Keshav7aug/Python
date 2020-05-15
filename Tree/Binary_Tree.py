class Node:
    def __init__(self,value=None):
        self.Left=None
        self.Right=None
        self.value=value
    def get_value(self):
        return self.value
    def set_value(self,value):
        self.value=value
    def set_left_child(self,node):
        self.Left=node
    def set_right_child(self,node):
        self.Right=node
    def get_left_child(self):
        return self.Left
    def get_right_child(self):
        return self.Right
    def has_left_child(self):
        return self.Left!=None
    def has_right_child(self):
        return self.Right!=None
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
class Tree:
    def __init__(self,value=None):
        self.root=Node(value)
    def get_root(self):
        return self.root
    
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"
def pre_order_traversal(tree):
    vis=list()
    stack=Stack()
    node=tree.get_root()
    vis.append(node.get_value())
    stack.push(node)
    while node.has_left_child():
        node=node.get_left_child()
        vis.append(node.get_value())
        stack.push(node)
   #node=stack.pop()
    while not stack.is_empty():
        node=stack.pop()
        #print(node.has_right_child())
        
        if node.has_right_child():
            node=node.get_right_child()
            tree=Tree(node.get_value())
            vis+=pre_order_traversal(tree)
        #print(node,end=' ')
    return vis
def pre_order_traversal1(tree):
    vis=list()
    root=tree.get_root()
    def trav(node):
        if node:
            vis.append(node.get_value())
            trav(node.get_left_child())
            trav(node.get_right_child())
        
    trav(root)
    return vis
    
def in_order_traversal(tree):
    vis=list()
    root=tree.get_root()
    def trav(node):
        if node:
            trav(node.get_left_child())
            vis.append(node.get_value())
            trav(node.get_right_child())
    trav(root)
    return vis


def post_order_traversal(tree):
    vis=list()
    root=tree.get_root()
    def trav(node):
        if node:
            trav(node.get_left_child())
            trav(node.get_right_child())
            vis.append(node.get_value())
    trav(root)
    return vis
    
    
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
visit_order = list()
stack = Stack()

print(pre_order_traversal(tree))
print(pre_order_traversal1(tree))
print(in_order_traversal(tree))
print(post_order_traversal(tree))
'''vis=list()
stack=Stack()
node = tree.get_root()
stack.push(node)
vis.append(node.get_value())
print(vis)'''
