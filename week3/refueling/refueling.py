def convert(fraction:str)->int:
    if not "/" in fraction:
        raise ValueError("Invalid expression!")
    fraction_list = []
    number = ""
    for c in fraction:
        if c in "-." or c.isdigit():
            number+=c
        elif c == "/":
            fraction_list.append(number)
            number = ""
        else:
            raise ValueError("Invalid expression!")

    fraction_list.append(number)
    first_number = float(fraction_list[0])
    second_number = float(fraction_list[1]) 
    if not first_number.is_integer() or  first_number < 0:
        raise ValueError("Invalid expression!")
    if not second_number.is_integer() or  second_number <= 0:
        raise ZeroDivisionError("Invalid expression!")
    if first_number > second_number:
        raise ValueError("Invalid expression!")
    return round(first_number/second_number*100)  


def gauge(percentage:int)->str:
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


def main():
    precentage = convert("33/0")
    result = gauge(precentage)
    print(result)


if __name__ == "__main__":
    main()