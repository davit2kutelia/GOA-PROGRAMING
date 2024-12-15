def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result



    def difference_in_ages(ages):
    oldest = max(ages)
    youngest = min(ages)
    diference = oldest - youngest
    return youngest, oldest, diference 



    def greet(name):
    greet = []
    name = input("enter name:")
    greet = (("hello")(name)(" how are you doing today?"))
    
    return greet

name = input("enter name:")