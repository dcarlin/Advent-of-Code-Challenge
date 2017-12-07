'''
--- Part Two ---

Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

Your puzzle answer was 25347697.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Share] this puzzle.

'''

file = open('DayFiveInput.txt', 'r')
list = list(file)

counter = 0
temp = 0
x = 0

while x in range (0, len(list)):
    temp = x #Sets 'temp' = the value of x
    x += int(list[x]) # Adds the integer value of the current array position to x
    if int(list[temp]) >= 3:
        list[temp] = int(list[temp]) - 1
    else:
        list[temp] = int(list[temp]) + 1 #Increments the original value of x by 1 in the list
    counter += 1

print counter