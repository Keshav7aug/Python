class Node:
    def __init__(self,value,prev=None):
        self.value=value
        self.next=None
        self.prev=prev

def traverseLL(node):
    while node is not None:
        print(node.value,end='->')
        node=node.next
    print(None)

def create_LL(in_li):
    head=Node(in_li.pop(0))
    node=head
    for i in in_li:
        node.next=Node(i,node)
        node=node.next
        
    return head,node

def traverseLL_B(node):
    while node is not None:
        print(node.value,end='->')
        node=node.prev
    print(None)
head,tail= create_LL([1,2,'a',4,5,6])
traverseLL(head)
traverseLL_B(tail)