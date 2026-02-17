def value(greeting:str)->int:
    value = 0
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        value = 0
    elif greeting.startswith("h"):
        value = 20
    else:
        value = 100
    return value    

def main():
    print(value("Hello"))
    print(value("hello, Sunny"))
    print(value("How are you Sunny?"))
    print(value("Where are you Sunny?"))


if __name__ == "__main__":
    main()