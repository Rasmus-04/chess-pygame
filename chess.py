from funktions import *


def start():
    def draw_window():
        win.fill((0,0,255))
        draw_grid(win)

        for i in pos_sq:
            if len(i[2]) > 0:
                i[2][0].draw()

        pygame.display.update()

    run = True

    while run:
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                check_click(pygame.mouse.get_pos())


if __name__ == "__main__":
    start()
