# model

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
	__slots__ = ("lband2", "lband3", "sun", "uhf", "xband", "charge", "R", "current_time", "lock", "uhf_check", "lband2_check", "lband3_check", "xband_check", "l2_count", "l3_count", "x_count", "sun_load", "uhf_load", "lband2_load", "lband3_load", "xband_load", "gc", "Lband2_location", "i", "Lband3_location", "j", "Xband_location", "i_1", "Sun_location", "i_2", "UHF_location", "i_3", "LinearBattery_location", "last_time", "last_load")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.lband2
		elif variable == 1:
			return self.lband3
		elif variable == 2:
			return self.sun
		elif variable == 3:
			return self.uhf
		elif variable == 4:
			return self.xband
		elif variable == 5:
			return self.charge
		elif variable == 6:
			return self.R
		elif variable == 7:
			return self.current_time
		elif variable == 8:
			return self.lock
		elif variable == 9:
			return self.uhf_check
		elif variable == 10:
			return self.lband2_check
		elif variable == 11:
			return self.lband3_check
		elif variable == 12:
			return self.xband_check
		elif variable == 13:
			return self.l2_count
		elif variable == 14:
			return self.l3_count
		elif variable == 15:
			return self.x_count
		elif variable == 16:
			return self.sun_load
		elif variable == 17:
			return self.uhf_load
		elif variable == 18:
			return self.lband2_load
		elif variable == 19:
			return self.lband3_load
		elif variable == 20:
			return self.xband_load
		elif variable == 21:
			return self.gc
		elif variable == 22:
			return self.Lband2_location
		elif variable == 23:
			return self.i
		elif variable == 24:
			return self.Lband3_location
		elif variable == 25:
			return self.j
		elif variable == 26:
			return self.Xband_location
		elif variable == 27:
			return self.i_1
		elif variable == 28:
			return self.Sun_location
		elif variable == 29:
			return self.i_2
		elif variable == 30:
			return self.UHF_location
		elif variable == 31:
			return self.i_3
		elif variable == 32:
			return self.LinearBattery_location
		elif variable == 33:
			return self.last_time
		elif variable == 34:
			return self.last_load
	
	def copy_to(self, other: State):
		other.lband2 = list(self.lband2)
		other.lband3 = list(self.lband3)
		other.sun = list(self.sun)
		other.uhf = list(self.uhf)
		other.xband = list(self.xband)
		other.charge = self.charge
		other.R = self.R
		other.current_time = self.current_time
		other.lock = self.lock
		other.uhf_check = self.uhf_check
		other.lband2_check = self.lband2_check
		other.lband3_check = self.lband3_check
		other.xband_check = self.xband_check
		other.l2_count = self.l2_count
		other.l3_count = self.l3_count
		other.x_count = self.x_count
		other.sun_load = self.sun_load
		other.uhf_load = self.uhf_load
		other.lband2_load = self.lband2_load
		other.lband3_load = self.lband3_load
		other.xband_load = self.xband_load
		other.gc = self.gc
		other.Lband2_location = self.Lband2_location
		other.i = self.i
		other.Lband3_location = self.Lband3_location
		other.j = self.j
		other.Xband_location = self.Xband_location
		other.i_1 = self.i_1
		other.Sun_location = self.Sun_location
		other.i_2 = self.i_2
		other.UHF_location = self.UHF_location
		other.i_3 = self.i_3
		other.LinearBattery_location = self.LinearBattery_location
		other.last_time = self.last_time
		other.last_load = self.last_load
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.lband2 == other.lband2 and self.lband3 == other.lband3 and self.sun == other.sun and self.uhf == other.uhf and self.xband == other.xband and self.charge == other.charge and self.R == other.R and self.current_time == other.current_time and self.lock == other.lock and self.uhf_check == other.uhf_check and self.lband2_check == other.lband2_check and self.lband3_check == other.lband3_check and self.xband_check == other.xband_check and self.l2_count == other.l2_count and self.l3_count == other.l3_count and self.x_count == other.x_count and self.sun_load == other.sun_load and self.uhf_load == other.uhf_load and self.lband2_load == other.lband2_load and self.lband3_load == other.lband3_load and self.xband_load == other.xband_load and self.gc == other.gc and self.Lband2_location == other.Lband2_location and self.i == other.i and self.Lband3_location == other.Lband3_location and self.j == other.j and self.Xband_location == other.Xband_location and self.i_1 == other.i_1 and self.Sun_location == other.Sun_location and self.i_2 == other.i_2 and self.UHF_location == other.UHF_location and self.i_3 == other.i_3 and self.LinearBattery_location == other.LinearBattery_location and self.last_time == other.last_time and self.last_load == other.last_load
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		for x in self.lband2:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.lband3:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.sun:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.uhf:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.xband:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.charge)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.current_time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.lock)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.uhf_check)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.lband2_check)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.lband3_check)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.xband_check)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.l2_count)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.l3_count)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x_count)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.sun_load)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.uhf_load)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.lband2_load)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.lband3_load)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.xband_load)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.gc)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Lband2_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Lband3_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.j)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Xband_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Sun_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.UHF_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i_3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.LinearBattery_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.last_time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.last_load)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "lband2 = " + str(self.lband2)
		result += ", lband3 = " + str(self.lband3)
		result += ", sun = " + str(self.sun)
		result += ", uhf = " + str(self.uhf)
		result += ", xband = " + str(self.xband)
		result += ", charge = " + str(self.charge)
		result += ", R = " + str(self.R)
		result += ", current_time = " + str(self.current_time)
		result += ", lock = " + str(self.lock)
		result += ", uhf_check = " + str(self.uhf_check)
		result += ", lband2_check = " + str(self.lband2_check)
		result += ", lband3_check = " + str(self.lband3_check)
		result += ", xband_check = " + str(self.xband_check)
		result += ", l2_count = " + str(self.l2_count)
		result += ", l3_count = " + str(self.l3_count)
		result += ", x_count = " + str(self.x_count)
		result += ", sun_load = " + str(self.sun_load)
		result += ", uhf_load = " + str(self.uhf_load)
		result += ", lband2_load = " + str(self.lband2_load)
		result += ", lband3_load = " + str(self.lband3_load)
		result += ", xband_load = " + str(self.xband_load)
		result += ", gc = " + str(self.gc)
		result += ", Lband2_location = " + str(self.Lband2_location)
		result += ", i = " + str(self.i)
		result += ", Lband3_location = " + str(self.Lband3_location)
		result += ", j = " + str(self.j)
		result += ", Xband_location = " + str(self.Xband_location)
		result += ", i_1 = " + str(self.i_1)
		result += ", Sun_location = " + str(self.Sun_location)
		result += ", i_2 = " + str(self.i_2)
		result += ", UHF_location = " + str(self.UHF_location)
		result += ", i_3 = " + str(self.i_3)
		result += ", LinearBattery_location = " + str(self.LinearBattery_location)
		result += ", last_time = " + str(self.last_time)
		result += ", last_load = " + str(self.last_load)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("prop3_edge_reward", "done", "cost")
	
	def copy_to(self, other: Transient):
		other.prop3_edge_reward = self.prop3_edge_reward
		other.done = self.done
		other.cost = self.cost
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.prop3_edge_reward == other.prop3_edge_reward and self.done == other.done and self.cost == other.cost
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.prop3_edge_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.done)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cost)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "prop3_edge_reward = " + str(self.prop3_edge_reward)
		result += ", done = " + str(self.done)
		result += ", cost = " + str(self.cost)
		result += ")"
		return result

