#6 kyu Mexican Wave

def wave(people):
    result = []
    
    for i in range(len(people)):
        if people[i] != " ":
            word = people[0:i] + people[i].upper() + people[i + 1:]
            result.append(word)
    
    return result