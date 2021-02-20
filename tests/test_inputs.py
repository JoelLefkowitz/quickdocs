from quickdocs.inputs import Inputs

def test_from_json():
    print(Inputs.from_file("tests/inputs.json", "json"))
