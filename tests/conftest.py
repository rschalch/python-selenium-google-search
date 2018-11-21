import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    with webdriver.Firefox() as browser:
        yield browser


@pytest.fixture
def input_json(tmpdir):
    f = tmpdir.join("input.json")
    content = """{"google-me": ["Nextel", "telefonia do futuro", "selenium python"]}"""
    f.write(content)

    return f


@pytest.fixture
def expected_json():
    return """{"google-me": ["Nextel", "telefonia do futuro", "selenium python"]}"""
