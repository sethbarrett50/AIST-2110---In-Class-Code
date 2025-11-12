# In-Lab Examples (AIST-2110)

This repository contains the Jupyter Notebooks and small helper scripts I use during AIST-2110 labs at Augusta University. Content is organized by week under `src/`.

---

## Usage

There are several ways to use these materials:

1. **Open in Google Colab (no install)**
   - Upload any `*.ipynb` to Google Drive.
   - Right-click -> **Open with -> Google Colab**.
   - If you need local files from this repo (e.g., small `.py` helpers), upload them to the Colab runtime or mount Drive within the notebook.

2. **Run locally with a Jupyter server (recommended)**
   - Install Python and Jupyter (see “Guidelines for local install” below).
   - Start a Jupyter server:
     - VS Code (recommended, just like CodeSpace): install the **Python** and **Jupyter** extensions, open this folder, and open notebooks directly in VS Code.
     - JupyterLab: `jupyter lab`
     - Classic Notebook: `jupyter notebook`
   - Select the **correct kernel** for the notebook (the environment where you installed the dependencies).

3. **Run individual Python scripts**
   - A few weeks include `.py` files (e.g., formatting helpers). You can run them directly with `python path/to/script.py`.

---

## Guidelines for local install

> **Recommended:** Use [uv](https://docs.astral.sh/uv/) for fast, reproducible environments. A `pyproject.toml` and `uv.lock` are included.

### Option A — Using `uv` (recommended)

1. **Install uv**  
   See: <https://docs.astral.sh/uv/getting-started/features/>
2. **Create/sync the environment**  
   ```bash
   uv sync
   ```

This will create a virtual environment and install all dependencies specified in `pyproject.toml`.
3. **Select the kernel in Jupyter**

* If prompted by VS Code/Jupyter, choose the `uv` virtual environment as the interpreter/kernel.
* Alternatively, register the kernel explicitly:

  ```bash
  uv run python -m ipykernel install --user --name aist2110 --display-name "Python (aist2110)"
  ```


### Option B — Using `pip` (simpler, fewer guarantees)

1. **Create/activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv .venv
   # Linux/macOS:
   source .venv/bin/activate
   # Windows (PowerShell):
   .\.venv\Scripts\Activate.ps1
   ```
2. **Install minimal tools**

   ```bash
   python -m pip install --upgrade pip
   python -m pip install ipython ipykernel 
   ```
3. **Register a kernel (optional, helps with selection)**

   ```bash
   python -m ipykernel install --user --name aist2110 --display-name "Python (aist2110)"
   ```

> If you prefer VS Code: install the **Python** and **Jupyter** extensions, select the interpreter from the Command Palette (“Python: Select Interpreter”), then open any `*.ipynb`.

---

## Project Layout

```
.
├── create_REPL.ps1           # Windows: launches Python REPL with a preloaded clear() helper
├── create_REPL.sh            # macOS/Linux: same as above, POSIX shell script
├── LICENSE                   # Project license
├── pyproject.toml            # Project dependencies & metadata (used by uv/pip)
├── README.md                 # This document
├── src
│   ├── week1
│   │   └── week1_code.ipynb  # Week 1 in-class notebook
│   ├── week2
│   │   ├── test.txt
│   │   └── week2_code.ipynb
│   ├── week3
│   │   └── week3_code.ipynb
│   ├── week4
│   │   └── week4_code.ipynb
│   ├── week5
│   │   ├── in_class.py       # Helper/companion code for Week 5
│   │   ├── ticket.py         # Small exercise or sample program
│   │   └── week5_code.ipynb
│   ├── week6
│   │   ├── grade_formatter.py
│   │   ├── grades.py
│   │   └── week6_code.ipynb
│   ├── week7
│   │   ├── grade_formatter.py
│   │   ├── grades.py
│   │   └── week7_code.ipynb
│   ├── week8
│   │   └── no_class_this_week.txt
│   ├── week9
│   │   └── week9_code.ipynb
│   ├── week10
│   │   └── week10_code.ipynb
│   ├── week11
│   │   └── week11_code.ipynb
│   ├── week13
│   │   └── week13_code.ipynb
│   └── week14
│       └── week14_code.ipynb
└── uv.lock                   # Lockfile for uv to guarantee reproducible installs
```

* **Per-week notebooks**: `src/weekX/weekX_code.ipynb` contain the in-class examples and exercises used that week.
* **Helper scripts** (Weeks 5–7): small Python modules used in demonstrations (e.g., simple grading/formatting utilities).
* **`pyproject.toml` / `uv.lock`**: define and lock dependencies. Use `uv sync` to reproduce the environment.

---

## Python REPL Scripts

If you want a bare Python REPL with a convenient `clear()` helper (as used in lab):

* **Windows (PowerShell):**

  ```powershell
  # If execution policy prevents running scripts:
  powershell -ExecutionPolicy Bypass -File .\create_REPL.ps1
  # or, if permitted:
  .\create_REPL.ps1
  ```
* **macOS/Linux:**

  ```bash
  chmod +x ./create_REPL.sh
  ./create_REPL.sh
  ```

Each script ensures Python 3 is available and then launches a REPL where `clear()` is pre-defined:

```python
clear = lambda: os.system("cls" if os.name == "nt" else "clear")
```

---

## Troubleshooting

* **Kernel not found / wrong environment selected**

  * Re-install the kernel with:

    ```bash
    # Using uv environment
    uv run python -m ipykernel install --user --name aist2110 --display-name "Python (aist2110)"
    ```
  * In VS Code, use “Python: Select Interpreter” and choose the environment created by `uv` or your venv.

* **Permission errors on scripts (macOS/Linux)**

  * Add execute permission: `chmod +x create_REPL.sh`

* **Windows PowerShell policy blocks script**

  * Run with: `powershell -ExecutionPolicy Bypass -File .\create_REPL.ps1`

* **Package/version mismatches**

  * Prefer `uv sync` (it respects `uv.lock`). For pip, ensure you’re in the right venv and re-install:

    ```bash
    python -m pip install --upgrade pip
    python -m pip install ipython ipykernel # Version issues are common with pip; uv essentially solves this
    ```

---

## License

See [LICENSE](LICENSE) for terms.

---
