#Programmer's Note: This was one of my very first projects, written during my introduction to programming (2021 Pre-AI era).
# I'm keeping it as a milestone, a reminder of where I started.

import sys

with open (sys.argv[1]) as inpt:
    board=[line.strip().split(" ") for line in inpt.readlines()]
for i in board:    
    print(*i)
print("\nYour score is: 0" )
colordic={"B": 9,"G": 8,"W": 7,"Y": 6,"R" :5,"P": 4,"O": 3,"D": 2,"F": 1,"X": 0}
score=0

#checks if there is any possible move left, if not returns True, otherwise returns False
def over():
    ovr=True
    for rowno in range(len(board)):
        for columnno in range(len(board[rowno])):
            try: 
                if board[rowno][columnno]==board[rowno][columnno+1] and board[rowno][columnno]!=" " :
                    ovr=False
            except: pass
            try:
                if board[rowno][columnno]==board[rowno+1][columnno] and board[rowno][columnno]!=" " :
                  ovr=False
            except: pass
        if "X" in board[rowno]:
            ovr=False
    return ovr        

#shifts the board down and to the left after each move, deletes empty rows and columns
def shifting():
    for count in range(len(board)):
        for rownu in range(len(board)):
            for columnnu in range(len(board[0])):
                try:
                    if board[rownu+1][columnnu]==" ":
                        board[rownu+1][columnnu]=board[rownu][columnnu]
                        board[rownu][columnnu]=" "
                except: pass
        for colmnu in range(len(board[0])) :
            try:
                if board[-1][colmnu]==" ":
                    for rows in board:
                        rows.pop(colmnu)
            except: pass
    for y in board:
        if  y.count(" ")==len(y):
            board.remove(y)


#asks user for a coordinate, checks if it is valid, if not asks again, otherwise executes the move and updates the score
# prints the board and score after each move, if there is no possible move left, prints the final score and game over message           
def main():
    global score
    row=None
    col=None
    colour=""
    coordinate_list=[]
    try:
        coordinates=input("\nPlease enter a row and column number: ").split(" ")
        row=int(coordinates[0])
        col=int(coordinates[1])
        colour=board[row][col]
    except:
        print("\nPlease enter a valid size!")
        main()
    else:
        if colour==" ":
            print("\nPlease enter a valid size!")
            main()
    try:
        coordinate_list.append([row,col])
        if colour!="X" :
            for coordinate in coordinate_list:
                try:
                    if board[coordinate[0]-1][coordinate[1]]==colour and [coordinate[0]-1,coordinate[1]] not in coordinate_list :
                        if coordinate[0]-1 !=-1:
                            coordinate_list.append([coordinate[0]-1,coordinate[1]])                           
                except IndexError:
                    pass
                try:
                    if board[coordinate[0]+1][coordinate[1]]==colour and [coordinate[0]+1,coordinate[1]] not in coordinate_list :
                        coordinate_list.append([coordinate[0]+1,coordinate[1]])                         
                except IndexError:
                    pass
                try:
                    if board[coordinate[0]][coordinate[1]-1]==colour and [coordinate[0],coordinate[1] - 1] not in coordinate_list :
                        if coordinate[1]-1 !=-1:
                            coordinate_list.append([coordinate[0],coordinate[1] - 1])                                          
                except IndexError:
                    pass
                try:
                    if board[coordinate[0]][coordinate[1]+1]==colour and [coordinate[0],coordinate[1] + 1] not in coordinate_list :
                        coordinate_list.append([coordinate[0],coordinate[1] + 1])           
                except IndexError:
                    pass
            if len(coordinate_list)>1:
                for crd in coordinate_list:
                        score+=colordic[board[crd[0]][crd[1]]]
                        board[crd[0]][crd[1]]=" "   
        elif colour=="X":
            bomb_list=coordinate_list.copy()
            bombrow=[]
            bombcol=[]
            for bomb_cordinate in bomb_list:
                for i in range(len(board[bomb_cordinate[0]])):
                    if board[bomb_cordinate[0]][i]=="X" and [bomb_cordinate[0],i] not in bomb_list :
                        bomb_list.append([bomb_cordinate[0],i])
                for j in range(len(board)):
                    if board[j][bomb_cordinate[1]]=="X" and [j,bomb_cordinate[1]] not in bomb_list:
                        bomb_list.append([j,bomb_cordinate[1]])
                bombrow.append(bomb_cordinate[0])
                bombcol.append(bomb_cordinate[1])
            for b_row in set(bombrow):
                for col_no in range(len(board[b_row])):
                    if board[b_row][col_no]!=" ":
                        score+=colordic[board[b_row][col_no]]
                        board[b_row][col_no]=" "                      
            for b_col in set(bombcol):
                for rowss in board:
                    if rowss[b_col]!=" " :
                        score+=colordic[rowss[b_col]]
                        rowss[b_col]=" "      
        shifting()        
        if over():
            print()
            for i in board:    
                print(*i)
            print("\nYour score is: "+str(score)) 
            print("\nGame Over!")
        else:
            print()
            for i in board:    
                print(*i)
            print("\nYour score is: "+str(score))  
            main()
    except: pass

main()


