import sys

def dollars_float(money:str) -> float:
    # check the first char whether is $
    money = money.strip()
    if not money.startswith("$"):
        print("currency should be dollar!")
        sys.exit(0)
    #remove $ and check the rest of part whether is postive number
    money = money.removeprefix("$")
    result:float
    try:
        result = float(money)
        if result < 0:
            print("please fill in the postive number.")
            sys.exit(0)
    except ValueError:
        print("please fill the number..")
        sys.exit(0)
    return result    
        
def percent_float(percent:str)->float:
     # check the last char whether is %
     percent = percent.strip()
     if not percent.endswith("%"):
         print("input should be percentage!")
         sys.exit(0)
    # remove % and check the rest of part whether is postive number        
     percent = percent.removesuffix("%")
     result:float
     try:
        result = float(percent)
        if result < 0:
            print("please fill in the postive number.")
            sys.exit(0) 
     except ValueError:
         print("please fill the number..")
         sys.exit(0)
     result = result / 100.0
     return result 


def main():
    money = input("How much was the meal? ")
    moneyResult = float(dollars_float(money=money))
    percent = input("What percentage would you like to tip? ")
    percentResult = float(percent_float(percent=percent))
    tips = moneyResult * percentResult
    print(f"Leave ${tips:.2f}")

main()