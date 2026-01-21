# AI-Powered Test Data Generation

This document describes how to use and extend AI-powered test data generation in the k11softwaresolutions.com Playwright Python Test Automation Framework.

## Overview

The framework supports advanced test data generation using both the Faker library and optional AI/LLM integration. This enables:
- Creation of highly realistic, edge-case, or scenario-specific data for robust test coverage
- On-demand generation of user profiles, emails, passwords, and more, tailored to your test needs
- (Optional) Use of LLMs (e.g., OpenAI, Azure OpenAI, or local models) to generate complex or context-aware data for advanced scenarios

## Usage

- Use the `RandomDataUtil` class in `utilities/random_data.py` for standard and AI-powered data generation.
- Extend `RandomDataUtil` with an `ai_generate_data(prompt: str)` method to leverage LLMs for custom data (see code comments for integration points).

### Example
```python
from utilities.random_data import RandomDataUtil
random_data = RandomDataUtil()
user_profile = random_data.get_user_profile()  # Standard random data
# ai_data = random_data.ai_generate_data("Generate a valid user with a strong password and a .edu email")
```

## Integration

To enable AI-powered data, integrate your preferred LLM provider (e.g., OpenAI, Azure OpenAI, or a local model) in the `ai_generate_data` method. See the comments in `random_data.py` for guidance.

## Best Practices
- Use AI-generated data for complex, scenario-based, or edge-case testing.
- Validate AI-generated data to ensure it meets your application's requirements.
- Combine Faker and AI data for maximum coverage.

---

For more AI features, see other docs in the `doc/` folder.
