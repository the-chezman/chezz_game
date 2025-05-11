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

white_pawn = pygame.image.load("assets_chess/white_pawn.png") # loads image into variable
white_pawn = pygame.transform.scale(white_pawn, (80, 80)) # scales image to fit in square
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45)) # scales image to fit in side bar (after capture)
black_pawn = pygame.image.load("assets_chess/black_pawn.png")
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_rook = pygame.image.load("assets_chess/white_rook.png")
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
black_rook = pygame.image.load("assets_chess/black_rook.png")
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
white_knight = pygame.image.load("assets_chess/white_knight.png")
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
black_knight = pygame.image.load("assets_chess/black_knight.png")
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
white_bishop = pygame.image.load("assets_chess/white_bishop.png")
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
black_bishop = pygame.image.load("assets_chess/black_bishop.png")
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
white_king = pygame.image.load("assets_chess/white_king.png")
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
black_king = pygame.image.load("assets_chess/black_king.png")
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
white_queen = pygame.image.load("assets_chess/white_queen.png")
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
black_queen = pygame.image.load("assets_chess/black_queen.png")
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop] # easy access list for later
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"] # associate name with image, VERY IMPORTANT THAT THIS ORDER IS SAME AS CHESS PIECES LIST

counter = 0 #flasher
winner = ""
game_over = False

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
        screen.blit(big_font.render("resign", True, "black"), (810, 810))

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

#checks all options for pieces to move on board - valid spots

def check_options(pieces, locations, turn):
    moves_list = [] #initializes lists to be empty
    all_moves_list = []

    for i in range(len(pieces)): #goes through all pieces
        location = locations[i] #checks current location
        piece = pieces[i] #checks current piece

        if piece == "pawn": # gives full check if the piece at this location is this piece
            moves_list = check_pawn(location, turn) # will update list based on valid moves
        elif piece == "rook":
            moves_list = check_rook(location, turn)
        elif piece == "knight":
            moves_list = check_knight(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop(location, turn)
        elif piece == "queen":
            moves_list = check_queen(location, turn)
        elif piece == "king":
            moves_list = check_king(location, turn)

        all_moves_list.append(moves_list)



    return all_moves_list

# all individual checking functions

def check_king(position, color):
    moves_list = []
    if color == "white":
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations

    # 8 spots for king
    targets = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,1), (0,-1)]

    for i in range(8): #can use code for knight as only target coordinates change
        target = (position[0] + targets[i][0], position[1] + targets[i][1])

        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7: #checks valid moves
            moves_list.append(target)
    
    return moves_list

def check_queen(position, color):
    moves_list = check_bishop(position, color) #can use existing functions to simplify queen's movement
    second_list = check_rook(position, color) #queen is combo of rook and bishop movement

    for i in range(len(second_list)):
        moves_list.append(second_list[i]) #adds rook moves to bishop moves list
    
    return moves_list

def check_bishop(position, color):
    moves_list = []
    if color == "white":
        enemies_list = black_locations  #sets up enemies and friends lists
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations

    for i in range(4): # up-right, up-left, down-right, down-left
        path = True 
        chain = 1 

        if i == 0:
            x = 1
            y = -1 #just changing coordinates
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        elif i == 3:
            x = -1
            y = 1

        while path: # why this works: bishop has same path determination as rook (all valid spots in available directions) so can just change og coords to work 
            if (position[0] + (chain * x), (position[1] + (chain * y))) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                
                moves_list.append((position[0] + (chain * x), (position[1] + (chain * y))))

                if (position[0] + (chain * x), (position[1] + (chain * y))) in enemies_list: 
                    path = False
                chain += 1 
            else:
                path = False

    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == "white":
        
        friends_list = white_locations #no enemies list needed since it wont be used
    else:
        
        friends_list = black_locations

    # 8 locations for knight
    targets = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]

    for i in range(8): #iterates through possible moves
        target = (position[0] + targets[i][0], position[1] + targets[i][1])

        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7: #checks valid moves
            moves_list.append(target)

    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == "white":
        enemies_list = black_locations #testing if locations that rook lands on are from team or enemy
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations

    for i in range(4): #down up left right spots
        path = True #the rook can move, no blocking paths
        chain = 1 #how many pieces can be taken

        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0

        while path: #while there exists a path -- depending on the increment of chain value, this will repeatedly check more valid moves of the rook, and checks for empty spaces
            if (position[0] + (chain * x), (position[1] + (chain * y))) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                #assumes path is still available
                moves_list.append((position[0] + (chain * x), (position[1] + (chain * y))))

                if (position[0] + (chain * x), (position[1] + (chain * y))) in enemies_list: #when rook hits an enemy piece, path ends there
                    path = False
                chain += 1 #checks other squares
            else:
                path = False # no more available path for rook to follow

    return moves_list

