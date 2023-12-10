# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.


import itertools
mydict={"1":["a","b"],"2":["c","d"]}
for combo in itertools.product(*[mydict[k] for k in sorted(mydict.keys())]):
    print("".join(combo))