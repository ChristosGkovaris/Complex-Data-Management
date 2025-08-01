# Author: Gkovaris Christos-Grigorios



import sys
import time
import ast



# Reads the file line by line and converts each line (e.g., '[1, 2, 3]') into a Python set
def load_data(filepath):
    with open(filepath, 'r') as file:
        return [set(ast.literal_eval(line.strip())) for line in file]



# Performs naive containment query: checks if pattern is a subset of each transaction
def naive_search(data, pattern):
    matches = set()
    
    for idx in range(len(data)):
        if pattern <= data[idx]:
            matches.add(idx)
    
    return matches



# Creates a signature (bitmap) for each transaction using bitwise OR on shifted values
def make_signature_index(data):
    index = []
    
    for entry in data:
        code = sum((1 << item) for item in entry)
        index.append(code)
    
    # Saves the signature index to a file
    with open("sigfile.txt", "w") as output:
        output.write("\n".join(str(num) for num in index))
    
    return index



def search_signature(index, pattern):
    # Converts pattern to bitmap and checks if it is contained in each transaction's signature
    query_mask = sum((1 << val) for val in pattern)
    return {i for i, sig in enumerate(index) if (sig & query_mask) == query_mask}



# Creates a bitslice index: each item maps to a bitmap indicating presence across transactions
def make_bitslice_index(data):
    index = dict()
    
    for i in range(len(data)):
        for token in data[i]:
            index[token] = index.get(token, 0) | (1 << i)
    
    # Saves the bitslice index to a file
    with open("bitslice.txt", "w") as output:
        for token in sorted(index):
            output.write(f"{token}: {index[token]}\n")
    
    return index



# Starts with a bitmap with all bits set (assuming all transactions match)
def search_bitslice(index, pattern, total):
    bitmap = (1 << total) - 1
    
    # ANDs the bitmaps of all pattern items to find common transactions
    for item in pattern:
        if item not in index:
            return set()
        
        bitmap &= index[item]
    
    # Returns transaction IDs (indices) for which the resulting bit is still set
    return {i for i in range(total) if bitmap & (1 << i)}



# Builds inverted index: each item maps to list of transaction IDs where it appears
def make_inverted_index(data):
    inverted = dict()
    
    for i in range(len(data)):
        for val in data[i]:
            inverted.setdefault(val, []).append(i)
    
    # Saves the inverted index to a file
    with open("invfile.txt", "w") as output:
        for key in sorted(inverted):
            output.write(f"{key}: {sorted(inverted[key])}\n")
    
    return inverted



# Computes the intersection of multiple lists (as sets)
def intersect_sorted(lists):
    if not lists:
        return set()
    
    result = set(lists[0])
    
    for lst in lists[1:]:
        result &= set(lst)
    
    return result



# Retrieves the posting list for each item in the pattern
def search_inverted(index, pattern):
    involved = []
    for token in pattern:
        if token not in index:
            return set()
        
        involved.append(index[token])
    
    # Returns intersection of posting lists
    return intersect_sorted(involved)



# Label and function mapping for method IDs
def dispatch(method_id, trans, queries, query_idx):
    label = ["Naive", "Signature", "Bitslice", "Inverted"]
    method = [naive_search, search_signature, search_bitslice, search_inverted]
    builder = [None, make_signature_index, make_bitslice_index, make_inverted_index]

    obj = None
    
    if method_id > 0:
        # Preprocess structure if needed
        obj = builder[method_id](trans)

    # Internal execution function for a single query
    def execute(q):
        if method_id == 0:
            return method[method_id](trans, q)
        
        elif method_id == 2:
            return method[method_id](obj, q, len(trans))
        
        else:
            return method[method_id](obj, q)

    start = time.time()
    
    # Execute for all queries or a specific one
    if query_idx == -1:
        for q in queries:
            execute(q)
    
    else:
        result = execute(queries[query_idx])
        print(f"{label[method_id]} Method result:")
        print(result)
    
    end = time.time()
    print(f"{label[method_id]} Method computation time = {end - start:.4f} seconds")



if __name__ == "__main__":
    # Expects exactly 4 command-line arguments
    if len(sys.argv) != 5:
        print("Usage: python containment_queries.py <transactions_file> <queries_file> <query_id> <method>")
        sys.exit(1)

    # Parse command-line arguments
    transactions_file = sys.argv[1]
    queries_file = sys.argv[2]
    query_id = int(sys.argv[3])
    method_id = int(sys.argv[4])

    # Load data
    transactions = load_data(transactions_file)
    queries = load_data(queries_file)

    # Execute requested method(s)
    if method_id == -1:
        for m in range(4):
            dispatch(m, transactions, queries, query_id)
    
    else:
        dispatch(method_id, transactions, queries, query_id)