import math
import os
import random
import re
import sys
# Complete the 'fairRations' function below.
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
def fairRations(B):
    # Write your code here
    c = 0
    L = len(B)
    for i in range(1, L):
        if(B[i-1]%2 == 0):
            continue
        else:
            B[i-1] += 1
            B[i] += 1
            c += 2
    if((B[L-1])%2 == 0):
        return str(c)
    else:
        return 'NO'  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    fptr.write(result + '\n')
    fptr.close()