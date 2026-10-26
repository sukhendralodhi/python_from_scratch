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


myFun(1)


# Can function call itself ? The answer is YES - Recursion
# ------------------------------------------------------------------
# Functions stays in memory until resolved
# Only when a function finishes the execution then only it comes out of programme to the line it was called from and get deleted from stack

# RECURSION - A function calling itself

### IMPORTANT
# RECURSION = RECURSION IS WHEN SOLUTION OF PROBLEM DEPENDS ON THE SAME SMALLER PROBLEM
