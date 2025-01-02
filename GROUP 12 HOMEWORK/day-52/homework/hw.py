def cakes(recipe, available):
    max_cakes = float('inf')
    
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        
        required_amount = recipe[ingredient]
        available_amount = available[ingredient]
        
        if available_amount < required_amount:
            return 0
        
        cakes_possible = available_amount // required_amount
        
        if cakes_possible < max_cakes:
            max_cakes = cakes_possible
    
    return max_cakes




def solution(s):
    result = ''
    for i in s:
        if i.isupper() and result:
            result += ' ' + i
        else:
            result += i
    return result