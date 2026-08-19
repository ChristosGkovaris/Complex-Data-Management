# SET DATA QUERIES

This project implements **containment and relevance query processing over transactional set data in Python**, using signature files, bitslice signatures, inverted indexes, and occurrence-based relevance scoring. It was developed as **Assignment 3** of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

---

## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Architecture](#architecture)
5. [Project Structure](#project-structure)
6. [Input Data](#input-data)
7. [Algorithms Implemented](#algorithms-implemented)
8. [Installation](#installation)
9. [Usage](#usage)
10. [Contributors](#contributors)
11. [License](#license)
12. [Contact](#contact)

---

## OVERVIEW

The project evaluates two types of queries over transactional item data:

- **Containment Queries** — identify transactions containing every item of a query
- **Relevance Queries** — rank transactions according to item occurrence frequency and dataset-level item frequency

Multiple query-processing strategies are implemented to compare direct scanning with precomputed indexing structures.

Containment processing uses set semantics, while relevance processing preserves repeated item occurrences within transactions.

---

## TECH STACK

- **Language:** Python
- **Data Structures:** Sets, dictionaries, bitmaps, posting lists
- **Indexing:** Signature files, bitslice signatures, inverted indexes
- **Ranking:** Occurrence-based relevance scoring
- **Libraries:** Python Standard Library
- **Core Modules:** `sys`, `time`, `ast`, `collections`

---

## FEATURES

- **Containment Query Processing**
  - Naive transaction scanning
  - Exact signature file
  - Exact bitslice signature file
  - Inverted index

- **Relevance Query Processing**
  - Naive relevance computation
  - Inverted-index relevance computation
  - Top-`k` result selection

- **Index Generation**
  - Transaction signature file
  - Item bitslice signatures
  - Item posting lists
  - Posting lists with occurrence counts and item-frequency weights

- **Execution Measurement**
  - Measures query-processing time for each selected method
  - Supports execution of individual or complete query sets

---

## ARCHITECTURE

The project is divided into two command-line programs.

`containment_queries.py` loads transactions using set semantics and evaluates containment queries through four alternative strategies: direct scanning, exact transaction signatures, bitslice signatures, and inverted indexes.

`relevance_queries.py` preserves duplicate item occurrences and builds an inverted index containing transaction IDs and per-transaction occurrence counts. A separate item-frequency table is used by both the naive and indexed ranking methods.

Both programs support method selection through command-line arguments and measure the execution time of the selected query-processing strategy.

---

## PROJECT STRUCTURE

```text
.
├── containment_queries.py
├── relevance_queries.py
└── README.md
```

Generated index files include:

```text
sigfile.txt
bitslice.txt
invfile.txt
invfileocc.txt
```

---

## INPUT DATA

### Transactions

`transactions.txt` contains one transaction per line. Each transaction consists of item identifiers.

Transactions may contain repeated items.

### Queries

`queries.txt` contains queries using the same list-based representation as the transaction dataset.

For containment queries, transactions and queries are converted to sets.

For relevance queries, transactions remain lists so repeated item occurrences can contribute to the relevance score.

---

## ALGORITHMS IMPLEMENTED

### Naive Containment Search

Every transaction is examined directly.

A transaction is returned when the query set is a subset of the transaction:

```text
query ⊆ transaction
```

### Exact Signature File

Each transaction is represented as a bitmap in which bit `i` indicates whether item `i` occurs in the transaction.

A query is converted to the same representation and tested using bitwise operations:

```text
transaction_signature & query_signature == query_signature
```

### Bitslice Signature File

Instead of storing one bitmap per transaction, the bitslice structure stores one bitmap per item.

Bit `i` represents whether the corresponding item occurs in transaction `i`.

Containment is computed by applying bitwise AND across the bitmaps associated with all query items.

### Inverted Index Containment

Each item is mapped to the transaction IDs containing it.

For a query, the corresponding posting lists are intersected to obtain transactions containing every requested item.

### Relevance Scoring

Relevance processing preserves item multiplicity and computes a score based on occurrence frequency and transaction frequency.

For transaction `t` and query `q`, the implemented scoring model is:

```text
rel(t, q) = Σ [occ(i, t) × |T| / trf(i, T)]
```

where:

- `occ(i, t)` is the number of occurrences of item `i` in transaction `t`
- `|T|` is the total number of transactions
- `trf(i, T)` is the number of transactions containing item `i`

### Naive Relevance Ranking

Every transaction is scanned and scored against the query. Transactions with positive scores are sorted in descending score order.

### Inverted-Index Relevance Ranking

The inverted index maps each item to pairs containing:

```text
[transaction_id, occurrence_count]
```

Only transactions associated with query items are processed. Their scores are accumulated from the relevant posting lists and the highest-scoring `k` results are returned.

---

## INSTALLATION

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Ensure Python is installed.

No external Python packages are required.

---

## USAGE

Run a containment query:

```bash
python containment_queries.py <transactions_file> <queries_file> <query_id> <method>
```

Containment methods:

```text
-1  All methods
 0  Naive
 1  Exact Signature File
 2  Exact Bitslice Signature File
 3  Inverted File
```

For example:

```bash
python containment_queries.py transactions.txt queries.txt 0 -1
```

Run a relevance query:

```bash
python relevance_queries.py <transactions_file> <queries_file> <query_id> <method> <k>
```

Relevance methods:

```text
-1  Both methods
 0  Naive
 1  Inverted Index
```

For example:

```bash
python relevance_queries.py transactions.txt queries.txt 0 -1 10
```

Generated index files include:

```text
sigfile.txt
bitslice.txt
invfile.txt
invfileocc.txt
```

---

## CONTRIBUTORS

- **Christos Gkovaris** — GitHub: [ChristosGkovaris](https://github.com/ChristosGkovaris)

---

## LICENSE

No formal software license is included in the provided project files.

This project was developed as **Assignment 3** of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

---

## CONTACT

**Christos Gkovaris**  
Computer Science and Engineering  
University of Ioannina  