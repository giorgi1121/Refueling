def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)
def convert(fraction):
    # make the loop
    while True:
        # try-except statment to catch errors
        try:
            x, y = fraction.split("/")
            x_int = int(x)
            y_int = int(y)

            d = x_int / y_int

            if d <= 1:
                percentage = round(d * 100)
                return percentage
            else:
                fraction = input("Fraction: ").split("/")

            # if there will be ValueError this will catch it
        except ValueError:
            raise

        # if there will be ZeroDivisionError this will catch it
        except ZeroDivisionError:
            raise


def gauge(percentage):
    # check with conditionals
    # if percentage is less or equal 1 than print E
    if percentage <= 1:
        return "E"

    # if percentage is equal or more than 99 print F
    elif percentage >= 99 and percentage <= 100:
        return "F"

    # if percentage is more than 1 and less than 99 print percentage
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
