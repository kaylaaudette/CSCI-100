# Creates a simulated game world consisting of a 2D grid.
# Life forms (bears or fish) can live only at specific
# locations in the grid. To start, life forms are placed at
# random locations. The simulation progresses by allowing
# one of the life-forms to live for one time unit, while all
# others are suspended in animation. Each life form is either
# (1) alive or (2) suspended. Each time a life-form is in the
# alive state, it must reevaluate its surroundings.
#
# Fish can breed (after alive 12 days), move, and die. If there
# are too many (2 or more) nearby fish, the fish will die.
#
# Bears will breed (after alive 8 days), move, eat nearby fish,
# and die (if starved 10 days).

import turtle
import random


# ---------------------------------------------------------
# World class
class World:
    
    # World constructor
    def __init__(self, mx, my):
        self.maxX = mx
        self.maxY = my
        self.thingList = []
        self.grid = []
    
        # create an empty 2D grid
        for arow in range(self.maxY):     
            row = []
            for acol in range(self.maxX):
                row.append(None)
            self.grid.append(row)        
    
        self.wturtle = turtle.Turtle()
        self.wscreen = turtle.Screen()
        self.wscreen.setworldcoordinates(0,0,self.maxX-1,self.maxY-1)   
        self.wscreen.addshape("Bear.gif")
        self.wscreen.addshape("Fish.gif")
        self.wturtle.hideturtle()               

    # draw the grid
    def draw(self):
        self.wscreen.tracer(0)
        self.wturtle.forward(self.maxX-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxY-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxX-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxY-1)
        self.wturtle.left(90)    
        for i in range(self.maxY-1):
            self.wturtle.forward(self.maxX-1)
            self.wturtle.backward(self.maxX-1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wturtle.forward(1)
        self.wturtle.right(90)
        for i in range(self.maxX-2):
            self.wturtle.forward(self.maxY-1)
            self.wturtle.backward(self.maxY-1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wscreen.tracer(1)
    
    # pause the world
    def freezeWorld(self):
        self.wscreen.exitonclick()
    
    # add something to the world at given x,y position
    def addThing(self, athing, x, y):   
        athing.setX(x)
        athing.setY(y)
        self.grid[y][x] = athing        
        athing.setWorld(self)
        self.thingList.append(athing)   
        athing.appear()                 
    
    # remove something from the world
    def delThing(self,athing):
        athing.hide()                                     
        self.grid[athing.getY()][athing.getX()] = None     
        self.thingList.remove(athing)                      
    
    # move whatever was at (oldx, oldy) to (newx, newy)
    def moveThing(self,oldx,oldy,newx,newy):
        self.grid[newy][newx] = self.grid[oldy][oldx]
        self.grid[oldy][oldx] = None
    
    # accessor method for maximum x position
    def getMaxX(self):
        return self.maxX
    
    # accessor method for maximum y position
    def getMaxY(self):
        return self.maxY
    
    # pick a random thing living in the world to set to alive
    def liveALittle(self):                                  
        if self.thingList != [ ]:
           athing = random.randrange(len(self.thingList))    
           randomthing = self.thingList[athing]              
           randomthing.liveALittle()                       
    
    # return whether the given (x,y) position is occupied
    def emptyLocation(self,x,y):
        if self.grid[y][x] == None:
            return True
        else:
            return False
    
    # return whatever is stored at the given (x,y) position
    def lookAtLocation(self,x,y):
       return self.grid[y][x]


# ---------------------------------------------------------
# Fish class
class Fish:
    
    # Fish constructor
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Fish.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None                 
        
        self.breedTick = 0

    # mutator for x position
    def setX(self,newx):
        self.xpos = newx
    
    # mutator for y position
    def setY(self,newy):
        self.ypos = newy
    
    # accessor for x position
    def getX(self):
        return self.xpos
    
    # accessor for y position
    def getY(self):
        return self.ypos
    
    # mutator for world
    def setWorld(self,aworld):
        self.world = aworld
 
    # show this fish
    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        self.turtle.showturtle()

    # hide this fish
    def hide(self):
        self.turtle.hideturtle()
    
    # move to a new (x,y) position in the world
    def move(self,newx,newy):
        self.world.moveThing(self.xpos,self.ypos,newx,newy)
        self.xpos = newx
        self.ypos = newy
        self.turtle.goto(self.xpos, self.ypos)

    # set to alive state
    def liveALittle(self):
        # a list of distances from current position to adjacent ones
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]     
        adjfish = 0
        
        # for each possible grid item adjacent to this fish
        for offset in offsetList:                    
            newx = self.xpos + offset[0]             
            newy = self.ypos + offset[1]
            
            # as long as grid item is within the bounds of the world grid
            if 0 <= newx < self.world.getMaxX()  and  0 <= newy < self.world.getMaxY():
                
                # count how many adjacent fish there are
                if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Fish):
                    adjfish = adjfish + 1   
     
        # if too many adjacent fish, this fish will die
        if adjfish >= 2:                   
            self.world.delThing(self)      
        else:
            # otherwise, this fish can breed a new fish
            self.breedTick = self.breedTick + 1
            if self.breedTick >= 12:
                self.tryToBreed()

            # after trying to breed, move to a new spot
            self.tryToMove()

    # try to breed a new fish nearby
    def tryToBreed(self):
        
        # pick a random adjacent grid location
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]    
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        
        # keep picking a new random adjacent location until one
        # is found which is within the bounds of the world
        while not (0 <= nextx < self.world.getMaxX() and 
                   0 <= nexty < self.world.getMaxY() ):  
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
    
        # if that valid location is empty, breed a new fish
        if self.world.emptyLocation(nextx,nexty):    
           childThing = Fish()
           self.world.addThing(childThing,nextx,nexty)
           self.breedTick = 0

    # try to move this fish
    def tryToMove(self):
        
        # pick a random adjacent location
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]   
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        
        # keep picking a new random adjacent location until one
        # is found which is within the bounds of the world
        while not(0 <= nextx < self.world.getMaxX() and 
                  0 <= nexty < self.world.getMaxY() ):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
    
        # if that location is empty, move this fish to it
        if self.world.emptyLocation(nextx,nexty):
           self.move(nextx,nexty)

