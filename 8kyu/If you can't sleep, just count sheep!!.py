'''If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
'''

# ---start-of-solution---

# My solution
def count_sheep(n):
  result = "";
  count = 1;
  while count <= n:
    result += str(count) + " sheep...";
    count += 1;
  return result;

count_sheep(5)


# Best solution

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

# Second best solution

def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep