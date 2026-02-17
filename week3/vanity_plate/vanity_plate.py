def is_valid(plate:str)->str:
    length = len(plate)
    if length < 2 or length > 6:
        return "Invalid"
    if not plate.isalnum():
        return "Invalid"
    if not plate[:2].isalpha():
        return "Invalid"
    sub_str = plate[2:]
    sub_index = len(sub_str) - 1
    for i,c in enumerate(sub_str):
        if c.isdigit() and c == "0":
            return "Invalid"
        if i == sub_index and c.isalpha():
            return "Invalid"

    return "Valid"

def main():
    print(is_valid("Heelo, www"))
    print(is_valid("Heelo"))
    print(is_valid("GoodBye"))
    print(is_valid("cs5c2"))
    print(is_valid("CS50C"))

if __name__ == "__main__":
    main()


