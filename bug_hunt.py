count = 1
total = 0
# BUG: Missing colon after while condition causes SyntaxError, added colon
while count <= 5:
    # BUG: Original condition was count < 5 which gives 10 not 15, changed to <=5 to include 5
    total = total + count
    count = count + 1
# BUG: String + int causes TypeError, fixed with str(total)
print("Sum of 1 to 5 is: " + str(total))
