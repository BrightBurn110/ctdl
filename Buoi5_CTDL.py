### define a function to count the frequency of words in a given list of words
# def count_word_frequency(words):
#     word_freq = {}

#     for word in words:
#         if word in word_freq:
#             word_freq[word] = word_freq[word] + 1 
#         else:
#             word_freq[word] = 1

#     return word_freq

# #EX
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# result = count_word_frequency(words)
# print(result)

###2.	Define a function with takes two dictionaties as parameters and merge them and sum the values of common keys.
# def merge_and_sum(dict1, dict2):
#     merged_dict = {}

#     for key in dict1:
#         if key in dict2:
#             merged_dict[key] = dict1[key] + dict2[key]
#         else:
#             merged_dict[key] = dict1[key]
    
#     for key in dict2:
#         if key not in merged_dict:
#             merged_dict[key] = dict2[key]

#     return merged_dict

# #Ex
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# print(merge_and_sum(dict1, dict2))

###3.	Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
# def max_value_key(my_dict):
#     if not my_dict:
#         return None
    
#     max_value = max(my_dict.values())  # Tìm giá trị lớn nhất trong từ điển
#     for key, value in my_dict.items():
#         if value == max_value:
#             return key
        
# #Ex
# ex_dict = {'a': 5, 'b': 9, 'c': 2}
# print(max_value_key(ex_dict))

###4.	Define a function which takes as a parameter dictionary and returns a dictionary in which reverse the key-value pairs are reversed.
# def reverse_dict(my_dict):
#     reversed_dict = {}
#     for key, value in my_dict.items():
#         reversed_dict[value] = key
    
#     return reversed_dict

# #Ex
# ex_dict = {'a': 1,'b': 2,'c': 3}
# print(reverse_dict(ex_dict))

###5.	Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.
# def filter_dict(mydict, condition):
#     filtered_dict = {}
    
#     for key, value in mydict.items():
#         if condition(key, value):
#             filtered_dict[key] = value
#     return filtered_dict

# def is_even(key, value):
#     return value % 2 == 0

# #Ex
# ex_dict = {'a': 1, 'b': 2,'c': 3,'d': 4}
# print(filter_dict(ex_dict, is_even))

###6.	Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.
# def same_frequency(list1, list2):
#     if len(list1) != len(list2):
#         return False
    
#     freq_map1 = {}
#     freq_map2 = {}
    
#     for item in list1:
#         if item in list1:
#             freq_map1[item] = freq_map1.get(item, 0) + 1
#         else:
#             freq_map1[item] = 1
    
#     for item in list2:
#         if item in list2:
#             freq_map2[item] = freq_map2.get(item, 0) + 1
#         else:
#             freq_map2[item] = 1
    
#     return freq_map1 == freq_map2

# #Ex
# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# list3 = [1, 2, 3, 4, 5]
# list4 = [5, 4, 3, 2, 1]
# print(same_frequency(list1, list2))
# print(same_frequency(list3, list4))

### Tuple
# newTuple = ('a', 'b', 'c', 'd', 'e')
# newTuple1 = tuple('abcde')
# print(newTuple)
# print("New Tuple 1: ", newTuple1)
# print(newTuple[1])
# print(newTuple[-1])
# print(newTuple[-2])
# print(newTuple[1:3])
# print(newTuple[:3])
# print(newTuple[1:])
# print(newTuple[:])

# for i in newTuple:
#     print(i)

# for i in range(len(newTuple)):
#     print(newTuple[i])
    
# print('a' in newTuple)
# print(newTuple.index('c'))

# def seachTuple(p_tuple, element):
#     for i in range(0, len(p_tuple)):
#         if p_tuple[i] == element:
#             return f"The {element} is found at {i} index"
#     return 'The element is not found'
# print(seachTuple(newTuple, 'b'))

# myTuple = (1, 4, 3, 2, 5, 2)
# myTuple1 = (1, 2, 6, 9, 8, 7)
# print(myTuple + myTuple1)
# print(myTuple * 4)
# print(myTuple.count(2))
# print(tuple([1, 2, 3, 4]))

###8.	Write a function that calculates the sum and product of all elements in a tuple of numbers.
# def sum_and_product(numbers):
#     if not numbers:
#         return 0, 1
    
#     total_sum = sum(numbers)
#     total_product = 1
    
#     for num in numbers:
#         total_product *= num
#     return total_sum, total_product

# #Ex
# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_and_product(input_tuple)
# print("Sum:", sum_result)
# print("Product:", product_result)

###9.	Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
# def element_wise_sum(tuple1, tuple2):
#     result = tuple(x + y for x, y in zip(tuple1,tuple2))
#     return result

# #Ex
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# print(element_wise_sum(tuple1, tuple2))

###10.	Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
# def insert_value(ori, value):
#     newTuple = (value,) + ori
#     return newTuple

