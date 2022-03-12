from StaticController import StaticController
from NLPParser import NLPParser
import pandas as pd

def performAction(message):
    action,parameters = NLPParser.parse(message)
    if action =="move":
        StaticController.playerCharacter.move(parameters[0])
    if action== "pick":
        StaticController.playerCharacter.pick(parameters[0])
    if action== "drop":
        StaticController.playerCharacter.drop(parameters[0])
def printMsgs(msgs):
    for msg in msgs:
        print(msg[0]," : ",msg[1])
def performEffect():
    msgs= StaticController.getEffectSlice()
    newmsgs=[]
    for arr in msgs:
        for msg in arr:
            if len(msg)<1:
                continue
            newmsgs.append(["User",msg])
    return newmsgs
def getInitialCommunication():
    initialDialog = pd.read_excel(open('../Data/InitialCommunication.xlsx', 'rb'))
    msgs=[]
    for ind, row in initialDialog.iterrows():
        msgs.append([row["Sender"],row["Message"]])
    return msgs
    