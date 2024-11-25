from cell import Cell
from state import State
import numpy as np
from queue import Queue
from game_logic import *
import heapq
from itertools import count


def BFS(init_state):
    print("\nBFS Started...")
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

    return [init_state], len(visited_states)


