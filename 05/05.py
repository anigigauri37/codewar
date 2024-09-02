#Vowel Count 7kyu

def get_count(sentence):
    number_vowels = 0
    vowels = "aeiou"
    for i in sentence:
        if i in vowels:
            number_vowels += 1
    return number_vowels
        

