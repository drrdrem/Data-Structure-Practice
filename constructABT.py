"""ABT Construction"""


import numpy as np

class construct():
    """Construction of ABT Chain.

    Args:
        inp (dict): BT structure

    """

    def __init__(self):
        self.dic = {} # Adjacency list of the chain
        self.stack = [] # Visited leaves
        self.M = 2 # Number of absorbing states

    def _recur(self, inp):
        """Recurssion help function.

        Args:
            inp (dict): BT structure
            * Valid operators:
              '?': Selecred Node
              '>': Sequential Node
              '~': Repeat until suceess node
        Returns:
            ele (list): indexes of leaves in the layer

        """
        if isinstance(inp, int): 
            self.dic[inp] = [0, 0]
            self.stack.append(inp)
            return [inp]
        
        if isinstance(inp, list):
            ele = []
            for node in inp:
                ele.append(min(self._recur(node)))
            return ele
                
        if isinstance(inp, dict):
            for node in inp:
                ele = self._recur(inp[node])
                idxs = range(len(ele[1:]))
                if node in ['?', '>', '~']:
                    # Selected node
                    if node == '?': 
                        for idx in idxs:
                            for leaf in range(ele[idx], ele[idx+1]):
                                if not self.dic[leaf][1]:
                                    self.dic[leaf][1] = ele[idx+1]
                    # Sequence node
                    if node == '>': 
                        for idx in idxs:
                            for leaf in range(ele[idx], ele[idx+1]):
                                if not self.dic[leaf][0]:
                                    self.dic[leaf][0] = ele[idx+1]
                    # Repeat until success node
                    # Warning: Repeat until success has not checked the functionality
                    if node == '~': 
                        for idx in idxs:
                            for leaf in range(ele[idx], ele[idx+1]):
                                if not self.dic[leaf][0]:
                                    self.dic[leaf][0] = ele[0]
                            for leaf in range(ele[idx+1], len(self.stack)):
                                if not self.dic[leaf][0]:
                                    self.dic[leaf][0] = ele[0]
                else:
                    raise ValueError(node)
                    
            return ele

    def con_chain(self, inp, M=2):
        """Construct the chain.

        Args:
            inp (dict): BT structure
            M (int): Number of absorbing states, default 2 (success, failure)
        Returns:
            dic (dict): an adjecency list representation of the ABT chain

        """
        self.stack = []
        self.M = M
        _ = self._recur(inp)
        
        n = len(self.stack)

        # 2 absorbing states (sucess, failure)
        if self.M==2:
            s = n+1 # Success node
            f = n+2 # Failure node

            for st in self.dic:
                if self.dic[st][0]==0: self.dic[st][0] = s
                if self.dic[st][1]==0: self.dic[st][1] = f

        # 1 absorbing state (end of the procedure)
        elif self.M == 1:
            e = n+1 # Success node

            for st in self.dic:
                if self.dic[st][0]==0: self.dic[st][0] = e
                if self.dic[st][1]==0: self.dic[st][1] = e

        else:
            pass

        return self.dic            
    
    def init_Amat(self, init=None):
        """Initialize A matrix.
        Args:
            init (int, list): user defined initial proberbility, default None
                              int: all assighned the same success prob.
                              list: assighned a prob. for each state
        Returns:
            A (np array): a random transition matrix of the chain

        """
        n = len(self.stack)
        A = np.zeros((n+self.M, n+self.M))

        # Default uniformly assighned prob.
        if not init:
            for row in self.dic:
                # Buffer node
                if self.dic[row][0]==self.dic[row][1]:
                    A[row-1, self.dic[row][0]-1] = 1
                else:
                    s = round(np.random.uniform(), 2)
                    A[row-1, self.dic[row][0]-1] = s
                    A[row-1, self.dic[row][1]-1] = 1 - s
        # all assighned the same success prob.
        elif isinstance(init, int):
            if init>0 and init<=1:
                for row in self.dic:
                    # Buffer node
                    if self.dic[row][0]==self.dic[row][1]:
                        A[row-1, self.dic[row][0]-1] = 1
                    else:
                        A[row-1, self.dic[row][0]-1] = init
                        A[row-1, self.dic[row][1]-1] = 1 - init
            else:
                raise ValueError(init)
        # assighned a success prob. for each state
        elif isinstance(init, list):
            if len(init)==n:
                for row, ini in zip(self.dic, init):
                    # Buffer node
                    if self.dic[row][0]==self.dic[row][1]:
                        A[row-1, self.dic[row][0]-1] = 1
                    else:
                        A[row-1, self.dic[row][0]-1] = ini
                        A[row-1, self.dic[row][1]-1] = 1 - ini
            else:
                raise ValueError(init)
        
        else:
            raise TypeError(init)


        # 2 absorbing states (sucess, failure)
        if self.M==2:
            A[-1, -1] = 1
            A[-2, -2] = 1
        # 1 absorbing state (end of the procedure)
        elif self.M == 1:
            A[-1, -1] = 1

        else:
            pass

        return A             


def test(inp, M=2):
    print('BT structure = ')
    print(inp)
    c = construct()
    print('\nConstruct Graph....')
    print('Graph = ')
    print(c.con_chain(inp, M))
    print('\nInitialize A matrix....')
    print(c.init_Amat())
    print('\n================================\n')


if __name__ == "__main__":
    print('Test 6 states ABT conversion: ')
    inp2 = [{'>':[{'>': [1, 2]}, {'?': [3, 4]}]}]
    test(inp2)
    
    print('Test 16 states ABT conversion: ')
    inp3 = {'>':[1, {'?':[{'>': [2, 3]}, {'>':[4, 5]}]}, 6, {'?':[{'>': [7, 8]}, {'>':[9, 10]}]}, 11, {'>':[12, 13, 14]}]}
    test(inp3)

    print('Test 1 absorbing state ABT conversion (test 1): ')
    inp = {'>':[1, {'?': [2, 3]}, 4, {'?': [5, 6]}]}
    test(inp, 1)

    print('Test 1 absorbing state ABT conversion (test 2): ')
    inp = {'>':[1, {'>':[{'?': [2, 3]}, 4]}, {'?': [5, 6]}]}
    test(inp, 1)
    
