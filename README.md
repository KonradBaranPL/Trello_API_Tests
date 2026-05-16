# Trello API Tests

An automated REST API test suite for [Trello](https://trello.com), written in Python using the `requests` library and `pytest` framework. The project is built as an educational project, developed iteratively with code review from a mentor.
---


## Table of Contents

- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started Locally](#getting-started-locally)
- [Running Tests](#running-tests)
- [Project Status](#project-status)

---

## Project Description

An automated REST API test suite targeting the [Trello](https://trello.com) REST API. The framework verifies CRUD operations on boards, authorization behavior, and error handling for invalid input.

The project follows a layered structure:

- `api_clients/` – HTTP client classes (`BaseClient`, `BoardsClient`, `TrelloClient`) wrapping API calls
- `config/` – environment configuration (API key, token, base URL)
- `helpers/` – utility functions (e.g. unique name generation)
- `tests/` – test files separated into positive, negative, and boundary scenarios
- `conftest.py` – shared pytest fixtures handling authentication, resource creation, and cleanup

---

## Tech Stack

- **Python** 3.8+
- **pytest** 8.4.2 – test framework
- **requests** 2.32.5 – HTTP client
- **python-dotenv** 1.2.1 – environment variable management

---

## Getting Started Locally

**Clone the repository:**

```bash
git clone https://github.com/KonradBaranPL/Trello_API_Tests.git
cd Trello_API_Tests
```

**Create and activate a virtual environment:**

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Configure environment variables:**

Create a `.env` file in the root directory based on the template below:

```env
TRELLO_API_KEY=your_api_key
TRELLO_TOKEN=your_token
```

> The `.env` file is excluded from the repository via `.gitignore` — never commit your credentials.
>
> Your Trello API key and token can be generated at [https://trello.com/power-ups/admin](https://trello.com/power-ups/admin).

---

## Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_boards_positive.py

# Run with verbose output
pytest -v

# Generate an HTML report
pytest --html=report.html
```

> **Note on HTTP status codes:** The Trello API returns `200 OK` for POST requests creating resources, which differs from the standard REST convention of `201 Created`. This is intentional Trello behavior and the tests reflect it.

---

## Project Status

### ✅ Done

- Layered project structure separating clients, config, helpers, and tests
- pytest fixtures with setup and teardown for full test isolation
- HTTP client abstraction (`BaseClient`, `BoardsClient`, `TrelloClient`)
- Positive tests for board CRUD operations
- Negative tests for authorization errors
- Separate test files for positive, negative, and boundary scenarios
- Environment-based configuration
- HTML test reporting
- PEP 8 compliance, type annotations, and docstrings

### 🔧 Planned

- Expanded negative test coverage (invalid IDs, missing required fields)
- Expanded boundary test coverage using boundary value analysis
- Data-driven tests with parametrization for various input combinations
- Test coverage for additional Trello resources (lists, cards)
- CI/CD integration

## Authors

- **Konrad Baran** ([@KonradBaranPL](https://github.com/KonradBaranPL)) – project author
- **Michał Bandyszak** ([@Michal-Bandyszak](https://github.com/Michal-Bandyszak)) – mentor / code reviewer