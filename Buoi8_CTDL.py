### Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

### Insert
    def insert(self, value):
        # return Node(value)
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        # return False
        else:
            temp = self.root
            while temp:
                if value == temp.value:
                    return False
                elif value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else: 
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right
### Contains
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

bst = BinarySearchTree()
bst.insert(19)
bst.insert(3)
bst.insert(22)
bst.insert(10)
print("Contains 15:", bst.contains(15))
print("Contains 19:", bst.contains(19))