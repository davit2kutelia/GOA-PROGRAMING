def double_integer(i):
    return i * 2

def abbrev_name(name):
    words = name.split()
    first_word = words[0][0].upper()
    second_word = words[1][0].upper()
    return f"{first_word}.{second_word}"



def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

def filter_list(l):
    filtered_list =[]
    for i in l:
        if type(i) == int:
            filtered_list.append(i)
    return filtered_list 


    def litres(time):
    return int(time * 0.5)