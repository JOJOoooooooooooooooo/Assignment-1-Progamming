import pygame
import sprite_sheet_module

#to initialize pygame
pygame.init()

#Initializing font for text
pygame.font.init()

#create game window
WIDTH, HEIGHT = 768, 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set game window title
pygame.display.set_caption("ParallaxHoppitTest")

#for framerate
clock = pygame.time.Clock()
FPS = 60

#define game variables
scroll = 0

#adding images to window
bg_images = []
for i in range(1, 3):
    bg_image1 = pygame.image.load(f"clouds-1.png").convert_alpha()
    bg_image2 = pygame.image.load(f"town-2.png").convert_alpha()
    bg_image3 = pygame.image.load(f"tiles-broken-house.png").convert_alpha()
    bg_images.extend([bg_image1, bg_image2, bg_image3])
bg_width = bg_images[0].get_width()

#The images are now loaded but we need to draw them
def draw_bg():
    for x in range(7):
        speed = 0.5
        for i in bg_images:
            offset = (x * bg_width) - scroll * speed
            screen.blit(i, (offset, 0))
            speed += 0.2

#Sprite Sheet for player
sprite_sheet_image = pygame.image.load('gothic-hero-run.png').convert_alpha()
sprite_sheet = sprite_sheet_module.SpriteSheet(sprite_sheet_image)

#create animation list
animation_list = []
animation_steps = 12
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 65, 46, 1.5, "black"))

#Player width and player height and movement
PLAYER_WIDTH = 65
PLAYER_HEIGHT = 46
PLAYER_VELOCITY = 2

#creating and spawning player
player = pygame.Rect(200 - scroll, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

#creating background music
pygame.mixer.init()
pygame.mixer.music.load("Quest for the Enchanted Blade.mp3") 
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#player function
def player_func(player):
    hitbox = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT), pygame.SRCALPHA)  # Create an invisible surface for the hitbox
    pygame.draw.rect(hitbox, (255, 0, 0, 0), hitbox.get_rect())  # Draw the hitbox on the surface
    screen.blit(hitbox, (player.x, player.y))  # Blit the hitbox surface at the player's position

#game loop
run = True
while run:

    clock.tick(FPS)

    #Draw World
    draw_bg()

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    #show frame images
    screen.blit(animation_list[frame], (player.x, player.y))

    #draw player hitbox
    player_func(player)

    #get key presses and speed of scrolling and limitations of scroll
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_VELOCITY
        scroll -= PLAYER_VELOCITY
    if key[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_WIDTH:
        player.x += PLAYER_VELOCITY
        scroll += PLAYER_VELOCITY
    if key[pygame.K_UP]:
        player.y -= 10

    pygame.display.update()

pygame.quit()