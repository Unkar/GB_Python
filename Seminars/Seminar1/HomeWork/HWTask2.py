# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def check(X, Y, Z):
    return not (X or Y or Z) == (not X and not Y and not Z)

def main():
    for X in [True, False]:
        for Y in [True, False]:
            for Z in [True, False]:
                print(f"X={X}, Y={Y}, Z={Z} -> {check(X, Y, Z)}")

main()