# #Ex
# ori = (2, 3, 4)
# value_to_insert = 1
# print(insert_value(ori, value_to_insert))

###11.	Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
# def concatenate_strings(tuple):
#     concatenated_string = ' '.join(tuple)
#     return concatenated_string

# #Ex
# string_tuple = ('Hello', 'World', 'from', 'Python')
# print(concatenate_strings(string_tuple))

###12.  Create a fnction that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
# def get_diagonal_ele(tuple):
#     diagonal_ele = [tuple[i][i] for i in range(min(len(tuple), len(tuple[0])))]
#     return diagonal_ele

# #Ex
# input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print(get_diagonal_ele(input_tuple))

###13.	Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
# def common_ele(tuple1, tuple2):
#     common = tuple(set(tuple1) & set(tuple2))
#     return common

# #Ex
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_ele(tuple1, tuple2)
# print(output_tuple)

###     OPP
# class StarCookie:
#     pass

# star_cookie1 = StarCookie()
# star_cookie1.weight = 15
# star_cookie1.color = "Red"
# print(star_cookie1.weight)
# print(star_cookie1.color)

# star_cookie2 = StarCookie()
# star_cookie2.weight = 16
# star_cookie2.color = "Blue"
# print(star_cookie2.weight)
# print(star_cookie2.color)

### Phương thức khởi tạo
# class StarCookie:
#     def __init__(self, color, weight):
#         self.color = color
#         self.weight = weight
        
# star_cookie1 = StarCookie("Red", 16)
# print(star_cookie1.color)
# print(star_cookie1.weight)

# class Youtube:
#     def __init__(self, username, subscribers):
#         self.usetname = username
#         self.subscribers = subscribers

# user1 = Youtube("Khai", 1903)
# print(user1.usetname)
# print(user1.subscribers)

# user2 = Youtube("QuangKhai", 2210)
# print(user2.usetname)
# print(user2.subscribers)

###     ClassMethods
# class Youtube:
#     def __init__(self, username, subscribers = 0, subscriptions = 0):
#         self.username = username
#         self.subscribers = subscribers
#         self.subscriptions = subscriptions
        
#         def subscribe(self, user):
#             user.subscribers += 1
#             self.subscriptions += 1
            
# user1 = Youtube("Elshas")
# user2 = Youtube("Rena")
# user1.subscribers(user2)
# user2.subscribers(user1)
# print(f"User 1 subscribers: {user1.subscribers}")
# print(f"User 1 subscriptions: {user1.subscriptions}")
# print(f"User 2 subscribers: {user2.subscribers}")
# print(f"User 2 subscriptions: {user2.subscriptions}")

###     LinkesList
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def append(self, value):
#         new_node = Node(value)
#         self.tail.next = new_node
#         self.tail = new_node
#         self.length += 1

#     def prepend(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#         self.length += 1

#     def print_list(self):
#         current = self.head
#         while current is not None:
#             print(current.value, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage
# linked_list = LinkedList(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.prepend(0)

# linked_list.print_list()

# class Node:
#   def __init__(self, value):
#       self.value = value
#       self.next = None

# class LinkedList:
#   def __init__(self):
#       self.head = None  

#   def insert_at_beginning(self, value):
#       new_node = Node(value)
#       new_node.next = self.head
#       self.head = new_node

#   def print_list(self):
#       current = self.head
#       while current:
#           print(current.value, end=" -> ")
#           current = current.next
#       print("None")

# # Example usage
# linked_list = LinkedList()
# linked_list.insert_at_beginning(3)
# linked_list.insert_at_beginning(2)
# linked_list.insert_at_beginning(1)

# linked_list.print_list()
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.value, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage
# linked_list = LinkedList()
# linked_list.insert_at_end("VuQuangKhai")
# linked_list.insert_at_end("N20DCAT029")

# linked_list.print_list()
class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def insert_at_end(self, value):
      new_node = Node(value)
      if self.head is None:
          self.head = new_node
          return
      current = self.head
      while current.next is not None:
          current = current.next
      current.next = new_node

  def delete_node_at_index(self, index):
      if index < 0:
          raise ValueError("Chỉ số không phải số âm")
      if index == 0:
          if self.head is None:
              raise ValueError("Danh sách rỗng")
          deleted_node = self.head
          self.head = self.head.next
          deleted_node.next = None
          return deleted_node

      prev = None
      current = self.head
      count = 0
      while current is not None and count < index:
          prev = current
          current = current.next
          count += 1
      if current is None:
          raise ValueError("Chỉ số vượt quá giới hạn")
      deleted_node = current
      prev.next = current.next
      deleted_node.next = None
      return deleted_node

  def print_list(self):
      current = self.head
      while current:
          print(current.value, end=" -> ")
          current = current.next
      print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)

deleted_node = linked_list.delete_node_at_index(6)
print("Deleted node:", deleted_node.value)

linked_list.print_list()

