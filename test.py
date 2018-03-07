##0,8,7,6,5,4,3,2,1
# 
import sys,copy
constructor = sys.argv[1]
class WorkerOne:

    input_board_one  = None

    board = ()
    
    def __init__(self,input_board_one):
        
        self.input_board_one = input_board_one
    
    def createBoard(self):
        line = ()
        for i in self.input_board_one:

            line  =    (i,)

        print line



    
    
    
    
x = WorkerOne(constructor)
print x.input_board_one
x.createBoard()
