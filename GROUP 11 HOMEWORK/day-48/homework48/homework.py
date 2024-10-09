# def sum_two_smallest_numbers(numbers):
#     sorted_list = sorted(numbers)
#     return sorted_list[0] + sorted_list[1]

# ჩვენ უნდა გამოგვეთვალა ორი უმცირესი ციფრის ჯამი ამისთვის დავალგეთ რიცხვები ზრდის მიხედვით და ორი უმცირესი რიცხვი შევკრიბეთ

# def max_multiple(divisor, bound):
#      if bound % divisor == 0:
#         return bound
    
#     multiples = []
    
#     for num in range(divisor, bound):
#         if num % divisor == 0:
#             multiples.append(num)
    
#     return max(multiples)





# def check_exam(arr1,arr2):
#     score = 0
    
#     for index in range(len(arr1)):
#         if arr1[index] == arr2[index]:
#             score = score + 4
#         elif arr2[index]  == "":
#             score = score + 0
#         else:
#             score = score - 1
    
#     if score < 0:
#         return 0
#     else:
#         return score





# def row_weights(array):
#     even_sum = 0
#     odd_sum = 0
#     for index in range(len(array)):
#         if index % 2 == 0:
#             even_sum = even_sum += array[index]
#         else:
#             odd_sum = odd_sum += array[index]
    
#     return (even_sum, odd_sum)