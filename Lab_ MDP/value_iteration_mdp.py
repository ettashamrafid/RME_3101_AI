import math
grid_world=[
    [0,0,0,1],
    [0,0,0,-1],
    [0,0,0,0]
]

gamma=0.9 #discount
noise=0.2
row_no= len(grid_world)
column_no=len(grid_world[0])


action_lst={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

def terminal_state(state):
    (row,col)=state
    if (row,col)==(1,3) or (row,col)==(0,3):
        return True
    return False

main_prob=1-noise
side_prob=noise/2
value_space=[]

for i in range(row_no):
    x=[]
    for j in range(column_no):
        x.append(0)
    value_space.append(x)



def value(state):
    (i,j)=state
    return value_space[i][j]

def next_state(state,action):
    (i,j)=state
    next_i= i + action_lst[action][0]
    next_j=j + action_lst[action][1]
    if next_i<0 or next_i>=row_no or next_j<0 or next_j>=column_no:
        next_i,next_j= i,j
    return next_i, next_j

def get_value(action,state):
    (i,j)=state
    if action=='U':
        val= main_prob*gamma*value(next_state(state,"U"))+ side_prob*gamma*value(next_state(state,"L"))+ side_prob*gamma*value(next_state(state,"R"))
    elif action=='D':
        val= main_prob*gamma*value(next_state(state,"D"))+ side_prob*gamma*value(next_state(state,"L"))+ side_prob*gamma*value(next_state(state,"R"))
    elif action=='L':
        val= main_prob*gamma*value(next_state(state,"L"))+ side_prob*gamma*value(next_state(state,"U"))+ side_prob*gamma*value(next_state(state,"D"))
    elif action=='R':
        val= main_prob*gamma*value(next_state(state,"R"))+ side_prob*gamma*value(next_state(state,"U"))+ side_prob*gamma*value(next_state(state,"D"))

    return val

best_actions=[]
for i in range(row_no):
    x=[]
    for j in range(column_no):
        x.append(None)
    best_actions.append(x)



for k in range(100):
    for i in range(row_no):
        for j in range(column_no):
            state=(i,j)

            if terminal_state(state) or state==(1,1):
                value_space[i][j]=grid_world[i][j]
            
            else:
                max_v=-float('inf')
                for action in action_lst:
                    state_v=get_value(action,(i,j))
                    if state_v>max_v:
                        max_v=state_v
                        best_a=action

                value_space[i][j]=max_v
                best_actions[i][j]=best_a

final_value=[]
for i in range(row_no):
    x=[]
    for j in range(column_no):
        x.append((best_actions[i][j],value_space[i][j]))
    final_value.append(x)


for i in range(row_no):
    for j in range(column_no):
        print(final_value[i][j],end="")
    print("")
    



