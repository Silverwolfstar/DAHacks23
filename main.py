'''Title: Recycling Game
    Team: nullptr
    Members: Jessie Kuo, Brandon Phan, Hannah Dinh, An Hoang'''


from game_logic import *

# Initialize Pygame
pygame.init()

pygame.display.set_caption('Recycling Game')
font = pygame.font.SysFont('papyrus', 38, True)
bigFont = pygame.font.SysFont('papyrus', 30, True) #TODO fix this, no papyrus


#icon
gameIcon = pygame.image.load('img/testIcon.png') #TODO add this
pygame.display.set_icon(gameIcon)


#Functions: ?????????
class Item(pygame.sprite.Sprite):
    playerWidth = 0
    playerHeight = 0


    def __init__(self, x, y, scale):
        super().__init__()
        #if no more items in availableList, then win game
        if (len(availableList) < 1):
            #pick random item to load, then remove from availableList
            win = True
            gameOver = True #TODO
        else:
            index = random.randint(0, len(availableList)-1)

        item = pygame.image.load(availableList[index][2])
        self.item = pygame.transform.scale(item, (int(item.get_width()*scale), 
                                                  int(item.get_height()*scale)))
        self.playerWidth = item.get_width()*scale
        self.playerHeight = item.get_height()*scale
        self.rect = self.item.get_rect() #current position of item


    def move(self):
        #TODO: implement drag and drop
        key = pygame.key.get_pressed()
        #TODO: implement collision detection


    def draw(self):
        screen.blit(self.item, (SCREEN_WIDTH/2-int(self.item.get_width()/2),
                                SCREEN_HEIGHT/3 - int(self.item.get_height()/2)))

    #def update(self):

    #maybe later

class Bin(pygame.sprite.Sprite):
    binWidth = 0
    binHeight = 0

    def __init__(self, binNumber, x, scale):
        super().__init__()
        self.binNumber = binNumber
        bin = pygame.image.load(binList[binNumber][2])
        self.item = pygame.transform.scale(bin, (int(bin.get_width()*scale),
                                                  int(bin.get_height()*scale)))
        self.playerWidth = bin.get_width()*scale
        self.playerHeight = bin.get_height()*scale
        self.rect = self.item.get_rect() #current position of bin

    def draw(self):
        screen.blit(self.item, (SCREEN_WIDTH/2-int(self.item.get_width()/2),
                                SCREEN_HEIGHT/3 - int(self.item.get_height()/2)))



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
optionsButton = Button(optionsBoxCoord[0], optionsBoxCoord[1],
                       optionsBoxCoord[2], optionsBoxCoord[3], 'Options', Button.myFunction)
myItem = Item(itemx, itemy - 400, .1)


run = True
while run:
    #TODO handle pressed keys
    screen.fill('#D1FFBD')
    myItem.draw()


    #process objects
    for object in objects:
        object.process()

    #draw score box
    pygame.draw.rect(screen, 'black', (textBoxCoord[0], textBoxCoord[1],
                                       textBoxCoord[2], textBoxCoord[3]), 5)


    #draw option box
    pygame.draw.rect(screen, 'white', (optionsBoxCoord[0], optionsBoxCoord[1],
                                       optionsBoxCoord[2], optionsBoxCoord[3]), 3)

    #event handling
    for event in pygame.event.get():
        #key pressed
        if event.type == pygame.USEREVENT:
            if hearts_num < 1:
                gameOver = True
            # 1 pressed
            if event.key == pygame.K_1 and not gameOver:
                #handle answer
                pass
            # 2 pressed
            if event.key == pygame.K_2 and not gameOver:
                #handle answer
                pass
            # 3 pressed
            if event.key == pygame.K_3 and not gameOver:
                #handle answer
                pass
            #space to replay
            if event.key == pygame.K_SPACE and gameOver:
                #reset variables for new game
                gameOver = False
                #set new high score
                if (score > highScore):
                    highScore = score
                score = 0
        if event.type == pygame.QUIT:
            run = False


    #game end
    if (gameOver):
        gameOverText = bigFont.render('Game Over!', True, 'white', 'black')
        endScoreText = bigFont.render('Score: ' + str(score), True, 'black', '#D1FFBD')
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


    #score text
    scoreText = font.render('Score:  ' + str(score), True, '#006600', '#D1FFBD')
    # scoreText = pygame.transform.scale(scoreText,(100,40))
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.topleft = (50, 35)
    screen.blit(scoreText, scoreTextRect)


    #high score
    highScoreText = font.render('High Score:  ' + str(highScore), True, 'white', 'black')
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.topleft = (500, 600)
    screen.blit(highScoreText, highScoreTextRect)

    #Hearts
    # Load and scale the heart images
    if (hearts_num == 3):
        heart_img = pygame.image.load('img/threeHearts.png')
    elif (hearts_num == 2):
        heart_img = pygame.image.load('img/twoHearts.png')
    elif (hearts_num == 1):
        heart_img = pygame.image.load('img/oneHeart.png')
    else:
        heart_img = pygame.image.load('img/noHearts.png')
    scaled_heart = pygame.transform.scale(heart_img, (150, 50))
    screen.blit(scaled_heart, (SCREEN_WIDTH*4/5, 20))

    #Bins





    #update display and clock
    pygame.display.update()

pygame.quit()
