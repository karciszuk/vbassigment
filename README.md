# vbassigment
## Setup
### 1. Create virtual environment:
```
python -m venv .venv
```
### 2. Activate virtual environment:
#### Windows
```
.venv\Scripts\activate
```
#### Mac/Linux
```
source .venv/Scripts/activate
```
### 3. Install as editable:
```
pip install -e .
```

### 4. Create .env file based on .env.example:
```
PYTHONPATH = 'path to root folder'
DB_PATH = 'name of db file in root folder'
```

### 5. Run notebooks:
```
jupyter notebook
```
