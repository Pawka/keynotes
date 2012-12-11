import math

def isTriplet(a, b, c):
   if a < b and b < c:
       if pow(a, 2) + pow(b, 2) == pow(c, 2):
           return True
   return False

if __name__ == "__main__":
    print "Projecteuler.net - 009"
    max = 1000
    for a in range(max, 0, -1):
        for b in range(max - a, 0, -1):
            c = math.sqrt(pow(a, 2) + pow(b, 2))
            if a + b + c == 1000:
                if isTriplet(a, b, c) == True:
                    print "Triplet:", a, b, c
                    print a * b * c

        
