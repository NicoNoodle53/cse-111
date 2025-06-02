from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Bob", "McAllister") == "McAllister; Bob"
    assert make_full_name("Samantha", "Hellpingisfun") == "Hellpingisfun; Samantha"
    assert make_full_name("Jack", "Elliott-Little") == "Elliott-Little; Jack"

def test_extract_family_name():
    assert extract_family_name("Elliott; Bob") == "Elliott"
    assert extract_family_name("Hellpingisfun; Samantha") == "Hellpingisfun"
    assert extract_family_name("Elliott-Little; Jack") == "Elliott-Little"

def test_extract_gien_name():
    assert extract_given_name("Elliott; Bob") == "Bob"
    assert extract_given_name("Hellpingisfun; Samantha") == "Samantha"
    assert extract_given_name("Elliott-Little; Jack") == "Jack"



pytest.main(["-v", "--tb=line", "-rN", __file__])