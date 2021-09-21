class User:
    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            "name": self.name
        }