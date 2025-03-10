def cat_mouse(x):
    x = x.lower()
    cat_pos = x.index('c')
    mouse_pos = x.index('m')
    distance = mouse_pos - cat_pos
    
    if distance <= 4:
        return "Caught!"
    else:
        return "Escaped!"
    