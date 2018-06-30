# Question:
# Write a Python program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on
# a single line.
#
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Solution:
print(",".join(map(str, filter(lambda x: all(map(lambda y: int(y) % 2 == 0, list(str(x)))), range(1000, 3001)))))
