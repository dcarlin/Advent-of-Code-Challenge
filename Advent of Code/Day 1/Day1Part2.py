'''
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
What is the solution to your new captcha?

Your puzzle answer was 1156.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Share] this puzzle.
'''

#PART 2

file = open('dayOneInput.txt', 'r')
list = list(file.readline())
size = len(list)
holder = [0] * int(size/2)
size = int(size/2 - 1)
counter = 0
output = 0
for c in list:
    c = int(c)
    if holder[counter] == c:
        output += c
    holder[counter] = c
    counter += 1
    if counter > size:
        counter = 0


for x in range(0,size):
    if holder[x] == int(list[x]):
        output += holder[x]

print(output)
exit(0)
