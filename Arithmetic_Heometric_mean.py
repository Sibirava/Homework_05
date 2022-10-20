# # Counting arithmetic mean and geometric mean of digits of the number
# Version 1.1.1, 27.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

# Arithmetic mean
# def sum_all_number_digits(number):
#     number *= -1 if number < 0 else 1
#     s = 0
#     while number > 0:
#         s += number % 10
#         number //= 10
#     return s
#
#
# def count_amount_digits(number):
#     count = 0
#
#     while number != 0:
#         count += 1
#         number //= 10
#     return count
#
#
#
# def main():
#     number = int(input("Please input your number:  "))
#     s = sum_all_number_digits(number)
#     count = count_amount_digits(number)
#     avg = s / count
#     msg = f"Arithmetic mean of {number} is {avg} "
#     print(msg)
#
#
# main()

# Heometric mean
def multiply_all_number_digits(number):
    number *= -1 if number < 0 else 1
    mult = 1
    while number > 0:
        mult *= number % 10
        number //= 10
    return mult


def count_amount_digits(number):
    count = 0

    while number != 0:
        count += 1
        number //= 10
    return count


def main():
    number = int(input("Please input your number:  "))
    mult = multiply_all_number_digits(number)
    count = count_amount_digits(number)
    hm = round(mult ** (1 / count))

    msg = f"Heometric mean of {number} is {hm} "
    print(msg)


main()
