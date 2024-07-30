#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    ordered_keyboards = sorted(keyboards, reverse=True)
    ordered_drivers = sorted(drives, reverse=True)
    highest_vals = []
    for keyboard in ordered_keyboards:
        if keyboard >= b:
            continue
        else:
            for driver in ordered_drivers:
                print(driver, keyboard)
                if keyboard + driver > b:
                    continue
                else:
                    highest_vals.append(keyboard + driver)
    if len(highest_vals) < 1:
        return -1
    else:
        return max(highest_vals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
