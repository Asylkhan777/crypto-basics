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

print(mod_inverse(17, 3120))
