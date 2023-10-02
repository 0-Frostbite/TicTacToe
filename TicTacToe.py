import random, time

# ---------------------------------------------------------------------------

exit_code = 0
running = True
piece = ['X','O']

# ---------------------------------------------------------------------------

def Reset():
    global centre , corner , edge
    global matrix
    global board , img

    centre = False
    corner = ["00","02","20","22"] 
    edge = ["01","21","10","12"]
    matrix = [[" "," "," "],
              [" "," "," "],
              [" "," "," "]]
    board = f'\n\n_{matrix[0][0]}_|_{matrix[0][1]}_|_{matrix[0][2]}_\n_{matrix[1][0]}_|_{matrix[1][1]}_|_{matrix[1][2]}_\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} '
    img = '_7_|_8_|_9_\n_4_|_5_|_6_\n 1 | 2 | 3 '

def Menu():
    global exit_code
    print("\n\nWelcome to Tic Tac Toe\n")
    choice1=int(input('1. Start Game\n2. Instructions\n3. Quit\nEnter a number: '))
    if choice1 not in [1,2,3] or type(choice1) != int:
        choice1=int(input("\n**Enter a valid number: "))
    else:
        if choice1 == 1:
            exit_code = 1
        elif choice1 == 2:
            print('''
            
    To play on an empty space type in the number on that specific place on the numpad or refer to the image. 
        
        __|__|__              _7_|_8_|_9_
        __|__|__              _4_|_5_|_6_
          |  |                 1 | 2 | 3

    Inorder to play on the 5th position enter 5 as an input.
        
        ''' )
        elif choice1 == 3:
            exit_code = 5
    
def Start():
    global play_pc , com_pc , piece
    global board
    global exit_code
    play_pc = input("\n\nChoose your piece (X/O or any other): ").upper()
    print(f"\nPlayer chose {play_pc}\n")
    for i in piece:
        if play_pc != i:
            com_pc = i
            break
    print(board,'\n\n')
    print(img,'\n\n-----------\n')
    toss = 1 #random.randrange(2)
    if toss == 1:
        print("You go first\n")
        exit_code = 2
    else:
        print("Computer goes first\n")
        exit_code = 3

def Update():
    global board

    board = f'\n\n_{matrix[0][0]}_|_{matrix[0][1]}_|_{matrix[0][2]}_\n_{matrix[1][0]}_|_{matrix[1][1]}_|_{matrix[1][2]}_\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} '

    time.sleep(random.randrange(2,11)/10)
    print(board,'\n \n')
    print(img,'\n\n-----------\n')

def Play():
    global exit_code
    global move1 , move2
    global matrix
    global corner , edge
    
    index = int(input("Your Turn: "))

    while index not in range(10) or not type(index) == int:
        index = int(input("\n*Enter a valid number: "))

    if index>=7:
        move1,move2 = 0,index-7      
    elif index<=3:
        move1,move2 = 2,index-1     
    else:
        move1,move2 = 1,index-4
     
    while matrix[move1][move2] != ' ':
        index = int(input("\n**Choose a valid space: "))
        if index>=7:
            move1,move2 = 0,index-7      
        elif index<=3:
            move1,move2 = 2,index-1     
        else:
            move1,move2 = 1,index-4

    matrix[move1][move2] = play_pc

    if str(move1) + str(move2) in corner:
        del corner[corner.index(str(move1) + str(move2) )]
    elif str(move1) + str(move2) in edge:
        del edge[edge.index(str(move1) + str(move2) )]
        
    exit_code = 3
    Update()
    WinCheck('player')   

