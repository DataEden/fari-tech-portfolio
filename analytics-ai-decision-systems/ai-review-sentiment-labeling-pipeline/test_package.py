# Import the OpenAI client library
from openai import OpenAI

# Test to ensure OpenAI client can be instantiated
client = OpenAI()

# Define test functions
def assert_equal(result: list, correct: list, name: str) -> None:
    """
    A function to assert correct implementation of functions
    
    Args:
        result (list): The output from the function being tested.
        correct (list): The expected output for the test case.
        name (str): A descriptive name for the test case.
    Returns:
        None: The function prints the result of the test case.
    """
    if result == correct:
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"Expected {correct}, got {result}")
print("SUCCESS!")
