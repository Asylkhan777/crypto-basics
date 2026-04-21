import secrets
def is_prime(n, k=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def generate_prime(bits):
    while True:
        candidate = secrets.randbits(bits)
        candidate |= 1
        candidate |= (1 << bits-1)
        if is_prime(candidate):
            return candidate
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
def mod_inverse(a, m):
    if m <= 1:
        raise ValueError("The modulus m must be greater than 1")
    gcd, x, y = extended_gcd(a, m)
    if a%m == 0:
        raise ValueError("Inverse does not exist for a ≡ 0 (mod m)")
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m
def rsa_keygen(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    print(f"p = {p} and q = {q}")
    while p == q:
        q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"phi = {phi}")
    e = 65537
    if phi % e == 0:
        raise ValueError("e is not coprime with phi(n)")
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

def rsa_encrypt(m, public_key):
    n, e = public_key
    if m < 0 or m >= n:
        raise ValueError("Message out of range")
    c = pow(m, e, n)
    return c

def rsa_decrypt(c, private_key):
    n, d = private_key
    m = pow(c, d, n)
    return m

public_key, private_key = rsa_keygen(8)
m = 65
c = rsa_encrypt(m, public_key)
print("Encrypted message:", c)
print("Decrypted message:", rsa_decrypt(c, private_key))
