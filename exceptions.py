class WrongNumberOfCommandLineArgs(Exception):
    pass


class PathDoesNotExist(Exception):
    pass


class PathIsNotFilepath(Exception):
    pass


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
