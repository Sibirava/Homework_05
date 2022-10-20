def count_amount_squares(b, c, a):
    count = (b * c) // (a * a)
    s_left = ((b * c) % (a ** 2))
    return (count, s_left)


def main():
    b = int(input("Input first side of rectangle b: "))
    c = int(input("Input second side of rectangle c: "))
    a = int(input("Input the side of a squarе a: "))

    if a <= b and a <= c:
        count, s_left = count_amount_squares(b, c, a)
    else:
        print("Invalid data")
        return


    msg = f"The amount of squares in a rectangle is {count}. " \
          f"And the square left in rectangle is {s_left}"
    print(msg)


main()
