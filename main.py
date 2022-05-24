from xmlrpc.client import Boolean
import pygame
import os
import random
import time
WIDTH, HEIGHT= 500, 400
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cow Climbs")


WHITE = (255,255,255)

FPS = 60
VEL=5
JIM_IMAGE = pygame.image.load(os.path.join('Assets',"cow.png"))
JIM = pygame.transform.scale(JIM_IMAGE,(100,100))

PLATFORM_IMAGE = pygame.image.load(os.path.join('Assets',"platform.png"))
PLATFORM = pygame.transform.scale(PLATFORM_IMAGE,(120 ,16))



GRAVITY=1.1



total_platforms=100

platform_separation=120

platforms_height=200
platforms= []

while total_platforms>0:
    # platform =  pygame.Rect(100, 80, 120, 16)
    platform =  pygame.Rect(random.randint(1,300), platforms_height, 120, 16)
    platforms.append(platform)
    total_platforms=total_platforms-1
    platforms_height=platforms_height-platform_separation


can_jump=False
jumpCount=20

def draw_window(jim, all_platforms):
    global can_jump
    WIN.fill(WHITE)
    WIN.blit(JIM, (jim.x,jim.y))
    for platform in all_platforms:
        WIN.blit(PLATFORM, (platform.x,platform.y+22))
    pygame.display.update()

def jim_movement(keys_pressed, jim,all_platforms):
        global can_jump
        global jumpCount
        if keys_pressed[pygame.K_a]:
            jim.x-=VEL
        if keys_pressed[pygame.K_d]:
            jim.x+=VEL
        if not(can_jump):
            jim.y+=VEL
            if keys_pressed[pygame.K_w]:
                can_jump=True
                for platform in all_platforms:
                    platform.y+=VEL
            if keys_pressed[pygame.K_s]:
                jim.y+=VEL
        else:
            #dont know what to do lol
                for platform in all_platforms:
                    platform.y+=VEL
                #FINALLY IT WORKS
                if keys_pressed[pygame.K_w]:
                    if jumpCount >= -10:
                        jim.y -= (jumpCount * abs(jumpCount)) * 0.5
                        jumpCount -= 1
                    else: # This will execute if our jump is finished
                        jumpCount = 10
                        can_jump = False
        
def gravity(jim, all_platforms):
    global can_jump
    platform_num=1
    platform_ToF=[]
    result=[]
    while platform_num<len(all_platforms):
        if jim.colliderect(platforms[platform_num]):
            platform_ToF.append(0)
            platform_num=platform_num+1
        else:
            # jim.y+=GRAVITY
            platform_ToF.append(1)
            platform_num=platform_num+1

    result = all(platform_ToF)
    if result==True:
        can_jump=False

    else:

        can_jump=True


    
def main():
    
    jim = pygame.Rect(300, 00, 70, 70)
    clock= pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        if jim.y>=HEIGHT-10:
            run=False
        keys_pressed = pygame.key.get_pressed()
        #jim.y+=GRAVITY*GRAVITY
        jim_movement(keys_pressed, jim,platforms)
        draw_window(jim,platforms)
        gravity(jim, platforms)
        print(jim.x,jim.y)

    pygame.quit

if __name__ == "__main__":
    main()