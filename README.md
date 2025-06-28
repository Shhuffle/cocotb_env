# Cocotb Testbench Collection 

This repository contains a collection of **Cocotb-based testbenches** for various Verilog design modules. Each testbench uses a modular, reusable **UVM-style verification approach** in Python.

---

##  Projects Included

### 🔹 FIFO Buffer
- Implements a 1024-depth FIFO with `write`, `read`, `full`, `empty` control.
- Verified using UVM-style components: transaction, driver, monitor, scoreboard.
- 📄 **Design description** is available in the `designInfo` file inside the project folder.

### 🔹 8-bit ALU
- Supports basic arithmetic and logical operations.
- Uses random test vectors for functional verification.
- 📄 **Design description** available in `designInfo`.

### 🔹 8-bit Full Adder
- Adds two 8-bit inputs with carry support.
- Simple Cocotb testbench for validation.
- 📄 **Design description** available in `designInfo`.

---

##  How to Run

### 1. Environment Setup in UBUNTU

Inside the project folder open a terminal
python3 -m venv cocotb-env
source cocotb-env/bin/activate
pip install cocotb
make
