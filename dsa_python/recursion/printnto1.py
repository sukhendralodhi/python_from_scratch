def print_nton1(n):

    if n == 0:
        return

    print(n)
    print_nton1(n - 1)


print_nton1(5)
