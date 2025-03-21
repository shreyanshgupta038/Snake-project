import pygame
import random

pygame.init()
#game ko reset karne ke liye
reset_game=0
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 1200
screen_height = 800
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("GTA-69")
pygame.display.update()


# Game variables
exit_game = False
game_over = False
snake_x = [60]
snake_y = [60]
#SECOND snake
snake_x1=[100]
snake_y1=[100]

velocity_x = 0
velocity_y = 0
velocity_x1 = 0
velocity_y1 = 0
food_x=random.randint(40,int(screen_width/2))
food_y=random.randint(40,int(screen_height/2))

snake_size = 10
score=0
score1=0
fps = 15
number1=0
number=0

l=2
m=2
clock = pygame.time.Clock()
def reset():
    global snake_x1,snake_y1,snake_x,snake_y,velocity_x,velocity_y,velocity_x1,velocity_y1,l,m,score,score1,reset_game
    snake_x1=[100]
    snake_y1=[100]
    snake_x = [60]
    snake_y = [60]
    velocity_x = 0
    velocity_y = 0
    velocity_x1 = 0
    velocity_y1 = 0
    m=2
    l=2
    reset_game=0
    score=0
    score1=0
            
def rando():
    global snake_x,snake_y,snake_x1,snake_y1
    
    snake_x[0]=10*random.randint(0,int(screen_width/10))
    snake_y[0]=10*random.randint(0,int(screen_height/10))
    snake_x1[0]=10*random.randint(0,int(screen_width/10))
    snake_y1[0]=10*random.randint(0,int(screen_height/10))
def border(color):
    pygame.draw.rect(gameWindow,color,[0,0,screen_width,10])
    pygame.draw.rect(gameWindow,color,[0,0,10,screen_height])
    pygame.draw.rect(gameWindow,color,[0,screen_height-10,screen_width,10])
    pygame.draw.rect(gameWindow,color
                     ,[screen_width-10,0,10,screen_height])


    
# Game Loop
while not exit_game:
    try:
        if  gameWindow.get_at((snake_x[0]+velocity_x,snake_y[0]+velocity_y)) ==(125, 30, 200, 255):
            
  
            rando()
        if  gameWindow.get_at((snake_x1[0]+velocity_x1,snake_y1[0]+velocity_y1)) ==(135,160,170, 255):
            

            rando()

    except IndexError:
        pass
    if reset_game==1:
        reset()


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit_game = True
        
        
            
        
#change direction snake 1st
        if event.type == pygame.KEYDOWN:
            if event.key==13:
                print("---->")
                reset()

            
            if event.key == pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0
           

            if event.key == pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0

            if event.key == pygame.K_UP:
                velocity_y=-10
                velocity_x=0

            if event.key == pygame.K_DOWN:
                velocity_y=10
                velocity_x=0
#change direction of 2nd snake
        if event.type == pygame.KEYDOWN:
            if event.key == 100:
                velocity_x1=10
                velocity_y1=0

            if event.key == 97:
                velocity_x1=-10
                velocity_y1=0

            if event.key == 119:
                velocity_y1=-10
                velocity_x1=0

            if event.key == 115:
                velocity_y1=10
                velocity_x1=0
    
#telepory 1st snake    
    if snake_x[0]>screen_width-10:
        snake_x[0]=11
    if snake_x[0]<10:
        snake_x[0]=screen_width-12
    if snake_y[0]>screen_height-10:
        snake_y[0]=11
    if snake_y[0]<10:
        snake_y[0]=screen_height-12

#teleport 2nd snake
    if snake_x1[0]>screen_width-10:
        snake_x1[0]=12
    if snake_x1[0]<10:
        snake_x1[0]=screen_width-12
    if snake_y1[0]>screen_height-10:
        snake_y1[0]=12
    if snake_y1[0]<10:
        snake_y1[0]=screen_height-12
#make it move
    snake_x[0] = snake_x[0] + velocity_x
    snake_y[0] = snake_y[0] + velocity_y
#make 2nd snake move
    snake_x1[0] = snake_x1[0] + velocity_x1
    snake_y1[0] = snake_y1[0] + velocity_y1

    gameWindow.fill(black)
    if len(snake_x1)<m:
        snake_x1.append(0)
    if len(snake_y1)<m:
        snake_y1.append(0)

    

    #1st value ko baaki pr chadhane k liye    
    for i in range(l,0,-1):
         try:
              snake_x[i]=snake_x[i-1]
         except IndexError:
              pass
         try:
              snake_y[i]=snake_y[i-1]
         except IndexError:
              pass
    #for 2nd snake
    for i in range(m,0,-1):
         try:
              snake_x1[i]=snake_x1[i-1]
         except IndexError:
              pass
         try:
              snake_y1[i]=snake_y1[i-1]
         except IndexError:
              pass

    #increase length
    if len(snake_x)<l:
        snake_x.append(0)
    if len(snake_y)<l:
        snake_y.append(0)
    #increase length of 2nd snake
    if len(snake_x1)<m:
        snake_x1.append(0)
    if len(snake_y1)<m:
        snake_y1.append(0)

    

 #making snake& increasing length   
    try:
        for i in range(l):
             pygame.draw.rect(gameWindow, (135,160,170), [snake_x[i-1], snake_y[i-1], snake_size, snake_size])
        for i in range(m):
             pygame.draw.rect(gameWindow,(125,30,200), [snake_x1[i-1], snake_y1[i-1], snake_size, snake_size])
    except IndexError:
        pass
    

    pygame.draw.rect(gameWindow, red, [food_x, food_y,snake_size, snake_size])


    
    
    pygame.display.update()
    if abs(snake_x[0]-food_x)<15 and abs( snake_y[0]-food_y)<15:
        score+=1
        l+=1
        number1=number+1
    if abs(snake_x1[0]-food_x)<15 and abs( snake_y1[0]-food_y)<15:
        score1+=1
        m+=1
        number1=number+1

    if number1>number:
        number+=1
        
        food_x=10*random.randint(0,int((screen_width-40)/10))
        food_y=10*random.randint(0,int((screen_height-40)/10))


        pygame.draw.rect(gameWindow, red, [food_x, food_y,snake_size, snake_size])
    #green border

    border('green')    
    
    font=pygame.font.SysFont("Comic Sans MS",30)
    score_screen=font.render((f"score-->{score}"),True,"grey")
    score_screen1=font.render((f"score-->{score1}"),True,"violet")
    gameWindow.blit(score_screen,(30,30))
    gameWindow.blit(score_screen1,(930,30))
    pygame.display.update()
    

    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
