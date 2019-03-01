def blah(x):
    print('in blah')
    print(x*4)
    return 'see you later'

def adder(m,n):
    total = 0
    for k in range(m,n+1):
        total = total +k
    return total


def main():
    print('in main')
    print(blah(2))
    print(adder(4,6))
    print(add_primes(3,11))


def is_prime(n):
    """
    What comes in:  An integer n >= 1.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    if n == 1:
        return False

    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True

def add_primes(m,n):
    total = 0
    for k in range(m, n+1):
        print ('in for loop ',k)
        if is_prime(k):
            total = total + k
            print(total)
    return total

main()
