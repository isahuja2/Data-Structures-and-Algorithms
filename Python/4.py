# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(numbrs):
    total = 0
    add = True
    
    for n in numbrs:
        while add:
            if n != 6:
                total += n
                break
            else:
                add = False
            
        while not add:
            if n != 9:
                add = False
                break
            else:
                add = True
                break

    print(total)

summer_69([2, 1, 6, 9, 11])