def Comp():
    global exit_code
    global corner , edge , centre , matrix
    global com_pc , play_pc
    global move1 , move2
    
    call = Check()
    if call == 0 or call == None :
        if matrix[1][1] != ' ' :
            if (len(corner) != 4) and (centre == False) :
                if str(move2)+str(move1) in corner:
                    if move1 != move2:
                        matrix[move2][move1] = com_pc
                        del corner[corner.index(str(move2)+str(move1))]     
                    elif move1==move2==0:
                        matrix[2][2] = com_pc
                        del corner[corner.index('22')]                    
                    elif move1==move2==2:
                        matrix[0][0] = com_pc
                        del corner[corner.index('00')]                     
                    else:
                        pick=random.choice(corner)
                        matrix[int(pick[0])][int(pick[1])] = com_pc         
                        del corner[corner.index(pick)] 
                elif str(move1)+str(move2) in edge:
                    if move1==1:
                        matrix[move1][abs(move2-2)] = com_pc
                        del edge[edge.index(str(move1))+str(abs(move2-2))]  
                    elif move2==1:   
                        matrix[abs(move1-2)][move2] = com_pc
                        del edge[edge.index(str(abs(move1-2))+str(move2))] 
                elif corner != []:
                    pick=random.choice(corner)
                    matrix[int(pick[0])][int(pick[1])] = com_pc         
                    del corner[corner.index(pick)]
                else:
                    pick=random.choice(edge)
                    matrix[int(pick[0])][int(pick[1])] = com_pc             
                    del edge[edge.index(pick)]               
            elif (len(corner) != 4) and (centre == True) :
                if len(corner) == 3 and len(edge) == 3:
                    if  (move1 == move2) or (abs(move2 - move1) == 0) :
                        if move1 != move2:
                            matrix[move2][move1] = com_pc
                            del corner[corner.index(str(move2)+str(move1))]       
                        elif move1==move2:
                            matrix[abs(move1-2)][abs(move2-2)] = com_pc
                            del corner[corner.index(str(abs(move1-2))+str(abs(move2-2)))]                    
                    elif abs(move2 - move1) == 1 :
                        for i in corner:
                            if i[0] == i[1]:
                                if str(abs(int(i[0])-2))*2 not in corner:
                                    matrix[int(i[0])][int(i[1])] = com_pc
                                    del corner[corner.index(i)]
                            if i[0] != i[1]:
                                if (i[1] + i[0]) not in corner:
                                    matrix[int(i[0])][int(i[1])] = com_pc
                                    del corner[corner.index(i)]
                elif len(corner) == 3:
                    if move1 == move2:                                     
                        if '02' in corner:
                            matrix[0][2] = com_pc
                            del corner[corner.index('02')]                  
                        elif '20' in corner:
                            matrix[2][0] = com_pc
                            del corner[corner.index('20')]
                        elif corner != []:
                            pick=random.choice(corner)
                            matrix[int(pick[0])][int(pick[1])] = com_pc
                            del corner[corner.index(pick)]
                        else:
                            pick=random.choice(edge)
                            matrix[int(pick[0])][int(pick[1])] = com_pc
                            del edge[edge.index(pick)]    
                    elif move1 != move2:                                    
                        if '00' in corner:
                            matrix[0][0] = com_pc
                            del corner[corner.index('00')]
                        elif '11' in corner:
                            matrix[1][1] = com_pc
                            del corner[corner.index('11')]
                        elif '22' in corner:
                            matrix[2][2] = com_pc
                            del corner[corner.index('22')]
                        elif corner != []:
                            pick=random.choice(corner)
                            matrix[int(pick[0])][int(pick[1])] = com_pc
                            del corner[corner.index(pick)]
                        else:
                            pick=random.choice(edge)
                            matrix[int(pick[0])][int(pick[1])] = com_pc
                            del edge[edge.index(pick)]
                elif len(corner) == 2 and len(edge) == 4:
                        pick=random.choice(edge)
                        matrix[int(pick[0])][int(pick[1])] = com_pc
                        del edge[edge.index(pick)]

                else:
                    for i in edge:                                     
                        print("1.2.2")
                        if i[0]=='1' and (matrix[1][abs(int(i[1])-2)] != play_pc) and (matrix[2][int(i[1])] != play_pc) and (matrix[0][int(i[1])] != play_pc):
                            matrix[1][int(i[1])] = com_pc
                            del edge[edge.index(i)]
                        elif i[1]=='1' and (matrix[abs(int(i[0])-2)][1] != play_pc) and (matrix[int(i[0])][0] != play_pc ) and (matrix[int(i[0])][2] != play_pc ):
                            matrix[int(i[0])][1] = com_pc
                            del edge[edge.index(i)]
                        elif corner != []:
                            pick=random.choice(corner)
                            matrix[int(pick[0])][int(pick[1])] = com_pc
                            del corner[corner.index(pick)]
                        else:
                            pick=random.choice(edge)
                            matrix[int(pick[0])][int(pick[1])] = com_pc
                            del edge[edge.index(pick)]
                        break
            else:
                pick=random.choice(corner)
                matrix[int(pick[0])][int(pick[1])] = com_pc
                del corner[corner.index(pick)]
        else:
            matrix[1][1] = com_pc
            centre = True
    else:
        matrix[int(call[0])][int(call[1])] = com_pc
        if call in corner:
            del corner[corner.index(call)]
        elif call in edge:
            del edge[edge.index(call)]   
    print(corner,'\n',edge)
    exit_code = 2
    Update()
    WinCheck()
    
