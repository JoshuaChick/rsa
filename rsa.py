import random


"""
Creates RSA keys from two prime numbers.

The product of your two prime numbers must be greater than the number of numerical values you wish to encrypt,
e.g. if you had 100 possible values, your prime numbers must multiply to something greater than 100. This is because
the product will be used as the argument for taking the modulus, and the modulus cannot be greater than the 
argument of the modulus - 1.

A public and private key will be generated, such as "Public key (a, b)" and "Private key (x, b)". To send a message,
send the person you wish to communicate with the public key, have them convert their character to an integer, raise
that integer to "a" and take modulus "b", have them send you this, then raise that to "x" and take modulus
"b" to get the original integer, then convert that back to the original character. 
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
    x = abs(x)
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0:
        return False
    for num in range(2, int(x / 2)):
        if x % num == 0:
            return False
    return True


while True:
    p = abs(int(input("Enter the first prime number: ")))
    q = abs(int(input("Enter the second prime number (must be different): ")))
    if (is_prime(p) and is_prime(q)) and (p != q) and (p > 3 or q > 3):
        break
    if is_prime(p) and not is_prime(q):
        print(f"{q} is not prime.")
    elif not is_prime(p) and is_prime(q):
        print(f"{p} is not prime.")
    elif not is_prime(p) and not is_prime(q):
        print(f"{p} and {q} are not prime.")
    if p == q:
        print("Numbers must be different")
    if p <= 3 and q <= 3:
        print("At least one of the numbers must have an absolute value greater than 3.")

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