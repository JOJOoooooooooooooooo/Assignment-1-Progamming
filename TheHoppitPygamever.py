import pygame
import sprite_sheet_module
#import imagio #look at this for gif making


#to initialize pygame
pygame.init()
#Initializing font for text
pygame.font.init()

#create game window
WIDTH, HEIGHT = 768, 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#set Game Window Title
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
    bg_image3 = pygame.image.load(f"tiles-broken-house.png").convert_alpha() #how to change x and y of one image of parallax list?
    bg_images.extend([bg_image1, bg_image2, bg_image3])
bg_width = bg_images[0].get_width()


#The images are now loaded but we need to draw them
def draw_bg():
    for x in range(7):
        speed = 0.5
        for i in bg_images:
            offset = (x * bg_width) - scroll * speed #scroll and speed maybe affecting player movement
            screen.blit(i, (offset, 0))
            speed += 0.2
            

#if abs(scroll) > bg_width:  for endless scrolling
    #scroll= 0
#Sprite Sheet for player
sprite_sheet_image = pygame.image.load('spritesheet-2.png').convert_alpha()
sprite_sheet = sprite_sheet_module.SpriteSheet(sprite_sheet_image)

#create animation list
animation_list = []
animation_steps = [3, 2, 3, 2, 3, 4, 4, 12]
action = 0
last_update = pygame.time.get_ticks() # taking the time from when we execute the code
animation_cooldown = 96 # "100" is in miliseconds
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_image_list = []
    for _ in range(animation):
        temp_image_list.append(sprite_sheet.get_image(step_counter, 64, 100, 1.5, "black")) # Step counter replaces x in order to get the specific animation to go to the next frame #replace the first number with x because in this loop x will change through the different sprites
        step_counter += 1
    animation_list.append(temp_image_list)



#frame_0 = sprite_sheet.get_image(0, 65, 46, 1.5, "black") # the order in the brackets are "sheet, frame, width, height, scale, colour"
#frame_1 = sprite_sheet.get_image(1, 65, 46, 1.5, "black") # we dont need to supply the sheet because its already there as an instance
#frame_2 = sprite_sheet.get_image(2, 65, 46, 1.5, "black")
#frame_3 = sprite_sheet.get_image(3, 65, 46, 1.5, "black")

#Drawing player
def draw(player):
    pygame.draw.rect(screen, "red", player)
    
#Player width and player height and movement
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 67
PLAYER_VELOCITY_X = 2
PLAYER_VELOCITY_Y = 15
jump = False



#creating and spawning player #IMPORTANT!!! KEEPING THIS CODE INSIDE THE GAME LOOP BREAKS PLAYER MOVEMENT, KEEP IT OUTSIDE
player = pygame.Rect(5 - scroll, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) #to get the player to spawn at the very edge on the left put x "200" to "0"
#in brackets it goes, x, y, width height. We did y = height of game minus player height to get the player to spawn at the bottom of the screen.
#this is always the format wheber you use a rectangle in pygame "pygame.Rect()"

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
    if frame >= len(animation_list[action]):
        frame = 0
        

    #show frame images
    screen.blit(animation_list[action][frame], (player.x-45, player.y -30)) #Draw the sprite animation at the players position
    
    #get key presses and speed of scrolling and limitations of scroll
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a] and key[pygame.K_d]:
        player.x = player.x
        action = 5

    elif key[pygame.K_a] and scroll > 0:
        player.x -= PLAYER_VELOCITY_X
        scroll -= PLAYER_VELOCITY_X
        action = 7
        
        
   
    elif key[pygame.K_d] and scroll < 1900 and WIDTH - PLAYER_WIDTH:
        player.x += PLAYER_VELOCITY_X
        scroll += PLAYER_VELOCITY_X
        action = 7
        #This makes it so that everytime we press or hold this key the frame will start at 0 and use the update animation code to hold it so that it never goes above its frame list 
    
    elif key[pygame.K_c]:  # Crouching Added
        action = 3
        animation_cooldown = 400 #Since crouch only has 2 frames, i lower the animation cooldown so it doesnt go too fast
        
    else:
        action = 5
        animation_cooldown = 96 #because I changed the animation cooldown I have to make sure I change it back after key is pressed
    
        
    
    #Jump Button
    if jump is False and key[pygame.K_SPACE]:
        jump = True

    if jump is True:
        player.y -= PLAYER_VELOCITY_Y
        PLAYER_VELOCITY_Y -= 1
        action = 6
        
        if PLAYER_VELOCITY_Y < -15:  
            jump = False
            PLAYER_VELOCITY_Y = 15
    
    #if key[pygame.K_SPACE]:
      #  player.y -= 10
    #Character movement key presses
    
    pygame.display.update()

pygame.quit()