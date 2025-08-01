# SPATIAL DATA

This project implements an **R-Tree index** with **bulk loading** and supports **spatial queries** including **Range Query** and **k-Nearest Neighbor (kNN) Query**. It was developed as part of the **MΥΕ041 - ΠΛΕ081: Διαχείριση Σύνθετων Δεδομένων (Δ07: Spatial Data)** course at the **University of Ioannina**. The implementation constructs an **R-Tree** from polygonal object data using **Z-order (Morton) codes** and performs spatial queries efficiently.

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

This project focuses on **spatial indexing and querying**:

- Builds an **R-Tree** from polygonal spatial objects using **bulk loading**.
- Uses **Z-order (Morton) codes** to pack nearby objects in the same R-Tree nodes.
- Supports **Range Queries** (window queries) and **kNN Queries** for spatial search.
- Demonstrates **efficient tree traversal** without scanning all objects.

---

## FEATURES

- **Bulk Loading of R-Tree**
  - Computes Minimum Bounding Rectangles (MBRs) of objects
  - Uses Z-order curve for object sorting
  - Constructs tree levels respecting max/min node capacities (20 / 8)
- **Range Query (Rqueries.txt)**
  - Returns all objects intersecting a query rectangle
- **kNN Query (NNqueries.txt)**
  - Returns the k nearest neighbors to each query point
- **Efficient Traversal**
  - Non-leaf nodes store aggregated MBRs for fast pruning
  - Leaf nodes store `[object_id, MBR]` entries
- **TSV or console output** for queries

---

## PROJECT STRUCTURE

```
spatial-rtree/
│── README.md
│
├── src/
│   ├── rtree_builder.py      # Builds R-Tree using bulk loading
│   ├── range_query.py        # Performs range (window) queries
│   └── knn_query.py          # Performs k-nearest neighbor queries
│
├── data/
│   ├── coords.txt            # Coordinates of polygon vertices
│   ├── offsets.txt           # Object offsets defining polygons
│   ├── Rtree.txt             # Output R-Tree structure (generated)
│   ├── Rqueries.txt          # Range query rectangles
│   └── NNqueries.txt         # kNN query points
│
├── output/
│   ├── range_results.txt     # Output of range queries
│   └── knn_results.txt       # Output of kNN queries
│
└── docs/
    └── assignment.pdf        # Assignment description
```

---

## INPUT DATA

The project processes **polygonal objects** and **spatial queries**:

1. **coords.txt**
   - Format:  
     ```
     x,y
     ```
   - Contains the vertices of all polygons.

2. **offsets.txt**
   - Format:  
     ```
     object_id,startOffset,endOffset
     ```
   - Maps each object to its vertex coordinates in `coords.txt`.

3. **Rqueries.txt**
   - Range (window) queries in the form:  
     ```
     x_low y_low x_high y_high
     ```

4. **NNqueries.txt**
   - Query points for kNN search:  
     ```
     x y
     ```

---

## ALGORITHMS IMPLEMENTED

1. **R-Tree Bulk Loading (`rtree_builder.py`)**
   - Computes MBRs for all objects
   - Sorts objects using Z-order (Morton codes)
   - Packs objects into R-tree nodes with:
     - **Max entries = 20**
     - **Min entries = 8 (0.4 × max)**
   - Builds tree bottom-up to root

2. **Range Query (`range_query.py`)**
   - Input: `Rtree.txt`, `Rqueries.txt`
   - Traverses the tree, pruning subtrees whose MBRs do not intersect the query rectangle
   - Outputs object IDs intersecting each query window

3. **kNN Query (`knn_query.py`)**
   - Input: `Rtree.txt`, `NNqueries.txt`, `k`
   - Uses **Best-First Search** with a **min-heap** based on distance to MBRs
   - Returns the k nearest neighbors for each query point

---

## INSTALLATION

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/spatial-rtree.git
cd spatial-rtree
```

2. **Install Python (>=3.8) and required libraries:**
```bash
pip install -r requirements.txt
```

> **Note:** This project uses `pymorton` for Z-order code computation.

---

## USAGE

### **1. Build the R-Tree**
```bash
python src/rtree_builder.py data/coords.txt data/offsets.txt
```
Generates:
```
data/Rtree.txt
```

### **2. Run Range Queries**
```bash
python src/range_query.py data/Rtree.txt data/Rqueries.txt
```
Outputs results to console or can be redirected:
```
python src/range_query.py data/Rtree.txt data/Rqueries.txt > output/range_results.txt
```

### **3. Run kNN Queries**
```bash
python src/knn_query.py data/Rtree.txt data/NNqueries.txt k
```
Example for `k = 5`:
```
python src/knn_query.py data/Rtree.txt data/NNqueries.txt 5 > output/knn_results.txt
```

---

## OUTPUT FILES

- `Rtree.txt` → Stored R-tree structure with nodes and entries
- `range_results.txt` → Object IDs intersecting each query rectangle
- `knn_results.txt` → k nearest neighbors for each query point

---

## ✅ Testing

- **Visual Check:** Compare returned object IDs with manual small examples.
- **Performance Test:** Run queries on large datasets to verify efficient pruning.

---

## LICENSE

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## CONTACT

**Christos Gkovaris**  
University of Ioannina – Computer Engineering & Informatics  
[GitHub](https://github.com/ChristosGkovaris)