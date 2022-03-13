from StaticController import StaticController
from NLPParser import NLPParser
import pandas as pd
import os.path

def performAction(message):
    action,parameters = NLPParser.parse(message)
    if not action:
        msgs=StaticController.displayCD("invalid-input",{})
    else:
        if action =="move":
            msgs = StaticController.playerCharacter.move(parameters[0])
        if action== "pick":
            msgs = StaticController.playerCharacter.pick(parameters[0])
        if action== "drop":
            msgs = StaticController.playerCharacter.drop(parameters[0])
    msgs = parseResponses([[msgs]])
    printMsgs(msgs)
def printMsgs(msgs):
    for msg in msgs:
        print(msg[0]," : ",msg[1])
def parseResponses(msgs):
    newmsgs=[]
    for arr in msgs:
        for msg in arr:
            if type(msg)== type("123"):
                if len(msg)<1:
                    continue
                newmsgs.append(["User",msg])
    return newmsgs
def performEffect():
    msgs= StaticController.getEffectSlice()
    return parseResponses(msgs)
def getInitialCommunication():

    initialDialog = pd.read_excel(open(os.path.dirname(__file__)+'/../Data/InitialCommunication.xlsx', 'rb'))
    msgs=[]
    for ind, row in initialDialog.iterrows():
        msgs.append([row["Sender"],row["Message"]])
    return msgs
    