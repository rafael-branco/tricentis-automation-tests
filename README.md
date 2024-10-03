
# Tricentis Automation Tests

## Overview

This project contains automated tests for Tricentis sample pages using Selenium. The tests are organized under the `tests` folder, and the code for the web pages being tested is under the `pages` directory. Test results and screenshots are saved in the `screenshots` folder.

## Requirements

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Setup

1. Clone the repository to your local machine.

```bash
git clone https://github.com/rafael-branco/tricentis-automation-tests.git
cd tricentis-automation-tests
```

2. Create a virtual environment (optional but recommended).

```bash
python -m venv venv
```

3. Activate the virtual environment.

- On Windows:

```bash
venv\Scripts\activate
```

- On MacOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Running the Tests

To run the test suite, simply execute the following command:

```bash
python -m unittest tests.test_sample_app
```

Screenshots from the tests will be saved automatically in the `screenshots` folder.

## Notes

- This project uses `webdriver-manager` to automatically manage the web drivers required by Selenium.
- Ensure your environment is properly configured with Python and pip.
