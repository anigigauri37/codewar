#8 kyu Find the Difference in Age between Oldest and Youngest Family Members

def difference_in_ages(ages):
    youngest = min(ages)
    oldest = max(ages)
    difference = oldest - youngest
    return (youngest, oldest,  difference)