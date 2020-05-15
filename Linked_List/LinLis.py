class Node:
    def __init__(self,value,prev=None):
        self.value=value
        self.next=None
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None
    
    def prepend(self,value):
        node=Node(value,None)
        node.next=self.head
        self.head=node
    
    def append(self,value):
        if(self.head==None):
            self.head=Node(value)
        else:
            node1=self.head
            node=self.head.next
            while node is not None:
                node1=node
                node=node.next
            node1.next=Node(value,node1)
    
    def search(self,value):
        node=self.head
        pos=-1
        while node is not None:
            pos+=1
            if node.value==value:
                break
            node=node.next
        return node
       
    def remove(self,value):
        node=self.head
        if self.search(value)==-1:
            return False
        while node is not None:
            if node.value==value:
                if node.next!=None:
                    node.next.prev=node.prev
                if node.prev!=None:
                    node.prev.next=node.next
                else:
                    self.head=node.next
                return True
            node=node.next
    
    def pop(self):
        if(self.head==None):
            return None
        ans=self.head.value
        self.head=self.head.next
        self.head.prev=None
        return ans
    
    def insert(self,value,pos):
        if pos>self.size():
            pos=self.size()
        if pos==0:
            node1=Node(value,None)
            node1.next=self.head
            self.head=node1
        else:
            node=self.head
            for i in range(pos):
                temp=node
                node=node.next
            node1=Node(value,temp)
            node1.next=node
            temp.next=node1
        return True
        
    def size(self):
        node=self.head
        pos=0
        while node is not None:
            node=node.next
            pos+=1
        return pos
    def Traverse(self):
        node=self.head
        while node is not None:
            print(node.value,end='->')
            node=node.next
        print(None)
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
Li=LinkedList()
for i in range(7):
    Li.append(i)
Li.prepend('a')
print(Li.remove('b'))

print(Li.search(4).value)
print(Li.pop())
print(Li.size())
Li.insert(31,3)
Li.Traverse()

