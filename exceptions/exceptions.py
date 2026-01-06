class EmailException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PasswordException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotFoundIDTrip(Exception):
    def __init__(self, message):
        super().__init__(message)