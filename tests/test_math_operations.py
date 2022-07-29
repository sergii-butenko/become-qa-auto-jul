from libraries.print import Print


def test_division(fixture_42):
    Print.pretty_print("test_division")
    assert fixture_42.devision() == 2


def test_add(fixture_42):
    Print.pretty_print("test_add")
    assert fixture_42.add() == 6
