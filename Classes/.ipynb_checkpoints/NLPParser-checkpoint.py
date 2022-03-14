class NLPParser:
    def parse(message):
        message = message.lower()
        messageparts = message.split(" ")
        if len(messageparts)==1:
            #Movements
            if messageparts[0] =="wait":
                return None,None
            if messageparts[0] in ["n","w","s","e"]:
                return "move", [messageparts[0]]
            if messageparts[0] in ["north","west","south","east"]:
                return "move", [messageparts[0][0]]
            #Exit
            if messageparts[0] == "exit":
                return "exit", []
            
            #Inventory
            if messageparts[0]== "inv" or messageparts[0] == "inventory":
                return "inv",[]
        if len(messageparts)==2:
            #Movements
            if messageparts[0] == "move" or messageparts[0] == "go":
                if messageparts[1] in ["n","w","s","e"]:
                    return "move", [messageparts[1]]
                if messageparts[1] in ["north","west","south","east"]:
                    return "move", [messageparts[1][0]]
            
            #Pick objects
            if messageparts[0] == "pick" or messageparts[0] == "take":
                return "pick", [messageparts[1]]
            
            #Drop objects
            if messageparts[0] == "drop" or messageparts[0] == "throw":
                return "drop", [messageparts[1]]
            
        if len(messageparts)==4:
            if messageparts[0]=="use" and messageparts[2]=="on":
                return "use",[messageparts[1],messageparts[3]]
        
        return None,None
            
            
            
            
                