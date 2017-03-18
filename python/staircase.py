from __future__ import print_function
import sys
def  StairCase(n):
    ash = n
    for i in range(0,n):
        for j in range(0,n+1):
            if j < ash:
                sys.stdout.write(" ")
                sys.stdout.flush()
            else:
                sys.stdout.write("_")
                sys.stdout.flush()
        ash = ash - 1
        j=0

        print('\n')





StairCase(4)
