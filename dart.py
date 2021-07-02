import pygame,math,pygame.locals 
pygame.init()
font = pygame.font.Font('FreeSansBold.ttf', 20)
font1 = pygame.font.Font('FreeSansBold.ttf', 200)
font2 = pygame.font.Font('FreeSansBold.ttf', 100)
screen = pygame.display.set_mode((0,0), pygame.locals.RESIZABLE)
w, h = pygame.display.get_surface().get_size()
cx,cy= w//2 ,h//2
x,y=cx+100,cy+100
aim_length=20
width=3
r,r1=300,300

arcsize= r/8


boundary = 20000
# Run until the user asks to quit
running = True


active = False
throw = False
speed=False
gameover=False
playagainb=False
nextb=True
text = '0'
speedtext=1
done = False
delay=100
score=0
def polartocart(radius,theta):
    # Converting theta from degree to radian
    theta = theta * math.pi/180.0
    # Converting polar to cartesian coordinates
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    return x,y
def flipf():
    global flip,thetaflip,radius,theta
    if theta>360:
        theta//=360
    if flip:
        if radius>180:
            radius-=5
        else:
            radius-=20
    else:
        if radius>180:
            radius+=5
        else:
            radius+=20
    if radius>=360:
        flip=True
    elif radius<=0:
        flip=False
        thetaflip= not thetaflip
def scorecalc():
    global radius,score,gameover,r,speedtext
    if radius>r:
        gameover=True
    else:
        score1=(r1-radius)*speedtext
        r-=radius
        score+=score1

radius,theta=100,0
flip=False
thetaflip=False

while running:
   

        


    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    if thetaflip:
        x1,y1=polartocart(radius,180-theta)
    else:
        x1,y1=polartocart(radius,theta)

    x,y=cx+x1,cy-y1
    pygame.draw.circle(screen, (100, 100, 200), (cx,cy), r ,0)
    pygame.draw.circle(screen, (0,0,0), (cx,cy), r ,width)
    pygame.draw.line(screen,(0,0,0),(x-aim_length,y),(x+aim_length,y),width)
    pygame.draw.line(screen,(0,0,0),(x,y-aim_length),(x,y+aim_length),width)
    
    if gameover:
        screen.blit(font1.render(f'GAME OVER ', False, (255,0,0)),(cx-500,cy-200))
        screen.blit(font2.render(f'score : {score}', False, (255,200,0)),(cx-400,cy))
        playagain=screen.blit(font2.render(f'play again', False, (0,0,0)),(600,680))
        if playagainb:
            gameover=False
            score=0
            r=300
            playagainb=False
            throw=False
        nextb=False
    if nextb:
        theta+=5
        flipf()
        if throw:
            scorecalc()    
            throw=False
            nextb=False    
    

     

    
    screen.blit(font2.render(f'The Dart Game', False, (0,0,0)),(600,20))
    throwbutton=screen.blit(font.render(f'Throw', False, (0,0,0)),(300,350))
    nextbutton=screen.blit(font.render(f'Next', False, (0,0,0)),(300,680))
    
    speedincrease=screen.blit(font.render(f'+', False, (0,0,0)),(250,80))
    speeddecrease=screen.blit(font.render(f'-', False, (0,0,0)),(250,120))
    screen.blit(font.render(f'score : {score}', False, (0,0,0)),(150,50))
    screen.blit(font.render(f'speed : {speedtext}', False, (0,0,0)),(150,100))

    
    pygame.time.delay(delay)
    # Flip the display
    pygame.display.flip()



    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                
                if throwbutton.collidepoint(event.pos):
                    # Toggle the active variable.
                    throw = True
                if gameover:
                    if playagain.collidepoint(event.pos):
                        playagainb = True
                if speedincrease.collidepoint(event.pos):
                    if speedtext<3:
                        speedtext+=1
                if speeddecrease.collidepoint(event.pos):
                    if speedtext>1:
                        speedtext-=1
                if nextbutton.collidepoint(event.pos):
                    nextb=True
                

 
   
    delay=100//(2*speedtext)


    
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()