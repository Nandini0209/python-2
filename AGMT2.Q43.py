#Why Do You Use the Zip () Method in Python?
'''The zip() function in Python is used to combine multiple iterables (such as lists, tuples, or strings) element-wise.
It takes iterables as input and returns an iterator of tuples where the i-th tuple contains the i-th element
from each of the input iterables.If the input iterables are of different lengths,
the resulting iterator will be as long as the shortest iterable.'''

#eg
key=[1,2,3,4,5]
values=[101,102,103,104,105]
print(dict(zip(key,values)))
