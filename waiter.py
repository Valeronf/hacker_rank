# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_primes(count):
        primes = []
        num = 2
        while len(primes) < count:
            if is_prime(num):
                primes.append(num)
            num += 1
        return primes

    primes = generate_primes(q)
    ans = []

    for i in primes:
        if number:
            num = []
            for j in number:
                if j % i == 0:
                    ans.append(j)
                else:
                    num.append(j)

        num.reverse()
        number = num

    if number:
        number.reverse()
        ans = ans + number
    return ans