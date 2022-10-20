# Counting sec, minutes, hours from the beginning of the day" task
# Version 1.1.1, 27.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

def convert_from_sec_to_minutes(time):
    minutes = time / 60
    return minutes


def convert_from_sec_to_hour(time):
    hour = time / 3600
    return hour


def main():
    time = int(input("Please input time in sec: "))
    minutes = convert_from_sec_to_minutes(time)
    hour = convert_from_sec_to_hour(time)

    msg = f"{time}sec or {minutes}min or {hour} hours has passed from the beginning of the day."
    if 86400 >= time > 0:
        print(msg)
    else:
        print("Wrong number. Please enter number from 0 to 86400")


main()
