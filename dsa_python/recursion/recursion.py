# concept of function


def HPython():
    print("Hello Python for learning python")


# def HDSA(num):
#     a = 8
#     b = 7
#     print("Hello DSA", num)
#     HPython()


# def HDSA1(num):
#     print("Hello DSA", num)
#     HDSA2(2)


# def HDSA2(num):
#     print("Hello DSA", num)
#     HDSA3(3)


# def HDSA3(num):
#     print("Hello DSA", num)
#     HDSA4(4)


# def HDSA4(num):
#     print("Hello DSA", num)
#     HDSA5(5)


# def HDSA5(num):
#     print("Hello DSA", num)


# HDSA1(1)


def myFun(num):

    if num == 5:
        return

    print("Hello DSA", num)
    myFun(num + 1)


# myFun(1)


# Can function call itself ? The answer is YES - Recursion
# ------------------------------------------------------------------
# Functions stays in memory until resolved
# Only when a function finishes the execution then only it comes out of programme to the line it was called from and get deleted from stack

# RECURSION - A function calling itself

### IMPORTANT
# RECURSION = RECURSION IS WHEN SOLUTION OF PROBLEM DEPENDS ON THE SAME SMALLER PROBLEM


def factorial(n):

    print(n)

    if n == 1:
        return 1

    sAnswer = factorial(n - 1)
    ans = sAnswer * n
    return ans


# print(factorial(5))


# No we will not be making boxes or function every time


def power2(n):

    if n == 0:
        return 1

    sAnswer = power2(n - 1)
    ans = 2 * sAnswer

    return ans


# print(power2(5))


# def digit(num):

#     if num > 0 and num < 10:
#         return 1
#     elif num == 0:
#         return 0

#     smallN = int(num / 10)
#     sAns = digit(smallN)

#     return sAns + 1


# print(digit(0))


def digitCount(num):
    # print(num)
    # this will handle negative value
    num = abs(num)

    # this will handle base case

    if num < 10:
        return 1

    return digitCount(num // 10) + 1


print(digitCount(-10))
