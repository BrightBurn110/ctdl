# class Stack:
#     def __init__(self):
#         self.list = []
    
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)
    
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
    
#     def push(self, value):
#         self.list.append(value)
#         return "The element has been successfully inserted"
    
#     def pop(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             return self.list.pop()
        
#     def peek (self):
#         if self.isEmpty:
#             return "There is not any element in the stack"
#         else:
#             return self.list[len(self.list) - 1]
    
#     def delete(self):
#         self.list = None 
# ###
# # customStack = Stack()
# # print(customStack.isEmpty())

# ###
# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# # print(customStack)
# # print(customStack.pop())
# print(customStack.peek())
# print(customStack)

###
# class Stack:
#     def __init__(self, maxSize):
#         self.maxSize = maxSize
#         self.list = []
    
#     def __str__(self):
#         value = self.list.reverse()
#         value = [str(x) for x in self.list]
#         return '\n'.join(value)
    
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
        
#     def isFull(self):
#         if len(self.list) == self.maxSize:
#             return True
#         else:
#             return False
    
#     def push(self, value):
#         if self.isFull():
#             return "The stack is full"
#         else:
#             self.list.append(value)
#             return "The element has been successfully inserted"
    
#     def pop(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             return self.list.pop()
        
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             return self.list[len(self.list) - 1]
       
#     def delete(self):
#         self.list = None
         
# customStack = Stack(4)
# print(customStack.isEmpty())
# print(customStack.isFull())
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False 

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)