# 5.	Print how many digits does 2^1024 have.
# HINT: Convert to string and check the length of the string.

a5 = 2 ** 1024
a5 = str(a5)
nr_of_digits = len(a5)
print('\n Exercise 5')
print(f' 2^1024 has {nr_of_digits} digits.')