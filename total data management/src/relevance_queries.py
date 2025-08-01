# Author: Gkovaris Christos-Grigorios



import sys
import time
import ast
from collections import Counter, defaultdict



# Loads transactions from file, preserving duplicates (bag semantics)
def load_transactions_with_counts(path):
    with open(path, 'r') as f:
        return [list(ast.literal_eval(line.strip())) for line in f]



# Loads queries from file
def load_queries(path):
    with open(path, 'r') as f:
        return [list(ast.literal_eval(line.strip())) for line in f]



# Builds inverted index and IDF table
def create_inverted_with_idf(data):
    transaction_freq = {}
    inv = defaultdict(list)
    total = len(data)

    for tid, txn in enumerate(data):
        freq_map = Counter(txn)
        
        for itm, cnt in freq_map.items():
            inv[itm].append([tid, cnt])
            transaction_freq[itm] = transaction_freq.get(itm, 0) + 1

    idf = {itm: total / transaction_freq[itm] for itm in transaction_freq}
    
    # Save index to file
    with open("invfileocc.txt", "w") as f:
        for itm in sorted(inv):
            f.write(f"{itm}: {idf[itm]}, {inv[itm]}\n")
    
    return inv, idf



# Naive ranking: check all transactions
def simple_ranking_method(data, query, idf_table, limit=None):
    ranking = []
    
    for tid in range(len(data)):
        txn = data[tid]
        counter = Counter(txn)
        score = sum(counter[it] * idf_table[it] for it in query if it in counter and it in idf_table)
        
        if score > 0:
            ranking.append([score, tid])
    
    return sorted(ranking, reverse=True)[:limit]



# Faster ranking using inverted index
def inverted_ranking_method(inv_index, query, idf_table, limit=None):
    scores = defaultdict(float)
    
    for it in query:
        if it in inv_index and it in idf_table:
            for tid, freq in inv_index[it]:
                scores[tid] += freq * idf_table[it]
    
    return sorted([[val, tid] for tid, val in scores.items() if val > 0], reverse=True)[:limit]



# Preprocess index and IDF table
def execute(method, dataset, questions, qid, k):
    invfile, idf = create_inverted_with_idf(dataset)

    if method == 0:
        start = time.time()
        
        if qid == -1:
            for q in questions:
                _ = simple_ranking_method(dataset, q, idf, limit=k)
        
        else:
            output = simple_ranking_method(dataset, questions[qid], idf, limit=k)
            print("Naive Method result:")
            print(output)
        
        print(f"Naive Method computation time = {time.time() - start:.4f} seconds")

    elif method == 1:
        start = time.time()
        
        if qid == -1:
            for q in questions:
                _ = inverted_ranking_method(invfile, q, idf, limit=k)
        
        else:
            output = inverted_ranking_method(invfile, questions[qid], idf, limit=k)
            print("Inverted File result:")
            print(output)
        
        print(f"Inverted File computation time = {time.time() - start:.4f} seconds")



if __name__ == "__main__":
    # Command-line usage check
    if len(sys.argv) != 6:
        print("Usage: python relevance_rewritten.py <transactions_file> <queries_file> <qnum> <method> <k>")
        sys.exit(1)

    # Read arguments
    tx_file, q_file = sys.argv[1], sys.argv[2]
    qid, method, k = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])

    # Load input
    tx_data = load_transactions_with_counts(tx_file)
    q_data = load_queries(q_file)

    # Run method(s)
    if method == -1:
        execute(0, tx_data, q_data, qid, k)
        execute(1, tx_data, q_data, qid, k)
    
    else:
        execute(method, tx_data, q_data, qid, k)