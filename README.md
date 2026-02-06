# Automated Web Testing — Multi-Config Login

A macOS compatible automated web testing project that verifies login flows across multiple sites using Selenium and Python. This repository demonstrates scalable and configurable test automation suitable for technical operations or QA automation portfolios.

---

## Features

- Run multiple login tests from a single configuration file (`config.json`)  
- Launch Chrome automatically via Selenium WebDriver  
- Input username and password and assert successful login  
- Record structured logs and errors to `logs/test_login.log`  
- Configurable wait/timeouts per test case  
- Graceful exception handling and exit codes for CI

## Project Structure

project-02-web-test-automation/
├── test_login.py        # Main Selenium test script
├── config.json          # Multiple test configurations (URL, creds, selectors, timeouts)
├── requirements.txt     # Python dependencies (Selenium, webdriver-manager, etc.)
├── README.md
└── logs/
    └── .gitkeep         # keep logs folder in repo

Notes:
- `test_login.py` contains the automation logic and logging.
- `config.json` holds an array of test definitions so you can add tests without touching code.

## Prerequisites

- macOS
- Python 3.8+ (Python 3.12 recommended)
- Chrome browser installed
- Optional: `pyenv` for per-project Python version management 

## Setup

1. Clone the repo:

```bash
git clone <(https://github.com/ApBletsas/Automated-Web-Testing.git)>
cd automated-web-testing
```

2. Install and set Python with `pyenv`:

```bash
pyenv install 3.12.2
pyenv local 3.12.2
python --version
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

If the repository contains a differently named requirements file (e.g. `requirments.txt`), adjust the command accordingly.

## Configuration

- Edit `config.json` to add or update test entries. Each entry should include the target `url`, `username`, `password`, and any `wait` or selector overrides your script expects.

Example `config.json` snippet:

```json
[
  {
    "name": "example-site",
    "url": "https://example.com/login",
    "username": "user@example.com",
    "password": "s3cr3t",
    "wait": 10
  }
]
```

## Running Tests

```bash
python test_login.py
```

The script will iterate through the configurations and attempt each login, printing a summary to stdout and appending structured logs to `logs/test_login.log`.

## Logs

- Logs are written to `logs/test_login.log` and include timestamps, test names, pass/fail status, and traceback information for failures.

## CI / Exit Codes

- The script exits with `0` when all tests pass. Non-zero exit codes are returned for failures or unhandled exceptions, allowing CI systems to detect failures.

## Contributing

- Add test cases to `config.json` rather than modifying `test_login.py` where possible.
- Open an issue or PR for enhancements (additional browsers, parallel runs, reporting integrations).

## References

- Selenium Documentation: https://www.selenium.dev/documentation/webdriver/
- The Internet Test Site: https://the-internet.herokuapp.com/login

## License

This project is licensed under the MIT License
