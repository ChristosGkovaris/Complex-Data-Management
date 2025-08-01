# COMPLEX DATA MANAGEMENT

This repository contains **three projects** developed as part of the **MΥΕ041 - ΠΛΕ081: Διαχείριση Σύνθετων Δεδομένων** course at the **University of Ioannina**. Each project focuses
on a different **aspect of data management**, covering relational algebra, spatial indexing, and transactional query processing.

---

## RELATIONAL OPERATORS

**Goal:** Implement core **relational algebra operators** in Python using **merge-based algorithms**.

**Implemented Operators:**
- Merge-Join
- Union
- Intersection
- Set Difference
- Group-By with Sum

**Key Features:**
- Streaming, one-pass merge algorithms for set operations
- In-memory group-by with duplicate elimination
- Outputs stored as TSV files

**Folder:** `relational-operators/`  
**Main Script:** `src/relational_operators.py`

---

## SPACIAL DATA

**Goal:** Build an **R-Tree index** using **bulk loading** and support **spatial queries**.

**Implemented Queries:**
- Range Query (window queries)
- k-Nearest Neighbor (kNN) Query

**Key Features:**
- Bulk loading with Z-order (Morton) codes
- Node capacity constraints (max 20, min 8)
- Efficient tree traversal with pruning
- Generates `Rtree.txt` and query results

**Folder:** `spatial-rtree/`  
**Main Scripts:**  
- `src/rtree_builder.py` (build tree)  
- `src/range_query.py` (range queries)  
- `src/knn_query.py` (kNN queries)

---

## TOTAL DATA MANAGEMENT

**Goal:** Process **containment and relevance queries** on transactional datasets  
using various **indexing methods**.

**Containment Queries:**
- Naive scan
- Signature File
- Bitslice Signature File
- Inverted File

**Relevance Queries:**
- Naive TF×IDF ranking
- Inverted Index ranking

**Key Features:**
- Signature-based filtering for fast containment queries
- Inverted file structures for both set and ranking queries
- Generates `sigfile.txt`, `invfile.txt`, `invfileocc.txt`

**Folder:** `transaction-queries/`  
**Main Scripts:**  
- `src/containment_queries.py`  
- `src/relevance_queries.py`

---

## LICENSE

All projects are licensed under the **MIT License**.  
See the respective `LICENSE` files for details.

---

## AUTHOR

**Christos Gkovaris**  
University of Ioannina – Computer Science and Engineering
[GitHub](https://github.com/ChristosGkovaris)
University of Ioannina – Computer Engineering & Informatics  
[GitHub](https://github.com/ChristosGkovaris)
