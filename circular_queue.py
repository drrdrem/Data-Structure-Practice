class circular_queue(object):
    def __init__(self, size):
        self.size = size
        self.q = [0]*size
        self.front = -1
        self.rear = -1
        
    def _isFull(self):
        if self.front==self.rear+1 or (self.front==0 and self.rear==self.size-1): return True
        return False
    
    def _isEmpty(self):
        if self.front==-1: return True
        return False
    
    def enQueue(self, ele):
        if self._isFull(): print('Full!!')
        else:
            if self.front==-1: self.front = 0
            self.rear = (self.rear + 1)%self.size
            self.q[self.rear] = ele
            
    def deQueue(self):
        if self._isEmpty(): 
            print('Queue is Empty!!')
            return
        
        else:
            ele = self.q[self.front]
            if self.front==self.rear:
                self.front = -1
                self.rear = -1
            
            else:
                self.front = (self.front + 1)%self.size
                
        return ele