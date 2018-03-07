#  Each coordinate in this two-dimensional plan has an associated move precedencecertain move associated with it
#  This coordinate plan consists of 9 positions;
#  Contained in a 3X3 matrix
#  ***the first thing to do is generate the the path options based on matrix size
#  Coordinate | Move Options Starting with UDLR
######################################################################
#  If the nonce has location  y = 0 -> row[0][i] the next move sequence -> DLRU
######################################################################
#  If the nonce has location  y = 1 -> row[1][i] the next move sequence -> UDLR
######################################################################
#  If the nonce has location  x = 0 -> row[0][i] 
#  ....[0][0] -> [D]
#  ....[1][0] -> [D]
#  ....[2][0] -> [D]
#  If the nonce has location  x = 1 -> row[0][i] 
#  ....[1][1] -> [u]
#  ....[2][1] -> [u]
#  ....[3][1] -> [u]
#  If the nonce has location  x = 2 -> row[0][i] 
#  ....[1][2] -> [u]
#  ....[2][2] -> [u]
#  ....[3][2] -> [u]
# Psalm 10:1-18
# 1 Peter 1:13,14
# you're gifted, you're brave you must do better, because I know you can, 
# no matter your shame, gather your strength, you must find a way to
# help those that need you.
# you must gather your strength
#####################################################################

exploredFrontier = []
insert_count= 0
nonce_coordinate = []

def nonceExplored(move):
    global insert_count
    " the explored frontier  " + repr(len(exploredFrontier))
    if(exploredFrontier.count(move) == 0):
        print 'frontier not empty'
        exploredFrontier.insert(insert_count,move)
        insert_count = insert_count + 1

        return 0
    
    return 1

#####################################################################

                   
def findNonce(board):
    
    if (type(board) == list):

        x, y = 0,0

        for y in range(0, len(board)):

            for x in range(0, len(board[y])):

                if(board[y][x] == '0'):

                    current_nonce_location = [y, x]

                    return current_nonce_location


def getSequenceOfMoves(board):

    global nonce_coordinate

    print type(board)

    if( type(board) <> list):
        return 'bad input'
    # y position tests
    # if the first position of the coordinate returned or [y][0] = 0 it's on the top row
    # remove u from the option of moves
    # if the first position of the coordinate returned or [y][0] = 1 it's on the second row
    # send back all options
    # if the first position of the coordinate returned or [y][0] = 2
    # remove d from the  option of moves
    # x position test
    # if the seond position of the coorinate return  or [0][x] = 0  - it's on the left
    # remove left from option sequnce
    # if the seond position of the coorinate return  or [0][x] = 1  - it's on the second floor
    # send back all option
    # if the seond position of the coorinate return  or [0][x] = 2
    # remove right

    move_sequence = ['U','D','L','R']
    
    print "new board configuration is " + str(board)

    nonce_coordinate = findNonce(board)

    
    print "now the nonce is located - > " +  str(nonce_coordinate)

    if(nonce_coordinate[1] == 0): # first floor 
            
        move_sequence.remove('U')
                
    if(nonce_coordinate[1] == 1): # second floor

        pass

    if(nonce_coordinate[1] == 2): # third floor

        move_sequence.remove('D')

    if(nonce_coordinate[0] == 0): # first door

        move_sequence.remove('L')

    if(nonce_coordinate[0] == 1): # second door

        pass

    if(nonce_coordinate[0] == 2): # third door

        move_sequence.remove('R')

        print "third floor"
        
    return move_sequence


