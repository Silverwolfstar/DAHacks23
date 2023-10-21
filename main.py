'''Title: Recycling Game
    Team: nullptr
    Members: Jessie Kuo, Brandon Phan, Hannah Dinh, An Hoang'''

import random

import pygame

from variables import *

# Initialize Pygame
pygame.init()

pygame.display.set_caption('Recycling Game')
font = pygame.font.SysFont('papyrus', 38, True)
bigFont = pygame.font.SysFont('papyrus', 30, True)

#icon
gameIcon = pygame.image.load('img/icon.png')
pygame.display.set_icon(gameIcon)


#Functions: ?????????
class Item(pygame.sprite.Sprite):
    playerWidth = 0
    playerHeight = 0


    def __init__(self, x, y, scale):
        super().__init__()
        # #if no more items in availableList, then win game
        # if (len(availableList) < 1):     #pick random item to load, then remove from availableList
        #     win = True
        #     gameOver = True #TODO
        # else:
        if not availableList:
            gameOver = True
            self.item = None
            return  # Exit the __init__ early if the game is won
        index = random.randint(0, len(availableList)-1)
        #print("aaa = ", index)

        itemImage = pygame.image.load(availableList[index][2])
        self.itemAnswers = availableList[index][1]
        self.label = availableList[index][3]
        self.index = index
        self.item = pygame.transform.scale(itemImage, (int(itemImage.get_width()*scale),
                                                  int(itemImage.get_height()*scale)))
        self.playerWidth = itemImage.get_width()*scale
        self.playerHeight = itemImage.get_height()*scale
        self.rect = self.item.get_rect() #current position of item

    def getAnswers(self):
        if (self.item):
            return self.itemAnswers

    def move(self):
        #TODO: implement drag and drop
        key = pygame.key.get_pressed()
        #TODO: implement collision detection


    def draw(self):
        if (self.item):
            screen.blit(self.item, (SCREEN_WIDTH/2-int(self.item.get_width()/2),
                                SCREEN_HEIGHT/4 - int(self.item.get_height()/2)))

    #def update(self):

    #maybe later

class Bin(pygame.sprite.Sprite):
    binWidth = 0
    binHeight = 0

    def __init__(self, binNumber, x, scale):
        super().__init__()
        self.binNumber = binNumber
        bin = pygame.image.load(binList[binNumber-1][2])
        self.bin = pygame.transform.scale(bin, (int(bin.get_width()*scale),
                                                  int(bin.get_height()*scale)))
        self.binWidth = bin.get_width()*scale
        self.binHeight = bin.get_height()*scale
        self.rect = self.bin.get_rect() #current position of bin
        self.xBin = x

    def draw(self):
        screen.blit(self.bin, (self.xBin,
                                SCREEN_HEIGHT*3/4 - int(self.bin.get_height()/2)))



class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False


        #Can change this
        self.fillColors = {
            'normal': 'white',
            'hover': 'grey',
            'pressed': 'black',
        }


        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)


    def process(self):
        mousePos = pygame.mouse.get_pos()

        #button fill color
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos): #if mouse on button
            self.buttonSurface.fill(self.fillColors['hover']) #change to hover color


            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])


                if self.onePress: #if pressed
                    self.onclickFunction()


                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True


            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        screen.blit(self.buttonSurface, self.buttonRect)


    def myFunction(self):
        print('Open Option Menu')


#Below is example of multipress button
#Button(30, 140, 400, 100, 'Button Two (multiPress)', Button.myFunction, True)


#define entities
#optionsButton = Button(optionsBoxCoord[0], optionsBoxCoord[1],
#                       optionsBoxCoord[2], optionsBoxCoord[3], 'Options', Button.myFunction)
myItem = Item(itemx, itemy - 400, .1)

###### NEED TO CHANGE TRASH BIN X-POSITION FOR DIFFERENT SCREEN SIZE
trashBin = Bin(1,10,0.12)
recycleBin = Bin(2,SCREEN_WIDTH/2-120,0.12)
compostBin = Bin(3,SCREEN_WIDTH-275,0.12)




