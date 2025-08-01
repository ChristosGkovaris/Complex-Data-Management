# Author: Gkovaris Christos-Grigorios



# Importing necessary modules
import sys
from math import floor, ceil
from pymorton import interleave_latlng



# Constants defining R-tree node capacity
MAX_ENTRIES = 20
MIN_ENTRIES = 8



# Reads coordinate points from the input file
# Each line is of the form: x,y
def read_coords(filename):
    with open(filename, 'r') as f:
        return [tuple(map(float, line.strip().split(','))) for line in f]



# Reads object offsets defining polygons from the input file
# Each line is of the form: id,startOffset,endOffset
def read_offsets(filename):
    objects = []
    
    with open(filename, 'r') as f:
        for line in f:
            obj_id, start, end = map(int, line.strip().split(','))
            objects.append((obj_id, start, end))
    
    return objects



# Computes the Minimum Bounding Rectangle (MBR) for a set of points
# MBR = [x_min, x_max, y_min, y_max]
def compute_mbr(coords):
    xs = [pt[0] for pt in coords]
    ys = [pt[1] for pt in coords]
    return [min(xs), max(xs), min(ys), max(ys)]



# Computes the center of a given MBR
def center(mbr):
    x_low, x_high, y_low, y_high = mbr
    return ((x_low + x_high) / 2, (y_low + y_high) / 2)



# Computes the union MBR from a list of MBRs
def compute_mbr_union(mbr_list):
    x_lows = [m[0] for m in mbr_list]
    x_highs = [m[1] for m in mbr_list]
    y_lows = [m[2] for m in mbr_list]
    y_highs = [m[3] for m in mbr_list]
    return [min(x_lows), max(x_highs), min(y_lows), max(y_highs)]



# Splits a list of entries into chunks of size between MIN_ENTRIES and MAX_ENTRIES
# Ensures valid R-tree node constraints for all levels
def fix_chunks(entries):
    chunks = []
    i = 0
    n = len(entries)
    
    while i < n:
        remain = n - i
        
        if remain < MIN_ENTRIES:
            if chunks:
                last_chunk = chunks.pop()
                combined = last_chunk + entries[i:]
                
                if len(combined) <= MAX_ENTRIES:
                    chunks.append(combined)
                
                else:
                    chunks.append(combined[:-MIN_ENTRIES])
                    chunks.append(combined[-MIN_ENTRIES:])
            
            else:
                chunks.append(entries[i:])
            
            break
        
        elif remain > MAX_ENTRIES and remain - MAX_ENTRIES < MIN_ENTRIES:
            needed = MAX_ENTRIES - (MIN_ENTRIES - (remain - MAX_ENTRIES))
            chunks.append(entries[i:i + needed])
            i += needed
        
        else:
            chunks.append(entries[i:i + MAX_ENTRIES])
            i += MAX_ENTRIES
    
    return chunks



# Builds a level of the R-tree from a given list of entries
# If is_leaf=1 the entries are internal nodes, otherwise leaf-level objects
def build_level(entries, is_leaf, node_id_counter):
    nodes = []
    chunks = fix_chunks(entries)
    
    for chunk in chunks:
        node_id = next(node_id_counter)
        mbr = compute_mbr_union([entry[1] for entry in chunk])
        formatted_chunk = [(entry[0], entry[1]) for entry in chunk]
        nodes.append((is_leaf, node_id, formatted_chunk, mbr))
    
    return nodes



# Main execution of R-tree construction using bulk loading
# Takes two input files: coordinates and offsets
# Writes the constructed tree into Rtree.txt in the specified format
# MAIN function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rtree_builder.py coords.txt offsets.txt")
        sys.exit()

    coords_file, offsets_file = sys.argv[1], sys.argv[2]
    coords = read_coords(coords_file)
    offsets = read_offsets(offsets_file)

    # Extract and compute MBRs with z-order values
    objects = []
    
    for obj_id, start, end in offsets:
        points = coords[start:end+1]
        mbr = compute_mbr(points)
        cx, cy = center(mbr)
        zvalue = interleave_latlng(cy, cx)
        objects.append((obj_id, mbr, zvalue))

    # Sort objects by z-order value
    objects.sort(key=lambda x: x[2])

    # Unique node IDs
    node_id_counter = iter(range(1000000))

    # Build the leaf level
    leaf_level = build_level([(obj[0], obj[1]) for obj in objects], 0, node_id_counter)
    levels = [[[node[0], node[1], node[2]] for node in leaf_level]]
    current_level = [(node[1], node[3]) for node in leaf_level]

    # Iteratively build the upper levels
    while len(current_level) > 1:
        upper_level = build_level(current_level, 1, node_id_counter)
        levels.append([[node[0], node[1], node[2]] for node in upper_level])
        current_level = [(node[1], node[3]) for node in upper_level]

    # Output the number of nodes at each level
    for i, level in enumerate(levels):
        print(f"{len(level)} nodes at level {i}")

    # Write the R-tree structure to output file using JSON format for proper list brackets
    import json
    with open("Rtree.txt", 'w') as out:
        for level in levels:
            for node in level:
                out.write(json.dumps(node) + "\n")