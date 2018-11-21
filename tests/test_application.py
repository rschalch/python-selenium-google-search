from application.google import get_results


def test_application_results(driver):
    driver.get('http://www.google.com')
    results = get_results(driver, 'Nextel')
    assert len(results) == 3
