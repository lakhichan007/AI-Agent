from tools import (get_current_time,roll_dice,generate_secure_password,read_file);

def execute_tool(user_input):
    input = user_input.lower()
    
    if("time" in input):
        return {"content":f"Current time is- {get_current_time()}","is_response":True}

    elif("dice" in input):
        return {"content":f"Your dice - {roll_dice()}","is_response":True}

    elif("password" in input):
        return {"content":f"Generated pasword is - {generate_secure_password()}","is_response":True}
    elif("document" in input):
        filename = next((word for word in user_input.split() if word.endswith(".txt")),None)
        if(filename):
            data = read_file(f"data/{filename}")
            filecontent  = f"Please explain the Document:{data} and whenever question is asked you have to reply only document specific, nothing else. If no data in document simply ask I couldn't find information in this Document."
        else:
            filecontent = user_input
        return {"content":filecontent,"is_response":False}        
    else:         
        return {"content":user_input ,"is_response":False}