def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)



def draw_stairs(n):
    result = ""
    for i in range(n):
        result += ' ' * i + 'I' + '\n'
    return result.strip()