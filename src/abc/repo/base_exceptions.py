class RepoException(Exception):
    ex_data: str

    def __init__(self, ex_data: str, *args, **kwargs):
        super().__init__(*args)
        self.ex_data = ex_data


class NotFoundException(RepoException):
    pass


class UniqueViolationException(RepoException):
    pass

