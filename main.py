import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    score = 0
    lives = 3

    score_counter_font = pygame.font.SysFont('Arial', 40)
    life_counter_font = pygame.font.SysFont('Arial', 40)
    intro_font = pygame.font.SysFont('Arial', 100)

    intro_text = intro_font.render("Asteroids!", False, "white")
    intro_text_size = (intro_font.size("Asteroids"))
    intro_timer = INTRO_DURATION

    while True:
        # detect if the program should end
        for event in pygame.event.get():
            # if the close button on the window is pressed
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        # if the escape key is pressed
        if keys[pygame.K_ESCAPE]:
            sys.exit()
            
        # draw black background
        screen.fill("black")

        life_counter_text = life_counter_font.render(f"lives left: {lives}", False, "white")
        score_counter_text = score_counter_font.render(f"score: {score}", False, "white")
        screen.blit(life_counter_text, (0,SCREEN_HEIGHT-40))
        screen.blit(score_counter_text, (SCREEN_WIDTH-180 ,SCREEN_HEIGHT-40))

        # display intro splash
        if intro_timer > 1:
            screen.blit(intro_text, ((SCREEN_WIDTH / 2) - (intro_text_size[0]/2) , (SCREEN_HEIGHT / 4)))
            intro_timer -= 1

        # update positions of all updatable entities
        updatable.update(dt)

        # redraw all drawable entities at updated locations
        for object in drawable:
            if object == player and player.recovering == True and player.invuln_timer % 10 > 5:
                pass
            else:    
                object.draw(screen)

        # collision detection for player, asteroids, and shots
        for asteroid in asteroids:
            # only evaluate player collision if not recovering
            if player.recovering == False:
                if asteroid.collides(player):
                    if lives < 1:
                        print("Game over!")
                        print(f"Final score: {score}")
                        sys.exit()
                    else:
                        print("Life lost!")
                        lives -= 1
                        if lives == 1:
                            print(f"{lives} life left")
                        else:
                            print(f"{lives} lives left")
                        player.respawn()

            # always evaluate shot collision with asteroids
            for shot in shots:        
                if asteroid.collides(shot):
                    score += 1
                    shot.kill()
                    asteroid.split()

        # evaluate respawn invulnerability for player
        if player.recovering == True:
            player.invuln_timer -= 1
            if player.invuln_timer < 1:
                #print("invuln ended")
                player.recovering = False

        # not really sure.. update display?
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(FPS_LIMIT) / 1000

if __name__ == "__main__":
    main()