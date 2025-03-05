import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api_client import APIClient  

import pytest

@pytest.fixture(scope="module")
def api_client():
    """Fixture to create API client instance"""
    return APIClient()