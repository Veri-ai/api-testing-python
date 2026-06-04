## API Testing with Python
A demo project showcasing automated API testing using Python.

### Features
- Uses `requests` library to call public APIs
- Validates status codes and response fields with assertions
- Includes a `pytest` version for clean test reports
- Demonstrates reproducible results with screenshots

### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run tests:
   - Basic script: `python apiTest.py`
   - Pytest: `pytest`

### Pytest Demo
This repo includes a `test_api.py` file that uses pytest to validate GitHub API responses.

Run with:
```bash
pytest -v
