'''
--- Part Two ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?

Your puzzle answer was 265.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Share] this puzzle.
'''

#PART 2
file = open('DayTwoInput.txt', 'r')
rows = list(file)
checksum = 0
output = 0
found = False
large = 0
small = 0

for x in range(0, len(rows)):
    values = rows[x].split('\t')
    for x in range (0, len(values)):
        for y in range(x+1, len(values)):
            values[x] = int(values[x])
            values[y] = int(values[y])
            if values[x] > values[y]:
                large = values[x]
                small = values[y]
            else:
                large = values[y]
                small = values[x]
            if (large % small) == 0:
                found = True
                break
        if found:
            break

    checksum += (large / small)
    found = False

print(checksum)