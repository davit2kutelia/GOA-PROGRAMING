# def fake_bin(x):
#     result = "" 
#     for i in x:
#         if int(i) < 5:
#             result += '0'
#         else:
#             result += '1'
#     return result


#     def points(games):
#     score = 0 
#     for game in games:
#         x = int(game[0])
#         y = int(game[2]) 
#         if x > y:
#             score += 3 
#         elif x < y:
#             score += 0  
#         else:
#             score += 1  
#     return score






def flick_switch(lst):
    result = []  
    current_bool = True  
    for i in lst:
        if i == 'flick':  
            current_bool = not current_bool 
        result.append(current_bool)  
    return result