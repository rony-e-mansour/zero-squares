from queue import Queue
from game_logic import *
import heapq
from itertools import count


# =========== BFS ===========
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


# =========== DFS ===========
def DFS(init_state):
    print("\nDFS Started...")
    stack = []
    path = []
    visited_states = set()
    stack.append(init_state)
    visited_states.add(init_state)

    while stack:
        current_state = stack.pop()

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
                stack.append(state)
                visited_states.add(state)

    return [init_state], len(visited_states)


# =========== UCS ===========
def UCS(init_state):
    print("\nUCS Started...")
    priority_queue = []
    path = []
    counter = count()
    visited_states = set()
    heapq.heappush(priority_queue, (0, next(counter), init_state))

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

    return [init_state], len(visited_states)


# =========== DFS WIth Recursion ===========
def DFS_Rec(init_state):
    print("\nDFS Using Recursion Started...")

    def recursive_DFS(current_state, path, visited_states):
        if current_state.status:
            path.append(current_state)
            while current_state.previous is not None:
                current_state = current_state.previous
                path.append(current_state)
            path.reverse()
            return path, len(visited_states)

        next_states = find_next_states(current_state)
        for state in next_states:
            if state not in visited_states:
                visited_states.add(state)
                result = recursive_DFS(state, path, visited_states)
                if result:
                    return result

        return None

    return recursive_DFS(init_state, [], set())


# =========== UCS ===========
def A_star(init_state):
    print("\nUCS Started...")
    priority_queue = []
    path = []
    counter = count()
    visited_states = set()
    heapq.heappush(priority_queue, (0, next(counter), init_state))

    while priority_queue:
        cumulative_cost, _, current_state = heapq.heappop(priority_queue)

        if current_state.status:
            path.append(current_state)
            while current_state.previous is not None:
                current_state = current_state.previous
                path.append(current_state)
            path.reverse()
            print(f' ==> [len(visited_states)] = {len(visited_states)}')
            return path, len(visited_states)

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        next_states = find_next_states(current_state)

        if next_states:
            for next_state in next_states:
                # cost = cumulative_cost + next_state.calcCost()
                next_state.cost = calculate_heuristic(grid=next_state.grid)
                heapq.heappush(priority_queue, (next_state.cost, next(counter), next_state))

    return [init_state], len(visited_states)
