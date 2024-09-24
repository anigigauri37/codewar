#7 kyu Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    min_number = min(a,b)
    max_number = max(a,b)
    
    sum = 0
    
    for num in range(min_number, max_number + 1):
        sum = sum + num
    
    return sum