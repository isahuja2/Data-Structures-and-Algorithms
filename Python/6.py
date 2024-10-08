# Write a function that takes in a list of integers and returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
# spy_game([0,0,7,0]) --> False
# spy_game([0,7,0,7]) --> False


# My Solution
def spy_game(nums):

    state = ''

    for n in nums:

        if n == 0:
            if state == 'zero':
                state = 'doublezero'
            else:
                state = 'zero'
        elif n == 7:
            if state == 'doublezero':
                return True
            
    return False



# Solution from authors
# def spy_game(nums):

#     code = [0,0,7,'x']
    
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
       
#     return len(code) == 1




# Solution Form Instructor
# def spy_game(nums):
    
#     return any(num == 7 and nums[:i].count(0) > 1 for i,num in enumerate(nums))


# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))
# print(spy_game([0,0,7,0]))
print(spy_game([0,7,0,7]))