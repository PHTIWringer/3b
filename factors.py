# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# Date: 04/09/2024
# NOTE: No ReadMe Using other IDE
# Description: Asks the user to enter a positive integer and then prints a list of all positive integers that divide that number evenly including itself, in ascending order.

num = int(input("Please enter a positve integer: "))

print("The factors of", num, "are:")

for i in range(1, num + 1):
        if num % i == 0:
            print(i)
