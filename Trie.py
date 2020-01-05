class TreeNode(object):
    def __init__(self):
        self.isWord = False
        self.children={}
        
class Trie(object):
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.isWord = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isWord
    
    def startWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True