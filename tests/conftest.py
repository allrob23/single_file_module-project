import pytest
import random

@pytest.fixture(scope="session", autouse=True)
def set_random_seed():
    """Set a fixed seed for random number generation to ensure reproducibility."""
    random.seed(42)
    yield