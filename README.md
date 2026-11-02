# 1. First-time setup
git init
git add .
git commit -m "msg"
git remote add origin <url>
git push -u origin main

# 2. Feature branch
git checkout -b <branch>
# edit files
git add .
git commit -m "msg"
git push -u origin <branch>

# 3. After merging the PR on GitHub
git checkout main
git pull
git log --oneline

from calc import add
import pytest
@pytest.fixture
def input():
    return 10

@pytest.mark.math
def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 6),
    (4, 8),
])
def test_double(input, expected):
    assert input * 2 == expected

python -m venv venv
venv\Scripts\activate
pip install pytest
pytest --version


name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install pytest
        run: pip install pytest

      - name: Run tests
        run: pytest -v

Dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install pytest
CMD ["pytest", "-v"]

docker build -t calc-app .
docker run calc-app
docker ps -a
docker images

docker login
docker tag calc-app YOUR_DOCKERHUB_USERNAME/calc-app
docker push YOUR_DOCKERHUB_USERNAME/calc-app
