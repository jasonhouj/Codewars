'''Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

'''

# "john McClane" --> "McClane john"


# ---start-of-solution---

def name_shuffler(str_):
    str_ = str_.split()
    str_.reverse()
    return(' '.join(str_))