# Python program to find the maximum and minimum numbers from the specified decimal numbers.

from decimal import *
data=list(map(Decimal, "2.45 4.78 2.98 3.89 1.34 2.90 6.89 6.67 5.45".split()))
print("Maximum numbers are:",max(data))
print("Minimum numbers are:",min(data))