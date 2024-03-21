### Create an array and traverse
# import array
# my_array = array.array('i')
# print(my_array)
# my_array1 = array.array('i', [1,2,3,4,5,6,7,8,9])
# print(my_array1)

### Access individual elements through indexes
# import array
# my_array = array.array('i', [1,2,3,4,5])
# print(my_array[0])
# print(my_array[2])
# print(my_array[-1])

### Append any value to the array using append() method
# import array
# my_array = array.array('i', [1,2,3,4,5])
# my_array.append(6)
# print(my_array)

### Insert value in an array using insert() method
# import array
# my_array = array.array('i', [1,2,3,4,5])
# my_array.insert(2, 8)
# print(my_array)

### Extend python array using extend() method
# import array
# my_array = array.array('i', [1,2,3,4,5])
# my_array.extend([6, 7])
# print(my_array)

### Add items from list into array using fromlist() method
# import array
# my_array = array.array('i')
# my_list = ([5, 10, 15, 20])
# my_array.fromlist(my_list)
# print(my_array)

### Remove any array element using remove() method
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# my_array.remove(6)
# print(my_array)

### Remove last array element using pop() method
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# my_array.pop()
# print(my_array)

### Fetch any element through its index using index() method
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# print(my_array.index(6, 0, 4))

### Reverse a python array using reverse() method
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# my_array.reverse()
# print(my_array)

### Get array buffer information through buffer_info() method
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# my_array1 = my_array.buffer_info()
# print(my_array1[0])
# print(my_array1[1])

### Check for number of occurrences of an element using count() method
# import array
# my_array = array.array('i', [9, 2, 4, 2, 9, 3, 9, 10, 5])
# print(my_array.count(9))

### Convert array to string using tostring() method
# import array
# my_array = array.array('i', [10, 20, 30, 40, 50])
# my_array1 = ", ".join(map(str, my_array))
# print(my_array1)

### Convert array to a python list with same elements using tolist() method
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# print(my_array.tolist())

### Append a string to char array using fromstring() method
# import array as arr
# string = "Hello, world!"
# char_array = arr.array('u', string)
# print(char_array)

### Slice element from an array
# import array
# my_array = array.array('i', [2, 4, 6, 8, 10])
# print(my_array[:2])


### Questions - 1
def foo(array):
    sum_result = 0
    product_result = 1    
    for i in array:
        sum_result += i
    for i in array:
        product_result *= i
    print("Sum = {}, Product = {}".format(sum_result, product_result))

# Example usage:
my_array = [1, 2, 3, 4, 5]
foo(my_array)

### Questions - 2
def printPairs(array):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"{array[i]}, {array[j]}")

# Example usage:
my_array = [1, 2, 3, 4, 5]
printPairs(my_array)

### Questions - 3
def printUnorderedPairs(array):
    if len(array) < 2:
        print("Array must contain at least two elements.")
        return

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            print(f"({array[i]}, {array[j]})")

# Example usage:
my_array = [1, 2, 3, 4]
printUnorderedPairs(my_array)

# Questions - 4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            print(f"({arrayA[i]}, {arrayB[j]})")

# Example usage:
arrayA = [1, 2, 3]
arrayB = ['a', 'b', 'c']
printUnorderedPairs(arrayA, arrayB)

### Questions - 5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        elementA = arrayA[i]
        for j in range(len(arrayB)):
            elementB = arrayB[j]
            for k in range(0, 100000):
                print(str(elementA) + "," + str(elementB))

# Sử dụng hàm
arrayA = [1, 2, 3]
arrayB = ['a', 'b', 'c']
printUnorderedPairs(arrayA, arrayB)