# Automaton: Lband2
class Lband2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 2, 2, 2, 2, 2, 3, 1, 3, 3]
		self.transition_labels = [[8, 8, 7], [1, 7], [8, 7], [1, 7], [8, 7], [1, 7], [8, 7], [1, 1, 7], [7], [8, 8, 7], [8, 8, 7]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Lband2_location = 0
		state.i = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Lband2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Lband2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Lband2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Lband2_location
		if location == 8:
			return True
		elif location == 0:
			if transition == 0:
				return (state.gc >= (((state.lband2)[state.i] - 1200) - 600))
			elif transition == 1:
				return ((((state.gc >= (((state.lband2)[state.i] - 1200) - 600)) and (not state.lock)) and ((state.l2_count - state.l3_count) < 2)) and (state.R < 4))
			elif transition == 2:
				return (state.gc < (((state.lband2)[state.i] - 1200) - 600))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (((state.lband2)[state.i] - 1200) - 600))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.gc >= (state.lband2)[state.i])
			elif transition == 1:
				return (state.gc < (state.lband2)[state.i])
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (state.lband2)[state.i])
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (state.gc >= (state.lband2)[state.i])
			elif transition == 1:
				return (state.gc < (state.lband2)[state.i])
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (state.lband2)[state.i])
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return (state.gc >= ((state.lband2)[state.i] + 600))
			elif transition == 1:
				return (state.gc < ((state.lband2)[state.i] + 600))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.i < 15)
			elif transition == 1:
				return (state.i == 15)
			elif transition == 2:
				return (state.gc < ((state.lband2)[state.i] + 600))
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return (state.gc >= (((state.lband2)[state.i] - 1200) - 600))
			elif transition == 1:
				return ((((state.gc >= (((state.lband2)[state.i] - 1200) - 600)) and (not state.lock)) and ((state.l2_count - state.l3_count) < 2)) and (state.R < 4))
			elif transition == 2:
				return (state.gc < (((state.lband2)[state.i] - 1200) - 600))
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (state.i < 15)
			elif transition == 1:
				return (state.i == 15)
			elif transition == 2:
				return (state.gc < (((state.lband2)[state.i] - 1200) - 600))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Lband2_location
		if location == 8:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Lband2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Lband2_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
			elif transition == 1:
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
			elif transition == 1:
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
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Lband2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
						target_transient.cost = 5
				elif transition == 1:
					if branch == 0:
						target_state.lband2_load = 414
						target_state.current_time = (((state.lband2)[state.i] - 1200) - 600)
						target_state.lock = True
						target_state.l2_count = (state.l2_count + 1)
						target_state.R = (state.R + 2)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.lband2_load = 3863
						target_state.current_time = (state.lband2)[state.i]
						target_state.lband2_check = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
						target_transient.cost = (((((state.l2_count + state.l3_count) + 1) / (state.x_count + 1)) * (((state.l2_count + state.l3_count) + 1) / (state.x_count + 1))) + ((((state.l2_count * state.l2_count) + (state.l3_count * state.l3_count)) + 1) / ((state.l2_count * state.l3_count) + 1)))
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.lband2_load = 414
						target_state.current_time = (state.lband2)[state.i]
						target_state.lband2_check = False
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.lband2_load = 0
						target_state.current_time = ((state.lband2)[state.i] + 600)
						target_state.lock = False
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
				elif transition == 1:
					if branch == 0:
						target_state.i = 0
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
						target_transient.cost = 5
				elif transition == 1:
					if branch == 0:
						target_state.lband2_load = 414
						target_state.current_time = (((state.lband2)[state.i] - 1200) - 600)
						target_state.lock = True
						target_state.l2_count = (state.l2_count + 1)
						target_state.R = (state.R + 2)
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
				elif transition == 1:
					if branch == 0:
						target_state.i = 0
		elif assignment_index == 2:
			location = state.Lband2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Lband2_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Lband2_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Lband2_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Lband2_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Lband2_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Lband2_location = 10

