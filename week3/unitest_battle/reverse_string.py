def reverse_string(result:str) -> str:
    if len(result) < 2:
        return result
    
    left = 0
    right = len(result) - 1

    char_list = list(result)

    while left < right:
        char_list[left],char_list[right] = char_list[right],char_list[left]
        left +=1
        right -=1

    result_str  = "".join(char_list)        
    return result_str 