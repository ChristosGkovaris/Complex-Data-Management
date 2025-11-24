# COMPLEX DATA MANAGEMENT

This repository contains three projects developed as part of the **MΥΕ041 – Complex Data Management** course at the **University of Ioannina**.  
Each project explores a different aspect of advanced data management, including relational operators, spatial indexing, and transactional query processing.

---

## TABLE OF CONTENTS
1. [Overview](#overview)
2. [Project 1 – Relational Operators](#project-1--relational-operators)
3. [Project 2 – Spatial Data](#project-2--spatial-data)
4. [Project 3 – Total Data Management](#project-3--total-data-management)
5. [Installation](#installation)
6. [Usage](#usage)
7. [License](#license)
8. [Contact](#contact)

---

## OVERVIEW

This repository includes three standalone implementations that demonstrate core principles of complex data management. The projects cover relational algebra processing, spatial indexing through R-Trees, and transactional indexing for containment & relevance queries.

Each project includes Python scripts, example datasets, and output files generated during execution.

---

## PROJECT 1 – RELATIONAL OPERATORS

**Goal:** Implement essential **relational algebra operators** using efficient **merge-based algorithms**.

### **Implemented Operators**
- Merge-Join  
- Union  
- Intersection  
- Set Difference  
- Group-By with Sum  

### **Key Features**
- One-pass merge algorithms for large dataset compatibility  
- Duplicate elimination through sorted streams  
- Lightweight in-memory grouping  
- Outputs stored as `.tsv` files  

**Folder:** `src/relational-operators/`  
**Main Script:** `src/relational_operators.py`

---

## PROJECT 2 – SPATIAL DATA

**Goal:** Construct an **R-Tree spatial index** using **bulk loading**, and evaluate spatial queries.

### **Implemented Queries**
- Range Queries (window queries)  
- k-Nearest Neighbors (kNN)  

### **Key Features**
- Bulk loading with Z-order (Morton) encoding  
- Node capacity rules (min 8, max 20 entries)  
- Efficient tree traversal with pruning  
- Produces `Rtree.txt` and result files  

**Folder:** `src/spatial-data/`  
**Main Scripts:**  
- `src/rtree_builder.py`  
- `src/range_query.py`  
- `src/knn_query.py`

---

## PROJECT 3 – TOTAL DATA MANAGEMENT

**Goal:** Process **containment** and **relevance** queries on transactional datasets  
using multiple **indexing techniques**.

### **Containment Queries**
- Naive Sequential Scan  
- Signature File  
- Bitslice Signature File  
- Inverted File  

### **Relevance Queries**
- Naive TF×IDF ranking  
- Inverted Index–based ranking  

### **Key Features**
- Signature-based filtering  
- Inverted index construction for both set membership and ranking  
- Generates:  
  - `sigfile.txt`  
  - `bitslice.txt`  
  - `invfile.txt`  
  - `invfileocc.txt`  

**Folder:** `src/total-data-management/`  
**Main Scripts:**  
- `src/containment_queries.py`  
- `src/relevance_queries.py`

---

## INSTALLATION

1. Clone the repository:
```bash
git clone https://github.com/ChristosGkovaris/Complex-Data-Management.git
cd Complex-Data-Management
```
2. Ensure you have Python 3.8+ installed.
3. Install any required dependencies (if included in requirements):
```bash
pip install -r requirements.txt
```

---

## USAGE

1. Navigate to the folder of the project you want to run.
2. Execute the corresponding Python script.
3. View the output files generated in the same directory.
4. Modify parameters or datasets to explore different scenarios.
5. Use this repository as a reference for relational, spatial, and transactional indexing techniques.

---

## LICENSE

All projects are released under the **MIT License**.

See the `LICENSE` file for more details.

---

## CONTACT

**Christos Gkovaris**  
University of Ioannina – Computer Science and Engineering  
GitHub: https://github.com/ChristosGkovaris
