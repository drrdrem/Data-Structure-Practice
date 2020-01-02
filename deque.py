class deque(object):
    def __init__(self, size):
        self.front = -1
        self.rear = 0
        self.size = size
        self.arr = [0]*size
        
    def _isFull(self):
        return (self.front==0 and self.rear==self.size-1) or (self.front==self.rear+1)
    
    def _isEmpty(self):
        return self.front==-1
    
    def insert_front(self, key):
        if self._isFull():
            print("Overflow")
            return

        if self.front==-1:
            self.front = 0
            self.rear = 0
            
        elif self.front==0: self.front = self.size - 1
        else: self.front -= 1
        
        self.arr[self.front] = key
        
    def insert_rear(self, key):
        if self._isFull():
            print("Overflow")
            return
        
        if self.front==-1:
            self.front = 0
            self.rear = 0
            
        elif self.rear==self.size-1: self.rear = 0
        else: self.rear += 1
            
        self.arr[self.rear] = key
        
    def delete_front(self):
        if self._isEmpty():
            print("Underflow")
            return
        
        if self.front==self.rear:
            self.front = -1
            self.rear = -1
            
        else:
            if self.front==self.size-1: self.front=0
            else: self.front += 1
                
    def delete_rear(self):
        if self._isEmpty():
            print("Underflow")
            return
        
        if self.front==self.rear:
            self.front = -1
            self.rear = -1
            
        elif self.rear==0: self.rear = self.size-1
        else: self.rear -= 1
            
    def get_front(self):
        if self._isEmpty():
            print("Underflow")
            return -1
        return self.arr[self.front]
        
    def get_rear(self):
        if self._isEmpty() or self.rear<0:
            print("Underflow")
            return -1
        return self.arr[self.rear]