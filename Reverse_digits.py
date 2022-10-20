# Reverse digits of the number
# Version 1.1.1, 27.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

def reverse_digits(n1):
    n2 = 0
    while n1 > 0:
        digit = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10 + digit
    return n2


def main():
    n1 = int(input("Please input your number:  "))
    n2 = reverse_digits(n1)
    msg = f"Reverse of  {n1} is {n2} "
    print(msg)


main()
