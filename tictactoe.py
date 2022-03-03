"""
Tic Tac Toe Player
"""
import math
import sys
import copy
import random
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    
    numX = 0
    numO = 0
    for list in board:
        for item in list:
            if item == X:
                numX+=1
            if item == O:
                numO+=1    
    if numX > numO:
        return O
    elif numX == numO:
        return X    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_availible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                place = (i, j)
                actions_availible.add(place)
    return actions_availible

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board1 = copy.deepcopy(board)
    turn = player(board1)
    '''try:'''
    for i in range(2):
        if action[i] > 2:
            print("Invalid Move")
            raise

    board1[action[0]][action[1]] = turn
    #print(board, board1)
    """
    except:
        print("Invalid Move")
    """
    return board1


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """



    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == X:
            return X 
        elif board[0][0] == O:
            return O

    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] == X:
            return X 
        elif board[1][0] == O:
            return O

    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] == X:
            return X 
        elif board[2][0] == O:
            return O  
    
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == X:
            return X 
        elif board[0][0] == O:
            return O

    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] == X:
            return X 
        elif board[0][1] == O:
            return O

    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] == X:
            return X 
        elif board[0][2] == O:
            return O      

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X 
        elif board[0][0] == O:
            return O  
    

    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[0][2] == X:
            return X 
        elif board[0][2] == O:
            return O  
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """    
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                return False
    return True            
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner1 = winner(board)
    if winner1 == X:
        return 1
    elif winner1 == O:
        return -1
    else:
        return 0    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    
    currPlayer = player(board)
    allActions = actions(board)
    actionratings = []
    if terminal(board):
        return None
    for action in allActions:
        if terminal(result(board, action)):
            if currPlayer == X:
                if utility(result(board, action)) == 1:
                    return action
            else:
                if utility(result(board, action)) == -1:
                    return action      
            actionratings.append([utility(result(board, action)), action])
        elif currPlayer == O:
            value = [-2, None]
            newboard2 = result(board, action)
            actions1 = actions(newboard2)
            for action1 in actions1:
                helperboard = result(newboard2, action1)
                if player(helperboard) != None:
                    valuesFor = minimaxHelper(helperboard)
                    if valuesFor != None:
                        if valuesFor > value[0]:
                            value[0] = valuesFor
                            value[1] = action
            actionratings.append(value)  

        elif currPlayer == X:
            value = [2, None]
            newboard2 = result(board, action)
            actions1 = actions(newboard2)
            for action1 in actions1:
                helperboard = result(newboard2, action1)
                if player(helperboard) != None:
                    valuesFor = minimaxHelper(helperboard)
                    if valuesFor != None:
                        if valuesFor < value[0]:
                            value[0] = valuesFor
                            value[1] = action
            actionratings.append(value)  
    if currPlayer == X:
        final = [-2, None]
    else:
        final = [2, None]
    for action in actionratings:
        if action[1] != None:
            if currPlayer == X:
                if action[0] > final[0]:
                    final = action
                elif action[0] == final[0]:
                    if random.randint(0, 1) == 1:
                        final = action   
                
            else:
                if action[0] < final[0]:
                    final = action
                elif action[0] == final[0]:
                    if random.randint(0, 1) == 1:
                        final = action       
    return final[1]       


def minimaxHelper(board):
    """
    Returns the optimal action for the current player on the board.
    """

    currPlayer1 = player(board)
    if currPlayer1 == None:
        
        print("invalid", board)
        return None 
    if terminal(board):
        return utility(board)

    if currPlayer1 == X:
        value = -1
        actions1 = actions(board)
        for action in actions1:

            helperboard = result(board, action)
            if action[0] < 3 and action[1] < 3:
                minimaxHelperVal = minimaxHelper(helperboard)
                if minimaxHelperVal != None:
                    value = max(value, minimaxHelperVal)
        return value    
    elif currPlayer1 == O:  
        value = 1
        actions1 = actions(board)
        for action in actions1:
            helperboard = result(board, action)
            if action[0] < 3 and action[1] < 3:
                minimaxHelperVal = minimaxHelper(helperboard)
                if minimaxHelperVal != None:
                    value = min(value, minimaxHelperVal)
        return value  