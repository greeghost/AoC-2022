# AoC 2022

Here are my solutions for the 2022 edition of the [Advent of Code](https://adventofcode.com/), hosted by [Eric Wastl](https://github.com/topaz)

## How to improve the code

- Day 1: the parsing is not beautiful is because of the blank lines. Also the complexity of first case is slightly higher than it should because I wanted to solve the two cases with only one function. A call to `max` would make it faster.
- Day 2: pretty proud of that one, and using arithmetic instead of a bunch of nested `if`s to compute the scores. Removing the `if`s in the q1 score computation function would make it more beautiful.
- Day 3: `find_duplicate` and `find_truplicate` can definitely be merged into one function that computes the only element in all lists it has for arguments. Oh and `rank` is not beautiful
