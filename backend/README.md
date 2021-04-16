# Setup

Create virtual environment:
```
python -m venv venv
```
Activate virtual environment:
```
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Start backend server (development):
```
uvicorn index:app --host 0.0.0.0 --port 5000 --log-level debug --reload
```