# Automaton: Lband3
class Lband3Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 2, 2, 2, 2, 2, 3, 1, 3, 3]
		self.transition_labels = [[8, 8, 7], [2, 7], [8, 7], [2, 7], [8, 7], [2, 7], [8, 7], [2, 2, 7], [7], [8, 8, 7], [8, 8, 7]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Lband3_location = 0
		state.j = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Lband3_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Lband3_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Lband3_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Lband3_location
		if location == 8:
			return True
		elif location == 0:
			if transition == 0:
				return (state.gc >= (((state.lband3)[state.j] - 1200) - 600))
			elif transition == 1:
				return ((((state.gc >= (((state.lband3)[state.j] - 1200) - 600)) and (not state.lock)) and ((state.l3_count - state.l2_count) < 2)) and (state.R < 4))
			elif transition == 2:
				return (state.gc < (((state.lband3)[state.j] - 1200) - 600))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (((state.lband3)[state.j] - 1200) - 600))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.gc >= (state.lband3)[state.j])
			elif transition == 1:
				return (state.gc < (state.lband3)[state.j])
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (state.lband3)[state.j])
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (state.gc >= (state.lband3)[state.j])
			elif transition == 1:
				return (state.gc < (state.lband3)[state.j])
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (state.lband3)[state.j])
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return (state.gc >= ((state.lband3)[state.j] + 600))
			elif transition == 1:
				return (state.gc < ((state.lband3)[state.j] + 600))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.j < 15)
			elif transition == 1:
				return (state.j == 15)
			elif transition == 2:
				return (state.gc < ((state.lband3)[state.j] + 600))
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return (state.gc >= (((state.lband3)[state.j] - 1200) - 600))
			elif transition == 1:
				return ((((state.gc >= (((state.lband3)[state.j] - 1200) - 600)) and (not state.lock)) and ((state.l3_count - state.l2_count) < 2)) and (state.R < 4))
			elif transition == 2:
				return (state.gc < (((state.lband3)[state.j] - 1200) - 600))
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (state.j < 15)
			elif transition == 1:
				return (state.j == 15)
			elif transition == 2:
				return (state.gc < (((state.lband3)[state.j] - 1200) - 600))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Lband3_location
		if location == 8:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Lband3_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Lband3_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
			elif transition == 1:
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
			elif transition == 1:
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
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Lband3_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.j = (state.j + 1)
						target_transient.cost = 5
				elif transition == 1:
					if branch == 0:
						target_state.lband3_load = 414
						target_state.current_time = (((state.lband3)[state.j] - 1200) - 600)
						target_state.lock = True
						target_state.l3_count = (state.l3_count + 1)
						target_state.R = (state.R + 2)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.lband3_load = 3863
						target_state.current_time = (state.lband3)[state.j]
						target_state.lband3_check = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.j = (state.j + 1)
						target_transient.cost = (((((state.l2_count + state.l3_count) + 1) / (state.x_count + 1)) * (((state.l2_count + state.l3_count) + 1) / (state.x_count + 1))) + ((((state.l2_count * state.l2_count) + (state.l3_count * state.l3_count)) + 1) / ((state.l2_count * state.l3_count) + 1)))
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.lband3_load = 414
						target_state.current_time = (state.lband3)[state.j]
						target_state.lband3_check = False
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.lband3_load = 0
						target_state.current_time = ((state.lband3)[state.j] + 600)
						target_state.lock = False
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.j = (state.j + 1)
				elif transition == 1:
					if branch == 0:
						target_state.j = 0
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.j = (state.j + 1)
						target_transient.cost = 5
				elif transition == 1:
					if branch == 0:
						target_state.lband3_load = 414
						target_state.current_time = (((state.lband3)[state.j] - 1200) - 600)
						target_state.lock = True
						target_state.l3_count = (state.l3_count + 1)
						target_state.R = (state.R + 2)
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.j = (state.j + 1)
				elif transition == 1:
					if branch == 0:
						target_state.j = 0
		elif assignment_index == 2:
			location = state.Lband3_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Lband3_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Lband3_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Lband3_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Lband3_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Lband3_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Lband3_location = 10

