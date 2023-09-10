import pygame
import time
import random

pygame.font.init()


width,height = 1000,800

SCREEN = pygame.display.set_mode((width,height))

pygame.display.set_caption("Space Game")

background = pygame.transform.scale(pygame.image.load("bg.jpeg"),(width,height))

ship_width = 40
ship_height = 60
ship_speed = 5 # 5 pixel movement

meteor_width = 10
meteor_height = 20
meteor_speed = 3

Font = pygame.font.SysFont("Ariel" , 30) # font object


def draw(ship,played_time,meteors):
    SCREEN.blit(background, (0,0)) #blit helps to draw image on screen, (0,0) is top left coordinate of screen
    

    time_text = Font.render(f"Time: {round(played_time)}s", 1, "white") 

    SCREEN.blit(time_text,(10,10)) # (10,10) coordinates

    pygame.draw.rect(SCREEN, "red", ship) # ship = cordinates to draw rectandle

    for meteor_generated in meteors:
        pygame.draw.rect(SCREEN, "brown", meteor_generated)

    pygame.display.update() # upadte any change in screen


def main():

    run = True

    ship = pygame.Rect(200,height-ship_height, ship_width, ship_height) # Rect() to draw rectangle, (200=x_co, height-ship_height = 800-60 to display in bottom of screen)

    clock = pygame.time.Clock() # clock object

    played_time = 0

    game_start_time = time.time() # provides current time

    meteor = 4000 # 2000 milliseconds in this case
    meteor_count = 0

    meteors = []
    hit  = False


    
    

    while run:
        

        clock.tick(500) # 60 = max number of frames pre sec also it returns the number of miiliseconds since the last clock tick
        meteor_count += clock.tick(60) # it returns the number of miiliseconds since the last clock tick
        played_time = time.time() - game_start_time
     
        
            

        if meteor_count > meteor: # condition to generate meteor
            for _ in range(7): # to add 5 meteors in each iteration 
                meteor_x = random.randint(0,width - meteor_width) # meteor_x = meteor ko x coordinates , [0,width - meteor_width]= coordinates
                meteor_generated = pygame.Rect(meteor_x, -meteor_height,meteor_width,meteor_height) # -meteor_height = - kinani to fall meteor from void
                meteors.append(meteor_generated)
            
            meteor = max(200,meteor - 50) # [meteor = max(200,meteor - 50)] = yesle chai meteor ko generate huni speed badauxa ,200 = min millisecond to generate meteor, 
            meteor_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        
        keys = pygame.key.get_pressed() # pygame.key.get_pressed() yeuta function ho jasle keyboard ko keys press gareko input linxa
        if keys[pygame.K_LEFT] and ship.x - ship_speed  >=0:# K_LEFT = left arrow key , K_A = a key, K_(any key)   [ship.x - ship_speed] = left wall stop condition
            ship.x -= ship_speed        # here hamle chai rect ko position vanda left tira 5 pixel le move garirako xau
        
        if keys[pygame.K_RIGHT] and ship.x + ship_speed + ship.width <= width: # [ship.x + ship_speed + ship.width <= width] = right wall stopping condition
            ship.x += ship_speed        #  ship.x = here x vaneko 200 ho from ship coordiinate [ship = pygame.Rect(200,height-ship_height, ship_width, ship_height)] 
        

        for meteor_generated in meteors[:]:
            meteor_generated.y += meteor_speed # moves meteor in down position,  meteor_generated.y = y_coordinate
            if meteor_generated.y > height:     # check if meteor has reached to min height
                meteors.remove(meteor_generated) # remove that meteor which has reached min height
            elif meteor_generated.y + meteor_generated.height >= ship.y and meteor_generated.colliderect(ship): # yesle check garxa if meteor ra ship collide vako xa ki nai vanera 
                meteors.remove(meteor_generated)
                hit  = True
                break
        
        if hit:
            lost_text = Font.render("You Lost", 1, "white")
            SCREEN.blit(lost_text,(500,300))
            pygame.display.update()
            pygame.time.delay(4000) # to pause game for 4000 milli
            break


        draw(ship,played_time,meteors)


    pygame.quit()


if __name__ == "__main__":
    main()

