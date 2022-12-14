# AoC 2022

Here are my solutions for the 2022 edition of the [Advent of Code](https://adventofcode.com/), hosted by [Eric Wastl](https://github.com/topaz)

## How to improve the code

- Day 1: The parsing is not beautiful is because of the blank lines. Also the complexity of first case is slightly higher than it should because I wanted to solve the two cases with only one function. A call to `max` would make it faster.
- Day 2: Pretty proud of that one, and using arithmetic instead of a bunch of nested `if`s to compute the scores. Removing the `if`s in the q1 score computation function would make it more beautiful.
- Day 3: `find_duplicate` and `find_truplicate` can definitely be merged into one function that computes the only element in all lists it has for arguments. Oh and `rank` is not beautiful
- Day 4: There might be a nice way to merge the conditions in `inclusion` and `overlap`, I just can't think of it right now.
- Day 5: Honestly I'm not proud of that one at all, I should redo it completely (and do a curses animation of some sort of crane moving crates around)
- Day 6: Pretty proud of that one, nothing to change.
- Day 7: Lots of boilerplate, and the `create_filesystem` parsing function is a bit clunky, but other than that it's fine.
- Day 8: Some things could be factorized between the 4 directions in both functions, just did not have the motivation to do it.
- Day 9: I used an iterator as the input because I did not want to keep track of the index of the last instruction, or to `pop(0)` them because of the complexity. This means I had to duplicate it for the two parts, which I am not really happy about. Another solution could be found.
- Day 10: Part 1 and part 2 are really independent in this one, which bothers me. I would like it if there was some reusing of part 1 in part 2.
- Day 11: As I am writing this, I am refactoring the code into classes to make it nicer. However, I am not working on another solution for the weird `eval` + `MAGIC_OPERATION_CONSTANT` hack I made up to not parse the `Operation: ...` line at 6 AM.
- Day 12: The code could be made much better by specifying the graph and not having to have 2 bfs functions
- Day 13: ok. Parsing uses `eval` which is meh, but other than that everything is fine
- Day 14: The complexity on that one is awful.
- Day 15: The complexity on part 2 is even awful*er*
