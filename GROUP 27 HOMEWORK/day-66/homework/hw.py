def func(list):
    unique_list = []
    for num in (list):
        if list.count(num) == 1:
            unique_list.append(num)

    
    return unique_list


list = [1,2,1,3,4,1,2,3,4,1,44,6,7,2]
result = func(list)
print(result)
        

