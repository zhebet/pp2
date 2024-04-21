import pygame
import sys

def main():
    pygame.init()
    
    # Constants for the screen dimensions
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    
    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    # Sprite settings
    size = 50
    x, y = width // 2, height // 2
    speed = 5
    
    clock = pygame.time.Clock()
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Movement handling
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= speed
        if keys[pygame.K_RIGHT]:
            dx += speed
        if keys[pygame.K_UP]:
            dy -= speed
        if keys[pygame.K_DOWN]:
            dy += speed
        if keys[pygame.K_d]:  # Right
            dx += speed
        if keys[pygame.K_a]:  # Left
            dx -= speed
        if keys[pygame.K_w]:  # Up
            dy -= speed
        if keys[pygame.K_s]:  # Down
            dy += speed
        
        # Update sprite position with boundary checking
        x = max(0, min(width - size, x + dx))
        y = max(0, min(height - size, y + dy))
        
        # Screen clear and redraw
        screen.fill(black)
        pygame.draw.rect(screen, white, (x, y, size, size))
        pygame.display.flip()
        
        # Frame rate control
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()