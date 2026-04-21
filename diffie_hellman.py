import secrets
def diffie_hellman(p, g):
    a = secrets.randbelow(p-1) + 1
    b = secrets.randbelow(p-1) + 1
    print(f"a = {a}")
    print(f"b = {b}")
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"Public key A = {A}")
    print(f"Public key B = {B}")
    secret_a = pow(B, a, p)
    secret_b = pow(A, b, p)
    if secret_a == secret_b:
        print(f"Correct: {secret_a}")
    else:
        print("Incorrect")
p = 23
g = 5
diffie_hellman(p, g)
