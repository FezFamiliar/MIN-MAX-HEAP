import Queue
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


    def MaxInsert(self,data): 
        if data > self.data:
            return False        # you cant insert a value that is greater than the root in a max heap
            
        q = []
        q.append(self)
        #print(len(q))
        # if self.parent != None and self.parent.data > self.data: # then do the insertion otherwise dont do shit
        while (len(q)):
            aux = q[0]
            q.pop(0)
            if (aux.left == None):
                aux.left = Node(data)
                aux.left.parent = aux
                if aux.data < aux.left.data:
                   # print('left: %d' % aux.left.data)
                    aux.left = None
                
                break
            else:
                q.append(aux.left)
            if (aux.right == None):
                
                aux.right = Node(data)
                aux.right.parent = aux
                if aux.data < aux.right.data:
                   # print('right %d' % aux.data)
                    aux.right = None
                break
            else:
                q.append(aux.right)





    def MinInsert(self,data): 
        if data < self.data:
            return False        # you cant insert a value that is greater than the root in a max heap
            
        q = []
        q.append(self)
        #print(len(q))
        # if self.parent != None and self.parent.data > self.data: # then do the insertion otherwise dont do shit
        while (len(q)):
            aux = q[0]
            q.pop(0)
            if (aux.left == None):
                aux.left = Node(data)
                aux.left.parent = aux
                if aux.data > aux.left.data:
                   # print('left: %d' % aux.left.data)
                    aux.left = None
                
                break
            else:
                q.append(aux.left)
            if (aux.right == None):
                
                aux.right = Node(data)
                aux.right.parent = aux
                if aux.data > aux.right.data:
                   # print('right %d' % aux.data)
                    aux.right = None
                break
            else:
                q.append(aux.right)




    def preorder(self):
        if self != None:
            print(self.data)
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()


    def inorder(self):  
        if self != None:
            if self.left != None:
                self.left.inorder()
            print(self.data)
            if self.right != None:
                self.right.inorder()
    def Arrayify(self): 
        result = []
        q = Queue.Queue()
        q.put(self)
        while q.empty() == False:
            aux = q.get()
            result.append(aux.data)
            if aux.left != None:
                q.put(aux.left)
            if aux.right != None:
                q.put(aux.right)
            q.task_done()
        return result


class MaxHeap:
    def __init__(self):
        self.root = None
    
    def MaxInsert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.MaxInsert(data)

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder() 

    def Arrayify(self):
        return self.root.Arrayify()


class MinHeap:
    def __init__(self):
        self.root = None
    
    def MinInsert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.MinInsert(data)

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder() 

    def Arrayify(self):
        return self.root.Arrayify()



mymaxheap = MaxHeap()
mymaxheap.MaxInsert(50)
mymaxheap.MaxInsert(80)
mymaxheap.MaxInsert(20)
mymaxheap.MaxInsert(30)
mymaxheap.MaxInsert(70)
mymaxheap.MaxInsert(31)
mymaxheap.MaxInsert(2)
mymaxheap.MaxInsert(21)
print(mymaxheap.Arrayify())
#mymaxheap.preorder()

myminheap = MinHeap()
myminheap.MinInsert(10)
myminheap.MinInsert(12)
myminheap.MinInsert(15)
myminheap.MinInsert(8)
print(myminheap.Arrayify())
myminheap.preorder()
#mymaxheap.inorde4r()
