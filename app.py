"""
devops-demo / app.py
Simple Python application used to demonstrate Jenkins + GitHub integration.
Jenkins clones this repository and runs this file as the "build" step.
"""

from datetime import datetime
import platform
import sys


def add(a, b):
    """Return the sum of two numbers (used by the unit test)."""
    return a + b


def greet(name):
    """Return a greeting message (used by the unit test)."""
    return f"Hello, {name}! Welcome to the Jenkins-GitHub CI demo."


def main():
    print("=" * 55)
    print("   DevOps Demo Application - Jenkins + GitHub CI")
    print("=" * 55)
    print(greet("Jenkins"))
    print(f"Build time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Running on     : {platform.system()} {platform.release()}")
    print(f"Sample result  : add(10, 20) = {add(10, 20)}")
    print("=" * 55)
    print("Application executed successfully.")


if __name__ == "__main__":
    main()
