from tools import (get_current_time,roll_dice,generate_secure_password);

def execute_tool(user_input):
    input = user_input.lower()
    
    if("time" in input):
        return f"Current time is- {get_current_time()}"

    elif("dice" in input):
        return f"Your dice - {roll_dice()}"

    elif("password" in input):
        return f"Generated pasword is - {generate_secure_password()}"   

    return None