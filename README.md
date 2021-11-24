PubMedQuerier builds a series of TSVs from the PubMED database summarising the Papers, Colaborators and Research Areas of a single Author.

## RUN

To build a local python package (tested on Mac OS 10.2).

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
# Virtual env bundled with MacOS is faulty.
pip install --upgrade virtualenv
pip install pymed
python3 main.py
deactivate
```