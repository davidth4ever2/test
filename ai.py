import json

def test():

    line_one = []
    line_two = []
    static_number    = []
    static_numbers    = []

    

    for i in range(0,10):
        
        line_one.insert(i,str(i) )# symbol list



    for k in range(0,10):
        
        static_number = []
        
        for j in range(0,10):
            
            static_number.insert(j,str(k)) # static symbols list

        
        static_numbers.insert(i,static_number)  # all information in the list
       
    static_numbers.insert(0,line_one) 
    
    f = open('m.json','w')
    
    json.dump(static_numbers,f)

    return  "this is a test"




output = test()

print (output)

...............................................................................
.                     margin
..............................................................................
.         .           boarder
..............................................................................
.                     padding
..............................................................................
.                     content

When set you  the width and height of an element in CSS, you just set the width and height of the content area
.
.
.
.
.
.
...............................................................................
 
 
 
    Content - The content of the box, where text and images appear
    Padding - Clears an area around the content. The padding is transparent
    Border - A border that goes around the padding and content
    Margin - Clears an area outside the border. The margin is transparent

What is an emotional transaction to a machine
The character of Othelo and the need for more computational power and 
and the benefits and draw back of shared neutella network; 
you 


# breath-first search is a simple strategy in which the root nood is expanded first
# then, all of the successors of the root node are expanded next, then their successors, and soo on.
# all the nodes are expanded at the given depth in the seach tree before any notes at the next level
# are expanded
input = [[0,3,4],[8,1,2],[5,6,7]]

for i in input:
    for j in i:
        print "value: " + str(j) + ' floor ' + str(input.index(i))  + ' door ' + str(i.index(j))


def expandNode():

    floor = -1
    door  = -1

    input_array = [[8,3,4],[0,1,2],[5,6,7]]
    
    for i in input_array:
        
        for j in i:

            if(j == 0):

                floor = input_array.index(i)
                door  = i.index(j) 
                
                print "value: " + str(j) + ' floor ' + str(input_array.index(i))  + ' door ' + str(i.index(j))

        

    #UDLR
    def vertical(input_array):
        # 1. Copy Array

        input_array_copy = input_array[:][:]
        

    if(floor == 0 and door == 0):

        # options are R and D

        node_one = input_array[:]
        node_two = input_array[:]
       
        temp = node_one[floor + 1][door]
        node_one[floor][door] = temp
        node_one[floor+1][door] = 0

        print node_one


        node_two = input_array[:]

        temp = node_two[floor][door+1]
        node_two[floor][door] = temp
        node_two[floor][door+1] = 0

        print node_two
        
        
    if(floor == 1 and door == 0):
       # options are D R

        input_array_copy = input_array[:][:]

        node_one   = input_array[floor][:]

        print node_one

        temp = node_one[door+1]
        node_one[door] = temp
        node_one[door+1] = 0

        input_array_copy[floor] = node_one

        print input_array_copy

       
    if(floor == 2 and door == 0):
        pass # options are U
    if(floor == 1 and door == 0):
        pass # R
    if(floor == 1 and door == 1):
        pass # UDLF
    if(floor == 1 and door == 2):
        pass # L and D
    if(floor == 2 and door == 0):
        pass # R
    if(floor == 2 and door == 1):
        pass # UDLF
    if(floor == 2 and door == 2):
        pass # L and D
    

     branch_01_input.insert(branch_01_count,b)
               exploredBranch.insert(exploredCount, branch_01_input)

               exploredCount = exploredCount + 1
               branch_01_count = branch_01_count + 1
               
               branch_01_input = horizontal(a,1)



                else:

                    branch_02_input = vertical(branch_02_input,1)

                    if(exploredBranch.count(branch_02_input) < 1):

                       

                       exploredBranch.insert(exploredCount,branch_02_input)
                       exploredCount = exploredCount + 1

                       branch_02.insert(branch_02_count,branch_02_input)
                       branch_02_count = branch_02_count + 1

                       print "branch 2 ......" + str(branch_02)

                   



                        
    
   
