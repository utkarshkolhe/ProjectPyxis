from GameElementBase import GameElementBase
class LivingThings(GameElementBase):
    def __init__(self,position,beingid):
        self.beingid=beingid
        self.position = position
        self.mapsize=[3,3]
        self.inv=[]
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

        return self.position
        
    def getRoom(self):
        from StaticController import StaticController
        return StaticController.gameMap.getRoom(self.position)
        
    def pick(self,objectname):
        from StaticController import StaticController
        currentroom = StaticController.gameMap.getRoom(self.position)
        if currentroom.hasObject(objectname):
            currentroom.takeObject(objectname)
            self.inv.append(objectname)
            return ["SUCCESS"]
        else:
            return ["ERROR", "object-not-in-room",{"objectname":objectname,"roomname":currentroom.getRoomName()}]
    
    def drop(self,objectname):
        from StaticController import StaticController
        currentroom = StaticController.gameMap.getRoom(self.position)
        if objectname in self.inv:
            currentroom.putObject(objectname)
            self.inv.remove(objectname)
            return ["SUCCESS"]
        else:
            return ["ERROR", "object-not-with-user",{"objectname":objectname,"roomname":currentroom.getRoomName()}]
        
        