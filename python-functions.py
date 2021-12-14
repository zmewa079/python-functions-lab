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

print(largest([1, 4, 6, 7, 9, 5, 34, 65, 43]))

