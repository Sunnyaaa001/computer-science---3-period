def camel_case(camel:str)->str:
    word_list = []
    word = ""
    for c in camel:
        if c.isupper():
            word_list.append(word)
            word = ""
            word += c.lower()
        else:
            word+=c
    if word:
        word_list.append(word)        
       
    return "_".join(word_list)


amount_due = 50

def coke_machine(insert_coin:int)->int:
    global amount_due
    if insert_coin > amount_due:
        return amount_due
    amount_due -= insert_coin
    return amount_due


def just_setting_up_my_twttr(input:str)->str:
    remove_str = "AaEeIiOoUu"
    rule = str.maketrans("","",remove_str)
    result = input.translate(rule)
    return result