# Automaton: Xband
class XbandAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 2, 2, 2, 2, 2, 3, 1, 3, 3]
		self.transition_labels = [[8, 8, 7], [3, 7], [8, 7], [3, 7], [8, 7], [3, 7], [8, 7], [3, 3, 7], [7], [8, 8, 7], [8, 8, 7]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Xband_location = 0
		state.i_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Xband_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Xband_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Xband_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Xband_location
		if location == 8:
			return True
		elif location == 0:
			if transition == 0:
				return (state.gc >= (((state.xband)[state.i_1] - 1200) - 600))
			elif transition == 1:
				return (((state.gc >= (((state.xband)[state.i_1] - 1200) - 600)) and (not state.lock)) and (state.R >= 1))
			elif transition == 2:
				return (state.gc < (((state.xband)[state.i_1] - 1200) - 600))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (((state.xband)[state.i_1] - 1200) - 600))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.gc >= (state.xband)[state.i_1])
			elif transition == 1:
				return (state.gc < (state.xband)[state.i_1])
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (state.xband)[state.i_1])
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (state.gc >= (state.xband)[state.i_1])
			elif transition == 1:
				return (state.gc < (state.xband)[state.i_1])
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < (state.xband)[state.i_1])
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return (state.gc >= ((state.xband)[state.i_1] + 600))
			elif transition == 1:
				return (state.gc < ((state.xband)[state.i_1] + 600))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.i_1 < 19)
			elif transition == 1:
				return (state.i_1 == 19)
			elif transition == 2:
				return (state.gc < ((state.xband)[state.i_1] + 600))
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return (state.gc >= (((state.xband)[state.i_1] - 1200) - 600))
			elif transition == 1:
				return (((state.gc >= (((state.xband)[state.i_1] - 1200) - 600)) and (not state.lock)) and (state.R >= 1))
			elif transition == 2:
				return (state.gc < (((state.xband)[state.i_1] - 1200) - 600))
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (state.i_1 < 19)
			elif transition == 1:
				return (state.i_1 == 19)
			elif transition == 2:
				return (state.gc < (((state.xband)[state.i_1] - 1200) - 600))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Xband_location
		if location == 8:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Xband_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Xband_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
			elif transition == 1:
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
			elif transition == 1:
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
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Xband_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.i_1 = (state.i_1 + 1)
						target_transient.cost = 5
				elif transition == 1:
					if branch == 0:
						target_state.xband_load = 414
						target_state.current_time = (((state.xband)[state.i_1] - 1200) - 600)
						target_state.lock = True
						target_state.R = (state.R - 1)
						target_state.x_count = (state.x_count + 1)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.xband_load = 11945
						target_state.current_time = (state.xband)[state.i_1]
						target_state.xband_check = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.i_1 = (state.i_1 + 1)
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.xband_load = 414
						target_state.current_time = (state.xband)[state.i_1]
						target_state.xband_check = False
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.xband_load = 0
						target_state.current_time = ((state.xband)[state.i_1] + 600)
						target_state.lock = False
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.i_1 = (state.i_1 + 1)
				elif transition == 1:
					if branch == 0:
						target_state.i_1 = 0
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.i_1 = (state.i_1 + 1)
						target_transient.cost = 5
				elif transition == 1:
					if branch == 0:
						target_state.xband_load = 414
						target_state.current_time = (((state.xband)[state.i_1] - 1200) - 600)
						target_state.lock = True
						target_state.R = (state.R - 1)
						target_state.x_count = (state.x_count + 1)
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.i_1 = (state.i_1 + 1)
				elif transition == 1:
					if branch == 0:
						target_state.i_1 = 0
		elif assignment_index == 2:
			location = state.Xband_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Xband_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Xband_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Xband_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Xband_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Xband_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Xband_location = 10

