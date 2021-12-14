# QUESTION 1
# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  return sum(range(1, n+1))

print(sum_to(6))
print(sum_to(10))

# QUESTION 2
# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  return max(list)

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

# QUESTION 3
# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(string1, string2):
  return sum([string1.startswith(string2, i) for i in range(len(string1))])

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

# QUESTION 4
# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  multiply = 1
  for num in args:
    multiply *= num
  return multiply

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))

