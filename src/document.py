import sys
import copy
import pathlib

from exceptions import *


class Document:
    def __init__(self) -> None:
        self.path: pathlib.Path = Document.extract_path()
        self.current_content: list[str] = self.get_lines()
        self.previous_content: list[str] = copy.deepcopy(self.current_content)

    @staticmethod
    def extract_path() -> pathlib.Path:
        if len(sys.argv) != 2:
            raise WrongNumberOfCommandLineArgs(2, len(sys.argv))
        else:
            path = pathlib.Path(sys.argv[1])

        if not path.exists():
            raise PathDoesNotExist('Error! You must pass an existing path as a CL argument.')
        elif not path.is_file():
            raise PathIsNotFilepath('Error! You must pass a filepath as a CL argument.')
        else:
            return path

    def get_lines(self) -> list[str]:
        with self.path.open('r') as file:
            return file.readlines()

    def back_up(self) -> None:
        self.previous_content = copy.deepcopy(self.current_content)

    @property
    def number_of_lines(self) -> int:
        return len(self.current_content)

    def insert_line(self, text: str, line_number: int = None, column_number: int = None) -> None:
        if line_number is not None and column_number is not None:
            if line_number == 0:
                raise ZeroLineNumber("Error! You can't insert the line at this position. "
                                     'The number of the target line must be a natural number.')
            elif line_number > self.number_of_lines:
                raise TooLargeLineNumber("Error! You can't insert the line at this position. "
                                         f'The number of lines in the file: {self.number_of_lines}.')
            elif column_number == 0:
                raise ZeroColumnNumber("Error! You can't insert the line at this position. "
                                       'The number of the target column must be a natural number.')
            elif column_number > len(self.current_content[line_number - 1]):
                raise TooLargeColumnNumber("Error! You can't insert the line at this position. "
                                           'The number of characters in the target line: '
                                           f'{len(self.current_content[line_number - 1])}.')
            else:
                self.back_up()
                line_content = self.current_content[line_number - 1]
                self.current_content[line_number - 1] = ''.join(
                    (line_content[:column_number - 1], text, line_content[column_number - 1:]))
        elif line_number is not None:
            if line_number == 0:
                raise ZeroLineNumber("Error! You can't insert the line at this position. "
                                     'The number of the target line must be a natural number.')
            elif line_number > self.number_of_lines:
                raise TooLargeLineNumber("Error! You can't insert the line at this position. "
                                         f'The number of lines in the file: {self.number_of_lines}.')
            else:
                self.back_up()
                self.current_content[line_number - 1] = self.current_content[line_number - 1].removesuffix('\n')
                self.current_content[line_number - 1] += f'{text}\n'
        else:
            self.back_up()
            if not self.current_content[-1].endswith('\n'):
                self.current_content[-1] += '\n'
            self.current_content.append(text)

    def delete_line(self, line_number: int) -> None:
        if line_number == 0:
            raise ZeroLineNumber(f"Error! You can't delete the line №{line_number}. "
                                 'The number of the target line must be a natural number.')
        elif line_number > self.number_of_lines:
            raise TooLargeLineNumber(f"Error! You can't delete the line №{line_number}. "
                                     f'The number of lines in the file: {self.number_of_lines}.')
        else:
            self.back_up()
            del self.current_content[line_number - 1]

    def swap_lines(self, line1_number: int, line2_number: int) -> None:
        if line1_number == 0:
            raise ZeroLineNumber(f"Error! You can't move the line №{line1_number}. "
                                 'The number of the target line must be a natural number.')
        elif line1_number > self.number_of_lines:
            raise TooLargeLineNumber(f"Error! You can't move the line №{line1_number}. "
                                     f'The number of lines in the file: {self.number_of_lines}.')
        elif line2_number == 0:
            raise ZeroLineNumber(f"Error! You can't move the line №{line2_number}. "
                                 'The number of the target line must be a natural number.')
        elif line2_number > self.number_of_lines:
            raise TooLargeLineNumber(f"Error! You can't move the line №{line2_number}. "
                                     f'The number of lines in the file: {self.number_of_lines}.')
        elif line1_number == line2_number:
            raise LineSwappedWithItself("Error! You can't swap the line with itself.")
        else:
            self.back_up()

            if not self.current_content[line1_number - 1].endswith('\n'):
                self.current_content[line1_number - 1] += '\n'
            if not self.current_content[line2_number - 1].endswith('\n'):
                self.current_content[line2_number - 1] += '\n'

            self.current_content[line1_number - 1], self.current_content[line2_number - 1] = \
                self.current_content[line2_number - 1], self.current_content[line1_number - 1]

    def undo(self) -> None:
        self.current_content = copy.deepcopy(self.previous_content)

    def clear(self) -> None:
        self.back_up()
        self.current_content.clear()

    def save(self) -> None:
        with self.path.open('w+') as file:
            file.writelines(self.current_content)

    def close(self) -> None:
        with self.path.open('r') as file:
            if self.current_content != file.readlines():
                raise UnsavedChangesExist('All unsaved changes will be lost. '
                                          'Are you sure you want to close the editor? '
                                          '(Y/n): ')
