# Copilot Instructions for k11techlab-playwright-python-ai-assisted-framework

## Project Overview
- **Purpose:** Modern Playwright + Python test automation for SaaS, with advanced AI-assisted features (self-healing locators, AI data, natural language test authoring, etc.)
- **Architecture:**
  - **tests/**: Test logic, assertions, and AI-driven scenarios
  - **pages/**: Page Object Model (POM) classes for UI abstraction
  - **ai/**: AI/ML-powered utilities (self-healing, random data)
  - **utilities/**: Data readers, helpers
  - **testdata/**: Data files (CSV, JSON, SQL, Excel)
  - **reports/**: Artifacts (screenshots, videos, traces, HTML/Allure reports)
  - **config.py / pytest.ini / conftest.py**: Central config, fixtures, and hooks

## Key Conventions & Patterns
- **Page Object Model:** All UI logic in `pages/` (e.g., `login_page.py`). Expose clear methods for actions and assertions.
- **AI Self-Healing:** Use `find_element_with_self_healing` (from `ai/self_healing.py`) for robust element lookup. Pass alternative selectors and an AI model backend (see doc/ai_self_healing_locators.md).
- **AI Data Generation:** Use `RandomDataUtil` (`ai/random_data.py`) for scenario-based or LLM-generated test data.
- **Test Markers:** Use pytest markers (`sanity`, `regression`, `datadriven`, `ai`, etc.) as defined in `pytest.ini`.
- **Artifacts:** All screenshots, videos, and traces are saved in `reports/` and attached to reports automatically via `conftest.py`.
- **Custom CLI Options:** Use `--k11browser`, `--k11headed`, `--k11video`, `--k11screenshot`, `--k11tracing`, `--k11device` for advanced test runs (see `conftest.py`).

## Developer Workflows
- **Install:**
  - `pip install -r requirements.txt && pip install -r requirements-ai.txt`
  - `playwright install`
- **Run Tests:**
  - `pytest` (all tests)
  - `pytest -n 4 -m ai` (parallel, AI tests)
  - `pytest --browser=firefox --headed` (custom browser/mode)
- **Reports:**
  - HTML: `reports/myreport.html` (auto-generated)
  - Allure: `allure generate reports/allure-results --clean -o reports/allure-report`
- **Debugging:**
  - Artifacts auto-captured on failure (see `reports/`)
  - Use Playwright trace viewer: `playwright show-trace reports/traces/<file>.zip`

## AI Integration Points
- **Self-Healing Locators:**
  - Configure AI backend via `.env` (OpenAI, Ollama, local LLM, etc.)
  - See `ai/self_healing.py` and `doc/ai_self_healing_locators.md` for extension
- **AI Data:**
  - Use `ai/random_data.py` for LLM-based or random data
- **Prompt Templates:**
  - See `prompts/` for LLM prompt examples

## Examples
- See `tests/ai/test_self_healing.py` for AI locator usage
- See `pages/k11_platform/login_page.py` for POM pattern
- See `conftest.py` for artifact and fixture logic

## Project-Specific Notes
- All test data and credentials are managed in `config.py` (do not hardcode in tests)
- Use `pytest.ini` for default CLI/test config; override via command line as needed
- For new AI features, branch as `ai-powered-automation/<feature>`

---
For more, see `README.md` and `doc/`.
