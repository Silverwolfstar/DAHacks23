import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
textBoxCoord = (25, 25, 170, 75)
optionsBoxCoord = (20, SCREEN_HEIGHT-55, 97, 50)

# Variables
maxHearts = 3
hearts = maxHearts
itemx = 300
itemy = 450
score = 0
highScore = 0
gameOver = False
objects = []


defaultItemList = [["pizzaBox", "compost", "pizzabox.png"],  #default list of items
                   ["sodaCan", "recycle", "sodaCan.png"],
                   ["plasticContainer", "recycle", "pizzabox.png"],
                   ["glassBottle", "recycle", "pizzabox.png"],
                   ["branches", "compost", "pizzabox.png"],
                   ["flowers", "compost", "pizzabox.png"],
                   ["paper", "compost", "pizzabox.png"],
                   ["chickenBones", "compost", "pizzabox.png"],
                   ["chipBags", "trash", "pizzabox.png"],
                   ["styrofoamCup", "trash", "pizzabox.png"],
                   ["cardboard", "recycle", "pizzabox.png"],
                   ["leaves", "compost", "pizzabox.png"],
                   ["blackPlastic", "trash", "pizzabox.png"],
                   ["cerealBox", "recycle", "pizzabox.png"],
                   ["milkCarton", "recycle", "pizzabox.png"],
                   ["newspaper", "recycle", "pizzabox.png"],
                   ["diapers", "trash", "pizzabox.png"],
                   ["pizzaCrusts", "compost", "pizzabox.png"],
                   ["frozenFoodBox", "trash", "pizzabox.png"],
                   ["brokenPlate", "trash", "pizzabox.png"]]
availableList = defaultItemList[:]
