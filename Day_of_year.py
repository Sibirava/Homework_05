# Определить по номеру день недели
# Как установить день, с которого начинается год?
def define_day(number):
    if 365 >= number >= 1:
        day = number % 7
        if day == 0:
            print("monday")
        elif day == 1:
            print("tuesday")
        elif day == 2:
            print("wensday")
        elif day == 3:
            print("thursday")
        elif day == 4:
            print("friday")
        elif day == 5:
            print("saturday")
        else:
            print("sunday")
    else:
        print("Wrong number, enter one of 365 days a year")
    return (day)


def main():
    number = int(input("Please input your number: "))
    day = define_day(number)

main()
