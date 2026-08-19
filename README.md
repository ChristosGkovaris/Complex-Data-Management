# COMPLEX DATA MANAGEMENT

This repository contains three **Python projects** covering relational query processing, spatial indexing, and transactional set-data retrieval. The projects were developed as part of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

---

## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Architecture](#architecture)
5. [Project Structure](#project-structure)
6. [Algorithms Implemented](#algorithms-implemented)
7. [Installation](#installation)
8. [Usage](#usage)
9. [Contributors](#contributors)
10. [License](#license)
11. [Contact](#contact)

---

## OVERVIEW

The repository consists of three independent assignments focused on the implementation of data-management algorithms and indexing structures.

The projects cover:

- Relational algebra operators using streaming and merge-based processing
- Spatial indexing with R-Trees, Minimum Bounding Rectangles, and Z-order bulk loading
- Range and k-nearest-neighbor spatial queries
- Transaction containment queries using bitmap and inverted indexes
- Relevance queries using occurrence-based scoring and inverted indexes

Each assignment is implemented independently and includes its own source code and documentation.

---

## TECH STACK

- **Language:** Python
- **Data Processing:** File-based datasets, in-memory data structures
- **Spatial Indexing:** R-Tree, Minimum Bounding Rectangles, Z-order
- **Query Processing:** Merge-based operators, containment queries, relevance ranking
- **Indexing:** Signature files, bitslice signatures, inverted indexes
- **Python Libraries:** Standard Library, `pymorton`

---

## FEATURES

- **Relational Data Processing**
  - Merge-Join
  - Union
  - Intersection
  - Set Difference
  - Group-By with Sum aggregation

- **Spatial Data Processing**
  - R-Tree construction through bulk loading
  - Minimum Bounding Rectangle computation
  - Z-order spatial sorting
  - Range queries
  - k-nearest-neighbor queries

- **Transactional Data Processing**
  - Containment queries
  - Exact signature files
  - Bitslice signature files
  - Inverted indexes
  - Relevance-based transaction ranking

---

## ARCHITECTURE

The repository is organized as three independent command-line projects.

Each assignment separates a specific data-management problem from the others:

- **Assignment 1** processes relational data using sequential file access and merge-based algorithms.
- **Assignment 2** constructs a persistent R-Tree representation and uses it for spatial query processing.
- **Assignment 3** builds alternative indexing structures over transactional data and evaluates containment and relevance queries.

The implementations use explicit data structures and algorithms rather than database-management frameworks.

---

## PROJECT STRUCTURE

```text
.
├── assignment-1-relational-operators/
│   ├── relational_operators.py
│   └── README.md
│
├── assignment-2-spatial-data/
│   ├── rtree_builder.py
│   ├── range_query.py
│   ├── knn_query.py
│   └── README.md
│
├── assignment-3-set-data/
│   ├── containment_queries.py
│   ├── relevance_queries.py
│   └── README.md
│
└── README.md
```

---

## ALGORITHMS IMPLEMENTED

### Relational Operators

- Merge-Join with buffered matching tuples
- Merge-based Union
- Merge-based Intersection
- Merge-based Set Difference
- Sort-based Group-By with Sum aggregation

### Spatial Data

- Minimum Bounding Rectangle computation
- Z-order spatial ordering
- Bottom-up R-Tree bulk loading
- Recursive R-Tree range search
- Best-first incremental kNN search using a priority queue

### Transactional Set Data

- Naive containment search
- Exact signature file containment
- Bitslice signature containment
- Inverted-index containment
- Naive relevance ranking
- Inverted-index relevance ranking

---

## INSTALLATION

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Ensure Python is installed.

3. Install `pymorton` for the spatial-data assignment:

```bash
pip install pymorton
```

The remaining implementations use Python Standard Library modules.

---

## USAGE

Each assignment is executed independently from the command line.

Refer to the corresponding assignment README for:

- Required input files
- Command-line arguments
- Generated output files
- Algorithm-specific execution instructions

---

## CONTRIBUTORS

- **Christos Gkovaris** — GitHub: [ChristosGkovaris](https://github.com/ChristosGkovaris)

---

## LICENSE

No formal software license is included in the provided project files.

This repository contains academic projects developed as part of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

---

## CONTACT

**Christos Gkovaris**  
Computer Science and Engineering  
University of Ioannina  