# TOTAL DATA MANAGEMENT

This project implements **transactional set queries** for datasets consisting of multiple customer transactions. It covers **containment queries** (sets) and **relevance queries** (ranked results with bag semantics), using multiple indexing methods for efficiency. It was developed as part of the **MΥΕ041 - ΠΛΕ081: Διαχείριση Σύνθετων Δεδομένων** course at the **University of Ioannina**.

---

## TABLE OF CONTENTS
1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Input Data](#input-data)
5. [Algorithms Implemented](#algorithms-implemented)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Output Files](#output-files)
9. [Testing](#testing)
10. [License](#license)
11. [Contact](#contact)

---

## OVERVIEW

We are given a **transactional dataset** (`transactions.txt`),  
where each line is a **transaction** (a set or bag of items).  

The project implements two main types of queries:

1. **Containment Queries** – Find all transactions containing all items of a query set.  
2. **Relevance Queries** – Rank transactions by their relevance to a query using IDF-weighted scoring.

Indexing techniques are used to accelerate query processing, including **signature files**, **bitslice signatures**, and **inverted files**.

---

## FEATURES

- **Containment Queries**
  - Naive full scan
  - Signature File
  - Bitslice Signature File
  - Inverted File
- **Relevance Queries**
  - Naive ranking with TF × IDF
  - Inverted File with occurrence counts
- **Output files** for signatures and indexes
- **Efficient filtering and ranking** using precomputed structures

---

## PROJECT STRUCTURE

```
transaction-queries/
│── README.md
│
├── src/
│   ├── containment_queries.py        # Implements containment queries (4 methods)
│   └── relevance_queries.py          # Implements relevance queries (2 methods)
│
├── data/
│   ├── transactions.txt              # Input transactional dataset
│   ├── queries.txt                   # Query sets for containment/relevance
|
├── output/
│   ├── sigfile.txt                   # Signature file
│   ├── bitslice.txt                  # Bitslice signatures (generated)
│   ├── invfile.txt                   # Inverted file for containment queries
│   └── invfileocc.txt                # Inverted file with occurrences & IDF
|
└── docs/
    └── assignment.pdf                # Assignment description
```

---

## INPUT DATA

The project uses the following input files:

- **transactions.txt** → Each line is a transaction (set or bag of items)  
- **queries.txt** → Each line is a query transaction  
- **sigfile.txt** → Signature file for containment queries (generated)  
- **bitslice.txt** → Bitslice signatures (generated, format as in assignment)  
- **invfile.txt** → Inverted file with posting lists for items  
- **invfileocc.txt** → Inverted file with occurrence counts and IDF values  

---

## ALGORITHMS IMPLEMENTED

1. **Containment Queries (`containment_queries.py`)**
   - **Naive:** Linear scan of all transactions
   - **Signature File:** Compare bit signatures for early filtering
   - **Bitslice Signature File:** Use per-item bitmaps for fast AND filtering
   - **Inverted File:** Use posting lists to intersect relevant transactions

2. **Relevance Queries (`relevance_queries.py`)**
   - **Naive Ranking:** Compute similarity using TF × IDF
   - **Inverted Index Ranking:** Use `invfileocc.txt` for fast scoring

---

## INSTALLATION

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/transaction-queries.git
cd transaction-queries
```

2. **Install Python (>=3.8)**  
No external libraries are required beyond the Python Standard Library.

---

## USAGE

### **1. Containment Queries**
```bash
python src/containment_queries.py data/transactions.txt data/queries.txt <query_id> <method>
```

- `query_id`: Query to execute (`0`-based), or `-1` for all queries  
- `method`:
  - `0` → Naive
  - `1` → Signature File
  - `2` → Bitslice Signature File
  - `3` → Inverted File
  - `-1` → Run all methods

**Example:**
```bash
python src/containment_queries.py data/transactions.txt data/queries.txt -1 0
```

---

### **2. Relevance Queries**
```bash
python src/relevance_queries.py data/transactions.txt data/queries.txt <query_id> <method> <k>
```

- `query_id`: Query to execute, or `-1` for all queries  
- `method`: 
  - `0` → Naive
  - `1` → Inverted Index
  - `-1` → Run both
- `k`: Number of top results to return

**Example:**
```bash
python src/relevance_queries.py data/transactions.txt data/queries.txt 0 1 10
```

---

## OUTPUT FILES

- `sigfile.txt` → Transaction signatures for containment queries  
- `bitslice.txt` → Bitslice signatures (optional, format from assignment)  
- `invfile.txt` → Inverted file for containment queries  
- `invfileocc.txt` → Inverted file with occurrence counts for relevance queries  

---

## TESTING

- **Prepare sample queries** in `queries.txt`  
- **Run all query types** and verify results match expected logic  
- **Check generated signature and inverted files** against small test cases  

---

## LICENSE

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## CONTACT

**Christos Gkovaris**  
University of Ioannina – Computer Science and Engineering
[GitHub](https://github.com/ChristosGkovaris)
