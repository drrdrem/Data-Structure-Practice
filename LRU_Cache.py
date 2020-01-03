from collections import deque
class LRU_Cache(object):
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.q = deque()
        self.dic = {}
        
    def _isFull(self):
        return len(self.q) == self.cache_size
    
    def set(self, k, val):
        if k not in self.dic:
            if self._isFull():
                popped = self.q.pop()
                self.dic.pop(popped)
                self.q.appendleft(k)
                self.dic[k] = val
            else:
                self.q.appendleft(k)
                self.dic[k] = val
                
    def get(self, k):
        if k not in self.dic: return -1
        else: 
            self.q.remove(k)
            self.q.appendleft(k)
            return self.dic[k]