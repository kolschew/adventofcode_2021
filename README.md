# Advent of Code 2021
My contributions to the advent of code 2021!

What did I learn during this challenge:

### Day 3
- One can access the ith character in a dataframes containing of strings by df.str[i], which really came in handy during this task. Of course one can also split the different numbers with df.split() but the former approach seemed to be the most direct way for me.
- When working with Counters, cnt.most_common(x) is a really helpful thing. It returns the x most common entries; the least common ones can be accessed via cnt.most_common(x)[::-1].

### Day 5
- It is relatively annoying to create lists/vectors between two integers if you do not know whether your first argument 'x1' is larger than your second 'x2'.
Both range() and numpy.arange() need to receive explicitly -1 as a third argument if that is the case. In addition both do **not** automatically include the endpoint.
For me the best solution was to use numpy's linspace with a stepsize of 'x1 - x2 + 1' to cover all integer values and automatically go in the negative direction
if necessary.
- If rearranging a pandas dataframe e.g. by using df.loc() to get rid of certain entries, the indices will remain unchanged. Hence it is not possible to simple 
iterrate through the length of the dataframe anymore because certain indices do not exist and raise an error. This can be solved by using df.reset_index(drop=True),
which resets the indices and throughs the old ones away.
- Your best guess for iterrating through two lists at the same time without nesting them seems to actually be by indices. 