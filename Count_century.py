def count_century(year):
    if year % 100 == 0:
        century = year // 100
    else:
        century = year // 100 + 1
    return century

def main():
    year = int(input("Please input year : "))
    century = count_century(year)
    msg = f"Year {year} belongs to {century}th century."
    print(msg)

main()