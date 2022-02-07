# wordle-solver

A Quick and dirty wordle solver that will run off a dictionary of words and
take the inputs to solve it.


## How to use it
run python wordle.py.  It will give you instructions on how to use it and give
you the first word suggestion 'orate' I use this as it covers 'a', 'e', and
'o'.

You respond with the match as provided by wordle ie.  five character response
matching what the wordle UI does ie. 

b for black
y for yellow
g for green

The program will give progressive suggestions and nail down the answer.

## Quality of the solution
I dont have a way to measure the quality of the solution.  But I have seen it
solve problems within 3-6 tries.   There is a element of luck in wordle (look
for random.choice() usage in code :-) ).  So hard to build a solver that can
beat the randomness.


