def define_number_semmetric(number):
    n1 = number // 100
    n2 = number % 100
    n2 = n2 % 10 * 10 + n2 / 10
    return(n1, n2)

def main():
    number = int(input("Input your number: "))
    n1, n2 = define_number_semmetric(number)
    print (n1, n2)
main()