from cell import Cell
from state import State
from game_logic import *
import heapq
from itertools import count


def UCS(initial_state):
    print("\nUCS Started...")
    priority_queue = []
    path = []
    counter = count()
    visited_states = set()

    heapq.heappush(priority_queue, (0, next(counter), initial_state))

    while priority_queue:
        cumulative_cost, _, current_state = heapq.heappop(priority_queue)

        if current_state.status:
            path.append(current_state)
            while current_state.previous is not None:
                current_state = current_state.previous
                path.append(current_state)
            path.reverse()
            return path, len(visited_states)

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        next_states = find_next_states(current_state)

        if next_states:
            for next_state in next_states:
                cost = cumulative_cost + next_state.calcCost()
                next_state.cost = cost
                heapq.heappush(priority_queue, (cost, next(counter), next_state))

    return None