# ---------------------------------------------------------
# Bear class
class Bear:
    
    # constructor
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Bear.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None
        
        self.starveTick = 0
        self.breedTick = 0
    
    # mutator for x position
    def setX(self,newx):
        self.xpos = newx
    
    # mutator for y position
    def setY(self,newy):
        self.ypos = newy
    
    # accessor for x position
    def getX(self):
        return self.xpos
    
    # accessor for y position
    def getY(self):
        return self.ypos
    
    # mutator for world
    def setWorld(self,aworld):
        self.world = aworld
 
    # make this bear visible
    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        self.turtle.showturtle()

    # hide this bear
    def hide(self):
        self.turtle.hideturtle()
    
    # move to a new (x,y) position on the world grid
    def move(self,newx,newy):
        self.world.moveThing(self.xpos,self.ypos,newx,newy)
        self.xpos = newx
        self.ypos = newy
        self.turtle.goto(self.xpos, self.ypos)

    # set bear to the alive state
    def liveALittle(self):
        
        # keep track of how many days it has lived
        self.breedTick = self.breedTick + 1
        
        # if long enough, this bear tries to breed
        if self.breedTick >= 8:
            self.tryToBreed()
    
        # bear always tries to eat
        self.tryToEat()          
    
        # if bear hasn't been able to it, it dies,
        # otherwise, it tries to move at the end of the day
        if self.starveTick == 10:
            self.world.delThing(self)
        else:
            self.tryToMove()

    # bear tries to eat if it can find a fish
    def tryToEat(self):
        
        # check all adjacent positions to find nearby fish
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)] 
        adjprey = []                 
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
                if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Fish):
                    adjprey.append(self.world.lookAtLocation(newx,newy))       
        
        # if there's a nearby fish, pick a random one to eat.
        # otherwise, bear starves this turn
        if len(adjprey)>0:                
            randomprey = adjprey[random.randrange(len(adjprey))]   
            preyx = randomprey.getX()
            preyy = randomprey.getY()
        
            self.world.delThing(randomprey)                            
            self.move(preyx,preyy)                                      
            self.starveTick = 0                     
        else:
            self.starveTick = self.starveTick + 1  
            
    # bear tries to breed
    def tryToBreed(self):
        
        # pick a random adjacent world grid position which
        # is within the bounds of the world
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]    
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not (0 <= nextx < self.world.getMaxX() and 
                   0 <= nexty < self.world.getMaxY() ):  
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
    
        # if that position is empty, create a new bear
        if self.world.emptyLocation(nextx,nexty):    
           childThing = Bear()
           self.world.addThing(childThing,nextx,nexty)
           self.breedTick = 0

    # bear tries to move in the world
    def tryToMove(self):
        
        # pick a new adjacent grid location in valid range
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]   
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not(0 <= nextx < self.world.getMaxX() and 
                  0 <= nexty < self.world.getMaxY() ):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
 
        # if that position is empty, move bear to it
        if self.world.emptyLocation(nextx,nexty):
           self.move(nextx,nexty)


# ---------------------------------------------------------
def mainSimulation():
    
    # set up number of bears, fish, and world variables
    numberOfBears = 20
    numberOfFish = 20
    worldLifeTime = 200
    worldWidth = 50
    worldHeight =25
    
    # create and display a new world
    myworld = World(worldWidth,worldHeight)      
    myworld.draw()                               
    
    # add fish randomly to the world
    for i in range(numberOfFish):  
        newfish = Fish()
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())
        while not myworld.emptyLocation(x,y):
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newfish,x,y)        
    
    # add bears randomly to the world
    for i in range(numberOfBears):   
        newbear = Bear()
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())
        while not myworld.emptyLocation(x,y):   
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newbear,x,y)     
    
    # simulate world for duration of simulation
    for i in range(worldLifeTime):     
        myworld.liveALittle()          
    
    # stop when finished
    myworld.freezeWorld()          

# ---------------------------------------------------------
# main entry point of program
mainSimulation()