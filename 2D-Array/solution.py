#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    maxi = arr[0][0]+arr[0][1]+arr[0][2] + \
        arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
    for i in range(4):
        for j in range(4):
            temp = arr[i][j]+arr[i][j+1]+arr[i][j+2] + \
                arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if temp > maxi:
                maxi = temp
    return maxi


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
