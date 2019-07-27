smallest = None
print('Before', smallest)
for intervar in [3, 41, 12, 9, 74, 15] :
    if smallest is None or intervar < smallest :
        smallest = intervar
    print ('Loop:', intervar, smallest)
print ('Smallest is ', smallest)
