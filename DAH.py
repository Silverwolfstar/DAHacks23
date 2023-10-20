'''Title: Recycling Game
    Team: nullptr
    Members: Jessie Kuo, Brandon Phan, Hannah Dinh, An Hoang'''

#import libraries
import pygame

#mainClock = pygame.time.Clock()
pygame.init()

#variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
maxHearts = 3 #TODO can change later
hearts = maxHearts #current hearts
itemx = 300 #x axis
itemy = 450 #y axis
textBoxCoord = (30, 30, 200, 85)
optionsBoxCoord = (15, 587, 97, 40)
score = 0
highScore = 0 #might implement a scoreboard? idk
gameOver = False
objects = []

#screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Recycling Game')
font = pygame.font.SysFont('papyrus', 20, True)
bigFont = pygame.font.SysFont('papyrus', 30, True) #TODO fix this, no papyrus

#icon
gameIcon = pygame.image.load('DAH/img/testIcon.png') #TODO add this
pygame.display.set_icon(gameIcon)

#Functions: ?????????
class Item(pygame.sprite.Sprite):
    playerWidth = 0
    playerHeight = 0
    def __init__(self, x, y, scale):
        super().__init__()
        item = pygame.image.load('DAH/img/testItem.png')
        self.item = pygame.transform.scale(item, 
            (int(item.get_width()*scale), int(item.get_height()*scale)))
        self.playerWidth = item.get_width()*scale
        self.playerHeight = item.get_height()*scale
        self.rect = self.item.get_rect() #current position of item
        self.rect.center = (x, y)

    def move(self):
        #TODO: implement drag and drop
        key = pygame.key.get_pressed()
        #TODO: implement collision detection

    def draw(self):
        screen.blit(self.item, (SCREEN_WIDTH/2-int(self.item.get_width()/2),
                    SCREEN_HEIGHT/3 - int(self.item.get_height()/2)))
        
    #def update(self):
        
        #maaybe later

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
            'normal': BLACK,
            'hover': BLACK,
            'pressed': BLACK
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)
    
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
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

    def myFunction():
        print('Open Option Menu')


#Below is example of multipress button
#Button(30, 140, 400, 100, 'Button Two (multiPress)', Button.myFunction, True)

#define entities
optionsButton = Button(optionsBoxCoord[0], optionsBoxCoord[1], 
        optionsBoxCoord[2], optionsBoxCoord[3], 'Options', Button.myFunction)
myItem = Item(itemx, itemy - 400, .25)

run = True
while run:
    #TODO handle pressed keys
    screen.fill(BLACK)
    myItem.draw()

    #process objects
    for object in objects:
        object.process()
        
    #draw score box
    pygame.draw.rect(screen, WHITE, (textBoxCoord[0], textBoxCoord[1], 
        textBoxCoord[2], textBoxCoord[3]), 1)
    #draw option box
    pygame.draw.rect(screen, WHITE, (optionsBoxCoord[0], optionsBoxCoord[1], 
        optionsBoxCoord[2], optionsBoxCoord[3]), 1)
    
    #event handling
    for event in pygame.event.get():
        #key pressed
        if event.type == pygame.USEREVENT:
            if hearts < 1:
                gameOver = True
            # 1 pressed
            if event.key == pygame.K_1 and hearts > 0 and not gameOver:
                    #handle answer
                    pass
            # 2 pressed
            if event.key == pygame.K_2 and hearts > 0 and not gameOver:
                    #handle answer
                    pass
            # 3 pressed
            if event.key == pygame.K_3 and hearts > 0 and not gameOver:
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
        gameOverText = bigFont.render('Game Over!', True, WHITE, BLACK)
        endScoreText = bigFont.render('Score: ' + str(score), True, WHITE, BLACK)
        replayText = bigFont.render('[Space] to Replay', True, WHITE, BLACK)
        gameOverTextRect = gameOverText.get_rect()
        endScoreTextRect = endScoreText.get_rect()
        replayTextRect = replayText.get_rect()
        gameOverTextRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 65)
        endScoreTextRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 20)
        replayTextRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 25)
        screen.blit(gameOverText, gameOverTextRect)
        screen.blit(endScoreText, endScoreTextRect)
        screen.blit(replayText, replayTextRect)

    #score text
    scoreText = font.render('Score:  ' + str(score), True, WHITE, BLACK)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.topleft = (50, 40)
    screen.blit(scoreText, scoreTextRect)

    #high score
    highScoreText = font.render('High Score:  ' + str(highScore), True, WHITE, BLACK)
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.topleft = (500, 600)
    screen.blit(highScoreText, highScoreTextRect)

    #options
    optionsText = font.render('Options', True, WHITE, BLACK)
    optionsTextRect = optionsText.get_rect()
    optionsTextRect.topleft = (25, 590)
    screen.blit(optionsText, optionsTextRect)

    #update display and clock
    pygame.display.update()
pygame.quit()