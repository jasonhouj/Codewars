'''A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where l = 3 ( the number of digits in 153 )
13 + 53 + 33 = 153

Write a function that, given n, returns whether or not n is a Narcissistic Number.'''

# ----start of solution----


def is_narcissistic(i):
    x = [int(j) for j in str(i)]
    length = len(x)
    total = []
    for nums in x:
        total.append(nums ** length)
    answer = sum(total)
    if answer == i:
        return True
    else:
        return False