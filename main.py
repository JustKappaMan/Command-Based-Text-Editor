import re
import sys
import copy
import pathlib


def main():
    app = InputHandler(Document())
    app.start()


class InputHandler:
    def __init__(self, document) -> None:
        self.document = document
        self.user_input = None

    def start(self):
        while True:
            user_input = input('>>> ')

            if m := re.match(r'insert(?: (\d+))?(?: (\d+))? \"(.+)\"$', self.user_input):
                match len(args := [x for x in m.groups() if x is not None]):
                    case 1:
                        self.document.insert_line(text=args[0])
                    case 2:
                        self.document.insert_line(line_number=int(args[0]), text=args[1])
                    case 3:
                        self.document.insert_line(line_number=int(args[0]), column_number=int(args[1]), text=args[2])
            elif m := re.match(r'delete (\d+)$', user_input):
                self.document.delete_line(line_number=int(m.group(1)))
            elif m := re.match(r'swap (\d+) (\d+)$', user_input):
                if len(args := [x for x in m.groups() if x is not None]) == 2:
                    self.document.swap_lines(int(args[0]), int(args[1]))
            elif user_input == 'undo':
                self.document.undo()
            elif user_input == 'clear':
                self.document.clear()
            elif user_input == 'save':
                self.document.save()
            elif user_input == 'close':
                self.document.close()
            else:
                print('Error! Unknown command.')


class Document:
    def __init__(self) -> None:
        self.path: pathlib.Path = Document.extract_path()
        self.current_content: list[str] = self.get_lines()
        self.previous_content: list[str] = copy.deepcopy(self.current_content)

    @staticmethod
    def extract_path() -> pathlib.Path:
        if len(sys.argv) != 2:
            sys.exit('Wrong number of CL arguments! Check README for details.')
        else:
            path = pathlib.Path(sys.argv[1])

        if not path.exists():
            sys.exit('You must pass an existing path as a CL argument!')
        elif not path.is_file():
            sys.exit('You must pass a filepath as a CL argument!')
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

    def insert_line(self, line_number: int = None, column_number: int = None, text: str = None) -> None:
        if text is None:
            sys.exit('Error! You must specify the text of the line you want to insert.')
        if line_number is not None and column_number is not None:
            if line_number < 1:
                sys.exit("Error! You can't insert the line at this position. "
                         'The number of the target line must be a natural number.')
            elif line_number > self.number_of_lines:
                sys.exit("Error! You can't insert the line at this position. "
                         f'The number of lines in the file: {self.number_of_lines}.')
            elif column_number < 1:
                sys.exit("Error! You can't insert the line at this position. "
                         'The number of the target column must be a natural number.')
            elif column_number > len(self.current_content[line_number - 1]):
                sys.exit("Error! You can't insert the line at this position. "
                         f'The number of characters in the target line: {len(self.current_content[line_number - 1])}.')
            else:
                self.back_up()
                line_content = self.current_content[line_number - 1]
                self.current_content[line_number - 1] = ''.join(
                    (line_content[:column_number], text, line_content[column_number:]))
        elif line_number is not None:
            if line_number < 1:
                sys.exit("Error! You can't insert the line at this position. "
                         'The number of the target line must be a natural number.')
            elif line_number > self.number_of_lines:
                sys.exit("Error! You can't insert the line at this position. "
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

    def delete_line(self, line_number: int = None) -> None:
        if line_number is None:
            sys.exit('Error! You must specify the number of the line you want to delete.')
        elif line_number < 1:
            sys.exit(f"Error! You can't delete the line №{line_number}. "
                     'The number of the target line must be a natural number.')
        elif line_number > self.number_of_lines:
            sys.exit(f"Error! You can't delete the line №{line_number}. "
                     f'The number of lines in the file: {self.number_of_lines}.')
        else:
            self.back_up()
            del self.current_content[line_number - 1]

    def swap_lines(self, line1_number: int, line2_number: int) -> None:
        if line1_number < 1:
            sys.exit(f"Error! You can't move the line №{line1_number}. "
                     'The number of the target line must be a natural number.')
        elif line1_number > self.number_of_lines:
            sys.exit(f"Error! You can't move the line №{line1_number}. "
                     f'The number of lines in the file: {self.number_of_lines}.')
        elif line2_number < 1:
            sys.exit(f"Error! You can't move the line №{line1_number}. "
                     'The number of the target line must be a natural number.')
        elif line2_number > self.number_of_lines:
            sys.exit(f"Error! You can't move the line №{line2_number}. "
                     f'The number of lines in the file: {self.number_of_lines}.')
        elif line1_number == line2_number:
            sys.exit("Error! You can't swap the line with itself.")
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
        pass


if __name__ == '__main__':
    main()
