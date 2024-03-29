import pathlib


class WrongNumberOfCommandLineArgs(Exception):
    """
    Exception raised when an incorrect number of CL args is passed to a script.
    """

    def __init__(self, expected_args_count: int, actual_args_count: int):
        self.expected_args_count = expected_args_count
        self.actual_args_count = actual_args_count
        self.message = f"Error! Expected number of CL args: {expected_args_count}, but got {actual_args_count}."
        super().__init__(self.message)


class PathDoesNotExist(Exception):
    """
    Exception raised when a path doesn't exist.
    """

    def __init__(self, path: pathlib.Path):
        self.path = path
        self.message = f"Error! Following path doesn't exist: {self.path}"
        super().__init__(self.message)


class PathIsNotFilepath(Exception):
    """
    Exception raised when a path isn't a filepath.
    """

    def __init__(self, path: pathlib.Path):
        self.path = path
        self.message = f"Error! Following path isn't a filepath: {self.path}"
        super().__init__(self.message)


class ZeroLineNumber(Exception):
    """
    Exception raised when a line number is equal to zero.
    """

    def __init__(self):
        self.message = "Error! You can't access the line №0. The number of the line must be greater than 0."
        super().__init__(self.message)


class TooLargeLineNumber(Exception):
    """
    Exception raised when a line number exceeds total number of lines.
    """

    def __init__(self, line_number: int):
        self.line_number = line_number
        self.message = (
            f"Error! You can't access the line №{self.line_number}. "
            "The number of the line exceeds total number of lines."
        )
        super().__init__(self.message)


class ZeroColumnNumber(Exception):
    """
    Exception raised when a column number is equal to zero.
    """

    def __init__(self):
        self.message = "Error! You can't access the column №0. " "The number of the column must be greater than 0."
        super().__init__(self.message)


class TooLargeColumnNumber(Exception):
    """
    Exception raised when a column number exceeds total number of columns in the line.
    """

    def __init__(self, column_number: int):
        self.column_number = column_number
        self.message = (
            f"Error! You can't access the column №{self.column_number}. "
            "The number of the column exceeds total number of columns in the line."
        )
        super().__init__(self.message)


class LineSwappedWithItself(Exception):
    """
    Exception raised when attempting to swap a line with itself.
    """

    def __init__(self):
        self.message = "Error! You can't swap the line with itself."
        super().__init__(self.message)


class UnsavedChangesExist(Exception):
    """
    Exception raised when attempting to close the editor with unsaved changes.
    """

    def __init__(self):
        self.message = "All unsaved changes will be lost. Are you sure you want to close the editor? (Y/n): "
        super().__init__(self.message)
