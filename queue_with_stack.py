class queue_with_stack(object):
    def __init__(self):
        self.s1, self.s2 = [], []
        
    def enQueue(self, ele):
        self.s1.append(ele)
        
    def deQueue(self):
        if (not self.s1) and (not self.s2): 
            print("Queue is Empty!!")
            return
        
        if (not self.s2):
            while self.s1:
                self.s2.append(self.s1.pop())
                
        return self.s2.pop()