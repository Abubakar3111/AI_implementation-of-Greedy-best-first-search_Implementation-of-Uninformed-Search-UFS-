
#abubakarasif3111@gmail.com
#https://github.com/Abubakar3111
#https://www.linkedin.com/in/abubakar-asif-b3b94021a/
print("\n\n#Implementation of Uninformed Search (UFS):\n\n by Abubakar Asif \n\n")
from search import *
graph={'S':{('A',5),('B',2),('C',4)}
       ,'A':{('D',9),('E',4)}
       ,'B':{('G',6)}
       ,'C':{('F',2)}
       ,'D':{('H',7)}
       ,'E':{('G',6)}
       ,'F':{('G',1)}}
class Node():
    def __init__(self,state,parent=None,cost=0,heuristic=0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def __repr__(self):
        return repr(f"[{self.state},{self.cost}]")
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
def goal_test(state):
    if state==goal:
        return True
    else: 
        return False
def sucessors(state): 
    return graph[state]
def node_to_path(node): 
    path=[node.state]
    while node.parent != None: 
        node=node.parent
        path.append(node.state)
    path.reverse()
    return path
def ufs(initial):
    frontier=PriorityQueue()
    inode=Node(initial)
    frontier.push(inode)
    explored={initial:0}    
    while  frontier.empty:
       print(frontier)   
       current_node=frontier.pop()
       current_state=current_node.state
       if goal_test(current_state):
           print(node_to_path(current_node))
           print("\nTotal Cost:",new_cost)          
           return current_node
       for (child,cost) in sucessors(current_state):
           new_cost=current_node.cost+ cost        
           if child not in explored or new_cost<explored[child]:        
              frontier.push(Node(child,current_node,new_cost))            
              explored[child]=new_cost
    return None       
start='S'
goal='G'
ufs(start)
  
#Node(child).cost