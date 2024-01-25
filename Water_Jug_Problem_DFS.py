# User input
jug1_capacity = int(input("Enter capacity of Jug 1: "))
jug2_capacity = int(input("Enter capacity of Jug 2: "))
target_amount = int(input("Enter target amount of water: "))

# Main Algo
def DFS(a, b, target):
    # Stack for DFS, each element is a tuple (state, path)
    stack = [((0, 0), [])]
    visited = set()

    while stack:
        (jug1, jug2), path = stack.pop()

        # Skip if visited
        if (jug1, jug2) in visited:
            continue

        # Check for invalid states
        if jug1 > a or jug2 > b or jug1 < 0 or jug2 < 0:
            continue

        # Mark the current state as visited and store the path
        visited.add((jug1, jug2))
        current_path = path + [(jug1, jug2)]

        # Check for the goal state
        if jug1 == target or jug2 == target:
            # Adjust the final state to ensure the other jug is empty if needed
            if jug1 == target and jug2 != 0:
                current_path.append((jug1, 0))
            elif jug2 == target and jug1 != 0:
                current_path.append((0, jug2))
            return current_path

        # Transitions - fill, empty, and pour
        stack.append(((a, jug2), current_path))  # Fill Jug1
        stack.append(((jug1, b), current_path))  # Fill Jug2
        stack.append(((0, jug2), current_path))  # Empty Jug1
        stack.append(((jug1, 0), current_path))  # Empty Jug2

        # Pour from Jug2 to Jug1
        pour_amount = min(jug2, a - jug1)
        stack.append(((jug1 + pour_amount, jug2 - pour_amount), current_path))

        # Pour from Jug1 to Jug2
        pour_amount = min(jug1, b - jug2)
        stack.append(((jug1 - pour_amount, jug2 + pour_amount), current_path))

    return None

path = DFS(jug1_capacity, jug2_capacity, target_amount)

if path:
    print("Path from initial state to goal state:")
    print("Jug-1|Jug-2")
    for state in path:
        print(f"( {state[0]} ,  {state[1]} )")
else:
    print("No solution found.")


