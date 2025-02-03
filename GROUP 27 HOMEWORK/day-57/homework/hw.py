def area_or_perimeter(l , w):
    if l == w:
        return l*w
    else:
        return l*2 + w*2

def string_to_array(s):
    if s == "":
        return [""]
    else:
        result = s.split()
    return result