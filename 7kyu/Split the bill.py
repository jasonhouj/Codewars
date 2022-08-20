'''It's tricky keeping track of who is owed what when spending money in a group. Write a function to balance the books.

The function should take one parameter: an object/dict with two or more name-value pairs which represent the members of the group and the amount spent by each.
The function should return an object/dict with the same names, showing how much money the members should pay or receive.
Further points:

The values should be positive numbers if the person should receive money from the group, negative numbers if they owe money to the group.
If value is a decimal, round to two decimal places.
Translations and comments (and upvotes!) welcome.

Example
3 friends go out together: A spends £20, B spends £15, and C spends £10. The function should return an object/dict showing that A should receive £5, B should receive £0, and C should pay £5.
'''
# group = {
#     'A': 20, 
#     'B': 15, 
#     'C': 10
# }

# split_the_bill(group) # returns {'A': 5, 'B': 0, 'C': -5}



# ----start of solution----

def split_the_bill(x):
    dict_list = []
    group = {}
    for key, value in x.items():
        dict_list.append([key, value])
    
    money_paid = [row[1] for row in dict_list]
    people = [row[0] for row in dict_list]
    
    addition = 0
    for n in money_paid:
        addition += n
    average = addition/len(dict_list)
    
    for people,money_paid in dict_list:
        if (money_paid > average or money_paid < average):
            group[people] = round(money_paid - average,2)
        else:
            group[people] = 0
    return group