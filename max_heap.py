class max_heap(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0]*max_size
        self.Heap[0] = float('inf')
        
    def _parent(self, pos):
        return pos//2
    
    def _left_child(self, pos):
        return 2*pos
    
    def _right_child(self, pos):
        return (2*pos) + 1
    
    def _isLeaf(self, pos):
        if (pos>= self.size/2) and (pos<=self.size):
            return True
        return False
    
    def _max_heapify(self, pos):
        if self._isLeaf(pos): return
        if (self.Heap[pos]<self.Heap[self._left_child(pos)]) or (self.Heap[pos]<self.Heap[self._right_child]):
            if self.Heap[self._left_child(pos)]>self.Heap[self._right_child(pos)]:
                self.Heap[pos], self.Heap[self._left_child(pos)] = self.Heap[self._left_child(pos)], self.Heap[pos]
                self._max_heapify(self._left_child(pos))
            else:
                self.Heap[pos], self.Heap[self._right_child(pos)] = self.Heap[self._right_child(pos)], self.Heap[pos]
                self._max_heapify(self._right_child(pos))
                
    def insert(self, ele):
        self.size+=1
        self.Heap[self.size] = ele
        cur = self.size
        while self.Heap[cur]>self.Heap[self._parent(cur)]:
            self.Heap[cur], self.Heap[self._parent(cur)] = self.Heap[self._parent(cur)], self.Heap[cur]
            cur = self._parent(cur)
    def pop(self):
        popped = self.Heap[1]
        self.Heap[1] = self.Heap[-1]
        self._max_heapify(1)
        return popped

    def front(self):
        return self.Heap[1]