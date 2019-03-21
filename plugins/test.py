import abstract.abstract_plugin as ap


class TestPlugin(ap.AbstractPlugin):
    def __init__(self):
        print("testplug")

    def handling_score(self, command: dict):
        if command == "test":
            return 1

    def handle(self):
        print("handling")
