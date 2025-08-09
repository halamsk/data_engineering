# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(p):
    return p(lambda a,b: a)

def cdr(p):
    return p(lambda a,b: b)


if __name__== "__main__":
   print("Testing basic functionality...")
   pair1 = cons(3,4)
   assert car(pair1) == 3, f"Expected 3 got {car(pair1)}"
   assert cdr(pair1) == 4, f"Expected 4 got {cdr(pair1)}"


