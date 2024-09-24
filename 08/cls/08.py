#7 kyu Testing 1-2-3

def number(lines):
    result = []
    
    for index in range(len(lines)):
        word = str(index + 1) + ": " + lines[index]
        result.append(word)
    
    return result