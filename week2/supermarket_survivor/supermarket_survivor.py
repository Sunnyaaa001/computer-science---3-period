import numpy as np
import sys
import random

menu_list = []

def create_menus():
    # mention this variable is global
    global menu_list
    #set data type for every property
    data_type = [('menu','U50'),('index','i4'),('func','U20')]
    # set values into menu_list
    menu_list = np.array([
        ("File Extensions: What's in this file?", 1, "file_extension"),
        ("Math Interpreter: Unlock the safe", 2, "math_interpreter"),
        ("Nutrition Facts: Prepare a meal", 3, "nutrition_facts"),
        ("CamelCase Decoder: Decode the message", 4, "camelcase_decoder"),
        ("Emojize: Guess the clue", 5, "emojize"),
        ("Guessing Game: Guess the secret code", 6, "guessing_game"),
        ("Exit", 7, "exit")
    ], dtype=data_type)
    #according to the index, sort menu list
    menu_list.sort(order='index')

def file_extension():
    print("You find a file named 'recipe.pdf'.")
    file_input = input("Type the name of the file to check its extension: ")
    file_list = file_input.split(".")
    if len(file_list) != 2:
        print("Invalid file!")
        return
    if file_list[-1].lower() != "pdf":
        print("Unknown file type!")
        return    
    if "recipe" in file_input:
        print("This is a PDF file containing a recipe!")
    else:
        print("Unknown file type!")


def math_interpreter():
    print("A safe unlocks only with the correct mathematical calculation.")
    formula_str = input("Enter the mathematical expression (e.g., 2 + 3 * 4): ")
    formula_str = formula_str.replace(" ","")
    try:
        tokens = tokenize(formula_str)
        rpn = to_rpn(tokens=tokens)
        result = cal_rpn(rpn=rpn)
        print(f"The result is: {result}. The safe opens!")
    except ValueError:
        print("Invalid expression! Try again.")    
             
def nutrition_facts():
    total_calories = 0
    meal_list = [{"name":"apple","calories":50},{"name":"banana","calories":80},{"name":"cookie","calories":180}
                 ,{"name":"sandwich","calories":200},{"name":"water","calories":10}]
    print("Available options: " + ", ".join(meal["name"] for meal in meal_list))
    while total_calories < 500 :
        meal_name = input("Choose an item to add to your meal: ")
        meal_name = meal_name.replace(" ","").lower()
        if  meal_name not in (meal["name"] for meal in meal_list):
            print("please order something in the menu.")
        for meal in meal_list:
            if meal_name == meal["name"]:
                total_calories += meal["calories"]
                print(f"{meal_name} added! Total calories: {total_calories}")
                break
    print("Congratulations! Your meal is complete, and you have enough energy.")    



def camelcase_decoder():
    print("You find a message in CamelCase: 'EscapeNowThroughDoor'.")
    code = input("Type the CamelCase message to decode it: ")
    word = ""
    decode = []
    for c in code:
        if c.isupper():
            word+=c
        else:
            index = code.index(c)
            if index == (code.__len__() -1):
                word+=c
                decode.append(word)
            elif code[index + 1].isupper():
                word+=c
                decode.append(word)
                word = ""
            else:
                word+=c                   
    print("Decoded message: " +" ".join(item for item in decode))                 

def emojize():
    food_list = [
        {"name":"rice","emoji":"\U0001F35A"},{"name":"sushi","emoji":"\U0001F363"},{"name":"pasta","emoji":"\U0001F35D"},
        {"name":"bread","emoji":"\U0001F35E"},{"name":"soup","emoji":"\U0001F372"},{"name":"hotdog","emoji":"\U0001F32D"}
    ]
    #pick 3 random items
    pick_up_list = random.sample(food_list,3)
    print("You find a clue in emojis:"+ " ".join(item["emoji"] for item in pick_up_list))
    answer = input("What do these emojis mean? (Hint: food): ")
    answer = answer.strip()
    answer_list = answer.split(" ")
    if answer_list.__len__() != pick_up_list.__len__():
        print("That's not correct. Try again!")
        return
    for food in pick_up_list:
        index = pick_up_list.index(food)
        if food["name"] != answer_list[index]:
            print("That's not correct. Try again!")
            return
    print("Correct! You receive a key.")    

