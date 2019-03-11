"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        if root.children == []:
            return str(root.val) + ',' + str(0)
        else:
            s = str(root.val) +','+ str(len(root.children)) + ','
            for i in root.children:
                s += self.serialize(i) + ','
            s = s[:-1]
        return s

    def deserializeHelper(self, lst):
        root = Node(lst[0], [])
        size = lst[1]
        del lst[0]
        del lst[0]
        for i in range(size):
            root.children.append(self.deserializeHelper(lst))
        return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        lst = data.split(",")
        lst = [int(i) for i in lst]
        return self.deserializeHelper(lst)
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Credits: leetcode
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        arr = []
        
        def traverse(node):
            if node:
                arr.append(str(node.val))
                for c in node.children:
                    traverse(c)
                arr.append('#')
            
        traverse(root)
        return ' '.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return
        token = collections.deque(data.split())
        
        
        def helper(token):
            root = Node(int(token.popleft()), [])
            while token[0]!='#':
                root.children.append(helper(token))
            token.popleft()
            return root
            
            
        return helper(token)