run = True
while run:
    screen.fill('#D1FFBD')
    myItem.draw()
    trashBin.draw()
    recycleBin.draw()
    compostBin.draw()


    #process objects
    for object in objects:
        object.process()

    #draw score box
    pygame.draw.rect(screen, 'black', (textBoxCoord[0], textBoxCoord[1],
                                       textBoxCoord[2], textBoxCoord[3]), 5)


    #draw option box
    #pygame.draw.rect(screen, 'white', (optionsBoxCoord[0], optionsBoxCoord[1],
    #                                   optionsBoxCoord[2], optionsBoxCoord[3]), 3)

    #event handling
    for event in pygame.event.get():
        if (hearts_num <1):
            availableList = defaultItemList[:] #reset availableList
            gameOver = True
        # Key pressed
        if event.type == pygame.KEYDOWN:
            # Check if the key pressed is 1, 2 or 3 and game is not over
            if event.key in key_to_bin_mapping and not gameOver:
                bin_index = key_to_bin_mapping[event.key]
                if myItem.getAnswers() is None:
                    win = True
                    print("Congrats you win")
                    availableList = defaultItemList[:] #reset availableList
                    gameOver = True
                elif  binList[bin_index][1] in myItem.getAnswers():
                    score +=1
                    availableList.pop(myItem.index)
                else:
                    hearts_num -= 1

                if (availableList):
                    myItem = Item(itemx, itemy - 400, .1)
                    myItem.draw()
                else:
                    win = True
                    print("Congrats you win")
                    availableList = defaultItemList[:] #reset availableList
                    gameOver = True
                    

            # Space to replay
            elif event.key == pygame.K_SPACE and gameOver:
                # Reset variables for new game
                hearts_num = maxHearts
                gameOver = False
                win = False
                # Set new high score
                if score > highScore:
                    highScore = score
                score = 0
        if event.type == pygame.QUIT:
            run = False

    if gameOver:
        if win:
            gameOverText = bigFont.render('You Win!', True, 'white', 'black')
        else:
            gameOverText = bigFont.render('Game Over!', True, 'white', 'black')
        #Create end game table
        pygame.draw.rect(screen, 'black', (SCREEN_WIDTH*1/3,SCREEN_HEIGHT/3,SCREEN_WIDTH*1/3,SCREEN_HEIGHT*1/3-30))
        endScoreText = bigFont.render('Score: ' + str(score) + '/' + str(len(defaultItemList)), True, 'white', 'black')
        replayText = bigFont.render('[Space] to Replay', True, 'white', 'black')
        gameOverTextRect = gameOverText.get_rect()
        endScoreTextRect = endScoreText.get_rect()
        replayTextRect = replayText.get_rect()
        gameOverTextRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 65)
        endScoreTextRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 15)
        replayTextRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 25)
        screen.blit(gameOverText, gameOverTextRect)
        screen.blit(endScoreText, endScoreTextRect)
        screen.blit(replayText, replayTextRect)



    #item label text
    if myItem:
        labelText = font.render(myItem.label, True, 'black', None)
        #labelText = pygame.transform.scale(labelText,(100,40))
        labelTextRect = labelText.get_rect()
        labelTextRect.topleft = (SCREEN_WIDTH/2 - (labelText.get_width()/2), SCREEN_HEIGHT/2 - (labelText.get_height()/2))
        if not gameOver:
            screen.blit(labelText, labelTextRect)


    #score text
    scoreText = font.render('Score:  ' + str(score), True, '#006600', None)
    # scoreText = pygame.transform.scale(scoreText,(100,40))
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.topleft = (SCREEN_WIDTH/22, 35)
    screen.blit(scoreText, scoreTextRect)
    textBoxCoord = (25, 25, scoreText.get_width() + 20, scoreText.get_height()+10)


    #high score
    highScoreText = font.render('High Score:  ' + str(highScore), True, 'white', 'black')
    highScoreText = pygame.transform.scale (highScoreText, (140,50))
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.topleft = (SCREEN_WIDTH-highScoreText.get_width(), SCREEN_HEIGHT-highScoreText.get_height())
    screen.blit(highScoreText, highScoreTextRect)

    #Hearts
    scaled_heart = pygame.transform.scale(heart_images.get(hearts_num, heart_images[0]), (150, 50))
    screen.blit(scaled_heart, (SCREEN_WIDTH*4/5, 20))


    #update display and clock
    pygame.display.update()

pygame.quit()
