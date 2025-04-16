# Gkovaris Christos-Grigorios
# AM: 5203


# Importing required modules
import sys
import ast
import heapq
import math


# Loads an R-tree from the given file
# Returns a dictionary of nodes with node_id as key and its metadata as value
def load_rtree(file_path):
    rtree = {}
    
    with open(file_path, 'r') as f:
        for line in f:
            node = ast.literal_eval(line.strip())  # Parses each node line
            isnonleaf, node_id, entries = node
            rtree[node_id] = {"isnonleaf": isnonleaf, "entries": entries}
    
    return rtree


# Computes the shortest Euclidean distance between a point and an MBR
# If the point is inside the MBR, the distance is 0
def point_mbr_distance(point, mbr):
    x, y = point
    x_low, x_high, y_low, y_high = mbr

    dx = max(x_low - x, 0, x - x_high)
    dy = max(y_low - y, 0, y - y_high)
    return math.sqrt(dx*dx + dy*dy)


# Performs best-first (incremental) kNN search using a priority queue
# Pushes both node and object MBRs into the queue, sorted by distance
def knn_search(root_id, point, k, rtree):
    heap = []

    # Start with root node at distance 0
    heapq.heappush(heap, (0, ("node", root_id)))  

    result = []
    visited = set()

    while heap and len(result) < k:
        dist, (item_type, item_id) = heapq.heappop(heap)

        if (item_type, item_id) in visited:
            continue
        visited.add((item_type, item_id))

        if item_type == "node":
            node = rtree[item_id]
            for entry_id, entry_mbr in node["entries"]:
                d = point_mbr_distance(point, entry_mbr)
                entry_type = "node" if node["isnonleaf"] else "object"

                # Add to heap
                heapq.heappush(heap, (d, (entry_type, entry_id)))  

        elif item_type == "object":
            # Add object id to result list
            result.append(item_id)  

    return result


# Main function to parse arguments and process queries
def main():
    if len(sys.argv) != 4:
        print("Usage: python knn_query.py Rtree.txt NNqueries.txt k")
        return

    rtree_file = sys.argv[1]      # Input file containing R-tree structure
    queries_file = sys.argv[2]    # Input file with query points
    k = int(sys.argv[3])          # Number of nearest neighbors to return

    rtree = load_rtree(rtree_file)

    # The root node is the one with the largest ID
    root_id = max(rtree.keys())   

    with open(queries_file, 'r') as f:
        for i, line in enumerate(f):

            # Parse query point
            x, y = map(float, line.strip().split())  
            neighbors = knn_search(root_id, (x, y), k, rtree)

            # Print kNN result
            print(f"{i}: {','.join(map(str, neighbors))}")  


# MAIN function
if __name__ == "__main__":
    main()