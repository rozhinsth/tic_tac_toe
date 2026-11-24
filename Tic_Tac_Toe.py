import pygame

pygame.init()

screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("My First Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200,0,0)
GREEN =(0,200,0)

BG = (250, 246, 243)
CARD = (255, 252, 250)
PURPLE = (174, 151, 197)
LIGHT_PURPLE = (229, 218, 238)
PINK = (211, 145, 169)
DARK = (92, 79, 102)

SOFT_RED = (215, 145, 150)
HOVER_RED = (230, 165, 170)

SOFT_GREEN = (145, 185, 155)
HOVER_GREEN = (165, 205, 175)

running = True
clik = ['', '', '', '', '', '', '', '', '', ]
player = 'x'
win=[[0,1,2],[3,4,5],[6,7,8],[1,4,7],[2,5,8],[0,3,6],[2,4,6],[0,4,8]]
again = 7

font = pygame.font.SysFont("segoeui", 45)
title_font = pygame.font.SysFont("segoeui", 38, bold=True)
small_font = pygame.font.SysFont("segoeui", 23)
button_font = pygame.font.SysFont("segoeui", 25, bold=True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # row = ستون
            # col = ردیف
            if 100 < x < 400 and 100 < y < 400:
                row = y
                col = x
                col -= 100
                col = col // 100
                row -= 100
                row = row // 100
                num = row * 3 + col
                if clik[num] == '' and again == 7 :
                    clik[num] = player
                    for line in win:
                        if clik[line[0]] == clik[line[1]] == clik[line[2]] != '':
                            again = 3
                            t = pygame.time.get_ticks()
                    if '' not in clik and again != 3:
                        again = 4
                        t = pygame.time.get_ticks()

                    if player == 'x':
                        player = 'o'
                    else:
                        player = 'x'

            if 300 < x < 450 and 500 < y < 550 and again != 7:
                clik = ['', '', '', '', '', '', '', '', '', ]
                again = 7
                player = "x"

            if 100 < x < 250 and 500 < y < 550 and again != 7:
                running = False

    # Background
    screen.fill(BG)

    # Title
    title = title_font.render("TIC TAC TOE", True, DARK)
    screen.blit(title, (175, 25))

    subtitle = small_font.render("Let's play together!", True, PURPLE)
    screen.blit(subtitle, (205, 67))

    # Game board background
    pygame.draw.rect(screen, CARD, (75, 95, 350, 350), border_radius=20)

    # Mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Hover effect for cells
    if 100 < mouse_x < 400 and 100 < mouse_y < 400 and again == 7:
        row_hover = (mouse_y - 100) // 100
        col_hover = (mouse_x - 100) // 100
        hover_num = row_hover * 3 + col_hover

        if clik[hover_num] == '':
            hover_x = 100 + col_hover * 100
            hover_y = 100 + row_hover * 100
            pygame.draw.rect(screen, LIGHT_PURPLE,
                             (hover_x + 8, hover_y + 8, 84, 84),
                             border_radius=15)

    # Board lines
    pygame.draw.rect(screen, PURPLE, (196, 100, 8, 300), border_radius=4)
    pygame.draw.rect(screen, PURPLE, (296, 100, 8, 300), border_radius=4)
    pygame.draw.rect(screen, PURPLE, (100, 196, 300, 8), border_radius=4)
    pygame.draw.rect(screen, PURPLE, (100, 296, 300, 8), border_radius=4)

    # Win and draw messages
    if again == 3:
        text = font.render('You won!', True, PINK)
        screen.blit(text, (195, 440))

    if again == 4:
        text = font.render('Try again!', True, PURPLE)
        screen.blit(text, (180, 430))

    now = pygame.time.get_ticks()

    if again == 7:
        turn_text = small_font.render("Current turn: " + player.upper(),
                                      True, DARK)
        screen.blit(turn_text, (205, 455))

    if again != 7 and now-t>1500:

        # Quit button
        if 100 < mouse_x < 250 and 500 < mouse_y < 550:
            quit_color = HOVER_RED
        else:
            quit_color = SOFT_RED

        pygame.draw.rect(screen, quit_color,
                         (100, 500, 150, 50), border_radius=15)

        quit_text = button_font.render('Quit', True, WHITE)
        screen.blit(quit_text, (145, 509))

        # Return button
        if 300 < mouse_x < 450 and 500 < mouse_y < 550:
            return_color = HOVER_GREEN
        else:
            return_color = SOFT_GREEN

        pygame.draw.rect(screen, return_color,
                         (300, 500, 150, 50), border_radius=15)

        return_text = button_font.render('Return', True, WHITE)
        screen.blit(return_text, (326, 509))

    # Draw X and O
    for i in range(9):
        row = i // 3
        col = i % 3
        cx = 150 + col * 100
        cy = 150 + row * 100

        if clik[i] == 'o':
            pygame.draw.circle(screen, PURPLE, (cx, cy), 29, 7)

        elif clik[i] == 'x':
            pygame.draw.line(screen, PINK,
                             (cx-25, cy-25), (cx+25, cy+25), 7)
            pygame.draw.line(screen, PINK,
                             (cx+25, cy-25), (cx-25, cy+25), 7)

    pygame.display.flip()

pygame.quit()

