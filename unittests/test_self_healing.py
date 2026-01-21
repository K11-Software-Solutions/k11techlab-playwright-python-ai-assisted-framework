from ai.self_healing import find_element_with_self_healing
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import unittest
from unittest.mock import MagicMock
from ai.self_healing import find_element_with_self_healing


class TestSelfHealing(unittest.TestCase):
    def setUp(self):
        self.page = MagicMock()


    def test_fallback_to_alternative(self):
        # Each selector string returns a fresh MagicMock with locator.first = locator
        def locator_side_effect(selector):
            locator = MagicMock()
            locator.first = locator  # Chain .first to self
            if selector == "#notfound":
                locator.wait_for.side_effect = PlaywrightTimeoutError("fail")
            elif selector == "#found":
                locator.wait_for.return_value = "element-found"
            else:
                raise ValueError(f"Unexpected selector: {selector}")
            return locator

        self.page.locator.side_effect = locator_side_effect

        result = find_element_with_self_healing(
            self.page,
            "#notfound",
            alternatives=["#found"]
        )
        self.assertEqual(result, "element-found")


    def test_ai_model_used(self):
        # Each selector string returns a fresh MagicMock with locator.first = locator
        def locator_side_effect(selector):
            locator = MagicMock()
            locator.first = locator  # Chain .first to self
            if selector == "#notfound":
                locator.wait_for.side_effect = PlaywrightTimeoutError("fail")
            elif selector == "#stillnotfound":
                locator.wait_for.side_effect = PlaywrightTimeoutError("fail")
            elif selector == "#ai-found":
                locator.wait_for.return_value = "ai-element-found"
            else:
                raise ValueError(f"Unexpected selector: {selector}")
            return locator

        self.page.locator.side_effect = locator_side_effect

        def dummy_ai_model(selector, alternatives):
            return "#ai-found"

        result = find_element_with_self_healing(
            self.page,
            "#notfound",
            alternatives=["#stillnotfound"],
            ai_model=dummy_ai_model
        )
        self.assertEqual(result, "ai-element-found")

if __name__ == "__main__":
    unittest.main()
