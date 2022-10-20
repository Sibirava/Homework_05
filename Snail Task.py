def count_snail_speed(h, a, b):
    day = 1 + (h - a) // (a - b)

    return(day)


def main():
    h = int(input("Input the height of a stick: "))
    a = int(input("Input the distance of a snail during the day: "))
    b = int(input("Input the antidistance of a snail during the night :"))

    day = count_snail_speed(h, a, b)

    if a > b and h > b:
        print("Snail will approach to the end of a stick in {} days".format(day))
    else:
        print("Invalid data")


main()
