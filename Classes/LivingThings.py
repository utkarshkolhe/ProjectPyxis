from GameElementBase import GameElementBase
class LivingThings(GameElementBase):
    def __init__(self,position,beingid,name,fullname):
        self.beingid=beingid
        self.position = position
        self.mapsize=[3,3]
        self.inv=[]
        self.name=name
        self.fullname = fullname
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
        elif self.beingid == "PLAYER":
            direction_long = {"n":"North","w":"West","s":"South","e":"East"}[direction]
            return StaticController.displayCD("map-edge",{"direction":direction_long})
        
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
            if self.beingid == "PLAYER":
                return StaticController.displayCD("object-added-in-inventory",{"objectname":objectname})
        else:
            if self.beingid == "PLAYER":
                return StaticController.displayCD("object-not-in-room",{"objectname":objectname})
    
    def drop(self,objectname):
        from StaticController import StaticController
        currentroom = StaticController.gameMap.getRoom(self.position)
        if objectname in self.inv:
            currentroom.putObject(objectname)
            self.inv.remove(objectname)
            if self.beingid == "PLAYER":
                return StaticController.displayCD("object-not-in-room",{"objectname":objectname})
        else:
            if self.beingid == "PLAYER":
                return StaticController.displayCD("object-not-with-user",{"objectname":objectname,"roomname":currentroom.getRoomName()})
    def getInventory(self):
        if len(self.inv)==0:
            if self.beingid == "PLAYER":
                return StaticController.displayCD("user-inventory-empty",{})
            else:
                return StaticController.displayCD("npc-inventory-empty",{"npcname":self.name})
        elif len(self.inv)==1:
            itemstr = self.inv[0]
        else:
            itemstr = ""
            lenitems=len(self.inv)
            itemstr += self.inv[0]
            for i in range(1,lenitems-1):
                itemstr+= ", " +self.inv[i]
            itemstr+= " and " +self.inv[lenitems-1]
        if self.beingid == "PLAYER":
            return StaticController.displayCD("user-inventory",{"itemstr" : itemstr})
        else:
            return StaticController.displayCD("npc-inventory",{"npcname":self.name,"itemstr" : itemstr})
            
    def hasObject(self,objectname):
        if objectname in self.inv:
            return True
        return False