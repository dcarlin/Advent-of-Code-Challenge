'''
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle answer was 312453.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.

Your puzzle input was 312051.

You can also [Share] this puzzle.
'''

#PART 2

# x, y, value
p_input = 312051

values = [(0, 0, 1)]

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

level = 1
x, y = 0, 0

terminate = False

while not terminate:

    for direction in range(4):

        if terminate:
            break

        dirX, dirY = directions[direction]

        if direction == 0:
            moveN = level - 2
        elif direction in [1, 2]:
            moveN = level - 1
        else:
             moveN = level

        for _ in range(moveN):

            x += dirX
            y += dirY

            new = sum([k[2] for k in values if abs(x-k[0]) <= 1 and abs(y-k[1]) <= 1])
            values.append((x, y, new))

            if new >= p_input:
                print new

                terminate = True
                break

    level += 2