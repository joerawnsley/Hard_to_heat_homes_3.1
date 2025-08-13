from src.property import Property

test_prop = Property(1)

def test_property_has_score():
    assert type(test_prop.calculate_score()) is int

def test_standalone_property_score_equals_1():
    test_prop.connectivity = "Standalone"
    test_prop.epc_rating = "C"
    assert test_prop.calculate_score() == 1

def test_property_not_brick_score_adds_1():
    test_prop.material = "Wood"
    assert test_prop.calculate_score() == 2

def test_property_epc_rating_below_d_adds_point():
    test_prop.epc_rating = "E"
    assert test_prop.calculate_score() == 3

def test_property_age_before_1960_adds_point():
    test_prop.age = 1950
    assert test_prop.calculate_score() == 4

def test_property_age_range_before_1960_adds_point():
    test_prop_2 = Property(1)
    test_prop_2.epc_rating = "D"
    test_prop_2.age = "1940-1950"
    assert test_prop_2.calculate_score() == 1

def test_property_with_mixed_point_attributes():
    test_prop_three = Property(3)
    test_prop_three.material = 'Brick Or Block Or Stone'
    test_prop_three.connectivity = "Standalone"
    test_prop_three.age = "1959-1961"
    test_prop_three.epc_rating = "E"
    assert test_prop_three.calculate_score() == 2 

# Need to double check about unknown adding a point vs no adding point
def test_property_age_unknow():
    test_prop_four = Property(4)
    test_prop_four.epc_rating = "C"
    test_prop_four.age = "Unknown"
    assert test_prop_four.calculate_score() == 1

def test_property_epc_not_found():
    test_prop_five = Property(5)
    test_prop_five.epc_rating = ""
    assert test_prop_five.calculate_score() == 1