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
    """
    Exception raised when a line number is equal to zero.
    """

    def __init__(self):
        self.message = "Error! You can't access the line №0." \
                       'The number of the line must be greater than 0.'
        super().__init__(self.message)


class TooLargeLineNumber(Exception):
    """
    Exception raised when a line number exceeds total number of lines.

    Attributes:
        line_number (int): The line number that exceeds total number of lines.
    """

    def __init__(self, line_number):
        self.line_number = line_number
        self.message = f"Error! You can't access the line №{self.line_number}." \
                       'The number of the line exceeds total number of lines.'
        super().__init__(self.message)


class ZeroColumnNumber(Exception):
    """
    Exception raised when a column number is equal to zero.
    """

    def __init__(self):
        self.message = "Error! You can't access the column №0." \
                       'The number of the column must be greater than 0.'
        super().__init__(self.message)


class TooLargeColumnNumber(Exception):
    """
    Exception raised when a column number exceeds total number of columns in the line.

    Attributes:
        column_number (int): The column number that exceeds total number of columns in the line.
    """

    def __init__(self, column_number):
        self.column_number = column_number
        self.message = f"Error! You can't access the column №{self.column_number}." \
                       'The number of the column exceeds total number of columns in the line.'
        super().__init__(self.message)


class LineSwappedWithItself(Exception):
    pass


class UnsavedChangesExist(Exception):
    pass
