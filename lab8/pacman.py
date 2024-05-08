import pygame
import sys
import math
import random

# Constants
width, height = 640, 640
fps = 30
pellet_cl = (200, 200, 0)
pellet_score = 10
num_pellets = 20
num_power_ups = 5

# Colors
black =  (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

# Load power-up image
power_up_image = pygame.image.load('/Users/jebe/power_up.png')  
power_up_image = pygame.transform.scale(power_up_image, (40, 40))  

pygame.mixer.init()  # Initialize the mixer module
eat_pellet_sound = pygame.mixer.Sound('/Users/jebe/eat_pellet.wav')


# Pacman settings
x, y = width // 2, height // 2 #initial position
speed = 5 #скорость пакмана
radius = 20 #радиус пакмана
open_m = 0  # насколько рот открывается
open_s = 3  # скорость открытия рта
mouth_dir = 1  # 1 откр,-1 закр
speed_boost_dur = 0  # Duration left on speed boost

# Pellets and Power-ups positions
pellets = [(random.randint(radius, width - radius), random.randint(radius, height - radius)) for _ in range(num_pellets)]
power_ups = [(random.randint(radius, width - radius), random.randint(radius, height - radius)) for _ in range(num_power_ups)]

# Score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement controls
    keys = pygame.key.get_pressed()
    if speed_boost_dur > 0:
        speed_boost_dur -= 1
    effective_speed = speed * 2 if speed_boost_dur > 0 else speed

    if keys[pygame.K_LEFT]:
        x -= effective_speed
    if keys[pygame.K_RIGHT]:
        x += effective_speed
    if keys[pygame.K_UP]:
        y -= effective_speed
    if keys[pygame.K_DOWN]:
        y += effective_speed
    if keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        x -= effective_speed*2
    if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        x += effective_speed*2
    if keys[pygame.K_UP] and keys[pygame.K_SPACE]:
        y -= effective_speed*2
    if keys[pygame.K_DOWN] and keys[pygame.K_SPACE]:
        y += effective_speed*2
    # Compute movement
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * effective_speed
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * effective_speed

    # Update sprite position with boundary checking
    x = max(radius, min(width - radius, x + dx))
    y = max(radius, min(height - radius, y + dy))

    # Update mouth opening
    open_m += mouth_dir * open_s
    if open_m > 40 or open_m < 0:
        mouth_dir *= -1
        open_m = max(0, min(40,open_m))

    # Eat pellets
    remaining_pellets = []
    for pellet in pellets:
        if (x - pellet[0])**2 + (y - pellet[1])**2 < radius**2:
            score += pellet_score
            eat_pellet_sound.play()
        else:
            remaining_pellets.append(pellet)
    pellets = remaining_pellets

    # Eat power-ups
    remaining_power_ups = []
    for power in power_ups:
        if (x - power[0])**2 + (y - power[1])**2 < radius**2:
            speed_boost_duration = fps * 5  # 5 seconds of speed boost
        else:
            remaining_power_ups.append(power)
    power_ups = remaining_power_ups

    # Draw everything
    screen.fill(black)
    # Draw Pacman with a filled sector
    angle_offset = open_m / 2
    end_angle = 360 - angle_offset
    pygame.draw.circle(screen, yellow, (x, y), radius)  # Draw filled circle first
    pygame.draw.polygon(screen, black, [(x, y),
                                        (x + radius * math.cos(math.radians(angle_offset)), y +radius * math.sin(math.radians(angle_offset))),
                                        (x + radius * math.cos(math.radians(end_angle)), y + radius * math.sin(math.radians(end_angle)))])
   
    # Draw pellets and power-ups
    for pellet in pellets:
        pygame.draw.circle(screen, pellet_cl, pellet, 5)
    for power in power_ups:
        screen.blit(power_up_image, (power[0] - 10, power[1] - 10))
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, yellow)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()