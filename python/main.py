class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,root,data):
        if(root==None):
            temp = Node(data)
            return temp
        elif(data<= root.data):
            root.left=self.insert(root.left,data)
        elif(data> root.data):
            root.right=self.insert(root.right,data)
        return root
    def pretravesal(self,n1):
        if n1 is  None:
            return
        print(n1.data,end=",")
        self.pretravesal(n1.left)
        self.pretravesal(n1.right)
    def posttravesal(self,n1):
        if n1 is  None:
            return
        self.posttravesal(n1.left)
        self.posttravesal(n1.right)
        print(n1.data,end=",")
    def intravesal(self,n1):
        if n1 is  None:
            return
        self.intravesal(n1.left)
        print(n1.data,end=",")
        self.intravesal(n1.right)
n1=Node(10)
while(1):
    n=int(input("1. Insert 2, Display"))
    if(n==1):
        data=int(input("Data To insert"))
        n1.insert(n1,data   )
        print(data,"Inserted to Tree")
    if(n==2):
        print("Post-Order",end=" ")
        n1.posttravesal(n1)
        print()
        print("Pre-order",end=" ")
        n1.pretravesal(n1)
        print()
        print("In-Order",end=" ")
        n1.posttravesal(n1)
        print()