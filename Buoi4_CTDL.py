# Reversing an array in-place exercise
# def reverse_array_in_place(arr):
#     start_index = 0
#     end_index = len(arr) - 1

#     while start_index < end_index:
#         arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
#         start_index += 1
#         end_index -= 1

# # Ex
# my_array = [1, 2, 3, 4, 5]
# print("Mảng trước khi đảo chiều: ", my_array)
# reverse_array_in_place(my_array)
# print("Mảng sau khi đảo chiều: ", my_array)

# Palindrome exercise
# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     start = 0
#     end = len(s) - 1

#     while start < end:
#         if s[start] != s[end]:
#             return False
#         start += 1
#         end -= 1

#     return True
# # EX
# print(is_palindrome("rar"))
# print(is_palindrome("hello"))

# Integer reversion exercise
# def reverse_int(num):
#     reversed_num = 0

#     while num > 0:
#         x = num % 10
#         reversed_num = (reversed_num * 10) + x
#         num //= 10
#     return reversed_num

# #Ex
# num = 123456
# print("Số trước khi đảo ngược: ", num)
# reversed_num = reverse_int(num)
# print("Số sau khi đảo ngược: ", reversed_num)

# Anagram problem exercise
def are_anagram(word_1, word_2):
    word_1 = word_1.lower().replace(" ", "")
    word_2 = word_2.lower().replace(" ", "")
    return sorted(word_1) == sorted(word_2)
    
word_1 = "viet nam"
word_2 = "nam viet"
ketqua = are_anagram(word_1, word_2)

if ketqua:
    print(f"{word_1} and {word_2} are anagram")
else:
    print(f"{word_1} and {word_2} are not anagram")