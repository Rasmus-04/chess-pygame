from clases import *


def get_grid():
    # play area 600x600
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pos_sq.append([((WIDTH - 600) / 2 + i * 75, (HEIGHT - 600) / 2 + j * 75, 75), light, [], (a_h[i] + str(8-j))])
            else:
                pos_sq.append([((WIDTH - 600) / 2 + i * 75, (HEIGHT - 600) / 2 + j * 75, 75), dark, [], (a_h[i] + str(8-j))])


def draw_grid(win):
    for i in pos_sq:
        pygame.draw.rect(win, i[1], (i[0][0], i[0][1], i[0][2], i[0][2]))


def check_click(pos):
    global active_piece
    for i in pos_sq:
        x = i[0][0]
        y = i[0][1]
        if pos[0] > x and pos[0] < (x +i[0][2]):
            if pos[1] > y and pos[1] < (y + i[0][2]):
                if len(i[2]) > 0 and active_piece == None:
                    active_piece = i[3]
                    posible_pos(i)
                    print(active_piece)

                elif active_piece != None:
                    if i[2] == []:
                        for j in pos_sq:
                            if j[3] == active_piece:
                                if len(avible_pos) > 0:
                                    for s in avible_pos:
                                        if i[3] == pos_sq[s][3]:
                                            i[2] = j[2]
                                            i[2][0].pos = (i[0][0]+8, i[0][1]+15)
                                            j[2] = []
                                            active_piece = None
                                            clear_avilble_pos()
                    else:
                        active_piece = None
                        clear_avilble_pos()


def start_place():
    for i in pos_sq:
        x = i[0][0]
        y = i[0][1]
        row = i[3][1]
        rc = i[3]

        if row == "2":
            i[2] = [piece((x+8,y+15), pawn_w)]
        elif row == "7":
            i[2] = [piece((x + 8, y + 15), pawn_b)]

        elif rc == "b1" or rc == "g1":
            i[2] = [piece((x + 8, y + 15), knigt_w)]
        elif rc == "b8" or rc == "g8":
            i[2] = [piece((x + 8, y + 15), knigt_b)]

        elif rc == "c1" or rc == "f1":
            i[2] = [piece((x + 8, y + 15), bishop_w)]
        elif rc == "f8" or rc == "c8":
            i[2] = [piece((x + 8, y + 15), bishop_b)]

        elif rc == "a1" or rc == "h1":
            i[2] = [piece((x + 8, y + 15), rook_w)]
        elif rc == "a8" or rc == "h8":
            i[2] = [piece((x + 8, y + 15), rook_b)]

        elif rc == "d1":
            i[2] = [piece((x + 8, y + 15), queen_w)]
        elif rc == "d8":
            i[2] = [piece((x + 8, y + 15), queen_b)]

        elif rc == "e1":
            i[2] = [piece((x + 8, y + 15), king_w)]
        elif rc == "e8":
            i[2] = [piece((x + 8, y + 15), king_b)]

        else:
            i[2] = []


def posible_pos(pice):
    if pice[2][0].sprite == pawn_b:
        for index, i in enumerate(pos_sq):
            if i[3][0] == active_piece[0]:
                if int(i[3][1]) == (int(active_piece[1]) - 1):
                    if len(i[2]) == 0:
                        avible_pos.append(index)
                        if i[1] == light:
                            i[1] = light_active
                        else:
                            i[1] = dark_active
                    else:
                        return
                if int(i[3][1]) == (int(active_piece[1]) - 2):
                    if len(i[2]) == 0:
                        avible_pos.append(index)
                        if i[1] == light:
                            i[1] = light_active
                        else:
                            i[1] = dark_active

    if pice[2][0].sprite == pawn_w:
        for index, i in enumerate(pos_sq):
            if i[3][0] == active_piece[0]:
                if int(i[3][1]) == (int(active_piece[1]) + 1):
                    if len(i[2]) == 0:
                        avible_pos.append(index)
                        if i[1] == light:
                            i[1] = light_active
                        else:
                            i[1] = dark_active
                    else:
                        return
                if int(i[3][1]) == (int(active_piece[1]) + 2):
                    if len(i[2]) == 0:
                        avible_pos.append(index)
                        if i[1] == light:
                            i[1] = light_active
                        else:
                            i[1] = dark_active

def clear_avilble_pos():
    if len(avible_pos) > 0:
        for i in avible_pos:
            if pos_sq[i][1] == dark_active:
                pos_sq[i][1] = dark
            else:
                pos_sq[i][1] = light

    avible_pos.clear()
