from application.utils import read, write, make_obj, make_json


def test_read(input_json, expected_json):
    assert read(input_json) == expected_json


def test_write():
    import os.path

    write('./tmp_file', 'dummy content')

    assert os.path.exists('./tmp_file')
    assert os.path.isfile('./tmp_file')
    assert 'dummy content' in open('./tmp_file').read()

    os.remove('./tmp_file')


def test_make_obj(expected_json):
    obj = make_obj(expected_json)
    assert obj == {'google-me': ['Nextel', 'telefonia do futuro', 'selenium python']}

    obj = make_obj(expected_json, first_key=True)
    assert obj == ['Nextel', 'telefonia do futuro', 'selenium python']


def test_make_json():
    obj = {'google-me': ['Nextel', 'telefonia do futuro', 'selenium python']}

    expected_output = """{
    "google-me": [
        "Nextel",
        "telefonia do futuro",
        "selenium python"
    ]
}"""

    assert make_json(obj) == expected_output
