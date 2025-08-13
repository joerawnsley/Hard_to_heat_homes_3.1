from src.utils import *
import json
from tests.test_data.new_epc_dummy_data import epc_dummy_data


uprn = "100061342030"

QUERY_PARAMS = "uprn=200002791&uprn=100061342030"
HEADERS = {"Accept": "application/json", "Authorization": f"Basic EPC_TOKEN"}

def test_get_attributes_from_epc(mocker):
    mocker.patch("src.utils.epc_api_call", return_value=epc_dummy_data)
    with open("tests/test_data/os_dummy_data.json", "r") as data:
        os_dummy_data = json.load(data)
    dummy_props = get_properties_from_os(os_dummy_data["features"])
    uprn = "100061342030"
    prop = None
    for p in dummy_props:
        if str(p.uprn) == uprn:
            prop = p
            break
    get_attributes_from_epc(prop, uprn)
    matching_row = None
    for row in epc_dummy_data["rows"]:
        if row["uprn"] == uprn:
            matching_row = row
            break
    assert prop.epc_rating == matching_row["current-energy-rating"]
    assert prop.epc_score == matching_row["current-energy-efficiency"]
    assert prop.energy_usage == matching_row["energy-consumption-current"]
