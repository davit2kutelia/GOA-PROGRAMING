# def xo(s):
#     s = s.lower()
#     x = s.count("x")
#     o = s.count("o")
#     return x == o


# def longest_palindrome(s: str) -> int:
#     def expand_around_center(left: int, right: int) -> int:
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return right - left - 1

#     if not s:
#         return 0

#     max_length = 0

#     for i in range(len(s)):
#         len1 = expand_around_center(i, i)     
#         len2 = expand_around_center(i, i + 1) 
#         max_length = max(max_length, len1, len2)

#     return max_length



# def sort_array(source_array):
#     odds = []
#     for num in source_array:
#         if num % 2 != 0:
#             odds.append(num)
    
#     odds.sort()
    
#     result = []
#     odd_index = 0
#     for num in source_array:
#         if num % 2 != 0:
#             result.append(odds[odd_index])
#             odd_index += 1
#         else:
#             result.append(num)
    
#     return result



# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
#     x = 0
#     y = 0
#     for direction in walk:
#         if direction == 'n':
#             y += 1
#         elif direction == 's':
#             y -= 1
#         elif direction == 'e':
#             x += 1
#         elif direction == 'w':
#             x -= 1

#     return (x == 0 and y == 0)




# def binary_to_string(binary):
#     if binary == "":
#         return ""
    
#     result = ""
    
#     for i in range(0, len(binary), 8):
#         byte = binary[i:i+8]
#         decimal_value = int(byte, 2)
#         character = chr(decimal_value)
#         result += character
    
#     return result