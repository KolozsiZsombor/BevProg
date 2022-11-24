from datetime import datetime

raise Exception("Something is wrong!")

raise RuntimeError("Runtime Error")

class SuperError(Exception):
    def __init__(self, message):
        Exception.__init__(message)
        self.when = datetime.now()


raise SuperError("Something is wrong in class!")