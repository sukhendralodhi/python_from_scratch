def print_1ton(n):

    if n == 0:
        return

    print_1ton(n - 1)
    print(n)


print_1ton(5)
