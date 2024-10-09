# 1

# def filter_multiples_of_4(numbers):

#     filtered_numbers = []
#     for i in numbers:
      
#         if i % 4 == 0:
#             filtered_numbers.append(i)
#     return filtered_numbers


# numbers = (range(1, 21))
# filtered_numbers = filter_multiples_of_4(numbers)
# print("Filtered list:", filtered_numbers)

#2
# def list(first_name, last_name):
  
#     user_names = [first_name, last_name]
#     return user_names


# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# result =(first_name  +  last_name)
# print( result)




#3

# def filter_arr(start_num,end_num):
#     numbers = []
#     filtered_list = []

#     for i in range(start_num,end_num):
#         numbers.append(i)
#         return numbers
       

#         for i in numbers:
#             if i % 2 == 0:
#                 filtered_list.append(i ** 2)
#             else:
#                 filtered_list.append(i ** 0,5)

#     return filtered_list
        
# start_num =int(input("please enter  first number:"))
# end_num= int(input("please enter second number:"))

# result_list = filter_arr(start_num,end_num)
# print(result_list)



#4

# def even_indexes(lastname):
#     char_list = []
#     even_index_chars = []

    
#     for char in lastname:
#         char_list.append(char)

#     for index in range(len(char_list)):
#         if index % 2 == 0:
#             even_index_chars.append(char_list[index])
#     print(even_index_chars)


# lastname = input("enter lastname:")

# even_indexes(lastname)


#5

# def reverseword(word):
#     return word[::-1]


# word=input("please enter word:")
# print(word)


#6
# dups= [10,10,8,8,13,13]
# dup_set = set(dups)
# dups = list(dup_set)
# print(dups)