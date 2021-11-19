from clases import *


def get_grid():
    # play area 600x600
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pos_sq.append([((WIDTH - 600) / 2 + i * 75, (HEIGHT - 600) / 2 + j * 75, 75), (255, 255, 255), []])
            else:
                pos_sq.append([((WIDTH - 600) / 2 + i * 75, (HEIGHT - 600) / 2 + j * 75, 75), (0, 0, 0), []])
get_grid()

def draw_grid(win):
    for i in pos_sq:
        pygame.draw.rect(win, i[1], (i[0][0], i[0][1], i[0][2], i[0][2]))


def check_click(pos):
    for i in pos_sq:
        x = i[0][0]
        y = i[0][1]
        if pos[0] > x and pos[0] < (x +i[0][2]):
            if pos[1] > y and pos[1] < (y + i[0][2]):
                #i[1] = (69,69,69)
                i[2] = [piece((x+8,y+15), queen_b)]
