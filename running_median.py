import heapq
class running_median(object):
    def __init__(self):
        self.max_h, self.min_h= [], []
        
    def running_median(self, ele):
        if not self.max_h and not self.min_h:
            heapq.heappush(self.max_h, -ele)
            return float(ele)

        elif self.max_h:
            if ele>=-self.max_h[0]:
                heapq.heappush(self.min_h, ele)
            else:
                heapq.heappush(self.max_h, -ele)

            if len(self.max_h)==len(self.min_h): return float((-self.max_h[0]+self.min_h[0])/2)

            elif len(self.max_h)==len(self.min_h)+1: return float(-self.max_h[0])

            elif len(self.min_h)==len(self.max_h)+1: return float(self.min_h[0])

            elif len(self.min_h)==len(self.max_h)+2:
                heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
                return float((-self.max_h[0]+self.min_h[0])/2)

            elif len(self.max_h)==len(self.min_h)+2:
                heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
                return float((-self.max_h[0]+self.min_h[0])/2)