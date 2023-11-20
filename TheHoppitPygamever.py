import pygame
import sprite_sheet_module

#to initialize pygame
pygame.init()
#Initializing font for text
pygame.font.init()

#create game window
WIDTH, HEIGHT = 768, 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    bg_images.extend([bg_image1, bg_image2])
bg_width = bg_images[0].get_width()

#The images are now loaded but we need to draw them
def draw_bg():
    for x in range(5):
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
last_update = pygame.time.get_ticks() # taking the time from when we execute the code
animation_cooldown = 100 # "100" is in miliseconds
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 65, 46, 1.5, "black"))#replace the first number with x because in this loop x will change through the different sprites

#frame_0 = sprite_sheet.get_image(0, 65, 46, 1.5, "black") # the order in the brackets are "sheet, frame, width, height, scale, colour"
#frame_1 = sprite_sheet.get_image(1, 65, 46, 1.5, "black") # we dont need to supply the sheet because its already there as an instance
#frame_2 = sprite_sheet.get_image(2, 65, 46, 1.5, "black")
#frame_3 = sprite_sheet.get_image(3, 65, 46, 1.5, "black")

#Drawing player
def draw(player):
    pygame.draw.rect(screen, "red", player)
    
#Player width and player height and movement
PLAYER_WIDTH = 65
PLAYER_HEIGHT = 46
PLAYER_VELOCITY = 3.5

#creating background music
pygame.mixer.init() # the order for inside the brackets would go ( 44100, -16, 2, 2048) Frequency, size, channels, buffer

pygame.mixer.music.load("Quest for the Enchanted Blade.mp3") 
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) #-1 so that every time the song ends it will play it again

#game loop
run = True
while run:

    clock.tick(FPS)
    #Draw World
    draw_bg()

    #creating and spawning player
    player = pygame.Rect(200 - scroll, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) #to get the player to spawn at the very edge on the left put x "200" to "0"
    #in brackets it goes, x, y, width height. We did y = height of game minus player height to get the player to spawn at the bottom of the screen.
    #this is always the format wheber you use a rectangle in pygame "pygame.Rect()"

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw(player)
    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    #show frame images
    screen.blit(animation_list[frame], (300, 320))
    
    #get key presses and speed of scrolling and limitations of scroll
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 3.5
        
    if key[pygame.K_RIGHT] and scroll < 1900:
        scroll += 3.5
    #Character movement key presses
    if key[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_VELOCITY
    if key[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_WIDTH: #Player movement does not currently work
        player.x += PLAYER_VELOCITY
    pygame.display.update()

pygame.quit()