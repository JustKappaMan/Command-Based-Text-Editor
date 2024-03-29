import sys
import pathlib

from .exceptions import *


class Document:
    def __init__(self):
        self.path: pathlib.Path = Document.extract_path()
        self.current_content: list[str] = self.get_lines()
        self.previous_content: list[str] = self.current_content.copy()

    @staticmethod
    def extract_path() -> pathlib.Path:
        if len(sys.argv) != 2:
            raise WrongNumberOfCommandLineArgs(2, len(sys.argv))
        else:
            path = pathlib.Path(sys.argv[1])

        if not path.exists():
            raise PathDoesNotExist(path)
        if not path.is_file():
            raise PathIsNotFilepath(path)
        else:
            return path

    def get_lines(self) -> list[str]:
        with self.path.open("r", encoding="utf-8") as file:
            return file.readlines()

    def back_up(self) -> None:
        self.previous_content = self.current_content.copy()

    @property
    def number_of_lines(self) -> int:
        return len(self.current_content)

    @property
    def is_empty(self) -> bool:
        return self.current_content == []

    def insert_line(self, text: str, line_number: int | None = None, column_number: int | None = None) -> None:
        if line_number is not None and column_number is not None:
            if self.is_empty and line_number == 1 and column_number == 1:
                self.back_up()
                self.current_content.append(f"{text}\n")
            elif line_number == 0:
                raise ZeroLineNumber
            elif line_number > self.number_of_lines:
                raise TooLargeLineNumber(line_number)
            elif column_number == 0:
                raise ZeroColumnNumber
            elif column_number > len(self.current_content[line_number - 1]):
                raise TooLargeColumnNumber(column_number)
            else:
                self.back_up()
                line_content = self.current_content[line_number - 1]
                self.current_content[line_number - 1] = "".join(
                    (line_content[: column_number - 1], text, line_content[column_number - 1 :])
                )
        elif line_number is not None:
            if self.is_empty and line_number == 1:
                self.back_up()
                self.current_content.append(f"{text}\n")
            elif line_number == 0:
                raise ZeroLineNumber
            elif line_number > self.number_of_lines:
                raise TooLargeLineNumber(line_number)
            else:
                self.back_up()
                self.current_content[line_number - 1] = self.current_content[line_number - 1].removesuffix("\n")
                self.current_content[line_number - 1] += f"{text}\n"
        else:
            self.back_up()
            if not self.is_empty and not self.current_content[-1].endswith("\n"):
                self.current_content[-1] += "\n"
            self.current_content.append(text)

    def delete_line(self, line_number: int) -> None:
        if line_number == 0:
            raise ZeroLineNumber
        elif line_number > self.number_of_lines:
            raise TooLargeLineNumber(line_number)
        else:
            self.back_up()
            del self.current_content[line_number - 1]

    def swap_lines(self, line1_number: int, line2_number: int) -> None:
        if line1_number == 0 or line2_number == 0:
            raise ZeroLineNumber
        elif line1_number > self.number_of_lines:
            raise TooLargeLineNumber(line1_number)
        elif line2_number > self.number_of_lines:
            raise TooLargeLineNumber(line2_number)
        elif line1_number == line2_number:
            raise LineSwappedWithItself
        else:
            self.back_up()

            if not self.current_content[line1_number - 1].endswith("\n"):
                self.current_content[line1_number - 1] += "\n"
            if not self.current_content[line2_number - 1].endswith("\n"):
                self.current_content[line2_number - 1] += "\n"

            self.current_content[line1_number - 1], self.current_content[line2_number - 1] = (
                self.current_content[line2_number - 1],
                self.current_content[line1_number - 1],
            )

    def undo(self) -> None:
        self.current_content = self.previous_content.copy()

    def clear(self) -> None:
        self.back_up()
        self.current_content.clear()

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as file:
            file.writelines(self.current_content)

    def close(self) -> None:
        with self.path.open("r", encoding="utf-8") as file:
            if self.current_content != file.readlines():
                raise UnsavedChangesExist
