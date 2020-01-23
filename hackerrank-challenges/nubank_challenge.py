#!/bin/python

import math
import os
import random
import re
import sys

a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    u_count = int(raw_input().strip())

    u = []

    for _ in xrange(u_count):
        u_item = raw_input()
        u.append(u_item)

    result = usernamesSystem(u)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
