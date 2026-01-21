
<p align="center">
    <img src="https://raw.githubusercontent.com/K11-Software-Solutions/assets/main/k11-logo.png" alt="K11 Software Solutions Logo" height="60" style="margin-right:20px;vertical-align:middle;"/>
    <img src="https://playwright.dev/img/playwright-logo.svg" alt="Playwright Logo" height="60" style="margin-right:20px;vertical-align:middle;"/>
    <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" height="60" style="vertical-align:middle;"/>
</p>

# Playwright Python AI-Assisted Test Automation Framework

This repository provides a modern, maintainable automation solution crafted specifically for [k11softwaresolutions.com](https://k11softwaresolutions.com/). Built with **Playwright** and **Python**, the framework is designed for clarity, scalability, and real-world QA needs. It features a modular Page Object Model (POM), advanced AI-assisted testing, and robust support for data-driven and parallel test execution. The architecture is optimized for subscription and service-based SaaS flows, with a focus on maintainability and extensibility for teams and individuals alike.


---
## Table of Contents

- [Features](#-features)
- [Framework Architecture](#-framework-architecture)
- [Technologies & Tools](#-technologies--tools)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [Running Tests](#-running-tests)
- [Configuration](#-configuration)
- [Reporting](#-reporting)
- [Best Practices Implemented](#-best-practices-implemented)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---


## Features

### Key Capabilities
- **Modular Page Object Model (POM):** Maintainable, reusable page abstractions for robust test logic.
- **Flexible Data-Driven Testing:** Easily run tests with data from CSV, JSON, Excel, or SQL sources.
- **Parallel & Cross-Browser Execution:** Run tests concurrently across Chromium, Firefox, and WebKit for speed and coverage.
- **Headless/Headed Modes:** Choose between visible or background browser runs for local or CI environments.
- **Smart Waits & Stability:** Leverages Playwright’s auto-waiting for reliable, flake-resistant tests.
- **Automatic Artifacts:** Screenshots, video, and trace files are captured for every failure to aid debugging.
- **Retry & Marker Support:** Rerun flaky tests and organize suites with custom markers (sanity, regression, etc.).
- **Dynamic Test Data:** Generate realistic and edge-case data using the Faker library and custom utilities.
- **Comprehensive Reporting:** HTML and Allure reports with screenshots, videos, and trace integration.
- **Centralized & Overrideable Configuration:** Manage all settings in one place, with command-line flexibility.
- **Reusable Fixtures:** Clean, DRY setup and teardown for browsers, pages, and test data.
- **Extensive Logging:** Detailed logs for every test run and artifact.

### Advanced & AI-Assisted Features
- **AI-Assisted Testing:** [Explore all AI-powered features & roadmap →](#ai-assisted-testing-features)
- **Self-Healing Locators:** Automatically adapt to UI changes using AI/ML or heuristics.
- **Test Impact Analysis:** AI suggests or selects only the relevant tests to run after code changes.
- **Automated Test Generation:** Generate new test cases from requirements or logs using LLMs.
- **Intelligent Failure Analysis:** AI reviews failed test logs and screenshots to suggest root causes.
- **Natural Language Test Authoring:** Write tests in plain English and convert to Playwright code.
- **Visual Regression with AI:** Smarter image comparison that ignores minor, irrelevant UI changes.

> See the [AI-Assisted Testing Features](#ai-assisted-testing-features) section below for full details and roadmap.

---


## Framework Architecture

```
┌────────────────────────────────────────────────────────────────────┐
│                        TEST LAYER                                 │
│  (tests/k11-platform/) - Test logic, assertions, and AI-driven scenarios │
└───────────────────────┬───────────────────────────────────────────┘
                        │
┌───────────────────────▼───────────────────────────────────────────┐
│                    PAGE OBJECT LAYER                              │
│  (pages/) - UI locators, page actions, and adaptive selectors     │
└───────────────────────┬───────────────────────────────────────────┘
                        │
┌───────────────────────▼───────────────────────────────────────────┐
│                UTILITIES & AI/ML LAYER                            │
│  (utilities/) - Data utilities, randomization, and AI/ML helpers  │
└───────────────────────┬───────────────────────────────────────────┘
                        │
┌───────────────────────▼───────────────────────────────────────────┐
│                CONFIGURATION & INTEGRATION LAYER                  │
│  (config.py, conftest.py, pytest.ini, AI/LLM config)              │
└───────────────────────────────────────────────────────────────────┘
```

---

## Technologies & Tools

| Technology / Library      | Role in the Framework |
|--------------------------|-------------------------------------------------------------|
| **Python 3.8+**          | Core language for all test logic and framework code          |
| **Playwright**           | Fast, reliable browser automation across all major browsers  |
| **Pytest**               | Flexible, powerful test runner and assertion engine          |
| **pytest-xdist**         | Enables parallel test execution for speed and scalability    |
| **pytest-html**          | Generates detailed HTML reports for test runs                |
| **Allure**               | Advanced analytics and reporting with rich attachments       |
| **pytest-rerunfailures** | Automatic retries for flaky or unstable tests                |
| **Faker**                | Produces dynamic, realistic, and edge-case test data         |
| **openpyxl**             | Reads and writes Excel files for data-driven testing         |
| **AI/LLM Integrations**  | Empowers test data, selectors, and analysis with AI/LLMs     |
| **Custom ML/Heuristics** | Drives self-healing locators, test impact, and visual checks |

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **IDE** - VS Code, PyCharm, or any Python IDE

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/playwright-python-framework.git
cd playwright-python-framework
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

Or install specific browsers:
```bash
playwright install chromium
playwright install firefox
playwright install webkit
```

### 5. Verify Installation

```bash
pytest --version
playwright --version
```

---

## Project Structure

```
k11techlab-playwright-python-ai-assisted-framework/
│
├── config.py                      # Test configuration and credentials
├── conftest.py                    # Pytest fixtures and hooks
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
│
├── pages/                         # Page Object Model classes (about_page.py, login_page.py, etc.)
│   ├── __init__.py
│   ├── home_page.py              # Home page actions & locators
│   ├── login_page.py             # Login page actions & locators
│   ├── about_page.py             # About page actions & locators
│   ├── contact_page.py           # Contact page actions & locators
│   ├── dashboard_page.py         # Dashboard page actions & locators
│   ├── forgot_password_page.py   # Forgot password page actions & locators
│   ├── home_page.py              # Home page actions & locators
│   ├── insights_page.py          # Insights page actions & locators
│   ├── login_page.py             # Login page actions & locators
│   ├── logout_page.py            # Logout page actions & locators
│   ├── register_page.py          # Registration page actions & locators
│   ├── reset_password_page.py    # Reset password page actions & locators
│   └── service_page.py           # Service/Subscription page actions & locators
│
├── tests/
│   ├── k11-platform/              # Main test cases (test_login_data_driven.py, test_login_page.py, etc.)
│   ├── playwright-advanced/       # Advanced Playwright scenarios
│   ├── playwright-examples/       # Example Playwright tests
│   └── ai/                        # AI-related test cases
│   ├── __init__.py
│   ├── test_about_page.py            # About page tests
│   ├── test_contact_page.py          # Contact page tests
│   ├── test_dashboard_page.py        # Dashboard page tests
│   ├── test_end_to_end.py            # End-to-end subscription/service flow
│   ├── test_forgot_password_page.py  # Forgot password tests
│   ├── test_home_page.py             # Home page tests
│   ├── test_insights_page.py         # Insights page tests
│   ├── k11-platform/test_login_data_driven.py     # Data-driven login tests
│   ├── test_login_page.py            # Login page tests
│   ├── test_register_page.py         # Registration page tests
│   ├── test_reset_password_page.py   # Reset password tests
│   ├── test_services_page.py         # Service/Subscription page tests
│   └── test_user_logout.py           # Logout functionality tests
│
├── utilities/                     # Helper utilities
│   ├── __init__.py
│   └── data_reader.py       # Read data from CSV/JSON/Excel/SQL files
│
├── ai/                            # AI/ML-powered utilities and models
│   ├── random_data.py       # Generate random, scenario-based, and AI-powered test data
│   └── self_healing.py      # Self-healing locator utility (AI/ML/LLM powered)
│
├── mcp_prompts/                   # Prompt templates for LLM/AI features
│   └── testdata_generation_prompt.txt  # Example: prompt for AI test data generation
│
├── testdata/                      # Test data files
│   ├── logindata.json            # Login test data (JSON)
│   ├── logindata.csv             # Login test data (CSV)
│   ├── logindata.xlsx            # Login test data (Excel)
│   └── test_users.sql            # SQL test data for data-driven tests
│
└── reports/                       # Test execution reports
    ├── myreport.html             # HTML report
    ├── screenshots/              # Failed test screenshots
    ├── videos/                   # Test execution videos
    ├── traces/                   # Playwright trace files
    ├── allure-results/           # Allure raw results
    └── allure-report/            # Allure HTML report
```

---

## Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/k11-platform/test_login_page.py

# Run specific test function
pytest tests/k11-platform/test_login_page.py::test_valid_user_login

# Run tests with verbose output
pytest -v

# Run tests with print statements visible
pytest -s
```

### Browser Selection

```bash
# Run with Chromium (default)
pytest --browser=chromium

# Run with Firefox
pytest --browser=firefox

# Run with WebKit (Safari)
pytest --browser=webkit
```

### Headed vs Headless Mode

```bash
# Run in headless mode (default)
pytest

# Run in headed mode (visible browser)
pytest --headed
```

### Parallel Execution

```bash
# Run tests in parallel using 4 workers
pytest -n 4

# Run tests in parallel using auto-detected CPU count
pytest -n auto
```

### Test Markers

```bash
# Run only sanity tests
pytest -m sanity

# Run only regression tests
pytest -m regression

# Run sanity OR regression tests
pytest -m "sanity or regression"

# Run tests excluding certain markers
pytest -m "not sanity"
```

### Data-Driven Tests

```bash
# Run data-driven tests
pytest -m datadriven

# Run specific data-driven test
pytest tests/k11-platform/test_login_data_driven.py
```

### Rerun Failed Tests

```bash
# Rerun failed tests 2 times with 1 second delay
pytest --reruns 2 --reruns-delay 1
```

### Custom Test Run Examples

```bash
# Run with specific base URL
pytest --base-url=https://your-app-url.com

# Run with video recording
pytest --video=on

# Run with screenshot on failure
pytest --screenshot=only-on-failure

# Run with tracing enabled
pytest --tracing=on

# Combination example
pytest -v -n 4 --browser=firefox --headed -m sanity
```

---

## Configuration

### pytest.ini Configuration

The `pytest.ini` file contains default test execution settings:

```ini
[pytest]
addopts =
    -v                                          # Verbose output
    --browser=chromium                          # Default browser
    --base-url=https://k11softwaresolutions.com/ # Base URL
    --video=retain-on-failure                   # Video recording
    --screenshot=only-on-failure                # Screenshot capture
    --tracing=retain-on-failure                 # Trace files
    --html=reports/myreport.html                # HTML report
    --alluredir=reports/allure-results          # Allure results
```

### config.py - Test Data

Update `config.py` with your test credentials and data:

```python
class Config:
    email = "test123@abc.com"
    password = "testpass"
    invalid_email = "testl123@abc.com"
    invalid_password = "test@123xyz"
    service_name = "Consulting"
    # Add more configuration as needed
```

### Command-Line Overrides

Any pytest.ini setting can be overridden via command line:

```bash
pytest --browser=firefox --base-url=https://staging.example.com
```

---

## Reporting

### HTML Report

After test execution, open the HTML report:

```bash
# Report location
reports/myreport.html
```

Features:
- Test execution summary
- Pass/fail statistics
- Test duration
- Error details and stack traces
- Embedded screenshots

### Allure Report

Generate and view Allure report:

```bash
# Generate Allure report from results
allure generate reports/allure-results --clean -o reports/allure-report

# Open Allure report in browser
allure open reports/allure-report

# Or serve the report
allure serve reports/allure-results
```

Allure Report Features:
- Trends and statistics
- Test case duration graphs
- Screenshots and attachments
- Video recordings
- Detailed test steps
- Test categorization
- Retry information

### Debug Artifacts

When tests fail, the following artifacts are automatically captured:

- **Screenshots**: `reports/screenshots/`
- **Videos**: `reports/videos/`
- **Traces**: `reports/traces/` (open with `playwright show-trace <trace-file>`)

---

## Best Practices Implemented

### 1. **Page Object Model (POM)**
- Separation of concerns
- Reusable page components
- Easy maintenance

### 2. **DRY Principle**
- Reusable fixtures in conftest.py
- Utility classes for common operations
- Centralized configuration

### 3. **Naming Conventions**
- Descriptive test names
- Clear variable naming
- Consistent file structure

### 4. **Error Handling**
- Try-except blocks in page objects
- Meaningful error messages
- Graceful failure handling

### 5. **Documentation**
- Inline code comments
- Docstrings for classes and methods
- Comprehensive README

### 6. **Version Control**
- .gitignore for Python projects
- Requirements.txt for dependencies
- Clean commit history

### 7. **Scalability**
- Modular architecture
- Easy to add new tests
- Support for multiple environments

### 8. **CI/CD Ready**
- Command-line configuration
- Parallel execution support
- Multiple report formats

---

## Contributing

We welcome contributions from the community! To get started:

1. Fork this repository to your own GitHub account.
2. Create a new branch for your feature or fix (`git checkout -b feature/YourAmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add: YourAmazingFeature'`).
4. Push your branch to your fork (`git push origin feature/YourAmazingFeature`).
5. Open a Pull Request describing your changes.

> For AI-powered automation enhancements, please use a branch name starting with `ai-powered-automation/` (e.g., `ai-powered-automation/your-feature`).

### Contribution Guidelines

- Adhere to the PEP 8 style guide for Python code.
- Add or update tests for any new features or bug fixes.
- Update documentation as needed to reflect your changes.
- Ensure all tests pass locally before submitting your PR.

---

## Author

**Kavita Jadhav**

Test Automation Engineer with expertise in scalable test frameworks, Playwright, and quality engineering best practices.

LinkedIn: https://www.linkedin.com/in/kavita-jadhav-tech/
---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Playwright Documentation](https://playwright.dev/python/)
- [Playwright MCP (Model Context Protocol)](https://github.com/microsoft/playwright-mcp)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- Testing community for inspiration and best practices

---


## Future Enhancements

- [ ] AI-powered API testing and validation
- [ ] Advanced visual regression with AI/ML
- [ ] Autonomous test generation and maintenance using LLMs
- [ ] Self-healing and adaptive test suites
- [ ] CI/CD pipeline examples (GitHub Actions, Jenkins) with AI-driven test selection
- [ ] Docker containerization and cloud-native execution
- [ ] Performance and reliability testing with AI-based analysis
- [ ] Mobile and cross-platform automation with AI support
- [ ] Cloud execution and scaling (BrowserStack, Sauce Labs, Azure, AWS)
- [ ] Customizable, AI-enhanced reporting and analytics
- [ ] Integration with test management and ALM tools (TestRail, Zephyr, Jira)

## AI-Assisted Testing Features

### Implemented & Planned

- **AI-Powered Test Data Generation**: Use LLMs or advanced Faker patterns to generate realistic, edge-case, or scenario-based test data automatically.
- **Self-Healing Locators**: AI/ML or heuristic algorithms auto-update selectors when UI changes are detected, reducing test flakiness.
- **Test Impact Analysis**: AI analyzes code changes and suggests or auto-selects only the relevant tests to run, speeding up CI.
- **Automated Test Case Generation**: LLMs generate new test cases from requirements, user stories, or production logs.
- **Intelligent Failure Analysis**: AI assistant analyzes failed test logs/screenshots and suggests likely root causes or fixes.
- **Natural Language Test Authoring**: Write tests in plain English, which are then converted to Playwright code using an LLM.
- **Visual Regression with AI**: AI-based image comparison for smarter visual regression, ignoring minor or irrelevant UI changes.

> These features are being integrated to make the framework more robust, maintainable, and future-ready for modern QA needs.
---

## Learning Resources

### Recommended for Beginners

1. **Playwright Official Tutorial**: [playwright.dev/python](https://playwright.dev/python/)
2. **Pytest Documentation**: [docs.pytest.org](https://docs.pytest.org/)
3. **Python Testing with Pytest** by Brian Okken
4. **Page Object Model Explained**: [Martin Fowler's Blog](https://martinfowler.com/bliki/PageObject.html)

### Key Concepts Demonstrated

- Designing robust test automation frameworks
- Implementing the Page Object Model (POM)
- Utilizing pytest fixtures and hooks
- Creating data-driven test strategies
- Generating and analyzing test reports
- Applying browser automation best practices
- Structuring and maintaining clean, scalable code

---

**If you find this project helpful, please give it a star!**



## About k11 Software Solutions

**k11 Software Solutions** is a leading provider of modern, AI-powered test automation, DevOps, and quality engineering services. We help organizations accelerate digital transformation with robust, scalable, and intelligent automation solutions tailored for SaaS, web, and enterprise platforms.

- Website: [https://k11softwaresolutions.com](https://k11softwaresolutions.com)
- Contact: k11softwaresolutions@gmail.com

*Partner with us to future-proof your QA and automation strategy!*

