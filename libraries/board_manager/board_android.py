class BoardAndroid:

    def __init__(self, board_id, connection_string) -> None:
        self.board_id = board_id
        self.connection_string = connection_string

    def connect(self) -> True:
        print("CONNECT")

    def disconnect(self):
        print("DISCONNECT")

    def perform_action(self, action):
        return f"{action} {self.board_id}"
