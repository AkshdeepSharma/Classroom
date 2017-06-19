from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("MyPythonBot")

#moves towards the border
def towards_border(location):
    direction = EAST
    maxDistance = min(0.45 * gameMap.width, 0.45 * gameMap.height)
    for d in CARDINALS:
        distance = 0
        currentLocation = location
        site = gameMap.getSite(currentLocation, d)
        while (site.owner == myID and distance < maxDistance):
            distance += 1
            currentLocation = gameMap.getLocation(currentLocation, d)
            site = gameMap.getSite(currentLocation)
        if distance < maxDistance:
            direction = d
            maxDistance = distance
    return direction

def worthiness(location):
    return site.production / site.strength if site.strength else site.production

def move(location):
    border = False
    site = gameMap.getSite(location)  
    for d in CARDINALS:
        neighbourSite = gameMap.getSite(location, d)
        if neighbourSite.owner != myID and neighbourSite.strength < site.strength:
            return Move(location, d)
            border = True
        elif site.strength < site.production * 6:
            return Move(location, STILL)
    if not border:
        return Move(location, towards_border(location))
    return Move(location,STILL)

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(move(location))
    sendFrame(moves)