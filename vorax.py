def mirror(n):
    if n== 0:
        return 0
    rest = mirror(n - 1)
    return rest + 2 * n

n = int(input("Enter a number: "))
guess = int(input(f"What is the mirror of {n}?: "))
print(f"the mirror of {n} is {mirror(n)}, your guess: {guess}")

if guess == mirror(n):
    print("Your guess was correct.")
else:
    print("Your guess was wrong.")