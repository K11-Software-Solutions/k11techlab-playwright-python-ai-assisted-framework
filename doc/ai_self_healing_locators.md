# AI-Assisted Self-Healing Locators

This document describes the self-healing locator feature in the k11softwaresolutions.com Playwright Python Test Automation Framework.

## Overview

Self-healing locators use AI/ML or heuristic algorithms to automatically adapt to UI changes, reducing test flakiness and maintenance effort. When a selector fails, the framework attempts to find the correct element using alternative strategies and updates the locator for future runs.

## How It Works
- On locator failure, the framework tries alternative selectors (e.g., text, role, attributes, fuzzy matching).
- Optionally, an AI/ML model or LLM can be used to suggest or validate the best alternative.
- Successful alternatives are logged and can be persisted for future test runs.

## Usage
- Use the `find_element_with_self_healing` utility in your page objects instead of direct Playwright selectors.
- Integrate with an AI/ML model or LLM for advanced healing (see code comments for extension points).

### Example
```python
from utilities.self_healing import find_element_with_self_healing

element = find_element_with_self_healing(page, original_selector, alternatives=[...], ai_model=your_model)
```

## Best Practices
- Maintain a list of alternative selectors for each element.
- Log all healing attempts and outcomes for review.
- Periodically review and update selectors based on healing logs.

---

For more AI features, see other docs in the `doc/` folder.