def WinCheck(name='comp'):

    check = 0

    for i in matrix:
        if i[0]==i[1]==i[2] and (i[0]!=' ' and i[1]!=' ' and i[2]!=' '):
            check = 2
        for k in range(3):
            if matrix[0][k]==matrix[1][k]==matrix[2][k] and (matrix[0][k]!=' ' and matrix[1][k]!=' ' and matrix[2][k]!=' '):
                check = 2
        if (matrix[0][2]==matrix[1][1]==matrix[2][0] and (matrix[0][2]!=' ' and matrix[1][1]!=' ' and matrix[2][0]!=' ')) or (matrix[0][0]==matrix[1][1]==matrix[2][2] and (matrix[0][0]!=' ' and matrix[1][1]!=' ' and matrix[2][2]!=' ')):
            check = 2

        for j in i:
            if j == ' ' and check == 0:
                check = 1


    if check == 0:
        Win(name,0)
    elif check == 2:
        Win(name,1)

def Check():
    global com_pc , play_pc
    com_count,play_count = 0,0
    mark = []
    count = 0

    while count<2:
        for i in matrix :
            if (com_count == 2 and play_count==0):
                break
            com_count,play_count,mark = 0,0,0
            for j in i:
                if j == com_pc:
                    com_count+=1
                elif j == play_pc:
                    play_count+=1
                elif j == ' ':
                    mark = str(matrix.index(i))+str(i.index(j))

        if not ((com_count == 2 and play_count==0)):
            for a in range(3):
                if (com_count == 2 and play_count==0):
                    break
                com_count,play_count,mark = 0,0,0
                for b in range(3):
                    if matrix[b][a] == com_pc:
                        com_count+=1
                    elif matrix[b][a] == play_pc:
                        play_count+=1
                    elif matrix[b][a] == ' ':
                        mark = str(b)+str(a)

        if not ((com_count == 2 and play_count==0)):
            for a in range(3):
                if matrix[a][a] == com_pc:
                    com_count+=1
                elif matrix[a][a] == play_pc:
                    play_count+=1
                elif matrix[a][a] == ' ':
                    mark = str(a)+str(a)
                
        if not ((com_count == 2 and play_count==0)):
            com_count,play_count,mark = 0,0,0
            x,y = -2,0
            for c in range(3):
                if matrix[abs(x+c)][y+c] == com_pc:
                    com_count+=1
                elif matrix[abs(x+c)][y+c] == play_pc:
                    play_count+=1
                elif matrix[abs(x+c)][y+c] == ' ':
                    mark = str(abs(x+c))+str(y+c)

        if (com_count == 2 and play_count==0):
            if count == 1:
                com_pc , play_pc = play_pc , com_pc  
            count+=2
            return(mark)
        elif not ((com_count == 2 and play_count==0)):
            com_pc , play_pc = play_pc , com_pc
            count+=1        

def Quit():
    global exit_code
    choice = int(input('\n\n1. Play again\n2. Quit\nEnter a number: '))
    while choice not in [1,2]:
        choice = int(input("\n**Enter a valid number"))
    if choice == 1:
        exit_code = 1
    elif choice == 2:
        exit_code = 5

def Win(name,dgt):
    global exit_code
    if dgt == 0:
        print("\n\n-- It's a DRAW --")
    elif name == 'player':
        print("\n\n-- Congratulations!!! --\n-- You have WON --")
    else:
        print("\n\n-- Loser. --")
    exit_code = 4
    
def Run():
    global running
    if exit_code == 0:
        Menu()
    elif exit_code == 1:
        Reset()
        Start()
    elif exit_code == 2:
        Play()
    elif exit_code == 3:
        Comp()
    elif exit_code == 4:
        Quit()
    else:
        running = False
        print("\n\nApp Closed")

# ---------------------------------------------------------------------------

while running:
    Run()