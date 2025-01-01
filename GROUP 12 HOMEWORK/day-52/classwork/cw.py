def create_array_of_tiers(n):
    num_str = str(n)  
    result = []  
    for i in range(len(num_str)):  
        result.append(num_str[:i+1])
    return result



def min_max(lst):
    return [min(lst), max(lst)] 




