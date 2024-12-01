# def grow(arr):
#     result = 1
#     for num in arr:
#         result *= num
#     return result



# def count_positives_sum_negatives(arr):
#     if not arr:
#         return [0, 0]
    
#     positive = 0
#     negative = 0
    
#     for num in arr:
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += num
    
#     return [positive, negative]



# def paperwork(n, m):
#     if m<0 or n<0:
#         return 0
#     else:
#         return n*m