# Given a string, return a string where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result = ''
    for char in text:
        result += char*3 #char+char+char
    return result

print(paper_doll('Hello'))