class Unauthenticated(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

class Unauthorized(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None