import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #pygame.Surface.fill(screen, "black")
        screen.fill("black")

        #pygame.draw.polygon(screen,"white", player.triangle(), 2)
        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()