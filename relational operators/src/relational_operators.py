# Author: Gkovaris Christos-Grigorios


# Importing sys for MAIN function
import sys


# Merge and Join
def merge_join(r_file, s_file, output_file):
    # Open the input and output files
    with open(r_file, 'r') as r_f, open(s_file, 'r') as s_f, open(output_file, 'w') as out_f:
        # Read the first line from each input file
        r_line = r_f.readline().strip()
        s_line = s_f.readline().strip()

        # Stores matching values from s_file for a given key
        buffer = []  

        # Tracks the largest buffer size encountered
        max_buffer_size = 0

        # Keeps track of the previous key from r_file  
        prev_r_key = None  

        # Iterate over each line in r_file
        while r_line:  
            r_parts = r_line.split('\t')
            
            # Skip malformed lines
            if len(r_parts) < 2:  
                r_line = r_f.readline().strip()
                continue
            
            # Extract key-value pair
            r_key, r_value = r_parts[0], int(r_parts[1])
            
            # If the r_key has changed or the buffer is empty
            if r_key != prev_r_key or not buffer:
                # Clear the buffer to store new matching values from s_file
                buffer.clear()

                # Iterate over s_file to find matching keys
                while s_line:  
                    s_parts = s_line.split('\t')

                    # Skip malformed lines
                    if len(s_parts) < 2:  
                        s_line = s_f.readline().strip()
                        continue

                    # Extract key-value pair
                    s_key, s_value = s_parts[0], int(s_parts[1])  
                    
                    # Move forward in s_file if the key is smaller
                    if s_key < r_key:  
                        s_line = s_f.readline().strip()
                    
                    # Store matching values in buff er
                    elif s_key == r_key:  
                        buffer.append(s_value)
                        s_line = s_f.readline().strip()
                    
                    # Stop searching once s_key exceeds r_key
                    else:  
                        break

                # Update max buffer size
                max_buffer_size = max(max_buffer_size, len(buffer))  
            
            # Write all matches to the output file
            for s_val in buffer:  
                out_f.write(f"{r_key}\t{r_value}\t{s_val}\n")
            
            # Update previous key reference
            prev_r_key = r_key  

            # Read the next line from r_file
            r_line = r_f.readline().strip()  
            
    # Return the maximum buffer size encountered
    return max_buffer_size



# Union
def union(r_file, s_file, output_file):
    # Open the input and output files
    with open(r_file, 'r') as r, open(s_file, 'r') as s, open(output_file, 'w') as output:
        # Read the first line from each input file
        r_line = r.readline().strip()
        s_line = s.readline().strip()
        
        # Keeps track of the last written line to avoid duplicates
        previous_line = None
        
        # Iterate over both files until both are fully processed
        while r_line or s_line:
            # If r_file is exhausted, take from s_file
            if not r_line:
                current_line = s_line
                s_line = s.readline().strip()
            
            # If s_file is exhausted, take from r_file
            elif not s_line:
                current_line = r_line
                r_line = r.readline().strip()
            
            else:
                # Select the smaller line lexicographically to maintain sorted order
                if r_line < s_line:
                    current_line = r_line
                    r_line = r.readline().strip()
                
                # If s_line is smaller, use it instead
                elif s_line < r_line:
                    current_line = s_line
                    s_line = s.readline().strip()
                
                # If both lines are equal, write only once and advance both files
                else:
                    current_line = r_line
                    r_line = r.readline().strip()
                    s_line = s.readline().strip()
            
            # Write the line only if it hasn't been written before (to remove duplicates)
            if current_line != previous_line:
                output.write(f"{current_line}\n")
                previous_line = current_line



# Intersection
def intersection(r_file, s_file, output_file):
    # Open the input and output files
    with open(r_file, 'r') as r, open(s_file, 'r') as s, open(output_file, 'w') as output:
        # Read the first line from each input file
        r_line = r.readline().strip()
        s_line = s.readline().strip()
        
        # Keeps track of the last written line to avoid duplicates
        previous_line = None
        
        # Iterate through both files until one of them is fully read
        while r_line and s_line:
            # If the current lines match, write to the output file (if not a duplicate)
            if r_line == s_line:
                # Avoid writing duplicates
                if r_line != previous_line:
                    output.write(f"{r_line}\n")
                
                # Update the last written line
                previous_line = r_line

                # Move forward in both files
                r_line = r.readline().strip()
                s_line = s.readline().strip()

            # If r_line is smaller, move forward in r_file
            elif r_line < s_line:
                r_line = r.readline().strip()

            # If s_line is smaller, move forward in s_file
            else:
                s_line = s.readline().strip()



# Difference
def set_difference(r_file, s_file, output_file):
    # Open the input and output files
    with open(r_file, 'r') as r, open(s_file, 'r') as s, open(output_file, 'w') as output:
        # Read the first line from each input file
        r_line = r.readline().strip()
        s_line = s.readline().strip()
        
        # Keeps track of the last written line to avoid duplicates
        previous_line = None

        # Iterate through r_file until it is fully read
        while r_line:
            # If s_file is exhausted or r_line is smaller, write r_line to output
            if not s_line or r_line < s_line:
                
                # Avoid writing duplicates
                if r_line != previous_line:
                    output.write(f"{r_line}\n")
                
                # Update the last written line
                previous_line = r_line

                # Move forward in r_file
                r_line = r.readline().strip()

            # If r_line and s_line are equal, skip this value in both files (remove common elements)
            elif r_line == s_line:
                # Update previous line reference
                previous_line = r_line
                r_line = r.readline().strip()
                s_line = s.readline().strip()

            # If s_line is smaller, move forward in s_file
            else:
                s_line = s.readline().strip()



# Group By (Sort-Merge Algorithm)
def group_and_sum(input_file, output_file):
    # Read all data into a list
    data = []
    
    with open(input_file, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            
            if len(parts) == 2:
                key, value = parts[0], int(parts[1])
                
                # Store as tuple (key, value)
                data.append((key, value))  
    
    # Sort the list based on the first field (key)
    data.sort()

    # Merge and sum duplicates
    with open(output_file, 'w') as f:
        if not data:
            # If data is empty, do nothing
            return  

        # Initialize first key-value pair
        prev_key, sum_value = data[0]

        for i in range(1, len(data)):
            current_key, current_value = data[i]
            
            if current_key == prev_key:
                # Aggregate sum
                sum_value += current_value  
            
            else:
                # Write previous group
                f.write(f"{prev_key}\t{sum_value}\n")  

                # Reset values for the next group
                prev_key, sum_value = current_key, current_value  
        
        # Write the last group
        f.write(f"{prev_key}\t{sum_value}\n")



# MAIN function
if __name__ == "__main__":
    # Get command-line arguments (excluding script name)
    files = sys.argv[1:]

    # If two files are provided, perform join, union, intersection, and difference operations
    if len(files) == 2:
        merge_join(files[0], files[1], "join.tsv")             # Compute merge join
        union(files[0], files[1], "union.tsv")                 # Compute merge-based union
        intersection(files[0], files[1], "intersection.tsv")   # Compute intersection
        set_difference(files[0], files[1], "difference.tsv")   # Compute difference (R - S)
    
    # If only one file is provided, perform the group-by operation
    elif len(files) == 1:
        # Compute group by with sum aggregation
        group_and_sum(files[0], "groupby.tsv")  
    
    # If incorrect arguments are provided, display usage instructions
    else:
        print("Use: python assignment.py <R_file> <S_file> (part 1 to 4) or python assignment.py <R_file> (part 5)")