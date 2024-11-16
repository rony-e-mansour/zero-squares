from cell import Cell
from state import State
import numpy as np
from queue import Queue
from game_logic import *


def BFS(init_state):
    q = Queue()
    path = []
    visited_states = set()
    q.put(init_state)
    visited_states.add(init_state)

    while not q.empty():
        current_state = q.get()

        if current_state.status:
            path.append(current_state)
            while current_state.previous is not None:
                current_state = current_state.previous
                path.append(current_state)
            path.reverse()
            return path, len(visited_states)

        next_states = find_next_states(current_state)
        current_state.next_states = next_states

        for state in current_state.next_states:
            if state not in visited_states:
                q.put(state)
                visited_states.add(state)
            else:
                print('visited!')
                
    return [init_state], len(visited_states)


def DFS(init_state):
    stack = []  # Stack for DFS
    path = []  # Path to the goal state
    visited_states = set()  # Set to keep track of visited states
    stack.append(init_state)
    visited_states.add(init_state)

    while stack:
        current_state = stack.pop()

        # Check if the current state is the goal
        if current_state.status:
            path.append(current_state)
            while current_state.previous is not None:
                current_state = current_state.previous
                path.append(current_state)
            path.reverse()
            return path, len(visited_states)

        # Generate the next states
        next_states = find_next_states(current_state)
        current_state.next_states = next_states

        for state in current_state.next_states:
            if state not in visited_states:
                stack.append(state)
                visited_states.add(state)
            else:
                print("visited!")

    return [init_state], len(visited_states)


