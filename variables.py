import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
textBoxCoord = (25, 25, 170, 75)
optionsBoxCoord = (20, SCREEN_HEIGHT-55, 97, 50)

# Variables
maxHearts = 3
hearts_num = maxHearts
itemx = 300
itemy = 450
score = 0
highScore = 0
gameOver = False
objects = []
index = 0 #index of current item
win = False
answer = True   #if user anwser is true or false



defaultItemList = [["pizzaBox", "compost", "img/pizzabox.png"],  #default list of items
                   ["sodaCan", "recycle", "img/sodaCan.png"],
                   ["plasticContainer", "recycle", "img/pizzabox.png"],
                   ["glassBottle", "recycle", "img/pizzabox.png"],
                   ["branches", "compost", "img/pizzabox.png"],
                   ["flowers", "compost", "img/pizzabox.png"],
                   ["paper", "compost", "img/pizzabox.png"],
                   ["chickenBones", "compost", "img/pizzabox.png"],
                   ["chipBags", "trash", "img/pizzabox.png"],
                   ["styrofoamCup", "trash", "img/pizzabox.png"],
                   ["cardboard", "recycle", "img/pizzabox.png"],
                   ["leaves", "compost", "img/pizzabox.png"],
                   ["blackPlastic", "trash", "img/pizzabox.png"],
                   ["cerealBox", "recycle", "img/pizzabox.png"],
                   ["milkCarton", "recycle", "img/pizzabox.png"],
                   ["newspaper", "recycle", "img/pizzabox.png"],
                   ["diapers", "trash", "img/pizzabox.png"],
                   ["pizzaCrusts", "compost", "img/pizzabox.png"],
                   ["frozenFoodBox", "trash", "img/pizzabox.png"],
                   ["brokenPlate", "trash", "img/pizzabox.png"]]

# Copy available list from default
availableList = defaultItemList[:]
binList = [[1,"trash","img/trashBin.png"],
           [2,"recycle","img/recycleBin.png"],
           [3,"compost","img/compostBin.png"]]

key_to_bin_mapping = {
    pygame.K_1: 0,  # Mapping K_1 to index 0
    pygame.K_2: 1,  # Mapping K_2 to index 1
    pygame.K_3: 2   # Mapping K_3 to index 2
}
