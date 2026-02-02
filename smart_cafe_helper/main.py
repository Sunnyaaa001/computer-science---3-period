order_list = [
    {"order_name":"coffee",
     "emoji":"\u2615"},
    {"order_name":"cake",
     "emoji":"\U0001F370"},
    {"order_name":"tea",
     "emoji":"\U0001F375"}, 
]

total_price = 0.00
c = 3e8

def welcome_message():
    print("Weclome to Smart cafe!")
    while True:
        message_option = input("Would you like to customize the welcome message? (yes/no): ")
        message_option =  message_option.lower()
        if message_option == "yes" or message_option == "y":
            msg = input("Enter your custom message: ")
            print("Transformed welcome message: ",end="")
            # *msg means that String is sperated to a single character argument list. 
            # For exmaple, msg = "hello", *msg => (h,e,l,l,o)
            print(*msg,sep="...")
            return
        elif message_option == "no" or message_option == "n":
            return


def order_handling():
    global total_price
    while True:
        order = input("Please enter your order to type 'done' to finish: ")
        order = order.strip().lower()
        if order == "done":
            print(f"Your total is ${total_price:.2f}")
            return
        emojis_keyword(order=order)
        energy_caculation()
        while True:
            try:
               price = input("Enter the price of this item: ")
               price.strip()
               if not price.startswith("$"):
                  print("the currency should be dollars!")
                  continue
               price = price.removeprefix("$")
               price = float(price)
               if price < 0:
                 print("price is not less than 0!")
                 continue
               total_price += price
               break  
            except ValueError:
               print("please fill in the correct value!")    


def emojis_keyword(order:str):
    for item in order_list:
        if item["order_name"] == order:
            print(f"Okay, I will prepare {item['order_name']} {item['emoji']}")
            return
    print(f"Okay, I will prepare {order}")        
            


def energy_caculation():
    while True:
        option = input("Would you like caculate energy? (yes/no): ")
        option = option.strip().lower()
        if option == "yes" or option == "y":
            weight:float
            try:
                weight = float(input("Enter the weight in gram: "))
                if weight <= 0:
                    print("please fill the correct value!")
                energy = (weight / 1000.0) * c ** 2
                print(f"Energy: {energy:.2e} Joules.")
                return   
            except ValueError:
                print("please fill the correct value!")
        elif option == "no" or option == "n":
            return           

def order_total_with_tip():
    global total_price
    while True:
        try:
            tip = float(input("How much tip would you like to add? (10, 15, 20): "))
            if tip <= 0:
                print("tip is no less than 0!")
                continue
            final_price = (tip/100.0)*total_price
            print(f"With tip, your total is {final_price:.2f}")
            return
        except ValueError:
            print("please fill the correct tip number")    

def main():
    welcome_message()
    order_handling()
    order_total_with_tip()
    print("Thank you for visiting Smart Cafe!")

main()
