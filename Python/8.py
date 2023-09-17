# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"



import string

def ispangram(str1, alphabet=string.ascii_lowercase): 
    # Create a set of the alphabet
    alphaset = set(alphabet)  
    
    # Remove spaces from str1
    str1 = str1.replace(" ",'')
    
    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation 
    str1 = str1.lower()
    
    # Grab all unique letters in the string as a set
    str1 = set(str1)
    
    # Now check that the alpahbet set is same as string set
    return str1 == alphaset

ispangram("The quick brown fox jumps over the lazy dog")