from GameElementBase import GameElementBase
class LivingThings(GameElementBase):
    def __init__(self,position):
        self.position = position
        self.mapsize=[3,3]
        self.inventory=[]
    def move(self,direction):
        if direction=="n":
            if self.position[0]>0:
                self.position[0] -=1
                return True
        if direction=="s":
            if self.position[0]<(self.mapsize[0]-1):
                self.position[0] +=1
                return True
        if direction=="w":
            if self.position[1]>0:
                self.position[1] -=1
                return True
        if direction=="e":
            if self.position[1]<(self.mapsize[1]-1):
                self.position[1] +=1
                return True
        return False
    def getPosition(self):
        return self.position
        