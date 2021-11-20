from funktions import *


def start():
    get_grid()
    start_place()

    def draw_window():
        win.fill((0,0,0))
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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            start_place()


if __name__ == "__main__":
    start()
