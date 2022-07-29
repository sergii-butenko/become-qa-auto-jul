def test_board_action_move(android_board_123):
    action_result = android_board_123.perform_action('move')
    assert action_result == "move 123"


def test_board_action_goto(android_board_123):
    action_result = android_board_123.perform_action('goto')
    assert action_result == "goto 123"


def test_board_action_read(android_board_123):
    action_result = android_board_123.perform_action('read')
    assert action_result == "read 123"


def test_board_action_add(android_board_123):
    action_result = android_board_123.perform_action('add')
    assert action_result == "add 123"
