def all_num(numbers):
    result = []
    for i in numbers:
        if "0" not in i:
            result.append(i)
    return result

numbers = ["1", "0", "3", "0"]
result = all_num(numbers)
print(result) 