print('Give me a number to run the Collatz conjecture:')
a = int(input())
while a != 1:
    if a % 2 == 0:
        a = int(a / 2)
    else:
        a = int(3 * a + 1)
    print(a)
