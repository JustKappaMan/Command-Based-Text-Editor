class WrongNumberOfCommandLineArgs(Exception):
    """
    Exception raised when an incorrect number of CL args is passed to a script.

    Attributes:
        expected_args_count (int): The expected number of CL args.
        actual_args_count (int): The actual number of CL args passed to the script.

    Example:
        >>> raise WrongNumberOfCommandLineArgs(2, 1)
    """

    def __init__(self, expected_args_count, actual_args_count):
        self.expected_args_count = expected_args_count
        self.actual_args_count = actual_args_count
        self.message = f'Error! Expected number of CL args: {expected_args_count}, but got {actual_args_count}.'
        super().__init__(self.message)


class PathDoesNotExist(Exception):
    """
    Exception raised when a path doesn't exist.

    Attributes:
        path (pathlib.Path): The path that couldn't be found.
    """

    def __init__(self, path):
        self.path = path
        self.message = f"Error! Following path doesn't exist: {self.path}"
        super().__init__(self.message)


class PathIsNotFilepath(Exception):
    """
    Exception raised when a path isn't a filepath.

    Attributes:
        path (pathlib.Path): The path that isn't a filepath.
    """

    def __init__(self, path):
        self.path = path
        self.message = f"Error! Following path isn't a filepath: {self.path}"
        super().__init__(self.message)


class ZeroLineNumber(Exception):
    pass


class TooLargeLineNumber(Exception):
    pass


class ZeroColumnNumber(Exception):
    pass


class TooLargeColumnNumber(Exception):
    pass


class LineSwappedWithItself(Exception):
    pass


class UnsavedChangesExist(Exception):
    pass
