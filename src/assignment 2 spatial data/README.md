# SPATIAL DATA

This project implements **R-Tree construction and spatial query processing in Python**, including bulk loading, range queries, and incremental k-nearest-neighbor search. It was developed as **Assignment 2** of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

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

The project implements an R-Tree spatial index for polygonal objects and uses the generated index to evaluate spatial queries.

It consists of three stages:

- R-Tree construction through bulk loading
- Range queries over object Minimum Bounding Rectangles
- k-nearest-neighbor queries using best-first search

Polygon objects are represented by their Minimum Bounding Rectangles (MBRs). Their centers are mapped to Z-order values before bulk loading to preserve spatial locality during tree construction.

---

## TECH STACK

- **Language:** Python
- **Spatial Index:** R-Tree
- **Spatial Representation:** Minimum Bounding Rectangles (MBRs)
- **Spatial Ordering:** Z-order / Morton ordering
- **Search Structure:** Priority queue / min-heap
- **External Library:** `pymorton`
- **Standard Libraries:** `sys`, `ast`, `heapq`, `math`, `json`

---

## FEATURES

- **R-Tree Construction**
  - Reads polygon coordinates and object offsets
  - Computes object MBRs
  - Computes MBR centers
  - Orders objects using Z-order values
  - Builds the tree bottom-up
  - Enforces node occupancy constraints

- **Range Queries**
  - Loads the generated R-Tree
  - Tests MBR intersection
  - Recursively prunes non-intersecting subtrees
  - Returns matching object IDs

- **k-Nearest-Neighbor Queries**
  - Computes point-to-MBR distance
  - Uses best-first incremental traversal
  - Maintains candidate nodes and objects in a min-heap
  - Returns the first `k` object MBRs removed from the priority queue

---

## ARCHITECTURE

The project separates R-Tree construction and query processing into three command-line programs.

`rtree_builder.py` transforms polygon data into MBRs, orders them using Z-order values, and builds the R-Tree bottom-up. The resulting tree is persisted to `Rtree.txt`.

`range_query.py` reconstructs the tree from the generated file and recursively traverses nodes whose MBRs intersect each query rectangle.

`knn_query.py` also reconstructs the R-Tree and performs best-first traversal using a priority queue ordered by the minimum Euclidean distance between the query point and each candidate MBR.

---

## PROJECT STRUCTURE

```text
.
├── rtree_builder.py
├── range_query.py
├── knn_query.py
└── README.md
```

---

## INPUT DATA

### Polygon Coordinates

`coords.txt` contains polygon coordinates:

```text
x,y
```

### Object Offsets

`offsets.txt` maps each polygon identifier to its coordinate range:

```text
id,startOffset,endOffset
```

### Range Queries

`Rqueries.txt` contains query rectangles:

```text
x_low y_low x_high y_high
```

### kNN Queries

`NNqueries.txt` contains query points:

```text
x y
```

The R-Tree builder generates:

```text
Rtree.txt
```

which is subsequently consumed by both query programs.

---

## ALGORITHMS IMPLEMENTED

### Minimum Bounding Rectangles

For each polygon, the implementation computes:

```text
[x_min, x_max, y_min, y_max]
```

from the minimum and maximum coordinates of its vertices.

### Z-Order Bulk Loading

The center of each object MBR is computed and transformed into a Z-order value using `pymorton.interleave_latlng`.

Objects are sorted according to these values before being packed into leaf nodes.

R-Tree nodes use:

```text
Maximum entries: 20
Minimum entries: 8
```

The tree is then constructed bottom-up until a single root node remains.

### Range Query

For each query rectangle, the R-Tree is traversed recursively.

A subtree is explored only when its MBR intersects the query rectangle. At leaf level, intersecting object IDs are added to the result.

### k-Nearest-Neighbor Query

The kNN implementation performs incremental best-first search using a min-heap.

Candidate node and object MBRs are prioritized according to their shortest Euclidean distance from the query point:

```text
distance = sqrt(dx² + dy²)
```

where `dx` and `dy` represent the shortest distances between the point and the MBR along each dimension.

Objects removed from the priority queue are returned in increasing distance order until `k` results have been collected.

---

## INSTALLATION

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Ensure Python is installed.

3. Install the required external dependency:

```bash
pip install pymorton
```

---

## USAGE

Build the R-Tree:

```bash
python rtree_builder.py coords.txt offsets.txt
```

This generates:

```text
Rtree.txt
```

Run the range queries:

```bash
python range_query.py Rtree.txt Rqueries.txt
```

Run the k-nearest-neighbor queries:

```bash
python knn_query.py Rtree.txt NNqueries.txt <k>
```

For example:

```bash
python knn_query.py Rtree.txt NNqueries.txt 10
```

---

## CONTRIBUTORS

- **Christos Gkovaris** — GitHub: [ChristosGkovaris](https://github.com/ChristosGkovaris)

---

## LICENSE

No formal software license is included in the provided project files.

This project was developed as **Assignment 2** of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

---

## CONTACT

**Christos Gkovaris**  
Computer Science and Engineering  
University of Ioannina  