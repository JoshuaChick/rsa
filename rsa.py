import random


"""
Creates RSA keys from two prime numbers.

A public and private key will be generated, such as "Public key (a, b)" and "Private key (x, b)". To send a message,
send the person you wish to communicate with the public key, have them convert their character to an integer, raise
that integer to "a" and take modulus "b", have them send you this, then raise that to "x" and take modulus
"b" to get the original integer, then convert that back to the original character. 

The product of your two prime numbers must be greater than the largest value you wish to encrypt,
e.g. if you wish to use the values 0-100 to represent the characters in your message, your prime numbers must multiply
to something greater than 100. The simplest reason for this is that the final step of decryption uses the product of your
two prime numbers as the argument for taking a modulus, and the result from this (decrypted value) cannot be greater than
the argument - 1, e.g. if you used 7 and 13 as your prime numbers you would have an argument of 7 * 13 = 91, which means
you could only get values from 0-90 after decrypting.

Note: this script is meant for understanding how rsa keys are generated and is not intended for practical use, and that
in practice you would want the product of your two prime numbers to be very large (often 1024 bits minimum).
"""


def get_factors(x):
    """Returns a list of factors."""
    factors = []
    for num in range(1, x + 1):
        if x % num == 0:
            factors.append(num)

    return factors


def is_prime(x):
    """Returns True or False depending on if the number is prime."""
    if x == 0 or x == 1:
        return False

    if x == 2 or x == 3:
        return True

    if x % 2 == 0:
        return False

    for num in range(3, int(x / 2)):
        if x % num == 0:
            return False

    return True


while True:
    p = int(input("Enter the first prime number: "))
    if p < 0:
        print('Input must be positive.\n')
    elif not is_prime(p):
        print('Input not prime.\n')
    else:
        break

while True:
    q = int(input("Enter the second prime number (must be different): "))
    if q < 0:
        print('Input must be positive.\n')
    elif not is_prime(q):
        print('Input is not prime.\n')
    elif q == p:
        print('The second number must be different from the first.\n')
    elif p <= 3 and q <= 3:
        print('If the first number was less than or equal to 3, the second must be greater.\n')
    else:
        break


N = p * q
phi_N = (p - 1) * (q - 1)

N_factors = get_factors(N)
phi_N_factors = get_factors(phi_N)

e_candidates = []

for i in range(2, phi_N):
    i_factors = get_factors(i)
    # Removes 1, as this is not relevant to finding if numbers are coprime.
    i_factors.pop(0)
    coprime = True
    for factor in i_factors:
        if (factor in N_factors) or (factor in phi_N_factors):
            coprime = False
            break

    if coprime:
        e_candidates.append(i)

e = e_candidates[random.randint(0, len(e_candidates) - 1)]

d_candidates = []
# N * 100 is arbitrary and is done to get a large set of possible decryption indexes.
for i in range(1, N * 100 + 1):
    if (i * e) % phi_N == 1:
        d_candidates.append(i)

# Chooses a random number, in the d_candidates list, if possible it doesn't pick the first, as picking
# the first is considered bad practice.
if len(d_candidates) == 1:
    d = d_candidates[0]
else:
    d = d_candidates[random.randint(1, len(d_candidates) - 1)]

print(f"Public key ({e}, {N})")
print(f"Private key ({d}, {N})")
