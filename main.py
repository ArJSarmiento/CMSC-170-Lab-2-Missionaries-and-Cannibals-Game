# CMSC 170 Lab Exercise 2
# Arnel Jan Sarmiento and Sean Gabriel Bayron

# Missionaries and Cannibals Game
# State is represented as (M, C, B)
# M = Number of missionaries on the left side
# C = Number of cannibals on the left side
# B = Boat position (1 if on the left, 0 if on the right)

# Initial state: (3, 3, 1)
# Goal state: (0, 0, 0)

# Function to check if a state is valid
def is_valid_state(missionaries, cannibals):
    # More cannibals than missionaries on the left or right shore is not valid
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:  # Left side
        return False
    if missionaries < 3 and (3 - missionaries) < (3 - cannibals):  # Right side
        return False
    return True

# Function to get possible next states from current state
def get_successors(state):
    successors = []
    M, C, B = state
    
    # Boat is on the left side
    if B == 1:
        # Try all valid combinations of moves (1 missionary, 1 cannibal, or 2 people)
        for m, c in [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]:
            newM = M - m
            newC = C - c
            if is_valid_state(newM, newC):
                successors.append((newM, newC, 0))
    
    # Boat is on the right side
    if B == 0:
        # Try all valid combinations of moves (1 missionary, 1 cannibal, or 2 people)
        for m, c in [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]:
            newM = M + m
            newC = C + c
            if is_valid_state(newM, newC):
                successors.append((newM, newC, 1))
    
    return successors

# Function to check if a state is the goal state
def is_goal_state(state):
    return state == (0, 0, 0)

# Breadth-first search algorithm to solve the game
def breadth_first_search():
    initial_state = (3, 3, 1)
    queue = [(initial_state, [])]
    visited = set()

    while queue:
        (state, path) = queue.pop(0)
        if state in visited:
            continue
        
        visited.add(state)
        path = path + [state]

        if is_goal_state(state):
            return path
        
        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path))
    
    return None

# Function to print the solution path
def print_solution(path):
    if path:
        for step in path:
            M, C, B = step
            print(f"Left: Missionaries = {M}, Cannibals = {C}, Boat = {'Left' if B == 1 else 'Right'}")
    else:
        print("No solution found")

if __name__ == "__main__":
    print("Missionaries and Cannibals Game")
    solution = breadth_first_search()
    print_solution(solution)