def guessing_game():
    print("A secret code (between 1 and 10) must be guessed.")
    chance = 3
    answer = random.randint(1,10)
    while chance > 0 :
        if chance == 1:
            print("OR (if you lose)")
        try:
            value = int(input(f"Guess the code (attempts left: {chance}):"))
            if value < 1 or value > 10:
                print("The answer is between 1 and 10")
                continue
            if value > answer:
                chance -=1
                print("Too High!")
            elif value < answer:
                chance-=1
                print("Too Low!")
            else:
                print("Correct! The door opens.")
                return               
        except ValueError:
            print("please fill the number")
    print(f"Unfortunately! The code was {answer}.")            

def exit():
    print("Thanks for playing! See you next time.")
    #quit program normally
    sys.exit(0)

def tokenize(formula_str:str)->list[str]:
    # define a formula array
    formula_list = []
    num = ""
    # set value into formula array
    for c in formula_str:
        if c.isdigit() or c == ".":
            num += c
        else:
            if num:
                formula_list.append(num)
                num = ""
            if c in "()+-/*":
                formula_list.append(c)
            else:
                raise ValueError
    # put last number into the formula array        
    if num:
        formula_list.append(num)
    return formula_list    

def to_rpn(tokens:list[str])->list[str]:
    #define caculation symbol priority dict
    priority = {"+":1,"-":1,"*":2,"/":2}
    #define 2 arrays
    stack = [] # for store caculation symbol
    output = [] # store RPN array
    # loop tokens array
    for item in tokens:
        #check items whether is numbers
        if item.replace(".","",1).isdigit():
            output.append(item)
        #check caculation symbol  **--*
        elif item in "+-*/":
            while(stack and stack[-1] in "+-*/" and priority[stack[-1]] >= priority[item]):
                output.append(stack.pop())
            stack.append(item)

        elif item == "(":
            stack.append(item)

        elif item == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                raise ValueError
        else:
            raise ValueError        
        
    while stack:
        if stack[-1] in "()":
            raise ValueError
        output.append(stack.pop())
    return output

def cal_rpn(rpn:list[str])->float:
    stack = []
    for item in rpn:
        if item.isdigit():
            stack.append(item)
        elif item in "+-*/":
            if len(stack) < 2:
                raise ValueError
            b = float(stack.pop())
            a = float(stack.pop())

            if item == "+":
                stack.append(a+b)
            if item == "-":
                stack.append(a-b)
            if item == "*":
                stack.append(a*b)
            if item == "/":
                if b == 0:
                    raise ValueError
                stack(a/b)
    if len(stack) != 1:
        raise ValueError
    return stack[0]                            

def menu_choose():
    print("Welcome to Survival Simulator!")
    print("You are in an abondoned supermarket and must solve puzzles to escape!")
    print()  
    while True:
        print("Choose an option:")
        for menu in menu_list:
          print(f"{menu['index']}. {menu['menu']}")
        #get index list
        index_list = menu_list["index"]
        max_index = index_list.max()
        min_index= index_list.min() 
        try:
            #get user input number and check this number
            number = int(input(f"Make a choice ({min_index}-{max_index}): "))
            if number < min_index or number > max_index:
                print(f"plase fill the number between {min_index} and {max_index}")
                continue
            #get the menu item that user choose
            menu_item = menu_list[menu_list['index'] == number][0]
            #pick up function name
            func_name = menu_item["func"]
            # use reflection to excute related functions
            func = globals().get(func_name)
            if func:
                #excute function
                func()
        except ValueError:
            print(f"plase fill the number between {min_index} and {max_index}")    
    
def main():
    create_menus()
    menu_choose()

main()