def makeSomeMoves(options,input_array):

    global nonce_coordinate

    
    # print str(a[0][0]) +  ' ' +   str(a[1][0]) +  ' ' +  str(a[2][0])
    # print str(a[0][1]) +  ' ' +   str(a[1][1]) +  ' ' +  str(a[2][1])
    # print str(a[0][2]) +  ' ' +   str(a[1][2]) +  ' ' +  str(a[2][2])

    
    def moveRight():
        
        print 'moving right'

        
        new_x,new_y = 0,0
        old_x,old_y = 0,0


        nonce_coordinates =  findNonce(input_array)

        
        old_x,old_y  = int(nonce_coordinates[0]),int(nonce_coordinates[1])

        print '(old_x) ' + repr(old_x)
        print '(old_y) ' + repr(old_y)
        print 'nonce_coordinates swap ' + repr(input_array[old_x+1][old_y])

        print " reading nonce " +   repr(input_array[old_x][old_y] )              

        
        new_x,new_y = old_x,old_y+1

        print '(new_x) ' + repr(new_x)
        print '(new_y) ' + repr(new_y)
        

        temp =  input_array[new_x][new_y]

        print " swap value " + temp

        input_array[new_x][new_y] = input_array[old_x+1][old_y]
        input_array[old_x][old_y] = temp

        print "swap check fool" + repr(input_array)

        return input_array


    # print str(a[0][0]) +  ' ' +   str(a[1][0]) +  ' ' +  str(a[2][0])
    # print str(a[0][1]) +  ' ' +   str(a[1][1]) +  ' ' +  str(a[2][1])
    # print str(a[0][2]) +  ' ' +   str(a[1][2]) +  ' ' +  str(a[2][2])

        
    def moveLeft():
        

        new_x,new_y = 0,0
        old_x,old_y = 0,0


        nonce_coordinates[0] = nonce_coordinates[0]+1

        new_x,new_y = nonce_coordinates[0],nonce_coordinates[1]

        temp =  input_array[new_y][new_x]

        input_array[new_y][new_x] = '0'

        input_array[old_x][old_y] = temp

        exploredFrontier.append(input_array)

        print "moved left"

        return moving_array
    
    
    # print str(a[0][0]) +  ' ' +   str(a[1][0]) +  ' ' +  str(a[2][0])
    # print str(a[0][1]) +  ' ' +   str(a[1][1]) +  ' ' +  str(a[2][1])
    # print str(a[0][2]) +  ' ' +   str(a[1][2]) +  ' ' +  str(a[2][2])
    
    
    def moveUp():

        movementOptions = [[0,0],[0,1],[0,2]]

        print 'moving down'
        
        new_x,new_y = 0,0
        old_x,old_y = 0,0


        nonce_coordinates =  findNonce(input_array)

        
        old_x,old_y  = int(nonce_coordinates[0]),int(nonce_coordinates[1])

        print '(old_x) ' + repr(old_x)
        print '(old_y) ' + repr(old_y)
        print 'nonce_coordinates swap ' + repr(input_array[old_x][old_y-1])

        print " reading nonce " +   repr(input_array[old_x][old_y] )              

        
        new_x,new_y = old_x,old_y-1

        print '(new_x) ' + repr(new_x)
        print '(new_y) ' + repr(new_y)
        

        temp =  input_array[new_x][new_y]

        print " swap value " + temp

        input_array[new_x][new_y] = input_array[old_x][old_y]
        input_array[old_x][old_y] = temp

        print "swap check fool" + repr(input_array)

        return input_array

        
  
    # print str(a[0][0]) +  ' ' +   str(a[1][0]) +  ' ' +  str(a[2][0])
    # print str(a[0][1]) +  ' ' +   str(a[1][1]) +  ' ' +  str(a[2][1])
    # print str(a[0][2]) +  ' ' +   str(a[1][2]) +  ' ' +  str(a[2][2])

    
    def moveDown():

        movementOptions = [[0,0],[0,1],[0,2]]

        print 'moving down'
        
        new_x,new_y = 0,0
        old_x,old_y = 0,0


        nonce_coordinates =  findNonce(input_array)

        
        old_x,old_y  = int(nonce_coordinates[0]),int(nonce_coordinates[1])

        print '(old_x) ' + repr(old_x)
        print '(old_y) ' + repr(old_y)
        print 'nonce_coordinates swap ' + repr(input_array[old_x][old_y+1])

        print " reading nonce " +   repr(input_array[old_x][old_y] )              

        
        new_x,new_y = old_x,old_y+1

        print '(new_x) ' + repr(new_x)
        print '(new_y) ' + repr(new_y)
        

        temp =  input_array[new_x][new_y]

        print " swap value " + temp

        input_array[new_x][new_y] = input_array[old_x][old_y]
        input_array[old_x][old_y] = temp

        print "swap check fool" + repr(input_array)

        return input_array

    
    if(options.count('U') > 0):

        print " should be going up"

        return moveUp()
        
    if(options.count('D') > 0):

        print " should be going down"

        return moveDown()

    if(options.count('L') > 0):

        print " should be going left"

        return  moveLeft()
        
    if(options.count('R') > 0):

        print " should be going right"

        return moveRight()
         

def test():

    a = [['0','3','4'],['8','1','2'],['5','6','7']]

    
    
    print str(a[0][0]) +  ' ' +   str(a[1][0]) +  ' ' +  str(a[2][0])
    print str(a[0][1]) +  ' ' +   str(a[1][1]) +  ' ' +  str(a[2][1])
    print str(a[0][2]) +  ' ' +   str(a[1][2]) +  ' ' +  str(a[2][2])

    
    current_nonce_location = []

    test_count = 0
    
    #while (test_count < 5):

    sample = a
        
    move_options = getSequenceOfMoves(sample)

    print move_options
        
    print "before --"  + repr(sample)

    working_array = sample
    
    for i in range(0,4):    
      
        working_array = makeSomeMoves(move_options,working_array)
        move_options = getSequenceOfMoves(working_array)
        

    

        #print "after --"   + repr(a)
        #test_count = test_count + 1
    
