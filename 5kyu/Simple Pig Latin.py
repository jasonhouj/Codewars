'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
'''
# pig_it('Pig latin is cool') >> igPay atinlay siay oolcay
# pig_it('Hello world !')     >> elloHay orldway !

# ----start of solution----

# My solution
def pig_it(text):
    text = text.split()
    result = []
    punctuation = "!@#$%^&*()_+<>?:.,;"
    for x in text:
        if x not in punctuation:
            first_letter = x[0]
            x = x.replace(x[0], '', 1) + first_letter + "ay"
            result.append(x)
        else:
            result.append(x)
    return ' '.join(result)


# Best Solution

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


# Second Best Solution

def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)

# Solution with import re

import re

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)
