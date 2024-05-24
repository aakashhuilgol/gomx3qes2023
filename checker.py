# Run as python checker-demo.py model.py
# Requires Python 3.7 or newer

import sys
from importlib import util
from timeit import default_timer as timer
import heapq as hq
import pickle


class CostState(object):
    __slots__ = ("cost", "state")

    def __init__(self, cost: int, state):
        self.cost = cost
        self.state = state
    # def __eq__(self, other):
        # return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost


# Load the model
if len(sys.argv) < 2:
    print("Error: No model specified.")
    quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end="", flush=True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network()  # create network instance
print(" done.")


def checkBFS(prop):
    visited = set()
    init_state = network.get_initial_state()
    queue = [init_state]
    goal_exp = prop.exp.args[0].args[1].args[0] if prop.exp.args[0].op == "until" else prop.exp.args[0].args[0].args[0]
    safe_exp = prop.exp.args[0].args[0].args[0] if prop.exp.args[0].op == "until" else -1
    current_state = init_state
    parent = {current_state: (current_state, "")}
    if network.get_expression_value(init_state, goal_exp):
        return [init_state], True
    if not safe_exp == -1 and not (network.get_expression_value(init_state, safe_exp)):
        return ["false"], False
    while (queue):
        current_state = queue.pop(0)
        # if goal reached then return True
        if network.get_expression_value(current_state, goal_exp):
            path = [current_state]
            while current_state != init_state:
                path.append(parent[current_state][1])
                path.append(parent[current_state][0])
                current_state = parent[current_state][0]
            path = path[::-1]
            return path, True
        transitions = network.get_transitions(current_state)
        for transition in transitions:
            next_state = network.jump_np(current_state, transition)
            # sprint(safe_exp)
            # Evaluating if we are in safe states
            if not next_state in visited and (safe_exp == -1 or network.get_expression_value(next_state, safe_exp) or network.get_expression_value(next_state, goal_exp)):
                queue.append(next_state)
                parent[next_state] = (
                    current_state, network.transition_labels[transition.label])
                visited.add(next_state)
    return ["false"], False


def checkCost(prop):
    init_state = network.get_initial_state()
    queue = [CostState(0, init_state)]
    table = {init_state: (init_state, 0, 0)}
    current_state = init_state
    goal_exp = prop.exp.args[1].args[0]
    while (queue):
        current_state = hq.heappop(queue).state
        if network.get_expression_value(current_state, goal_exp):
            path = [current_state]
            cost = table[current_state][1]
            while table[current_state][0] != init_state:
                path.append(table[current_state][2])
                path.append(table[current_state][0])
                current_state = table[current_state][0]
            path.append(table[current_state][2])
            path.append(table[current_state][0])
            path = path[::-1]
            return (path, cost)
        current_state_transitions = network.get_transitions(current_state)
        for transition in current_state_transitions:
            reward_exps = [prop.exp.args[0]]
            jump_state = network.jump_np(
                current_state, transition, reward_exps)
            if jump_state not in table:
                table[jump_state] = (current_state, table[
                    current_state][1]+reward_exps[0], network.transition_labels[transition.label])
                hq.heappush(queue, CostState(
                    table[current_state][1]+reward_exps[0], jump_state))
            elif table[current_state][1] + reward_exps[0] < table[jump_state][1]:
                table[current_state] = (current_state, table[
                    current_state][1]+reward_exps[0], network.transition_labels[transition.label])
                hq.heappush(queue, CostState(
                    table[current_state][1]+reward_exps[0], jump_state))
    return ("", "infinite")

save_schedule = True
for prop in network.properties:
    print_path = False
    show_time = True
    if (prop.exp.op == "exists"):
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
        result = checkCost(prop)
        end = timer()
        if show_time:
            print("Done in {0:.3f} seconds".format(end - start))
        print(prop.name+":",  result[1])
        if (result[1] != "infinite"):
            if print_path:
                for p in result[0]:
                    print(str(p))
            # save the schedule in a pickle file
            if save_schedule:
                charge = []
                sun = []
                uhf = []
                lband2 = []
                lband3 = []
                xband = []
                prev_state = result[0][0]
                for p in result[0]:
                    if type(p) is model.State:
                        if p.gc != prev_state.gc:
                            charge.append(prev_state.charge)
                            if prev_state.uhf_check:
                                uhf.append(prev_state.gc)
                            if prev_state.sun_load != 0:
                                sun.append(prev_state.gc)
                            if prev_state.lband2_check:
                                lband2.append(prev_state.gc)
                            elif prev_state.lband3_check:
                                lband3.append(prev_state.gc)
                            elif prev_state.xband_check:
                                xband.append(prev_state.gc)
                            prev_state = p
                with open('schedule.pkl', 'wb') as f:
                    pickle.dump(sun, f)
                    pickle.dump(uhf, f)
                    pickle.dump(lband2, f)
                    pickle.dump(lband3, f)
                    pickle.dump(xband, f)
                    pickle.dump(charge, f)
    print()
