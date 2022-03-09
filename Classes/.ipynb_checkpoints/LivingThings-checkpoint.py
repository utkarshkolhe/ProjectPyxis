from GameElementBase import GameElementBase
class LivingThings(GameElementBase):
    def __init__(self,position,beingid):
        self.beingid=beingid
        self.position = position
        self.mapsize=[3,3]
        self.inventory=[]
    def move(self,direction):
        flag=False
        if direction=="n":
            if self.position[0]>0:
                self.position[0] -=1
                flag = True
        if direction=="s":
            if self.position[0]<(self.mapsize[0]-1):
                self.position[0] +=1
                flag = True
        if direction=="w":
            if self.position[1]>0:
                self.position[1] -=1
                flag = True
        if direction=="e":
            if self.position[1]<(self.mapsize[1]-1):
                self.position[1] +=1
                flag = True
        if flag and self.beingid == "PLAYER":
            from StaticController import StaticController
            StaticController.variableMap["JUST_ENTERED"] = 1
            room = StaticController.gameMap.getRoom(self.position)
            StaticController.variableMap["CURRENT_ROOM"] = room
        
        # roomname = StaticController.gameMap.getRoomName(self.position)
        # StaticController.variableMap[self.beingid + "."+"CURRENT_ROOM"] = roomname
        return flag
    def getPosition(self):
        print(StaticController.test)
        return self.position
        