import math
import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0
active_color = 'white'

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []


def draw_menu():
    circle_brush = [pygame.draw.rect(screen, 'white', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'black', (35, 35), 20)
    pygame.draw.circle(screen, 'white', (35, 35), 18)

    rect_brush = [pygame.draw.rect(screen, 'white', [10, 70, 50, 50]), 1]
    pygame.draw.rect(screen, 'black', [15, 70, 37, 20], 2)
    # Adding other brushes
    square_brush = [pygame.draw.rect(screen, 'white', [10, 100, 50, 50]), 2]
    pygame.draw.rect(screen, 'black', [15, 100, 35, 35], 2)

    right_triangle_brush = [
        pygame.draw.rect(screen, 'white', [10, 150, 50, 50]), 3
    ]
    pygame.draw.polygon(screen, 'black', [(15, 180), (55, 180), (15, 140)], 2)

    equilateral_triangle_brush = [
        pygame.draw.rect(screen, 'white', [10, 190, 50, 50]), 4
    ]
    side_length = 50
    center_x = 10 + side_length / 2
    center_y = 190 + side_length / 2
    triangle_height = side_length * math.sqrt(3) / 2
    triangle_height *= 1
    vertex1 = (center_x, center_y - triangle_height / 2)
    vertex2 = (center_x - side_length / 2 * 0.9,
               center_y + triangle_height / 2 * 0.9)
    vertex3 = (center_x + side_length / 2 * 0.9,
               center_y + triangle_height / 2 * 0.9)
    pygame.draw.polygon(screen, 'black', [vertex1, vertex2, vertex3], 2)

    rhombus_brush = [pygame.draw.rect(screen, 'white', [10, 250, 50, 50]), 5]
    top_left = (10, 250)
    top_right = (60, 250)
    bottom_left = (10, 300)
    bottom_right = (60, 300)
    mid_top = ((top_left[0] + top_right[0]) // 2,
               (top_left[1] + top_right[1]) // 2 + 4)
    mid_left = ((top_left[0] + bottom_left[0]) // 2 + 4,
                (top_left[1] + bottom_left[1]) // 2)
    mid_bottom = ((bottom_left[0] + bottom_right[0]) // 2,
                  (bottom_left[1] + bottom_right[1]) // 2 - 4)
    mid_right = ((top_right[0] + bottom_right[0]) // 2 - 4,
                 (top_right[1] + bottom_right[1]) // 2)
    pygame.draw.polygon(screen, 'black',
                        [mid_top, mid_left, mid_bottom, mid_right], 2)

    brush_list = [
        circle_brush, rect_brush, square_brush, right_triangle_brush,
        equilateral_triangle_brush, rhombus_brush
    ]

    eraser = pygame.image.load("images/eraser.png")
    eraser_rect = eraser.get_rect(topleft=(18, 320))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser, [18, 320, 25, 25])

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 40, 100, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 40, 130, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 40, 160, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 40, 190, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 40, 220, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 40, 250, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 40, 280, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list


def draw_painting(paints):
    for color, pos, figure in paints:
        if color == (255, 255, 255):
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, 20, 2)
            elif figure == 1:
                pygame.draw.rect(screen, color,
                                 [pos[0] - 15, pos[1] - 15, 37, 20], 2)
            elif figure == 2:
                pygame.draw.rect(screen, color,
                                 [pos[0] - 15, pos[1] - 15, 35, 35],
                                 2)  # Draw a square
            elif figure == 3:
                pygame.draw.polygon(screen, color,
                                    [(pos[0] - 15, pos[1] + 15),
                                     (pos[0] + 20, pos[1] + 15),
                                     (pos[0] - 15, pos[1] - 20)],
                                    2)  # Draw a right triangle
            elif figure == 4:
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (pos[0], pos[1] - triangle_height / 2)
                vertex2 = (pos[0] - size / 2, pos[1] + triangle_height / 2)
                vertex3 = (pos[0] + size / 2, pos[1] + triangle_height / 2)
                pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3],
                                    2)  # Draw an equilateral triangle
            elif figure == 5:
                pygame.draw.polygon(screen, color, [(pos[0] - 25, pos[1]),
                                                    (pos[0], pos[1] - 25),
                                                    (pos[0] + 25, pos[1]),
                                                    (pos[0], pos[1] + 25)],
                                    2)  # Draw a rhombus


run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs = draw_menu()

    if left_click and mouse[0] > 70 and mouse[0] < WIDTH - 70:
        painting.append((active_color, mouse, active_figure))
    draw_painting(painting)

    if mouse[0] > 70:
        if active_color == (255, 255, 255):
            pygame.draw.rect(screen, active_color,
                             [mouse[0] - 15, mouse[1] - 15, 37, 20])
        else:
            if active_figure == 0:
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:
                pygame.draw.rect(screen, active_color,
                                 [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
            elif active_figure == 2:  # Square
                pygame.draw.rect(screen, active_color,
                                 [mouse[0] - 15, mouse[1] - 15, 35, 35], 2)
            elif active_figure == 3:  # Right triangle
                pygame.draw.polygon(screen, active_color,
                                    [(mouse[0] - 15, mouse[1] + 15),
                                     (mouse[0] + 20, mouse[1] + 15),
                                     (mouse[0] - 15, mouse[1] - 20)], 2)
            elif active_figure == 4:  # Equilateral triangle
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (mouse[0], mouse[1] - triangle_height / 2)
                vertex2 = (mouse[0] - size / 2, mouse[1] + triangle_height / 2)
                vertex3 = (mouse[0] + size / 2, mouse[1] + triangle_height / 2)
                pygame.draw.polygon(screen, active_color,
                                    [vertex1, vertex2, vertex3], 2)
            elif active_figure == 5:  # Rhombus
                pygame.draw.polygon(screen, active_color,
                                    [(mouse[0] - 25, mouse[1]),
                                     (mouse[0], mouse[1] - 25),
                                     (mouse[0] + 25, mouse[1]),
                                     (mouse[0], mouse[1] + 25)], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

    pygame.display.flip()

pygame.quit()