largest = None
print ('Before: ', largest)
for intervar in [3, 41, 12, 9, 74, 15] :
    if largest is None or intervar > largest :
        largest = intervar
    print ('Loop: ', intervar, largest)
print ('Largest is ', largest)