# Automaton: Sun
class SunAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 3, 1, 2]
		self.transition_labels = [[8, 7], [4, 4, 7], [7], [8, 7]]
		self.branch_counts = [[1, 1], [1, 1, 1], [1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Sun_location = 0
		state.i_2 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Sun_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Sun_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Sun_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Sun_location
		if location == 2:
			return True
		elif location == 0:
			if transition == 0:
				return (state.gc >= (state.sun)[state.i_2])
			elif transition == 1:
				return (state.gc < (state.sun)[state.i_2])
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return (state.i_2 < 21)
			elif transition == 1:
				return (state.i_2 == 21)
			elif transition == 2:
				return (state.gc < (state.sun)[state.i_2])
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (state.gc >= (state.sun)[state.i_2])
			elif transition == 1:
				return (state.gc < (state.sun)[state.i_2])
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Sun_location
		if location == 2:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 3:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Sun_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Sun_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Sun_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.sun_load = (5700 * ((state.i_2 + 1) % 2))
						target_state.current_time = (state.sun)[state.i_2]
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.i_2 = (state.i_2 + 1)
				elif transition == 1:
					if branch == 0:
						target_state.i_2 = 0
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.sun_load = (5700 * ((state.i_2 + 1) % 2))
						target_state.current_time = (state.sun)[state.i_2]
		elif assignment_index == 2:
			location = state.Sun_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.Sun_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location = 3

# Automaton: UHF
class UHFAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 2, 2, 3, 1, 2]
		self.transition_labels = [[8, 7], [5, 7], [8, 7], [5, 7], [8, 7], [5, 5, 7], [7], [8, 7]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.UHF_location = 0
		state.i_3 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.UHF_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.UHF_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.UHF_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.UHF_location
		if location == 6:
			return True
		elif location == 0:
			if transition == 0:
				return (state.gc >= ((state.uhf)[state.i_3] - 1200))
			elif transition == 1:
				return (state.gc < ((state.uhf)[state.i_3] - 1200))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return (state.gc >= ((state.uhf)[state.i_3] - 1200))
			elif transition == 1:
				return (state.gc < ((state.uhf)[state.i_3] - 1200))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.gc >= (state.uhf)[state.i_3])
			elif transition == 1:
				return (state.gc < (state.uhf)[state.i_3])
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (state.gc >= (state.uhf)[state.i_3])
			elif transition == 1:
				return (state.gc < (state.uhf)[state.i_3])
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (state.gc >= (state.uhf)[state.i_3])
			elif transition == 1:
				return (state.gc < (state.uhf)[state.i_3])
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (state.i_3 < 11)
			elif transition == 1:
				return (state.i_3 == 11)
			elif transition == 2:
				return (state.gc < (state.uhf)[state.i_3])
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.gc >= ((state.uhf)[state.i_3] - 1200))
			elif transition == 1:
				return (state.gc < ((state.uhf)[state.i_3] - 1200))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.UHF_location
		if location == 6:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 7:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.UHF_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.UHF_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
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
			elif transition == 1:
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
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.UHF_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.uhf_load = 414
						target_state.current_time = ((state.uhf)[state.i_3] - 1200)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.uhf_load = 2630
						target_state.current_time = (state.uhf)[state.i_3]
						target_state.uhf_check = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.i_3 = (state.i_3 + 1)
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.uhf_load = 0
						target_state.current_time = (state.uhf)[state.i_3]
						target_state.uhf_check = False
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.i_3 = (state.i_3 + 1)
				elif transition == 1:
					if branch == 0:
						target_state.i_3 = 0
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.uhf_load = 414
						target_state.current_time = ((state.uhf)[state.i_3] - 1200)
		elif assignment_index == 2:
			location = state.UHF_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.UHF_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.UHF_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.UHF_location = 7

