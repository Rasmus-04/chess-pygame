import pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))

pos_sq = []
avible_pos = []
a_h = "abcdefgh"
active_piece = None

light = (250,229,174)
dark = (226,135,67)

light_active = (69,175,201)
dark_active = (3,52,108)


# white pices
queen_w = pygame.image.load("img/queen_w.png")
king_w = pygame.image.load("img/king_w.png")
pawn_w = pygame.image.load("img/pawn_w.png")
knigt_w = pygame.image.load("img/knight_w.png")
bishop_w = pygame.image.load("img/bishop_w.png")
rook_w = pygame.image.load("img/rook_w.png")


# black pices
queen_b = pygame.image.load("img/queen_b.png")
king_b = pygame.image.load("img/king_b.png")
pawn_b = pygame.image.load("img/pawn_b.png")
knigt_b = pygame.image.load("img/knight_b.png")
bishop_b = pygame.image.load("img/bishop_b.png")
rook_b = pygame.image.load("img/rook_b.png")
