# Renamed from random_data_util.py

from mimesis import Person, Address, Datetime
from mimesis.locales import Locale
import random
import string

class RandomDataUtil:
    def __init__(self):
        self.person = Person(Locale.EN)
        self.address = Address(Locale.EN)
        self.datetime = Datetime()

    def ai_generate_data(self, prompt: str) -> str:
        """
        Generate test data using a local AI language model (LLM).
        Example integration below uses llama-cpp-python (https://github.com/abetlen/llama-cpp-python).
        Install: pip install llama-cpp-python

        Example usage:
            ai_data = random_data_util.ai_generate_data("Generate a valid user with a strong password and a .edu email")

        Returns a string or JSON depending on the LLM response.
        """
        try:
            from llama_cpp import Llama
        except ImportError:
            raise ImportError("llama-cpp-python is not installed. Run 'pip install llama-cpp-python'.")

        # Path to your local Llama model (e.g., 'models/llama-2-7b-chat.Q4_K_M.gguf')
        model_path = "models/llama-2-7b-chat.Q4_K_M.gguf"
        llm = Llama(model_path=model_path, n_ctx=2048)
        response = llm(prompt, max_tokens=256, stop=["\n"])
        # The response format may vary by model; adjust as needed
        return response["choices"][0]["text"].strip()

    def get_first_name(self) -> str:
        return self.person.first_name()

    def get_last_name(self) -> str:
        return self.person.last_name()

    def get_full_name(self) -> str:
        return self.person.full_name()

    def get_email(self) -> str:
        return self.person.email()

    def get_phone_number(self) -> str:
        return self.person.telephone()

    def get_username(self) -> str:
        return self.person.username()

    def get_password(self, length: int = 10) -> str:
        # Mimesis does not have a direct password generator, so use random
        import random, string
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def get_random_country(self) -> str:
        return self.address.country()

    def get_random_state(self) -> str:
        return self.address.state()
