# TicTacToe
Stupid Python TicTacToe

# matrix 
    a nested list of 3 in 3 [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] - a grid to plot the pieces and process data
# corner 
    stores coordinates of the corners of matrix as strings - ['00','02','20','22']
# edge
    stores coordinates of the edges of matrix as strings 

# Reset()
    resets all the changed variables back to their original value (ik img and board are'nt  necessary)

# Menu()
    **Menu** WOW

# Start()
    play_pc is the piece used to represent your move

# Update()
    values upon changing werent updated so i created this - is called after every move

# Play()
    player input is taken as "index" and converted to 2 digits ("move1","move2") to access the table "matrix" and is used to calculate comps next move. If the space is empty the move is made and its deleted from "corner"/"edge".

# Comp()
    the logic for moves made by the computer 
    1. Check() is called to see if there is a win/lose possibilty - if yes play the move - else use the logic.
    2. Capture the centre if its empty (line 137,246)
    
    centre is computers: 
    1. If player has occupied 2 opposite corners (ex- at 0,0 and 2,2) take a random edge to block the 3 corner trick (line 218)
    2. If player has occupied 1 corner and 1 edge (ex- at 0,0 and 1,2) far from corner, take the corner adjacent to players blocks another win (line 169)
    3. In every other case it captures a random corner first (line 239) then an edge if its opposite edge is empty and of the sides (corner) one is empty and one is computers (line 222) . This way the empty corner and the empty edge create a win chance and the player can only block one. Tho winning is possible only if the player is RETARDED. I didnt use the 3 corner trick or 2 corner and edge one coz i by the i realized i was way ahead so i'd have to change alot of code.

    line 187 - scenario - computer goes first and take centre - player takes a corner - take a corner that isnt oppostie to the players **the code can be improved
    1. and 2. are possible only if player goes first and doesn't capture the centre
    
    centre is players: (possible only if player goes first)
    1. The goal in this case is to take a corner first (line 226)
    2. and mirror every move the player makes (ex- player goes (2,2) computer goes (0,0), player goes (1,0) computer goes (1,2)) 

# Check()
    checks if their is a win or lose possibility and return a str value of the matrix coordinate to be played to avoid lose or simply win
    1. it first check for the count of pieces of computer ("com_pc") and ("com_count") as in the case of both win and lose possibility win should we favored
    2. if in first loop there is no suggestion (check=0) the pieces swap places and loop runs again, tho its showing com_pc the variable is actually play_pc
    3. if there is not win/lose possibilty check+=1 in and swap, if there is a win possibility in first try check = 2 , if in second case checks if check is 1 i.e. checks whther swap took place and reverts the swap.

# Wincheck()
    is called by Comp() and Play() in the end to check the game outcome - has name variable to know who has won if thats the case, original is 'comp' and Player() calls with 'player'
    1. check variable is used to store the outcome of conditions
    2. check each column for same value in matrix and for if its not ' '. (line 262)
    3. check each row for same value in matrix and for if its not ' '. (line 264,265)
    4. check the two diagonals for same value in matrix and for if its not ' '. (line 267)
    5. check for empty spaces and check!=2 i.e. no win and spaces are empty - game continues
    6. if check is 2 game is declared, elif check is 0 which is tis original value its a draw

    Win() is called only if the match is concluded

# Win(name,dgt)
    dgt works w.r.t. check in Wincheck() - simply processes whether its a win, lose or draw for player. 

# Quit()
    basially an end screen
    
# Run()
    *in earlier version the program was making recursive calls to the methods, tho in this tiny program recursion wont make much difference but if one has a better solution o believe recursion should be avoid* - not much just 1st year CSE student trynna flex 
    based on "exit_code" call a method
