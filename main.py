import pygame
from ship import Ship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner
from alert_box import AlertBox
from event_handler import EventHandler



pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

#display setup
display = pygame.display.set_mode(c.DISPLAY_SIZE) #variable for display size
fps = 60 #variable for frames per second
clock = pygame.time.Clock() #variable for pygame clock
black = (0, 0, 0)

#Object setup
event_handler = EventHandler()
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()

# Music setup
pygame.mixer.music.load('.\\sound_fx\\music\\Battle in the Stars.ogg')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=True)

#variable for game loopd
running = True

#game loop
while running:
    #tick clock
    clock.tick(fps)

    #handle events
    event_handler.handle_events(player)

    #update all the objects
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()
    particle_spawner.update()

    # Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible and not player.is_invincible:
            player.get_hit()
            enemy[0].hp = 0 
            enemy[0].get_hit()
    for enemy in enemy_spawner.enemy_group:
        collided = pygame.sprite.groupcollide(sprite_group, enemy.bullets, False, True)
        for player, bullet in collided.items():
            if not player.is_invincible:
                player.get_hit()


    #Check for game over
    if not player.is_alive:
        enemy_spawner.clear_enemies()
        alert_box = AlertBox('GAME OVER')


    #render displayd
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    for enemy in enemy_spawner.enemy_group:
        enemy.bullets.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.icons_group.draw(display)
    pygame.display.update()