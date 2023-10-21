
# importing numpy
import numpy as np
import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
textBoxCoord = (25, 25, 185, 75)
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
answer = False   #if user anwser is true or false


#format: [name of item, waste type, img src, label, explanation]
defaultItemList = [["pizzaBox", ["compost"], "img/pizzabox.png", "Pizza Box", "Greasy cardboard cannot be recycled, but can be placed into the compost!"],  #default list of items
                   ["sodaCan", ["recycle"], "img/sodaCan.png", "Soda Can", "Metal cans can be recycled!"],
                   ["plasticContainer", ["recycle"], "img/plasticContainer.png", "Plastic Container", "Plastic containers can be recycled!"],
                   ["glassBottle", ["recycle"], "img/glassBottle.png", "Glass Bottle", "Glass bottles can be recycled!"],
                   ["branches", ["compost"], "img/branches.png", "Branch", "Organic matter can be composted!"],
                   ["flowers", ["compost"], "img/flowers.png", "Flower", "Organic matter can be composted!"],
                   ["paper", ["compost", "recycle"], "img/paper.png", "Paper", "Paper can be recycled or composted!"],
                   ["chickenBones", ["compost"], "img/chickenBones.png", "Chicken Bones", "Organic matter can be composted!"],
                   ["chipBag", ["trash"], "img/chipBag.png", "Chip Bag", "Chip bags cannot be recycled or composted."],
                   ["styrofoamCup", ["trash"], "img/styrofoamCup.png", "Styrofoam Cup", "Styrofoam cannot be recycled or composted."],
                   ["cardboard", ["recycle", "compost"], "img/cardboard.png", "Cardboard", "Cardboard can be recycled or composted!"],
                   ["leaves", ["compost"], "img/leaves.png", "Leaves", "Organic matter can be composted!"],
                   ["blackPlastic", ["trash"], "img/blackPlastic.png", "Black Plastic", "Black plastic cannot be recycled."],
                   ["cerealBox", ["recycle", "compost"], "img/cerealBox.png", "Cereal Box", "Cardboard can be recycled or composted!"],
                   ["milkCarton", ["recycle"], "img/milkCarton.png", "Milk Carton", "Milk cartons can be recycled!"],
                   ["newspaper", ["compost", "recycle"], "img/newspaper.png", "Newspaper", "Newspaper can be recycled or composted!"],
                   ["diapers", ["trash"], "img/diaper.png", "Diaper", "Diapers cannot be recycled or composted."],
                   ["pizzaCrusts", ["compost"], "img/pizzaCrusts.png", "Pizza Crusts", "Leftover food can be composted!"],
                   ["frozenFoodBox", ["trash"], "img/frozenFoodBox.png", "Frozen Food Box", "Frozen food boxes contain a plastic coating, and therefore cannot be recycled or composted."],
                   ["brokenPlate", ["trash"], "img/brokenPlate.png", "Broken Plate", "Broken ceramic cannot be recycled or composted."]]

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