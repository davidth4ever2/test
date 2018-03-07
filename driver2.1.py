import sys, copy, time, resource
from collections import deque
from string import Template
# notes on breath-first searchclass node:
# the shallowest unexpanded node is chosen for expansion. This is achieved by using FIFO Queue for the frontier
# the goal test is applied to each node when it is generated rather then when it is selected for expansion
# discards any new path to a state already in the frontier or explored set
# the nodes are expanded at a given depth in the search tree before any nodes at the next level arer expanded
# the number of successors = the number of 
# explored set - >  closed list 
# the frontier separates the state graph into an explored region and the unexplored region
# as every step moves a state from the frontier into the explored region while moving some # states from the 
# explored region into the frontier
# each nodes contains four components
# --- state - the state in the state space where the node corresponds
# --- parent - thenode in the each treat that generated this node
# --- action the actin that was applied to the parent to generate this node
# --- path cost - cost , g(n) -> of the path from the intial state to the node and indicated by parent pointers
# --- child node takes as an arguement
# --- a node is a bookkeeping datastructure used to represent the search tree
# --- state correspond to  the configuration of the world, 
# --- nodes are not paths as defined by the parent nodes
# algorithms are evaluated based on their completeness, optimality, time complexity, space complexity
# |V| + |E|  V is the set of all vertices ( nodes ) , E is the edges
# complexity is measure based on branching factor b; depth is the shallow is goal node, m - maximumn length

class Results:
    
    path_to_goal = []
    
    cost_of_path = 0
    
    nodes_expanded = 0
    
    search_depth = 0
    
    max_search_depth = 0
    
    running_time = 0
    
    max_ram_usage = 0

# book keeping stuff 


resultLog = Results()


class Node:
    
    parent   = None
    state    = None
    pathCost = 0
    STEPCOST = 1 
    
    def __init__(self,node):
        
        self.parent   = node
        self.state    = node.state
    
        
class Problem(Node):

    initialState = None
   # actions      = ["vertical","horizontal"]

    actions = ["up","down","left","right"]


    frontier = deque()
    explored = []

    problemBoard = []
    goalBoard    = []

    problemlist = sys.argv[2].split(',')
    problemBoard.append( problemlist[0:3] )
    problemBoard.append( problemlist[3:6] )
    problemBoard.append( problemlist[6:9] )

    goallist = sorted(sys.argv[2].split(','))
    goalBoard.append( goallist[0:3] )
    goalBoard.append( goallist[3:6] )
    goalBoard.append( goallist[6:9] )
    
    goalState = goalBoard


    def __init__(self):
        
        self.initialState = self.problemBoard
        self.pathCost     = 0 
        self.state        = self.initialState


        
    #done initializing variables

    def goalTest(self,node):
        
        if(node.state==self.goalState):
            
            return True
        
        else:
            
            return False

    def formatHTML(self,state):

        output = str()

        output = "<table>"            
        
        for i in state:
            
            output = output + "<tr>"
            
            for j in i:
                
                print str(j)  
            

            output = output + "</tr>"
        
        output = "</table>"

        return output

    def findNonce(self,input_array):

        
            floor, door  = 0,0
            expand_array = copy.deepcopy(input_array)
            
            for i in expand_array:
                
                for j in i:
                    
                    if(j==str(0)):
                        
                        floor = expand_array.index(i)
                        door  = i.index(j)
                   
            return floor,door

    
    def result(self,state,action):

        self.explored.append(state)


        return_state = None

        received_state = copy.deepcopy(state)

        floor,door = self.findNonce(received_state)
        
    
        if(action=="up" and floor == 0):
                        
            pass
        
        elif(action=="down" and floor == 2):
            
            pass
        
        elif(action=="left" and door == 0):
            
            pass
        
        elif(action=="right" and door == 2):
            
            pass
        
        elif(action=="up" and floor < 2 ):
            
            temp = received_state[floor-1][door]
            received_state[floor][door] = temp
            received_state[floor-1][door] = '0'
            
        elif(action=="down" and floor  > 0 ):
            
            temp = received_state[floor+1][door]
            received_state[floor][door] = temp
            received_state[floor+1][door] = '0'

        elif(action=="left" and  door  > 0):
            
            temp = received_state[floor][door-1]
            received_state[floor][door] = temp
            received_state[floor][door-1] = '0'
            
        elif(action=="right" and door < 2):

            temp = received_state[floor][door+1]
            received_state[floor][door] = temp
            received_state[floor][door+1] = '0'
            
                
        return received_state


    
    def childNode(self,in_node, action):

        node = Node(in_node)
        node.parent = copy.deepcopy(in_node)
        self.pathCost = self.pathCost + 1
        
        node.state = self.result(in_node.state,action)


        return (node)

    def bfs(self):

        time_start = time.time()

        resultLog.search_depth = resultLog.search_depth + 1

        node = Node(self)
        resultLog.nodes_expanded = resultLog.nodes_expanded + 1#check 1st parent

        if(self.goalTest(node)):

            return node

        self.frontier.append(node.state)


        resultLog.path_to_goal = list()

        goalMet = 0

        
        while (goalMet == 0):
 
            if(self.frontier==None):
                return "failure"

            new_state = list(self.frontier.pop())
            
            self.explored.append(new_state)

            for action in self.actions:

                resultLog.nodes_expanded = resultLog.nodes_expanded + 1 # check child 
                child = self.childNode(node,action)
               
                
                
                 #
                
                if(self.frontier.count(child.state) < 1 and self.explored.count(child.state) < 1):
                        
                    if(self.goalTest(child)):
                        goalMet = goalMet + 1
                        print child.state

                    resultLog.path_to_goal.append(action)
                 
                    self.frontier.append(child.state)
                      

                    resultLog.search_depth = resultLog.search_depth + 1
                    print str(child.state)
                    node = Node(child)


            usage = resource.getrusage(resource.RUSAGE_SELF)


            resultLog.max_ram_usage = getattr(usage,'ru_maxrss')
            time_end = time.time()
            resultLog.running_time = time_end-time_start
            

        
       
                
            


                                    
    
        

##################


p = Problem()

if(sys.argv[1]=="bfs"):
    
    p.bfs()
    print "path_to_goal:     " + str(resultLog.path_to_goal)
    print "cost_of_path:     " + str(len(resultLog.path_to_goal))
    print "nodes_expanded:   " + str( len(p.explored))
    print "max_search_depth: " + str((resultLog.search_depth))
    print "running_time:     " + str(resultLog.running_time) 
    print "max_ram_usage:    " + str(resultLog.max_ram_usage) 
        


#node.state = problem.initialState





#problem.frontier.append (node)

#current_node = node.frontier.pop()
#problem.explored.append(current_node)

#print "problem state -> " + str(node.state)










# class Driver:

#     def bfs:


#         return 
#          # s solution or failure

# class Node:
#     state
#     parent
#     action
#     pathCost

#     


    
#     current 
    
#     next []    


# mockboard = [0,1,2],[3,4,5],[6,7,8]

