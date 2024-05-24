# car_cruise_control

from __future__ import annotations
from typing import List, Union, Optional
import math

class ExplorationError(Exception):
	__slots__ = ("message")
	
	def __init__(self, message: str):
		self.message = message

class VariableInfo(object):
	__slots__ = ("name", "component", "type", "minValue", "maxValue")
	
	def __init__(self, name: str, component: Optional[int], type: str, minValue = None, maxValue = None):
		self.name = name
		self.component = component
		self.type = type
		self.minValue = minValue
		self.maxValue = maxValue

# States
class State(object):
	__slots__ = ("is_off", "is_on", "is_initiate", "is_stand_by", "is_set", "is_cruise", "is_hold", "is_warm_up", "i", "Main_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.is_off
		elif variable == 1:
			return self.is_on
		elif variable == 2:
			return self.is_initiate
		elif variable == 3:
			return self.is_stand_by
		elif variable == 4:
			return self.is_set
		elif variable == 5:
			return self.is_cruise
		elif variable == 6:
			return self.is_hold
		elif variable == 7:
			return self.is_warm_up
		elif variable == 8:
			return self.i
		elif variable == 9:
			return self.Main_location
	
	def copy_to(self, other: State):
		other.is_off = self.is_off
		other.is_on = self.is_on
		other.is_initiate = self.is_initiate
		other.is_stand_by = self.is_stand_by
		other.is_set = self.is_set
		other.is_cruise = self.is_cruise
		other.is_hold = self.is_hold
		other.is_warm_up = self.is_warm_up
		other.i = self.i
		other.Main_location = self.Main_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.is_off == other.is_off and self.is_on == other.is_on and self.is_initiate == other.is_initiate and self.is_stand_by == other.is_stand_by and self.is_set == other.is_set and self.is_cruise == other.is_cruise and self.is_hold == other.is_hold and self.is_warm_up == other.is_warm_up and self.i == other.i and self.Main_location == other.Main_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_off)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_on)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_initiate)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_stand_by)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_set)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_cruise)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_hold)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_warm_up)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Main_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "is_off = " + str(self.is_off)
		result += ", is_on = " + str(self.is_on)
		result += ", is_initiate = " + str(self.is_initiate)
		result += ", is_stand_by = " + str(self.is_stand_by)
		result += ", is_set = " + str(self.is_set)
		result += ", is_cruise = " + str(self.is_cruise)
		result += ", is_hold = " + str(self.is_hold)
		result += ", is_warm_up = " + str(self.is_warm_up)
		result += ", i = " + str(self.i)
		result += ", Main_location = " + str(self.Main_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("startCruiseSystem", "reward")
	
	def copy_to(self, other: Transient):
		other.startCruiseSystem = self.startCruiseSystem
		other.reward = self.reward
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.startCruiseSystem == other.startCruiseSystem and self.reward == other.reward
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.startCruiseSystem)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.reward)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "startCruiseSystem = " + str(self.startCruiseSystem)
		result += ", reward = " + str(self.reward)
		result += ")"
		return result

