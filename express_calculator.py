class express_tree(object):
    def __init__(self, char):
        self.val = char
        self.left = None
        self.right = None

def priority(operator):
    return 1 if operator in "+-" else 2 if operator in "*/" else 0

def infix2postfix(infix, postfix=True):
    _2stack, _2output = ('(', ')') if postfix else (')', '(')
    
    def _check_priority(char, stack, output):
        if stack == "" or priority(stack[-1]) < priority(char):
            return (stack + char, output)
        else:
            return _check_priority(char, stack[0:-1], output + stack[-1])
        
    def _check_2stack(stack, output):
        if stack[-1] ==  _2stack: return (stack[0:-1], output)
        else: return _check_2stack(stack[0:-1], output + stack[-1])
        
    def _2postfix(expr, stack = "", output = ""):
        if expr == "": return output + stack[::-1]
        elif expr[0] == _2stack: return _2postfix(expr[1:], stack + expr[0], output)
        elif expr[0] in "+-*/": return _2postfix(expr[1:], *_check_priority(expr[0], stack, output))
        elif expr[0] == _2output: return _2postfix(expr[1:], *_check_2stack(stack, output))
        else: return _2postfix(expr[1:], stack, output + expr[0])
    
    output = _2postfix(infix if postfix else infix[::-1])
    
    return output if postfix else output[::-1]

def isOperator(char):
    if char in '+-*/':return True
    else: return False
        
def construct_tree(postfix):
    stack = []
    for char in postfix:
        if not isOperator(char): 
            root = express_tree(char)
            stack.append(root)
        else:
            root = express_tree(char)
            r_child = stack.pop()
            l_child = stack.pop()
            
            root.right = r_child
            root.left = l_child
            
            stack.append(root)
                
    return stack.pop()

def evaluation_express_tree(root):
    if not root: return 0
    if not root.left and not root.right: return int(root.val) # Value is always the leaf
    
    l_sum = evaluation_express_tree(root.left)
    r_sum = evaluation_express_tree(root.right)
    
    if root.val == '+': return l_sum + r_sum
    if root.val == '-': return l_sum - r_sum
    if root.val == '*': return l_sum*r_sum
    if root.val == '/': return l_sum / r_sum
    
def calculator(infix):
    
    postfix = infix2postfix(infix)
    root = construct_tree(postfix)
    res = evaluation_express_tree(root)
    
    return res

if __name__ == "__main__":
    """
    Input type: infix sequence
    output: calculated result
    """
    calculator("(5-3)*2")