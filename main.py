import argparse

from application.google import get_results, get_driver
from application.utils import read, write, make_json, make_obj


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()

    driver = get_driver()

    json_str = read(args.file)
    terms = make_obj(json_str, first_key=True)
    final_result = {}

    for term in terms:
        final_result[term] = get_results(driver=driver, term=term)
        print(make_json(final_result, term))

    driver.quit()

    output = make_json(final_result)

    write('./output.json', output)
