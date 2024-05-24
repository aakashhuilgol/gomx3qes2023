# Run as python checker-demo.py model.py
# Requires Python 3.7 or newer

import sys
from importlib import util
from timeit import default_timer as timer
import heapq as hq

class CostState(object):
    __slots__ = ("cost", "state")

    def __init__(self, cost: int, state):
        self.cost = cost
        self.state = state
    #def __eq__(self, other):
        # return self.cost == other.cost
    def __lt__(self, other):
        return self.cost < other.cost

# Load the model
if len(sys.argv) < 2:
	print("Error: No model specified.")
	quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end = "", flush = True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network() # create network instance
print(" done.")

def checkBFS(prop):
    visited = set()
    init_state = network.get_initial_state()
    queue = [init_state]
    goal_exp = prop.exp.args[0].args[1].args[0] if prop.exp.args[0].op == "until" else prop.exp.args[0].args[0].args[0]
    safe_exp = prop.exp.args[0].args[0].args[0] if prop.exp.args[0].op == "until" else -1
    current_state = init_state
    parent = {hash(current_state) : (current_state, "")}
    while (queue):
        current_state = queue.pop(0)
        if network.get_expression_value(current_state, goal_exp): #if goal reached then return True
            path = []
            init_hashed = hash(init_state)
            hashed = hash(current_state)
            while hashed != init_hashed:
                path.append(parent[hashed][1])
                path.append(str(parent[hashed][0]))
                hashed = hash(parent[hashed][0])
            path = path[::-1]
            path.append(str(current_state))
            return path, True 
        transitions = network.get_transitions(current_state)
        for transition in transitions:
            next_state = network.jump_np(current_state, transition)
            next_hashed = hash(next_state)
            if not next_hashed in visited and (safe_exp == -1 or network.get_expression_value(next_state, safe_exp)): #Evaluating if we are in safe states
                queue.append(next_state)
                parent[next_hashed] = (current_state, network.transition_labels[transition.label])
                visited.add(next_hashed)
    return ["false"], False



def checkCost(prop):
    init_state = network.get_initial_state()
    queue = [CostState(0,init_state)]
    table = {hash(init_state):(init_state,0,0)}
    current_state = init_state
    goal_exp = prop.exp.args[1].args[0]
    visited = set()
    while(queue):
        current_state = hq.heappop(queue).state
        if network.get_expression_value(current_state, goal_exp):
            copy = hash(current_state)
            path = []
            while table[copy][0] != init_state:
                path.append(table[copy][2])
                path.append(str(table[copy][0]))
                copy = hash(table[copy][0])
            path.append(table[copy][2])
            path.append(str(table[copy][0]))
            path = path[::-1]
            path.append(str(current_state))
            return (path, table[hash(current_state)][1])
        current_state_transitions = network.get_transitions(current_state)
        for transition in current_state_transitions:
            reward_exps = [prop.exp.args[0]]
            jump_state = network.jump_np(current_state, transition, reward_exps)
            hashed = hash(jump_state)
            if hashed not in visited:
                table[hashed] = (current_state, table[hash(current_state)][1]+reward_exps[0], network.transition_labels[transition.label])
                visited.add(hashed)
                hq.heappush(queue, CostState(table[hash(current_state)][1]+reward_exps[0], jump_state))
            elif table[hash(current_state)][1] + reward_exps[0] < table[hashed][1]:
                table[hashed] = (current_state, table[hash(current_state)][1]+reward_exps[0], network.transition_labels[transition.label])
                hq.heappush(queue, CostState(table[hash(current_state)][1]+reward_exps[0], jump_state))
    return ("","infinite")

for prop in network.properties:
    print_path = True
    show_time = True
    if(prop.exp.op == "exists"):
        start = timer()
        result = checkBFS(prop)
        end = timer()
        if show_time:
            print("Done in {0:.3f} seconds".format(end - start))
        print(prop.name+":",  result[1])
        if (result[1] and print_path):
            print(result[0])
    elif (prop.exp.op == "e_min_s"):
        start = timer()
        result=checkCost(prop)
        end = timer()
        if show_time:
            print("Done in {0:.3f} seconds".format(end - start))
        print(prop.name+":",  result[1])
        if(result[1]!="infinite" and print_path):
            print(result[0])
    print()
