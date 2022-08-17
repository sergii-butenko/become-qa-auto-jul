class BoardAndroid:

    def __init__(self, board_id, connection_string):
        self.board_id = board_id
        self.connection_string = connection_string

    @staticmethod
    def connect_class_method():
        """Class method"""
        print("connect_class_method")

    def connect(self):
        """Class object method"""
        print("CONNECT")

    def disconnect(self):
        """Class object method"""
        print("DISCONNECT")

    def perform_action(self, action):
        """Class object method"""
        return f"{action} {self.board_id}"
