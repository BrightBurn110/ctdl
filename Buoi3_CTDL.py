### Create an array and traverse
# my_list = [1, 2, 3, 4, 5]
# print(my_list)

### Access individual elements through indexes
# my_list  = [1, 2, 3, 4, 5]
# print(my_list[1:2])
# print(my_list[1:4])
# print(my_list[0:3])

### Add items from list into array using fromlist() method
# my_list = [1, 2, 3, 4, 5]
# additional_elements = [6, 7, 8, 9, 10]
# my_list.extend(additional_elements)
# print("Danh sách sau khi thêm các phần tử từ danh sách mới:")
# print(my_list)

### Remove any array element using remove() method
# my_list = [1, 2, 3, 4, 5]
# print("Danh sách trước khi xóa:", my_list)
# my_list.remove()
# print("Danh sách sau khi xóa:", my_list)

### Remove last array element using pop() method
# my_list = [1, 2, 3, 4, 5]
# print("Danh sách trước khi xóa:", my_list)
# my_list.index()
# print("Danh sách sau khi xóa:", my_list)

###9.	Fetch any element through its index using index() method
# my_list = [1, 2, 3, 4, 5]
# element_at_index_2 = my_list.index(2)
# print(f"Phần tử tại chỉ số 2: {element_at_index_2}")

###10.	Reverse a python array using reverse() method
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print("Danh sách sau khi đảo ngược:")
# print(my_list)

###11.	Check for number of occurrences of an element using count() method
# my_list = [1, 2, 3, 4, 2, 5, 2]
# occurrences_of_2 = my_list.count(2)
# print(f"Số lần xuất hiện của phần tử có giá trị 2: {occurrences_of_2}")

# ###12.	Convert array to string using tostring() method
# my_list = ['Hello', 'World', '!']
# result_string = ' '.join(my_list)
# print("Chuỗi sau khi chuyển đổi từ danh sách:")
# print(result_string)

# ###13.	Slice element from an array
# danh_sach = [1, 2, 3, 4, 5]
# phần_tử_cắt = danh_sach[1:4]
# print("Phần tử đã cắt:", phần_tử_cắt)

###Question - 1
def foo(list):
    sum_result = 0
    product_result = 1
    
    for i in list:
        sum_result += i
    
    for i in list:
        product_result *= i
    
    print("Sum =", sum_result, ", Product =", product_result)

# Example usage
# my_list = [1, 2, 3, 4, 5]
# foo(my_list)

###Question - 2
def printPairs(list):
    for i in list:
        for j in list:
            print(str(i) + "," + str(j))

# Example usage
# my_list = [1, 2, 3, 4, 5]
# printPairs(my_list)

###Question - 3
def printUnorderedPairs(my_list):
    for i in range(0, len(my_list)):
        for j in range(i + 1, len(my_list)):
            print(str(my_list[i]) + "," + str(my_list[j]))

# Example usage with a list
# my_list = [1, 2, 3, 4, 5]
# printUnorderedPairs(my_list)

###Question - 4
def printUnorderedPairs(listA, listB):
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] < listB[j]:
                print(str(listA[i]) + "," + str(listB[j]))

# Example usage with lists
# my_listA = [1, 2, 3]
# my_listB = [2, 4, 6]
# printUnorderedPairs(my_listA, my_listB)

###Question - 5
def printUnorderedPairs(listA, listB):
    for itemA in listA:
        for itemB in listB:
            print(str(itemA) + "," + str(itemB))

# Example usage with lists
# my_listA = [1, 2, 3]
# my_listB = [4, 5, 6]
# printUnorderedPairs(my_listA, my_listB)

###Question - 6
def reverse(my_list):
    for i in range(0, int(len(my_list)/2)):
        other = len(my_list) - i - 1
        temp = my_list[i]
        my_list[i] = my_list[other]
        my_list[other] = temp
    print(my_list)

# Example usage with a list
# my_list = [1, 2, 3, 4, 5]
# reverse(my_list)

###Question - 8
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1

    result = 1
    factorials = [1]
    for i in range(1, n + 1):
        result *= i
        factorials.append(result)
    return factorials

# Example usage
# n = 5
# result_list = factorial(n)
# print(f"Factorials up to {n}:", result_list)

###Question - 9
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
def allFib(n):
    fibonacci_sequence = [fib(i) for i in range(n)]
    return fibonacci_sequence

# Example usage
# n = 5
# fibonacci_list = allFib(n)
# print(f"Fibonacci sequence up to {n}:", fibonacci_list)

###Question - 10
def powersOf2(n):
    if n < 1:
        return []
    elif n == 1:
        return [1]
    else:
        prev_powers = powersOf2(int(n/2))
        curr = prev_powers[-1] * 2
        return prev_powers + [curr]

# Example usage
# n = 5
# powers_list = powersOf2(n)
# print(f"Powers of 2 up to {n}:", powers_list)

def count_word_frequency(word_list):
    word_frequency = []

    for i in word_list:
        found = False
        for j in word_frequency:
            if j[0] == i:
                j[1] += 1
                found = True
                break
        if not found:
            word_frequency.append([i, 1])

    return word_frequency

# Example usage
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# result = count_word_frequency(words)

# # Convert the list of lists to a dictionary for better readability (optional)
# result_dict = dict(result)
# print(result_dict)


def merge_dicts(dict1, dict2):
    result_dict = dict1.copy()

    for i, j in dict2.items():
        if i in result_dict:
            result_dict[i] += j
        else:
            result_dict[i] = j

    return result_dict

# Example usage
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# result = merge_dicts(dict1, dict2)
# print(result)

a = [1,2,3]
a.extend('45')
print(a)
