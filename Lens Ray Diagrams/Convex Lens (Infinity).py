import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Convex Lens (Infinity)")

font_16 = pygame.font.Font("fonts/SF-Pro-Text-Bold.otf", 16)
font_23 = pygame.font.Font("fonts/SF-Pro-Text-Regular.otf", 23)

x1 = 10
x2 = 110
y1 = 200
y2 = 250
y3 = 350
y4 = 400
y11 = 200
y22 = 250
y33 = 350
y44 = 400

move = 5
o = False
f = False

running = True
while running:
    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.draw.ellipse(screen, (176, 200, 218), (385, 150, 30, 300))
        pygame.draw.line(screen, (255, 0, 0), (0, 300), (800, 300))

        pygame.draw.line(screen, (255, 0, 0), (200, 290), (200, 310))
        screen.blit(font_16.render("C", True, (255, 0, 0)), (195, 315))

        pygame.draw.line(screen, (255, 0, 0), (300, 290), (300, 310))
        screen.blit(font_16.render("F", True, (255, 0, 0)), (295, 315))

        pygame.draw.line(screen, (255, 0, 0), (400, 290), (400, 310))
        screen.blit(font_16.render("O", True, (255, 0, 0)), (395, 315))

        pygame.draw.line(screen, (255, 0, 0), (500, 290), (500, 310))
        screen.blit(font_16.render("F", True, (255, 0, 0)), (495, 315))

        pygame.draw.line(screen, (255, 0, 0), (600, 290), (600, 310))
        screen.blit(font_16.render("C", True, (255, 0, 0)), (595, 315))

        pygame.draw.line(screen, (255, 255, 255), (5, 190), (5, 410), 4)

        if not o:
            x1 += move
            x2 += move

            if x2 == 400:
                o = True

        if o and not f:
            move = 2
            x1 += move
            x2 += move

            y11 += 2
            y22 += 1
            y33 += -1
            y44 += -2

            if x2 == 500:
                f = True

        if f:
            move = 2
            x1 += move
            x2 += move

            y1 += 2
            y2 += 1
            y3 += -1
            y4 += -2

            y11 += 2
            y22 += 1
            y33 += -1
            y44 += -2

            if x2 > 605:
                move = 5
                x1 = 10
                x2 = 110
                y1 = 200
                y2 = 250
                y3 = 350
                y4 = 400
                y11 = 200
                y22 = 250
                y33 = 350
                y44 = 400

                o = False
                f = False

        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y11), 2)
        pygame.draw.line(screen, (255, 255, 255), (x1, y2), (x2, y22), 2)
        pygame.draw.line(screen, (255, 255, 255), (x1, 300), (x2, 300), 2)
        pygame.draw.line(screen, (255, 255, 255), (x1, y3), (x2, y33), 2)
        pygame.draw.line(screen, (255, 255, 255), (x1, y4), (x2, y44), 2)

        msg1 = "When an object is at infinity, the image formed at the focus is real and"
        msg2 = "point-sized, i.e., highly diminished."
        screen.blit(font_23.render(msg1, True, (255, 255, 255)), (5, 10))
        screen.blit(font_23.render(msg2, True, (255, 255, 255)), (5, 35))

        clock.tick(10)
        pygame.display.update()