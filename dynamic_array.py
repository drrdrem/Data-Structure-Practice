import ctypes
# Codes modified from: https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/
class dynamic_array(object):
    def __init__(self, capacity=1):
        self.n_ele = 0
        self.capacity = capacity
        self.d_a = self._make_array(self.capacity)
        
    def __len__(self):
        return self.n_ele
    
    def __getitem__(self, idx):
        if not 0<=idx<=self.n_ele:
            return IndexError("Index out of range!!!")
        return self.d_a[idx]
    
    def _make_array(self, size):
        return (size*ctypes.py_object)()
    
    def _resize(self, extend_size):
        d_a_ = self._make_array(extend_size)
        for idx in range(self.n_ele):
            d_a_[idx] = self.d_a[idx]
            
        self.d_a = d_a_
        self.capacity = extend_size
    
    def append(self, ele):
        if self.n_ele==self.capacity:
            self._resize(2*self.capacity)