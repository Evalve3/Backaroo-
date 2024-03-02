class UserException(Exception):
    ex_data: str

    def __init__(self, ex_data: str, *args, **kwargs):
        super().__init__(*args)
        self.ex_data = ex_data


class UserNotFoundException(UserException):
    pass


class UniqueViolationException(UserException):
    pass

