# RELATIONAL OPERATORS

This project implements **relational algebra operators in Python**, including Merge-Join, Union, Intersection, Set Difference, and Group-By with Sum aggregation. It was developed as **Assignment 1** of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

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

The project implements five relational data-processing operations over file-based relations:

- Merge-Join
- Union
- Intersection
- Set Difference
- Group-By with Sum aggregation

The first four operations process sorted relations through sequential file access and merge-based logic. Group-By operates on an unsorted relation by loading its tuples into memory, sorting them, and aggregating values with the same key.

---

## TECH STACK

- **Language:** Python
- **Input Format:** Tab-separated values (TSV)
- **Data Processing:** Sequential file access, in-memory sorting
- **Libraries:** Python Standard Library

---

## FEATURES

- **Merge-Join**
  - Joins relations using their first attribute
  - Reads the sorted input files sequentially
  - Buffers matching values from the second relation

- **Set Operations**
  - Union
  - Intersection
  - Set Difference
  - Duplicate elimination

- **Aggregation**
  - Groups tuples by their first attribute
  - Computes the sum of their second attribute
  - Sorts unsorted input before aggregation

---

## ARCHITECTURE

The project is implemented as a single command-line Python program containing separate functions for each relational operator.

The first four operators work directly with sorted input streams rather than loading both relations entirely into memory. The Merge-Join maintains a buffer for matching tuples from the second relation, while Union, Intersection, and Difference advance through both sorted files according to their current values.

The Group-By implementation follows a separate in-memory workflow: tuples are loaded, sorted by key, and sequentially aggregated.

---

## PROJECT STRUCTURE

```text
.
├── relational_operators.py
└── README.md
```

---

## INPUT DATA

The project operates on relations containing two attributes:

```text
A    B
```

where:

- `A` is a two-character string
- `B` is an integer

The assignment uses:

```text
R.tsv
R_sorted.tsv
S_sorted.tsv
```

`R_sorted.tsv` and `S_sorted.tsv` are used for the merge-based operators, while the unsorted `R.tsv` is used for Group-By.

---

## ALGORITHMS IMPLEMENTED

### Merge-Join

The implementation sequentially scans the two sorted relations and joins tuples with equal values in the first attribute.

Matching values from the second relation are temporarily stored in a buffer so they can be reused when consecutive tuples from the first relation share the same join key.

The output has the form:

```text
A    R.B    S.B
```

### Union

Both sorted relations are traversed simultaneously. At each step, the smaller tuple is selected, while equal tuples advance both inputs.

The last written tuple is tracked to eliminate duplicates.

### Intersection

The algorithm advances through both sorted relations until matching tuples are found. Only tuples present in both relations are written to the result.

Duplicate output tuples are eliminated.

### Set Difference

The implementation computes:

```text
R - S
```

Tuples from `R` that do not occur in `S` are written to the result while both sorted relations are traversed sequentially.

### Group-By with Sum

The unsorted relation is loaded into memory and sorted by its first attribute.

Consecutive tuples sharing the same key are aggregated as:

```text
(A, B1), (A, B2), ... → (A, B1 + B2 + ...)
```

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

For Merge-Join, Union, Intersection, and Set Difference, provide the two sorted relations:

```bash
python relational_operators.py R_sorted.tsv S_sorted.tsv
```

The program generates:

```text
join.tsv
union.tsv
intersection.tsv
difference.tsv
```

For Group-By with Sum, provide the unsorted relation:

```bash
python relational_operators.py R.tsv
```

The program generates:

```text
groupby.tsv
```

---

## CONTRIBUTORS

- **Christos Gkovaris** — GitHub: [ChristosGkovaris](https://github.com/ChristosGkovaris)

---

## LICENSE

No formal software license is included in the provided project files.

This project was developed as **Assignment 1** of the **MΥΕ041 - Complex Data Management** course at the **University of Ioannina**.

---

## CONTACT

**Christos Gkovaris**  
Computer Science and Engineering  
University of Ioannina  