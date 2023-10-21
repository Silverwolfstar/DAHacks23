
# importing numpy
import numpy as np
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
#global index
index = 0 #index of current item
win = False
answer = False   #if user anwser is true or false


#format: [name of item, waste type, img src, label]
defaultItemList = [["pizzaBox", ["compost"], "img/pizzabox.png", "Pizza Box"],  #default list of items
                   ["sodaCan", ["recycle"], "img/sodaCan.png", "Soda Can"],
                   ["plasticContainer", ["recycle"], "img/plasticContainer.png", "Plastic Container"],
                   ["glassBottle", ["recycle"], "img/glassBottle.png", "Glass Bottle"],
                   ["branches", ["compost"], "img/branches.png", "Branch"],
                   ["flowers", ["compost"], "img/flowers.png", "Flower"],
                   ["paper", ["compost", "recycle"], "img/paper.png", "Paper"],
                   ["chickenBones", ["compost"], "img/chickenBones.png", "Chicken Bones"],
                   ["chipBag", ["trash"], "img/chipBag.png", "Chip Bag"],
                   ["styrofoamCup", ["trash"], "img/styrofoamCup.png", "Styrofoam Cup"],
                   ["cardboard", ["recycle", "compost"], "img/cardboard.png", "Cardboard"],
                   ["leaves", ["compost"], "img/leaves.png", "Leaves"],
                   ["blackPlastic", ["trash"], "img/blackPlastic.png", "Black Plastic"],
                   ["cerealBox", ["recycle", "compost"], "img/cerealBox.png", "Cereal Box"],
                   ["milkCarton", ["recycle"], "img/milkCarton.png", "Milk Carton"],
                   ["newspaper", ["compost", "recycle"], "img/newspaper.png", "Newspaper"],
                   ["diapers", ["trash"], "img/diaper.png", "Diaper"],
                   ["pizzaCrusts", ["compost"], "img/pizzaCrusts.png", "Pizza Crusts"],
                   ["frozenFoodBox", ["trash"], "img/frozenFoodBox.png", "Frozen Food Box"],
                   ["brokenPlate", ["trash"], "img/brokenPlate.png", "Broken Plate"]]

# Copy available list from default
availableList = defaultItemList[:]
binList = [["1","trash","img/trashBin.png"],
           ["2","recycle","img/recycleBin.png"],
           ["3", "compost","img/compostBin.png"]]

key_to_bin_mapping = {
    pygame.K_1: 0,  # Mapping K_1 to index 0
    pygame.K_2: 1,  # Mapping K_2 to index 1
    pygame.K_3: 2   # Mapping K_3 to index 2
}

heart_images = {
    3: pygame.image.load('img/threeHearts.png'),
    2: pygame.image.load('img/twoHearts.png'),
    1: pygame.image.load('img/oneHeart.png'),
    0: pygame.image.load('img/noHearts.png')
}