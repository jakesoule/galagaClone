import pygame

class EventHandler:
    def __init__(self):
        pass

    def handle_events(self, actor):
    #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    actor.vel_x = -actor.speed
                elif event.key == pygame.K_d:
                    actor.vel_x = actor.speed

                if event.key == pygame.K_SPACE:
                    actor.shoot()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    actor.vel_x = 0
                elif event.key == pygame.K_d:
                    actor.vel_x = 0