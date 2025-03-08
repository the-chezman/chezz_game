import pygame

# i made a branch

# sets up main pygame basics

pygame.init() # intializes module
WIDTH = 1000 # sets screen width
HEIGHT = 900 # sets screen height
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # calls display to set dimensions
pygame.display.set_caption("chess wow") # sets application title
font = pygame.font.Font("freesansbold.ttf", 20) # calls font to set small font
big_font = pygame.font.Font("freesansbold.ttf", 50) # calls font to set large font
timer = pygame.time.Clock() # calls time to set a clock
fps = 60 # sets the frame per second

# sets up pieces and their images

white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", # sets white pieces
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), # top left is (0, 0) | bottom right is (7, 7)
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), ] # white at the top of board

black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), # top left is (0, 0) | bottom right is (7, 7)
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), ] # white at the top of board

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0 # 0 - white turn, no selection | 1 - white turn, piece selected | 2 - black turn, no selection | 3 - black turn, pirce selected
selection = -1 # index selection, -1 since no index exists on here
valid_moves = [] # displays all valid squares of movement, blank for later use

# sets up images for pieces

white_pawn = pygame.image.load("chess_game/assets_chess/white_pawn.png") # loads image into variable
white_pawn = pygame.transform.scale(white_pawn, (80, 80)) # scales image to fit in square
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45)) # scales image to fit in side bar (after capture)
black_pawn = pygame.image.load("chess_game/assets_chess/black_pawn.png")
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_rook = pygame.image.load("chess_game/assets_chess/white_rook.png")
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
black_rook = pygame.image.load("chess_game/assets_chess/black_rook.png")
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
white_knight = pygame.image.load("chess_game/assets_chess/white_knight.png")
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
black_knight = pygame.image.load("chess_game/assets_chess/black_knight.png")
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
white_bishop = pygame.image.load("chess_game/assets_chess/white_bishop.png")
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
black_bishop = pygame.image.load("chess_game/assets_chess/black_bishop.png")
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
white_king = pygame.image.load("chess_game/assets_chess/white_king.png")
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
black_king = pygame.image.load("chess_game/assets_chess/black_king.png")
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
white_queen = pygame.image.load("chess_game/assets_chess/white_queen.png")
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
black_queen = pygame.image.load("chess_game/assets_chess/black_queen.png")
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop] # easy access list for later
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"] # associate name with image, VERY IMPORTANT THAT THIS ORDER IS SAME AS CHESS PIECES LIST

# draw main game board

def draw_board():
    for i in range(32): # draw 32 squares since background is already dark gray
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "light gray", [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, "light gray", [700 - (column * 200), row * 100, 100, 100]) # draws rect offset
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100]) #bottom box
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5) #bottom box borders
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5) #side box borders
        status_text = ["hey white choose a piece", "hey white choose your move",
                       "hey black choose a piece", "hey black choose your move"] #text corresponding to turn_step
        screen.blit(big_font.render(status_text[turn_step], True, "black"), (20, 820)) #render(text, anti alias, color) | blit(image, position)

        for i in range(9): #draws lines to act as grid
            pygame.draw.line(screen, "black", (0, 100 * i), (800, 100 * i), 2) #horizontal, y val changes
            pygame.draw.line(screen, "black", (100 * i, 0), (100 * i, 800), 2) #vertical, x val changes

#important to setup AFTER draw_board, since board may override pieces

def draw_pieces():
    for i in range(len(white_pieces)): #white_pieces len can change
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 12)) # sets up white pawns
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10)) # sets up other white pieces
        if turn_step < 2: # according to turn_step, will guarantee white's move
            if selection == i:
                pygame.draw.rect(screen, "red", [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 2) # draw red rect

    for i in range(len(black_pieces)): 
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == "pawn":
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 12)) # sets up black pawns
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))# sets up other black pieces
        if turn_step >= 2: # according to turn_step, will guarantee black's move
            if selection == i:
                pygame.draw.rect(screen, "blue", [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2) # draw blue rect


# sets up event handler

run = True
while run:
    timer.tick(fps) # game runs at 60 fps
    screen.fill("dark gray") # background color is dark gray
    draw_board()
    draw_pieces()

    # handles all events like keyboard presses and mouse clicks
    for event in pygame.event.get():  # checks each event
        if event.type == pygame.QUIT: # if event is click X button
            run = False

    pygame.display.flip() # clears display

pygame.quit() # quits module