# implementing bidirectional search algorithm
from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start] 

    # Initialize the frontiers for both searches
    frontier_start = deque([start]) # Initialize start frontier
    frontier_goal = deque([goal]) # Initialize goal frontier

    # Initialize the explored sets for both searches
    explored_start = {start: None} # Keep track of parent nodes
    explored_goal = {goal: None} # Keep track of parent nodes

    while frontier_start and frontier_goal:
        # Expand from the start side
        if frontier_start: # Check if there are nodes to expand
            current_start = frontier_start.popleft() # Get the next node to expand
            for neighbor in graph[current_start]: # Explore neighbors
                if neighbor not in explored_start: # Check if neighbor has already been expanded
                    explored_start[neighbor] = current_start # Mark neighbor as explored
                    frontier_start.append(neighbor) # Add neighbor to frontier
                    if neighbor in explored_goal: # Check for intersection
                        return construct_path(explored_start, explored_goal, neighbor) # Construct path
 
        # Expand from the goal side
        if frontier_goal: # Check if there are nodes to expand
            current_goal = frontier_goal.popleft() # Get the next node to expand
            for neighbor in graph[current_goal]: # Explore neighbors
                if neighbor not in explored_goal: # Check if neighbor has already been expanded
                    explored_goal[neighbor] = current_goal # Mark neighbor as explored
                    frontier_goal.append(neighbor) # Add neighbor to frontier
                    if neighbor in explored_start: # Check for intersection
                        return construct_path(explored_start, explored_goal, neighbor) # Construct path

    return None  # No path found
def construct_path(explored_start, explored_goal, meeting_point): 
    # Construct path from start to meeting point
    path_start = [] # Initialize path list
    node = meeting_point # Start from the meeting point
    while node is not None: # Traverse the path back to the start
        path_start.append(node) # Add node to path
        node = explored_start[node] # Move to the parent node
    path_start.reverse() # Reverse the path to get correct order

    # Construct path from meeting point to goal
    path_goal = [] # Initialize path list
    node = explored_goal[meeting_point] # Start from the meeting point
    while node is not None:    # Traverse the path back to the goal
        path_goal.append(node) # Add node to path
        node = explored_goal[node] # Move to the parent node

    return path_start + path_goal # Combine both paths
# Example usage
if __name__ == "__main__": # Check if the script is being run as the main program
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start = 'A'
    goal = 'F'
    path = bidirectional_search(graph, start, goal)
    print(f"Path from {start} to {goal}: {path}")