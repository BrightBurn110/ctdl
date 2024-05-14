# ### Bai 1
# def max_in_window(num_list, k=3):
#     if not num_list:
#         return []

#     result = []
#     window = []

#     for i in range(len(num_list)):
#         if i >= k and window[0] <= i - k:
#             window.pop(0)
#         while window and num_list[i] >= num_list[window[-1]]:
#             window.pop()
#         window.append(i)
#         if i >= k - 1:
#             result.append(num_list[window[0]])

#     return result

# #Ex
# num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
# k = 3
# print(max_in_window(num_list, k))

### Bai 2
# def intersection(nums1, nums2):
#     num_count = {}
#     intersection_list = []
#     for num in nums1:
#         num_count[num] = num_count.get(num, 0) + 1
#     for num in nums2:
#         if num in num_count and num_count[num] > 0:
#             intersection_list.append(num)
#             num_count[num] -= 1

#     return intersection_list

# #Ex
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# print(intersection(nums1, nums2))

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
# print(intersection(nums1, nums2))

### BAi 3
# def count_chars(word):
#     char_count = {}
    
#     for char in word:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     return char_count

# # Test cases
# string = 'QuangKhai'
# print(count_chars(string))

# string = 'N20DCAT029'
# print(count_chars(string))

### Bai 4
def word_count(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                word = ''.join(char for char in word if char.isalpha())
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

file_path = 'D:\CTDL\TH_Buoi2.txt'
print(word_count(file_path))


