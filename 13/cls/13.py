#6 kyu Replace With Alphabet Position

def alphabet_position(text):
    result = []
    for i in text.lower():
        if i.isalpha(): 
            position = ord(i) - ord('a') + 1 
            result.append(str(position))
    return " ".join(result)


print(alphabet_position("The sunset sets at twelve o' clock."))