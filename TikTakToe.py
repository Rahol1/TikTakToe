def getSymbols(number):
    
    if(number==0):
        return ' '
    elif(number == 1):
        return 'O'
    else:
        return 'X'
    
def refBoard():
    count = 1
    for i in range(3):
        for j in range(3):
            if(i<2):
                 if(j<2):
                     print('_',count,'_',end='|')
                     count += 1
                 else:
                     print('_',count,'_')
                     count += 1
            else:
                 if(j<2):
                     print(' ',count,' ',end='|')
                     count += 1
                 else:
                     print(' ',count,' ')
                     count += 1
                     
                     
def drawBoard(array2D):
    
    for i in range(len(array2D)):
        for j in range(len(array2D[0])):
            if(i<len(array2D)-1):
                 if(j<len(array2D[0])-1):
                     print('_'+getSymbols(array2D[i][j])+'_',end='|')
                 else:
                     print('_'+getSymbols(array2D[i][j])+'_')
            else:
                 if(j<len(array2D[0])-1):
                     print(' '+getSymbols(array2D[i][j])+' ',end='|')
                 else:
                     print(' '+getSymbols(array2D[i][j])+' ')

def checkRows(ar):
    
    flag = 0
    for i in range(len(ar)):
        
        if (ar[i].count(1) == 3 ):
            flag = 1
            break
        elif ( ar[i].count(2) == 3):
            flag = 2
            break
            
    return flag

def checkColumns(ar):
    
    flag = 0
    for i in range(len(ar[0])):
        
        temp = [ar[0][i], ar[1][i], ar[2][i]]
        
        if (temp.count(1) == 3 ):
            flag = 1
            break
        elif (temp.count(2) == 3):
            flag = 2
            break
            
    return flag       
            
def checkDiagonals(ar):
    
    flag = 0
      
    temp = [ar[0][0], ar[1][1], ar[2][2]]
    temp2 = [ar[0][2], ar[2][0], ar[1][1]] 
        
    if (temp.count(1) == 3 or temp2.count(1) ==3 ):
        flag = 1
           
    elif (temp.count(2) == 3 or temp2.count(2) == 3):
        flag = 2
                        
    return flag 
def positionToBoard(board, turn, position):
    
    if(position == 1):
        if(board[0][0] == 0):
            
            board[0][0] = turn
        else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
            
    elif(position ==2):
         if(board[0][1] == 0):
            board[0][1] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
       
    elif(position == 3):
         if(board[0][2] == 0):
            board[0][2] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    elif(position == 4):
         if(board[1][0] == 0):
            board[1][0] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    elif(position == 5):
         if(board[1][1] == 0):
            board[1][1] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    elif(position == 6):
         if(board[1][2] == 0):
            board[1][2] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    elif(position == 7):
         if(board[2][0] == 0):
            board[2][0] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    elif(position == 8):
         if(board[2][1] == 0):
            board[2][1] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    elif(position == 9):
         if(board[2][2] == 0):
            board[2][2] = turn
            
         else:
            print("invalid move, enter position again")
            p = int(input())
            board = positionToBoard(board, turn, p)
        
    
    return board
    
    
    
def game(board,streak):
    
    current_board = board
    print(drawBoard(current_board) )
    for i in range(1,10):
        
        if(i%2 == 1):
            turn = 1
        else:
            turn = 2
        
        print("Player ",turn," enter the position")
        
        pos = int(input())
        
        current_board = positionToBoard(current_board, turn, pos)
        print(drawBoard(current_board) )
        flag = checkRows(current_board)
        if(flag == 0):
            
            flag = checkColumns(current_board)
            if(flag == 0):
                
                flag = checkDiagonals(current_board)
        if(flag != 0):
            break

                    
        
    if(flag == 0):
        print("Draw")
    elif(flag == 1):
        print("Player 1 wins")
        streak [0] += 1
        
    else:
        print("player 2 wins")
        streak[1] += 1
    print("The Score is:  Player 1:",streak[0],"  Player 2:",streak[1])
    return streak
if __name__ == "__main__" :
    
    print("Welcome\n")
    print("Here is the board details , Kindly input your choice of boxes according to this system\n\n")
    
    print(refBoard())
    
    
    
    print("Do you want to start the game:   enter 1 for yes and 0 for no")
    
    game_choice = int(input())
    
    if(game_choice == 1):
        
        play_again = 1
    game_streak = [0,0]
    
    while(play_again == 1):
        
        
        init = [[0 for i in range(3)] for i in range(3)]
        game_streak = game(init,game_streak)
        print("Play again? 0 for no and 1 for yes")
        play_again = int(input())
    
    print("Final Score: \n")
    print("Player 1: ",game_streak[0])
    print("Player2: ",game_streak[1])