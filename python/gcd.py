def gcd(a,b):
    print (a)
    print (b)
    if a == 0 or b == 0:
        return a+b
    return gcd(b,a%b)

val = gcd(77,44)
print (val)
