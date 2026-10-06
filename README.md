# devops-demo

Sample project for **Assignment No. 6 – Jenkins Integration with GitHub**.

Jenkins pulls this repository from GitHub, runs the Python application and its unit tests.

## Structure
```
devops-demo/
├── README.md        # This file
├── index.html       # Simple project web page
├── app.py           # Python application (build step)
├── Jenkinsfile      # Declarative pipeline (Checkout → Build → Test)
└── tests/
    ├── __init__.py
    └── test_app.py  # Unit tests (test step)
```

## Run locally
```bash
python app.py                                # Windows
python3 app.py                               # Linux
python -m unittest discover -s tests -v      # run tests
```

## CI Workflow
Developer → GitHub Repository → Jenkins → Build/Test → Build Result
