import datetime


class Print():
    @staticmethod
    def pretty_print(message):
        print(f"{datetime.datetime.now()} - {message}")