def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False



def square_sum(numbers):
    result = 0
    for i in numbers:
        result += i**2 
    return result


def spin_words(sentence):
    result = []
    words = sentence.split()
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)



    def move_zeros(lst):
    non_zeros = []
    zeros = []
    
    for i in lst:
        if i != 0:
            non_zeros.append(i)
        else:
            zeros.append(i)
            
    return non_zeros + zeros