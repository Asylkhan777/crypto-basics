import secrets
def mitm(p, g):
    a = secrets.randbelow(p-1) + 1
    b = secrets.randbelow(p-1) + 1
    c = secrets.randbelow(p-1) + 1
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    A = pow(g, a, p)
    B = pow(g, b, p)
    C = pow(g, c, p)
    a_received = C
    b_received = C
    print(f"Public key A = {A}")
    print(f"Public key B = {B}")
    print(f"Public key C = {C}")
    secret_a = pow(a_received, a, p)
    secret_b = pow(b_received, b, p)
    secret_c_a = pow(A, c, p)
    secret_c_b = pow(B, c, p)
    print(f"Secret of A = {secret_a}")
    print(f"Secret of B = {secret_b}")
    print(f"Secret of C for A = {secret_c_a}")
    print(f"Secret of C for B = {secret_c_b}")
p = 23
g = 5
mitm(p, g)