# Automaton: LinearBattery
class LinearBatteryAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [7, 2, 1, 7]
		self.transition_labels = [[4, 5, 1, 2, 3, 6, 7], [8, 7], [7], [4, 5, 1, 2, 3, 6, 7]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1], [1, 1], [1], [1, 1, 1, 1, 1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.LinearBattery_location = 0
		state.last_time = 0
		state.last_load = 2989
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.LinearBattery_location
		if location == 2:
			if transient_variable == "done":
				return True
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.LinearBattery_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.LinearBattery_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.LinearBattery_location
		if location == 2:
			return True
		elif location == 0:
			if transition >= 0 and transition < 5:
				return True
			elif transition == 5:
				return (state.gc == 54000)
			elif transition == 6:
				return (state.charge >= 67392000)
			else:
				raise IndexError
		elif location == 1:
			return True
		elif location == 3:
			if transition >= 0 and transition < 5:
				return True
			elif transition == 5:
				return (state.gc == 54000)
			elif transition == 6:
				return (state.charge >= 67392000)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.LinearBattery_location
		if location == 2:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 3:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.LinearBattery_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.LinearBattery_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
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
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.LinearBattery_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 1:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 2:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 3:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 4:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 5:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (54000 - state.last_time)))))
						target_state.last_time = -1800
						target_state.last_load = -2711
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 1:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 2:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 3:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 4:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (state.current_time - state.last_time)))))
						target_state.last_load = (((((2989 - state.sun_load) + state.uhf_load) + state.lband2_load) + state.lband3_load) + state.xband_load)
						target_state.last_time = state.current_time
				elif transition == 5:
					if branch == 0:
						target_state.charge = max(0, min(149760000, (state.charge - (state.last_load * (54000 - state.last_time)))))
						target_state.last_time = -1800
						target_state.last_load = -2711
		elif assignment_index == 1:
			location = state.LinearBattery_location
			if location == 2:
				if transition == 0:
					if branch == 0:
						target_transient.done = True
		elif assignment_index == 2:
			location = state.LinearBattery_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 5:
					if branch == 0:
						target_state.LinearBattery_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.LinearBattery_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.LinearBattery_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.LinearBattery_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.LinearBattery_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.LinearBattery_location = 3
				elif transition == 5:
					if branch == 0:
						target_state.LinearBattery_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.LinearBattery_location = 3

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[7, 8]]
		self.branch_counts = [[1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			return True
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = 0
		if location == 0:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.gc = min((state.gc + 1), 54601)
		elif assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_transient.prop3_edge_reward = transient.cost

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Lband2", "_aut_Lband3", "_aut_Xband", "_aut_Sun", "_aut_UHF", "_aut_LinearBattery", "_aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.model_type = "lts"
		self.transition_labels = { 0: "τ", 1: "lband2_update", 2: "lband3_update", 3: "xband_update", 4: "sun_update", 5: "uhf_update", 6: "finished", 7: "tick", 8: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, -1, -1, 0], [-1, -1, 0, -1, -1, -1, -1, 0], [-1, -1, -1, 0, -1, -1, -1, 0], [-1, -1, -1, -1, 0, -1, -1, 0], [-1, -1, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, -1, -1, 0, 0], [-1, -1, -1, -1, -1, 6, 8, 6], [1, -1, -1, -1, -1, 1, 8, 1], [-1, 2, -1, -1, -1, 2, 8, 2], [-1, -1, 3, -1, -1, 3, 8, 3], [-1, -1, -1, 4, -1, 4, 8, 4], [-1, -1, -1, -1, 5, 5, 8, 5], [8, -1, -1, -1, -1, -1, 8, 0], [-1, 8, -1, -1, -1, -1, 8, 0], [-1, -1, 8, -1, -1, -1, 8, 0], [-1, -1, -1, 8, -1, -1, 8, 0], [-1, -1, -1, -1, 8, -1, 8, 0], [-1, -1, -1, -1, -1, 8, 8, 0], [7, 7, 7, 7, 7, 7, 7, 7]]
		self.properties = [
			Property("prop3", PropertyExpression("e_min_s", [0, PropertyExpression("ap", [1])]))
		]
		self.variables = [
			VariableInfo("lband2", None, None),
			VariableInfo("lband3", None, None),
			VariableInfo("sun", None, None),
			VariableInfo("uhf", None, None),
			VariableInfo("xband", None, None),
			VariableInfo("charge", None, "int", 0, 149760000),
			VariableInfo("R", None, "int"),
			VariableInfo("current_time", None, "int", -1800, 54600),
			VariableInfo("lock", None, "bool"),
			VariableInfo("uhf_check", None, "bool"),
			VariableInfo("lband2_check", None, "bool"),
			VariableInfo("lband3_check", None, "bool"),
			VariableInfo("xband_check", None, "bool"),
			VariableInfo("l2_count", None, "int"),
			VariableInfo("l3_count", None, "int"),
			VariableInfo("x_count", None, "int"),
			VariableInfo("sun_load", None, "int", 0, 5700),
			VariableInfo("uhf_load", None, "int", 0, 2630),
			VariableInfo("lband2_load", None, "int", 0, 3863),
			VariableInfo("lband3_load", None, "int", 0, 3863),
			VariableInfo("xband_load", None, "int", 0, 11945),
			VariableInfo("gc", None, "int", 0, 54601),
			VariableInfo("Lband2_location", 0, "int", 0, 10),
			VariableInfo("i", 0, "int"),
			VariableInfo("Lband3_location", 1, "int", 0, 10),
			VariableInfo("j", 1, "int"),
			VariableInfo("Xband_location", 2, "int", 0, 10),
			VariableInfo("i", 2, "int"),
			VariableInfo("Sun_location", 3, "int", 0, 3),
			VariableInfo("i", 3, "int"),
			VariableInfo("UHF_location", 4, "int", 0, 7),
			VariableInfo("i", 4, "int"),
			VariableInfo("LinearBattery_location", 5, "int", 0, 3),
			VariableInfo("last_time", 5, "int", -1800, 54600),
			VariableInfo("last_load", 5, "int", -2711, 25290)
		]
		self._aut_Lband2 = Lband2Automaton(self)
		self._aut_Lband3 = Lband3Automaton(self)
		self._aut_Xband = XbandAutomaton(self)
		self._aut_Sun = SunAutomaton(self)
		self._aut_UHF = UHFAutomaton(self)
		self._aut_LinearBattery = LinearBatteryAutomaton(self)
		self._aut_GlobalSync = GlobalSyncAutomaton(self)
		self.components = [self._aut_Lband2, self._aut_Lband3, self._aut_Xband, self._aut_Sun, self._aut_UHF, self._aut_LinearBattery, self._aut_GlobalSync]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.lband2 = [6172, 11742, 11914, 17484, 17750, 23320, 23776, 29346, 29859, 35429, 35769, 41339, 41549, 47119, 47276, 52846]
		state.lband3 = [3491, 9061, 9245, 14815, 15112, 20682, 21165, 26735, 27217, 32787, 33096, 38666, 38862, 44432, 44587, 50157]
		state.sun = [0, 2088, 4097, 7594, 9601, 13101, 15105, 18608, 20609, 24115, 26113, 29622, 31618, 35129, 37122, 40636, 42626, 46144, 48130, 51651, 53634, 54000]
		state.uhf = [3318, 3542, 8830, 9348, 14488, 15067, 20188, 20767, 25907, 26424, 31718, 31931]
		state.xband = [2993, 3426, 7741, 8152, 8603, 9203, 13374, 13949, 14355, 14933, 20138, 20692, 25884, 26476, 31616, 32201, 37454, 37723, 48773, 49242]
		state.charge = 89856000
		state.R = 0
		state.current_time = 0
		state.lock = False
		state.uhf_check = False
		state.lband2_check = False
		state.lband3_check = False
		state.xband_check = False
		state.l2_count = 0
		state.l3_count = 0
		state.x_count = 0
		state.sun_load = 0
		state.uhf_load = 0
		state.lband2_load = 0
		state.lband3_load = 0
		state.xband_load = 0
		state.gc = 0
		self._aut_Lband2.set_initial_values(state)
		self._aut_Lband3.set_initial_values(state)
		self._aut_Xband.set_initial_values(state)
		self._aut_Sun.set_initial_values(state)
		self._aut_UHF.set_initial_values(state)
		self._aut_LinearBattery.set_initial_values(state)
		self._aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.prop3_edge_reward = 0
		transient.done = False
		transient.cost = 0
		self._aut_Lband2.set_initial_transient_values(transient)
		self._aut_Lband3.set_initial_transient_values(transient)
		self._aut_Xband.set_initial_transient_values(transient)
		self._aut_Sun.set_initial_transient_values(transient)
		self._aut_UHF.set_initial_transient_values(transient)
		self._aut_LinearBattery.set_initial_transient_values(transient)
		self._aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return self.network._get_transient_value(state, "prop3_edge_reward")
		elif expression == 1:
			return self.network._get_transient_value(state, "done")
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return transient.prop3_edge_reward
		elif expression == 1:
			return transient.done
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Lband2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Lband3.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Xband.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Sun.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_UHF.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_LinearBattery.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Lband2 = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Lband2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Lband2.get_guard_value(state, i):
				trans_Lband2[self._aut_Lband2.get_transition_label(state, i)].append(i)
		trans_Lband3 = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Lband3.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Lband3.get_guard_value(state, i):
				trans_Lband3[self._aut_Lband3.get_transition_label(state, i)].append(i)
		trans_Xband = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Xband.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Xband.get_guard_value(state, i):
				trans_Xband[self._aut_Xband.get_transition_label(state, i)].append(i)
		trans_Sun = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Sun.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Sun.get_guard_value(state, i):
				trans_Sun[self._aut_Sun.get_transition_label(state, i)].append(i)
		trans_UHF = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_UHF.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_UHF.get_guard_value(state, i):
				trans_UHF[self._aut_UHF.get_transition_label(state, i)].append(i)
		trans_LinearBattery = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_LinearBattery.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_LinearBattery.get_guard_value(state, i):
				trans_LinearBattery[self._aut_LinearBattery.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self._aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1, -1, -1, -1]]
			# Lband2
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Lband2[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Lband2[sv[0]][0]
						for i in range(1, len(trans_Lband2[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Lband2[sv[0]][i]
			# Lband3
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Lband3[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Lband3[sv[1]][0]
						for i in range(1, len(trans_Lband3[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Lband3[sv[1]][i]
			# Xband
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Xband[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Xband[sv[2]][0]
						for i in range(1, len(trans_Xband[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Xband[sv[2]][i]
			# Sun
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Sun[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Sun[sv[3]][0]
						for i in range(1, len(trans_Sun[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Sun[sv[3]][i]
			# UHF
			if synced is not None:
				if sv[4] != -1:
					if len(trans_UHF[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_UHF[sv[4]][0]
						for i in range(1, len(trans_UHF[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_UHF[sv[4]][i]
			# LinearBattery
			if synced is not None:
				if sv[5] != -1:
					if len(trans_LinearBattery[sv[5]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][5] = trans_LinearBattery[sv[5]][0]
						for i in range(1, len(trans_LinearBattery[sv[5]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][5] = trans_LinearBattery[sv[5]][i]
			# GlobalSync
			if synced is not None:
				if sv[6] != -1:
					if len(trans_GlobalSync[sv[6]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][6] = trans_GlobalSync[sv[6]][0]
						for i in range(1, len(trans_GlobalSync[sv[6]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][6] = trans_GlobalSync[sv[6]][i]
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
		combs = [[-1, -1, -1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Lband2.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Lband2.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Lband2.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_Lband3.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Lband3.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Lband3.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Xband.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Xband.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Xband.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_Sun.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_Sun.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Sun.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self._aut_UHF.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self._aut_UHF.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self._aut_UHF.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		if transition.transitions[5] != -1:
			existing = len(combs)
			branch_count = self._aut_LinearBattery.get_branch_count(state, transition.transitions[5])
			for i in range(1, branch_count):
				probability = self._aut_LinearBattery.get_probability_value(state, transition.transitions[5], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][5] = i
					probs.append(probs[j] * probability)
			probability = self._aut_LinearBattery.get_probability_value(state, transition.transitions[5], 0)
			for i in range(existing):
				combs[i][5] = 0
				probs[i] *= probability
		if transition.transitions[6] != -1:
			existing = len(combs)
			branch_count = self._aut_GlobalSync.get_branch_count(state, transition.transitions[6])
			for i in range(1, branch_count):
				probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[6], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][6] = i
					probs.append(probs[j] * probability)
			probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[6], 0)
			for i in range(existing):
				combs[i][6] = 0
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
		for i in range(0, 3):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_Lband2.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Lband3.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Xband.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_Sun.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self._aut_UHF.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			if transition.transitions[5] != -1:
				self._aut_LinearBattery.jump(state, transient, transition.transitions[5], branch.branches[5], i, target_state, target_transient)
			if transition.transitions[6] != -1:
				self._aut_GlobalSync.jump(state, transient, transition.transitions[6], branch.branches[6], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
