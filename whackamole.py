import pygame
import random

pygame.display.set_caption("Holly's Whack A Mole")

def draw_lines(screen,Width,Height,square_width):
    line_Color=(61, 110, 92)
    #prints row
    for i in range(1,16):
        pygame.draw.line(screen, line_Color, (0, i*square_width), (Width, i*square_width))
    #prints cols
    for i in range(1,20):
        pygame.draw.line(screen, line_Color, (i * square_width,0), ( i * square_width,Height))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        #I added
        Width = screen.get_width()
        Height = screen.get_height()
        square_width = Height / 16

        mole_x =0
        mole_y=0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    col = position[0]//square_width
                    row =position[1]//square_width
                    if mole_x==col and mole_y==row:
                        mole_x= random.randrange(0, 19)
                        mole_y=random.randrange(0, 15)

            screen.fill("light green")
            draw_lines(screen, Width, Height, square_width)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*square_width, mole_y*square_width)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
