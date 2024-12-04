def find_average(numbers):
    if not numbers:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average


    def count_by(x, n):
        multied = []  
    
    for i in range(1, n + 1):  
        multiple = x * i  
        multied.append(multiple) 
    
    return multied 

    def positive_sum(arr):
    total = 0
    
    for num in arr:
        if num > 0:
            total += num
    
    return total


    def get_count(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    
    return count




    def find_smallest_int(arr):
    return min(arr)