def check_pawn(position, color):
    moves_list = []
    #checks everything for white - going down board
    if color == "white":
        if (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations and position[1] < 7: # checking if square below that is empty and can be occupied by pawn, also prevents from going off board
            moves_list.append((position[0], position[1] + 1)) #adds valid move
        if (position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations and position[1] == 1: # checking if 2 square below is empty and can be occupied by pawn, also restricts to starting row
            moves_list.append((position[0], position[1] + 2))

        if(position[0] + 1, position[1] + 1) in black_locations: #if white pawn can take black piece directly diagonal | right
            moves_list.append((position[0] + 1, position[1] + 1))
        if(position[0] - 1, position[1] + 1) in black_locations: #if white pawn can take black piece directly diagonal | left
            moves_list.append((position[0] - 1, position[1] + 1))

    #checks for black - going up board
    else:
        if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations and position[1] > 0: 
            moves_list.append((position[0], position[1] - 1)) 
        if (position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations and position[1] == 6: 
            moves_list.append((position[0], position[1] - 2))

        if(position[0] + 1, position[1] - 1) in white_locations: 
            moves_list.append((position[0] + 1, position[1] - 1))
        if(position[0] - 1, position[1] - 1) in white_locations: 
            moves_list.append((position[0] - 1, position[1] - 1))

    return moves_list


#check valid moves for selected piece
def check_valid_moves():
    if turn_step < 2: # checks if white or black
        options_list = white_options
    else:
        options_list = black_options

    valid_options = options_list[selection] #should give back all valid moves for that selection already
    return valid_options


#draw moves

def draw_valid(moves):
    if turn_step < 2: #gets color of dots depending on whos turn
        color = "red"
    else:
        color = "blue"

    for i in range(len(moves)): #for all valid move squares
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5) #draw dot indicating its a legal move


def draw_captured(): #uses index of piece, gets that to board, draws
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50*i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50*i))

def draw_check():
    if turn_step < 2:
        if "king" in white_pieces:
            king_index = white_pieces.index("king")
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, "dark red", [white_locations[king_index][0] * 100 + 1, white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if "king" in black_pieces:
            king_index = black_pieces.index("king")
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, "dark blue", [black_locations[king_index][0] * 100 + 1, black_locations[king_index][1] * 100 + 1, 100, 100], 5)

def draw_game_over():
    pygame.draw.rect(screen, "black", [200, 200, 400, 70])
    screen.blit(font.render(f"u are the winner {winner}", True, "white"), (210, 210))
    screen.blit(font.render(f"enter to replay", True, "white"), (210, 240))


black_options = check_options(black_pieces, black_locations, "black")
white_options = check_options(white_pieces, white_locations, "white")


# sets up event handler

run = True
while run:
    timer.tick(fps) # game runs at 60 fps
    if counter < 30:
        counter += 1
    else:
        counter = 0

    screen.fill("dark gray") # background color is dark gray
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != -1:
        valid_moves = check_valid_moves() #take out valid moves for just selected piece
        draw_valid(valid_moves)

    # handles all events like keyboard presses and mouse clicks
    for event in pygame.event.get():  # checks each event
        if event.type == pygame.QUIT: # if event is click X button
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over: # checks if mouse is clicked on left button
            x_coord = event.pos[0] // 100 # x coord of mouse, floor divided by 100 due to grid size
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord) #stores in tuple
            

            if turn_step <= 1: #if white turn
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = "black"
                if click_coords in white_locations: #if click is on white piece location
                    selection = white_locations.index(click_coords) #self explanatory
                    if turn_step == 0:
                        turn_step = 1 # if hasn't selected, now it has selected
                
                if click_coords in valid_moves and selection != -1: #if valid and selected a piece
                    white_locations[selection] = click_coords #selects piece if in hitbox vicinity of piece
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords) # captures black piece as part of white's valid move
                        captured_pieces_white.append(black_pieces[black_piece]) #adds captured piece to white collection
                        if black_pieces[black_piece] == "king":
                            winner = "white"
                        black_pieces.pop(black_piece) # pop is remove
                        black_locations.pop(black_piece)
                    
                    black_options = check_options(black_pieces, black_locations, "black") #checks options of pieces
                    white_options = check_options(white_pieces, white_locations, "white")
                    turn_step = 2 #white move done
                    selection = -1 #waiting for selection
                    valid_moves = [] #reset valid moves

            if turn_step > 1: #if black turn
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = "white"
                if click_coords in black_locations: 
                    selection = black_locations.index(click_coords) 
                    if turn_step == 2:
                        turn_step = 3 
                
                if click_coords in valid_moves and selection != -1: 
                    black_locations[selection] = click_coords 
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords) 
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == "king":
                            winner = "black" 
                        white_pieces.pop(white_piece) 
                        white_locations.pop(white_piece)
                    
                    black_options = check_options(black_pieces, black_locations, "black")
                    white_options = check_options(white_pieces, white_locations, "white")
                    turn_step = 0 #black move done
                    selection = -1 
                    valid_moves = [] 
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ""
                white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", 
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), ] 

                black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), ] 

                captured_pieces_white = []
                captured_pieces_black = []

                turn_step = 0 
                selection = -1 
                valid_moves = [] 
                black_options = check_options(black_pieces, black_locations, "black")
                white_options = check_options(white_pieces, white_locations, "white")

    if winner != "":
        game_over = True
        draw_game_over()

    pygame.display.flip() # clears display

pygame.quit() # quits module