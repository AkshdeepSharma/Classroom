from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("RandomPythonBot")

#moves towards the border
def towardsBorder(location):
    direction = NORTH
    maxDistance = min(0.25 * gameMap.width, 0.25 * gameMap.height)
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

def move(location):
    site = gameMap.getSite(location)
    border = False   
    for d in CARDINALS:
        neighbour_site = gameMap.getSite(location, d)
        if neighbour_site.owner != myID and neighbour_site.strength < site.strength:            
            border = True
            return Move(location, d)
    if site.strength < (site.production * 9):
        return Move(location, STILL)
    if not border:
        return Move(location, towardsBorder(location))
    return Move(location, STILL)

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(move(location))
    sendFrame(moves)