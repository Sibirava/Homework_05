def define_number_digit_equal(num):
    num1 = 0
#Либо добавить новую функцию, которая считает количество цифр в числе и потом сравнить его с 4
#и дальше *10 if-else
    while num != 0:
        digit = num % 10
        num //= 10
        num1 = num1 * 10
        num1 = num1 + digit
    return (num1)

# def count_number_digits(num):
#     count = 0
#
#     while num !=0:
#         count += 1
#         num //= 10
#     return count

def main():
    num = int(input("Input your number: "))
    num1 = define_number_digit_equal(num)

    if num == num1:
        print("Number's digits are equal")
    else:
        print("Number's digits are NOT equal")


main()
