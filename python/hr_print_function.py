#!/Users/siyer/virtualenv/flask/bin/python
from __future__ import print_function
if __name__ == '__main__':
    #n = int(raw_input())
    negative_flag = False
    n = 0
    if n <= 0:
        negative_flag = True
    n=abs(n)
    sum = 0
    for i in range(1,n+1):
        sum = (sum*10) + i
    if negative_flag:
        pass
    else:
        print(sum,sep=' ')
