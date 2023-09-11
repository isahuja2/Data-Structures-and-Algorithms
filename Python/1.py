# Given a list of ints, return True if the array contains 3 next to a 3 somewhere

# has_33([1,3,3]) -> True
# has_33([1,3,1,3]) -> false
# has_33([3,1,3]) -> false


def has_33(inputArray):
    for i in range(0, len(inputArray) - 1):  #Did not include last digit because there is no next digit to compare
        if inputArray[i] == 3 and inputArray[i+1] == 3: 
        # More optimized, [i:i+2] == [3,3]
        #if inputArray[i:i+2] == [3,3]: 
            return True
    return False


# More optimized, [i:i+2] == [3,3]
def has_threethree(inputArray):
    for i in range(0, len(inputArray) - 1):  #Did not include last digit because there is no next digit to compare
        if inputArray[i:i+2] == [3,3]: 
            return True
    return False

print(has_33([1,3,3]))
print(has_threethree([1,3,3]))