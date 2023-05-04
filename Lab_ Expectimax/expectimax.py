import math

adj_lst={'A':{'B','C','D'}, 'B':{'E','F'}, 'C':{'G','H'}, 'D':{'I','J'}}
terminal_value={'E':[90,0.5],'F':[12,0.5],'G':[8,0.5],'H':[112,0.5],'I':[4,0.5],'J':[90,0.5]}

def is_terminal(state):
    if state in terminal_value:
        return True
    
def val_terminal(state):
    return terminal_value[state][0]

def max_value(state):
    if is_terminal(state)==True:
        return val_terminal(state)
    else:
        max_val=-float('inf')
        for x in adj_lst[state]:
            max_val=max(avg_value(x), max_val)
        return max_val
    

def avg_value(state):
    if is_terminal(state)==True:
        return val_terminal(state)
    else:
        sum = 0
        for x in adj_lst[state]:
            sum += terminal_value[x][1]*max_value(x)
        return sum


print(max_value('A'))
            
