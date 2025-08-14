from src.council_data_utils import get_bbox_for_council_code, get_formatted_bbox_for_council_code

def test_get_bbox_for_council_returns_correct_for_valid_council():
    council_code = "E07000207"
    expected_bbox = "-0.4812058077066727,51.29485438921932,-0.30738853934695304,51.41205084255087"

    bbox = get_bbox_for_council_code(council_code)
    assert bbox == expected_bbox

def test_get_bbox_for_council_returns_false_for_invalid_council():
    invalid_council_code = "have a nice day!"
    bbox = get_bbox_for_council_code(invalid_council_code)
    assert bbox is False

def test_get_bbox_for_council_returns_false_for_null():
    invalid_council_code = None
    bbox = get_bbox_for_council_code(invalid_council_code)
    assert bbox is False

#Formatted Bounding box

def test_get_formatted_bbox_for_council_code_returns_floats():
    council_code = "E07000207"
    expected_bbox = (-0.4812058077066727,51.29485438921932,-0.30738853934695304,51.41205084255087)

    bbox = get_formatted_bbox_for_council_code(council_code)
    assert bbox == expected_bbox

def test_get_formatted_bbox_for_council_returns_false_for_invalid_council():
    invalid_council_code = "have a nice day!"
    bbox = get_formatted_bbox_for_council_code(invalid_council_code)
    assert bbox is False

def test_get_formatted_bbox_for_council_returns_false_for_null():
    invalid_council_code = None
    bbox = get_formatted_bbox_for_council_code(invalid_council_code)
    assert bbox is False