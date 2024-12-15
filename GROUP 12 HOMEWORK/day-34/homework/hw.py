def odd_or_even(arr):
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return "even"
    else:
        return "odd"


        def is_isogram(string):
    string = string.lower()
    seen = []
    for char in string:
        if char in seen:
            return False
        seen.append(char)
    return True

    def find_uniq(arr):
    arr.sort()
    
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[-1]


        def solution(number):
    result = []
    for i in range (1,number):
        if i % 3 ==0 or i % 5 ==0:
            result.append(i)
    return sum(result) 


    def points(games):
    score = 0 
    for game in games:
        x = int(game[0])
        y = int(game[2]) 
        if x > y:
            score += 3 
        elif x < y:
            score += 0  
        else:
            score += 1  
    return score