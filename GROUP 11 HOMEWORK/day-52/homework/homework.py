# def get_count(sentence):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     count = 0
#     for char in sentence:
#         if char in vowels:
#             count += 1
    
#     return count

# def descending_order(num):
#     digits = []
#     for i in str(num):  
#         digits.append(i)
#         digits.sort()
#         sorted_list = digits[::-1]
#         sorted_str = ''.join(sorted_list)
#     sorted_num = int(sorted_str)  
#     return sorted_num



# def filter_list(l):
#     filtered_list = []
#     for i in l:
#         if isinstance(i, int):
#             filtered_list.append(i)
#     return filtered_list


# def digital_root(n):
#     while n >= 10:
#         sum_of_digits = 0
#         while n > 0:
#             sum_of_digits += n % 10
#             n //= 10
#         n = sum_of_digits
#     return n