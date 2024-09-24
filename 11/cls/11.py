#5 kyu Simple Pig Latin

def pig_it(text):
    words = []
    for word in text.split(" "):
        if word.isalpha():
            words.append(word[1:] + word[0] + "ay")
        else:
            words.append(word)
            
    return " ".join(words)