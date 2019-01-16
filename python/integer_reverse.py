class Reverse_Integer(object):
    def reverse(self,x):
        result = 0
        while x > 0:
            rem = x % 10
            x = x / 10
            result = result * 10 + rem
            print(result)
        return result


ri = Reverse_Integer()
print(ri.reverse(312))
