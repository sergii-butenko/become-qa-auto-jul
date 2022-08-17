from libraries.math_operations import MathOperations
from libraries.board_manager.board_android import BoardAndroid
from libraries.print import Print

import pytest


@pytest.fixture
def fixture_42():
    math_operations = MathOperations(4, 2)
    math_operations.check_parameters()

    yield math_operations


@pytest.fixture()
def android_board_123():
    Print.pretty_print("Open connection start")
    board = BoardAndroid('123', '127.0.0.1')
    board.connect()

    yield board

    board.disconnect()
    Print.pretty_print("Open connection end")
    