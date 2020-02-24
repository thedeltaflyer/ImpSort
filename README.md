# ImpSort
Improbably bad sorting for lists in Python.


## Why?
There was a conversation at a coffee shop about how terrible Bogo Sort is, so the question became can we use that concept to make even worse algorithms.


## What?
This library has implementations of some terrible sorting algorithms with some added "niceties" such as:
* Keeping track of metadata
* Having iterable (generator) versions of the algorithms
* Having equally terrible comparisons
* Timeouts for sanity's sake


## Algorithms
These are the algorithms currently implemented in ImpSort.

### Bogo Sort
This is the sorting algorithm that started this whole project.

It works by randomly re-sorting the entire list then checking if the new order is sorted.

### Random Swap Sort
This is like Bogo Sort... but worse.

It works by randomly picking two items in the list, then swapping them. It then checks to see if the whole list is sorted. It is also able to pick the same item, which would result in no change to the list at all!

### Recompile Sort
This is based on the old adage that states that if your code doesn't compile on the first try, it might on the next try....

So basically this goes through the whole list and sets each item to the same value it had, then checks if the list is now sorted. I believe Einstein would call this pure madness.


## Installation
Use pip to install:

`pip install ImpSort`

## Usage
Basic usage:

```python
# ImpSort objects are used to perform sorting operations
# TimeOutException can be used to detect timeouts
from ImpSort import (ImpSort, TimeOutException)

# The default algorithm is 'rand_swap'
# You can alternatively set it as 'bogo' or 'recompile'
# You can also provide a random to use (such as a random.SystemRandom instance)
sorter = ImpSort()

unsorted_list = [24, 106, 2, 42]  # This is a sample unsorted list

# To simply sort the list:
sorter.sort(unsorted_list)

# To get metadata about the most recent run, use the meta attribute:
print(sorter.meta)

# To get each iteration as the sort progresses, use the sort_generator method to get an iterable
for u in sorter.sort_generator(unsorted_list):
    print(u)

# To set a timeout, use the timeout argument:
try:
    # This will time out if it hasn't returned in 10 seconds
    sorter.sort(unsorted_list, timeout=10)
except TimeOutException as e:
    # You can catch a TimeOutException
    print(e)  # The exception includes some statistics about the failed run
```
