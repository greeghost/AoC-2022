# AoC 2022

Here are my solutions for the 2022 edition of the [Advent of Code](https://adventofcode.com/), hosted by [Eric Wastl](https://github.com/topaz)

## How to improve the code

- Day 1: the parsing is not beautiful is because of the blank lines. Also the complexity of first case is slightly higher than it should because I wanted to solve the two cases with only one function. A call to `max` would make it faster.
- Day 2: pretty proud of that one, and using arithmetic instead of a bunch of nested `if`s to compute the scores. Removing the `if`s in the q1 score computation function would make it more beautiful.
- Day 3: `find_duplicate` and `find_truplicate` can definitely be merged into one function that computes the only element in all lists it has for arguments. Oh and `rank` is not beautiful
- Day 4: There might be a nice way to merge the conditions in `inclusion` and `overlap`, I just can't think of it right now.
- Day 5: Honestly I'm not proud of that one at all, I should redo it completely (and do a curses animation of some sort of crane moving crates around)
- Day 6: Pretty proud of that one, nothing to change.
- Day 7: Lots of boilerplate, and the `create_filesystem` parsing function is a bit clunky, but other than that it's fine.
