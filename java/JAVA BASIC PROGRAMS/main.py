class Node:
    nodes = 0 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,root,data):
        if(root==None):
            temp = Node(data)
            self.nodes+=1
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
    def search(self,root,data):
        if(root is None):
            return False
        if(root.data==data):
            return True
        elif(root.data<data):
            return self.search(root.right,data)
        elif(root.data>data):
            return self.search(root.left,data)
    def count_node(self):
        return self.nodes
n1=Node(10)
n1.nodes=1
while(1):
    n=int(input("1. Insert 2. Display 3. Search 4. Count Nodes: "))
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
    if(n==3):
        t = int(input("Enter Search Element: "))
        s=n1.search(n1,t)
        if(s):
            print("Element Found")
        else:
            print("Element Not Found")
    if(n==4):
        print("No of Nodes in Tree : " ,n1.count_node())