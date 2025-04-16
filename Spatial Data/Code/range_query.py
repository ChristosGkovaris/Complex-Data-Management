# Gkovaris Christos-Grigorios
# AM: 5203


# Importing required modules
import sys
import ast


# Checks whether two MBRs intersect
# Returns True if they overlap, otherwise False
def mbr_intersects(mbr1, mbr2):
    return not (
        mbr1[1] < mbr2[0] or      # mbr1.x_high < mbr2.x_low
        mbr1[0] > mbr2[1] or      # mbr1.x_low > mbr2.x_high
        mbr1[3] < mbr2[2] or      # mbr1.y_high < mbr2.y_low
        mbr1[2] > mbr2[3]         # mbr1.y_low > mbr2.y_high
    )


# Loads an R-tree from a given file into a dictionary
# Each node is stored with its ID and entries
def load_rtree(file_path):
    rtree = {}
    
    with open(file_path, 'r') as f:
        for line in f:
            # Parses the string into a Python object
            node = ast.literal_eval(line.strip())  
            isnonleaf, node_id, entries = node
            rtree[node_id] = {"isnonleaf": isnonleaf, "entries": entries}
    
    return rtree


# Performs a range query starting from a specific node
# Recursively visits relevant nodes whose MBRs intersect the query rectangle
def range_query(node_id, query_rect, rtree, results):
    node = rtree[node_id]
    
    for entry_id, entry_mbr in node["entries"]:
        if mbr_intersects(entry_mbr, query_rect):
            if node["isnonleaf"]:
                # Recurse on child node
                range_query(entry_id, query_rect, rtree, results)  
            
            else:
                # Add object id to results
                results.append(entry_id)  


# Main function to handle input/output and invoke range query logic
def main():
    if len(sys.argv) != 3:
        print("Usage: python range_query.py Rtree.txt Rqueries.txt")
        return

    rtree_file = sys.argv[1]           # R-tree structure input file
    queries_file = sys.argv[2]         # Query rectangles input file

    rtree = load_rtree(rtree_file)     # Load R-tree
    root_id = max(rtree.keys())        # Root node is the last one created (as per construction order)

    with open(queries_file, 'r') as f:
        for i, line in enumerate(f):
            # Parse query rectangle line
            x_low, y_low, x_high, y_high = map(float, line.strip().split())
            query_rect = [x_low, x_high, y_low, y_high]
            results = []

            # Perform the actual range query
            range_query(root_id, query_rect, rtree, results)

            # Sort and display the result object IDs
            results.sort()
            print(f"{i} ({len(results)}): {','.join(map(str, results))}")


# MAIN function
if __name__ == "__main__":
    main()