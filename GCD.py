# GCD Program
print("Program to get GCD of 2 numbers\n")

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

gcd = get_gcd(num1, num2)
print("GCD of {0} and {1} is : {2}".format(num1, num2, gcd))
