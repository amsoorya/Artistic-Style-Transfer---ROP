# ROP-AST Analysis

This Jupyter Notebook demonstrates techniques for analyzing binary executables, focusing on **Return-Oriented Programming (ROP)** chains and **Abstract Syntax Trees (AST)**. The notebook is intended for security researchers, reverse engineers, or enthusiasts exploring symbolic execution and binary exploitation.

## 📌 Features

* **Binary Loading and Analysis** using `angr`
* **Intermediate Representation** with `pyvex`
* **Symbolic Execution** with `claripy`
* **ROP Chain Construction**
* **AST Generation** and inspection of instructions
* **Control Flow Graph (CFG) Analysis**
* Commented explanations for each section

## 🧰 Requirements

Install the required packages via pip:

```bash
pip install angr pyvex claripy
```

Make sure you're using **Python 3.8 or 3.9** as `angr` has compatibility constraints.

## 📁 Files

* `rop-ast.ipynb`: Main notebook containing code and explanations
* Target binary (if required): You'll need to provide your own ELF binary or modify the path in the notebook

## 🚀 Usage

1. Clone this repo or open the notebook locally.
2. Run each cell sequentially.
3. Observe the symbolic execution traces, disassembled instructions, and ASTs.

## 📷 Sample Output

* CFG graphs
* Disassembled instruction trees
* Symbolic paths and constraints

## ⚠️ Disclaimer

This project is intended for **educational purposes only**. Do not use these techniques for unauthorized analysis or exploitation.

## 📧 Contact

For questions, feedback, or collaboration opportunities, please contact:

**Jaya Soorya**  
Email: [amjayasoorya@gmail.com](mailto:amjayasoorya@gmail.com)

---

*Happy analyzing! 🔍*