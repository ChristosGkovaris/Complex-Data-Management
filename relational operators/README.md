# RELATIONAL OPERATORS

This project implements **relational algebra operators** (Merge-Join, Union, Intersection, Difference, and Group-By with Sum) in **Python**. It was developed as part of the **MΥΕ041 - ΠΛΕ081: Διαχείριση Σύνθετων Δεδομένων** course at the **University of Ioannina**. The implementation reads **TSV files** representing relations **R** and **S**, performs the required operations using **merge-based algorithms**, and outputs results in separate files.

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

The project demonstrates the **implementation of core relational algebra operators** using **merge-based algorithms**, which are fundamental in database query evaluation. It processes two input files (`R.tsv` and `S.tsv`) and their **sorted versions** (`R_sorted.tsv` and `S_sorted.tsv`) to compute:

- Merge-Join
- Union
- Intersection
- Set Difference
- Group-By with Sum

The **implementation avoids reading entire files into memory** for operators 1–4, complying with **streaming merge** logic, while **Group-By** uses in-memory sort-merge.

---

## FEATURES

- **Merge-Join** using one-pass streaming and buffered matching
- **Union, Intersection, Difference** using variations of merge-based scanning
- **Duplicate elimination** for all set-based operations
- **Group-By Sum** using an in-memory sort-merge algorithm
- **Efficient streaming**: files are read only once for operators 1–4
- **TSV output** for each operation

---

## PROJECT STRUCTURE

```
relational-operators/
│── README.md
│
├── src/
│   └── relational_operators.py       # Main Python script
│
├── data/
│   ├── R.tsv
│   ├── S.tsv
│   ├── R_sorted.tsv
│   └── S_sorted.tsv
│
├── output/
│   ├── join.tsv
│   ├── union.tsv
│   ├── intersection.tsv
│   ├── difference.tsv
│   └── groupby.tsv
│
└── docs/
    └── assignment.pdf                # Assignment description
```

---

## INPUT DATA

The input files are **tab-separated values (TSV)** representing relations:

- **R.tsv** and **S.tsv** → unsorted input relations
- **R_sorted.tsv** and **S_sorted.tsv** → sorted versions for merge-based operations

**Schema:**
```
A   B
```
- `A` → 2-character string key
- `B` → integer value

---

## ALGORITHMS IMPLEMENTED

1. **Merge-Join (`join.tsv`)**
   - Joins R and S on the first attribute (A)
   - Buffers matching S tuples for repeated R keys
   - Outputs `(A, R.B, S.B)`

2. **Union (`union.tsv`)**
   - Computes `R ∪ S`  
   - Removes duplicates  
   - Outputs `(A, B)`

3. **Intersection (`intersection.tsv`)**
   - Computes `R ∩ S`  
   - Removes duplicates  
   - Outputs `(A, B)`

4. **Difference (`difference.tsv`)**
   - Computes `R − S`  
   - Removes duplicates  
   - Outputs `(A, B)`

5. **Group-By with Sum (`groupby.tsv`)**
   - Groups tuples of R by `A` and sums their `B` values
   - Outputs `(A, SUM(B))`

---

## INSTALLATION

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/relational-operators.git
cd relational-operators
```

2. **Install Python (>=3.8) and dependencies:**
```bash
pip install -r requirements.txt
```

---

## USAGE

Run the script from the command line:

### **1. Operators 1–4 (Join, Union, Intersection, Difference)**
```bash
python src/relational_operators.py data/R_sorted.tsv data/S_sorted.tsv
```
Generates:
```
output/join.tsv
output/union.tsv
output/intersection.tsv
output/difference.tsv
```

### **2. Operator 5 (Group-By with Sum)**
```bash
python src/relational_operators.py data/R.tsv
```
Generates:
```
output/groupby.tsv
```

---

## OUTPUT FILES

- `join.tsv` → `(A, R.B, S.B)`
- `union.tsv` → `(A, B)`
- `intersection.tsv` → `(A, B)`
- `difference.tsv` → `(A, B)` (R − S)
- `groupby.tsv` → `(A, SUM(B))`

---

## TESTING

- **Manual test:** Compare outputs with expected relational algebra results.  
- **Visual check:** Ensure duplicates are removed where needed.  
- **Optional:** Create a `tests/` folder for unit tests of each operator.

---

## LICENSE

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## CONTACT

**Christos Gkovaris**  
University of Ioannina – Computer Science and Engineering
[GitHub](https://github.com/ChristosGkovaris)