# Automaton: Main
class MainAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1]
		self.transition_labels = [[1], [0, 0], [2], [3, 4], [0], [5, 6], [5, 4], [0], [4, 7], [7], [0], [8]]
		self.branch_counts = [[1], [1, 1], [1], [1, 1], [1], [1, 1], [1, 1], [1], [1, 1], [1], [1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Main_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Main_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Main_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Main_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Main_location
		if location == 0 or location == 2 or location == 4 or location == 7 or location == 9 or location == 10 or location == 11:
			return True
		elif location == 1:
			if transition == 0:
				return (state.i < 10)
			elif transition == 1:
				return (state.i >= 10)
			else:
				raise IndexError
		elif location == 3:
			return True
		elif location == 5:
			return True
		elif location == 6:
			return True
		elif location == 8:
			return True
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Main_location
		if location == 0 or location == 2 or location == 4 or location == 7 or location == 9 or location == 10 or location == 11:
			return None
		elif location == 1:
			return None
		elif location == 3:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 8:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Main_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Main_location
		if location == 0:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Main_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.is_on = True
						target_state.Main_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
						target_state.Main_location = 11
				elif transition == 1:
					if branch == 0:
						target_state.is_warm_up = True
						target_state.Main_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.is_initiate = True
						target_state.is_warm_up = False
						target_state.is_on = False
						target_state.i = (state.i + 1)
						target_state.Main_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.is_set = True
						target_state.is_initiate = False
						target_state.i = (state.i + 2)
						target_state.Main_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.is_off = True
						target_state.is_initiate = False
						target_state.Main_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Main_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.is_stand_by = True
						target_state.is_set = False
						target_state.i = (state.i + 3)
						target_state.Main_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.is_hold = True
						target_state.is_set = False
						target_state.Main_location = 6
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.is_stand_by = True
						target_state.is_hold = False
						target_state.i = (state.i + 1)
						target_state.Main_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.is_off = True
						target_state.is_hold = False
						target_state.Main_location = 7
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Main_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.is_off = True
						target_state.is_stand_by = False
						target_state.Main_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.is_cruise = True
						target_state.is_stand_by = False
						target_transient.reward = state.i
						target_state.Main_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Main_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Main_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_transient.startCruiseSystem = state.i
						target_state.Main_location = 1

class PropertyExpression(object):
	__slots__ = ("op", "args")
	
	def __init__(self, op: str, args: List[Union[int, float, PropertyExpression]]):
		self.op = op
		self.args = args
	
	def __str__(self):
		result = self.op + "("
		needComma = False
		for arg in self.args:
			if needComma:
				result += ", "
			else:
				needComma = True
			result += str(arg)
		return result + ")"

class Property(object):
	__slots__ = ("name", "exp")
	
	def __init__(self, name: str, exp: PropertyExpression):
		self.name = name
		self.exp = exp
	
	def __str__(self):
		return self.name + ": " + str(self.exp)

class Transition(object):
	__slots__ = ("sync_vector", "label", "transitions")
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Main")
	
	def __init__(self):
		self.network = self
		self.model_type = "lts"
		self.transition_labels = { 0: "τ", 1: "on", 2: "initiate", 3: "set", 4: "off", 5: "stand_by", 6: "hold", 7: "cruise", 8: "warm_up" }
		self.sync_vectors = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
		self.properties = [
			Property("Prop1", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])),
			Property("Prop2", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [1])])])),
			Property("Prop3", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [2])])])),
			Property("Prop4", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [3])])])),
			Property("Prop5", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [4])])])),
			Property("Prop6", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [5])])])),
			Property("Prop7", PropertyExpression("exists", [PropertyExpression("until", [PropertyExpression("ap", [6]), PropertyExpression("ap", [7])])])),
			Property("Prop8", PropertyExpression("exists", [PropertyExpression("until", [PropertyExpression("ap", [8]), PropertyExpression("ap", [3])])])),
			Property("Prop9", PropertyExpression("exists", [PropertyExpression("until", [PropertyExpression("ap", [9]), PropertyExpression("ap", [7])])])),
			Property("PropCruiseReward", PropertyExpression("e_min_s", [10, PropertyExpression("ap", [7])])),
			Property("PropCruiseSystemCost", PropertyExpression("e_min_s", [11, PropertyExpression("ap", [12])]))
		]
		self.variables = [
			VariableInfo("is_off", None, "bool"),
			VariableInfo("is_on", None, "bool"),
			VariableInfo("is_initiate", None, "bool"),
			VariableInfo("is_stand_by", None, "bool"),
			VariableInfo("is_set", None, "bool"),
			VariableInfo("is_cruise", None, "bool"),
			VariableInfo("is_hold", None, "bool"),
			VariableInfo("is_warm_up", None, "bool"),
			VariableInfo("i", None, "int"),
			VariableInfo("Main_location", 0, "int", 0, 11)
		]
		self._aut_Main = MainAutomaton(self)
		self.components = [self._aut_Main]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.is_off = False
		state.is_on = False
		state.is_initiate = False
		state.is_stand_by = False
		state.is_set = False
		state.is_cruise = False
		state.is_hold = False
		state.is_warm_up = False
		state.i = 0
		self._aut_Main.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.startCruiseSystem = 0
		transient.reward = 0
		self._aut_Main.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return state.is_on
		elif expression == 1:
			return state.is_initiate
		elif expression == 2:
			return state.is_stand_by
		elif expression == 3:
			return state.is_set
		elif expression == 4:
			return state.is_hold
		elif expression == 5:
			return state.is_off
		elif expression == 6:
			return (state.i <= 20)
		elif expression == 7:
			return state.is_cruise
		elif expression == 8:
			return (((not state.is_on) and (not state.is_warm_up)) and (not state.is_initiate))
		elif expression == 9:
			return (((((not state.is_on) and (not state.is_initiate)) and (not state.is_set)) and (not state.is_hold)) and (not state.is_stand_by))
		elif expression == 10:
			return self.network._get_transient_value(state, "reward")
		elif expression == 11:
			return self.network._get_transient_value(state, "startCruiseSystem")
		elif expression == 12:
			return state.is_warm_up
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return state.is_on
		elif expression == 1:
			return state.is_initiate
		elif expression == 2:
			return state.is_stand_by
		elif expression == 3:
			return state.is_set
		elif expression == 4:
			return state.is_hold
		elif expression == 5:
			return state.is_off
		elif expression == 6:
			return (state.i <= 20)
		elif expression == 7:
			return state.is_cruise
		elif expression == 8:
			return (((not state.is_on) and (not state.is_warm_up)) and (not state.is_initiate))
		elif expression == 9:
			return (((((not state.is_on) and (not state.is_initiate)) and (not state.is_set)) and (not state.is_hold)) and (not state.is_stand_by))
		elif expression == 10:
			return transient.reward
		elif expression == 11:
			return transient.startCruiseSystem
		elif expression == 12:
			return state.is_warm_up
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Main.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Main = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Main.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Main.get_guard_value(state, i):
				trans_Main[self._aut_Main.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1]]
			# Main
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Main[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Main[sv[0]][0]
						for i in range(1, len(trans_Main[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Main[sv[0]][i]
			if synced is not None:
				for sync in synced:
					sync[-1] = sv[-1]
					sync.append(svi)
				transitions.extend(filter(lambda s: s[-2] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][-1], transitions[i][-2], transitions[i])
			del transitions[i].transitions[-1]
			del transitions[i].transitions[-1]
		# Done
		return transitions
	
	def get_rate(self, state: State, transition: Transition) -> Optional[float]:
		for i in range(len(self.components)):
			if transition.transitions[i] != -1:
				rate = self.components[i].get_rate_value(state, transition.transitions[i])
				if rate is not None:
					for j in range(i + 1, len(self.components)):
						if transition.transitions[j] != -1:
							check_rate = self.components[j].get_rate_value(state, transition)
							if check_rate is not None:
								raise ExplorationError("Invalid MA model: Multiple components specify a rate for the same transition.")
					return rate
		return None
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Main.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Main.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Main.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		result = list(filter(lambda b: b.probability > 0.0, combs))
		if len(result) == 0:
			raise ExplorationError("Invalid model: All branches of a transition have probability zero.")
		return result
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 1):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_Main.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
