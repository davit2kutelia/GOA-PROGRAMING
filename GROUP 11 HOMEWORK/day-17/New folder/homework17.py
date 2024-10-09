def sum(numbers):
   
    total = 0
    for num in numbers:
        total += num
    return total


numbers = [1, 2, 3, 4, 5]
print("Sum of numbers in the list:", sum(numbers))