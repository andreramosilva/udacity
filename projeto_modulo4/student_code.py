from math import sqrt
from queue import PriorityQueue


def shortest_path(M, start, goal):
    
    frontier_queue = PriorityQueue()
        
    prev_link = {start: None}
    
    G = {start: 0}
    
    H = {}
    for node, coord in M.intersections.items():
        H[node] = calc_dist(M, node, goal)
        
    frontier_queue.put(start, H[start])
    
    while not frontier_queue.empty():
        
        current_node = frontier_queue.get()
        
        if current_node == goal:
            reconstruct_path(prev_link, start, goal)
        
 
        for neighbor in M.roads[current_node]:
            
            g_tentative = G[current_node] + calc_dist(M, current_node, neighbor)

            if neighbor not in G or g_tentative < G[neighbor]:
                G[neighbor] = g_tentative

                f = g_tentative + H[neighbor]

                frontier_queue.put(neighbor, f)
                
                prev_link[neighbor] = current_node

                
    return reconstruct_path(prev_link, start, goal) 
 


def calc_dist(M, node1, node2):
    
    x1, y1 = tuple(M.intersections[node1])
    x2, y2 = tuple(M.intersections[node2])
    
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def reconstruct_path(prev_link, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev_link.get(curr, None)
        if curr == None:
            print("No path between start and goal")
            return None
        path.append(curr)
        
    path.reverse()
    return path