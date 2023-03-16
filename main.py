import sys
import copy
import pathlib


def main():
    pass


class Document:
    def __init__(self):
        self.path = Document.get_path()
        self.current_content = self.get_lines()
        self.previous_content = copy.deepcopy(self.current_content)

    @staticmethod
    def get_path():
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

    def get_lines(self):
        with self.path.open('r') as file:
            return file.readlines()

    def back_up(self):
        self.previous_content = copy.deepcopy(self.current_content)

    def insert_line(self, text, row=None, column=None):
        self.back_up()

        if row and column:
            if 1 <= row <= len(self.current_content):
                if 1 <= column < len(self.current_content[row - 1]):
                    row_content = self.current_content[row - 1]
                    self.current_content[row - 1] = ''.join((row_content[:column], text, row_content[column:]))
        elif row:
            if 1 <= row <= len(self.current_content):
                self.current_content[row - 1] = self.current_content[row - 1].removesuffix('\n')
                self.current_content[row - 1] += f'{text}\n'
        else:
            if not self.current_content[-1].endswith('\n'):
                self.current_content[-1] += '\n'
            self.current_content.append(text)

    def delete_line(self, row=None):
        pass

    def swap_lines(self, row1, row2):
        pass

    def clear(self):
        self.back_up()
        self.current_content.clear()

    def undo(self):
        self.back_up()
        self.current_content = copy.deepcopy(self.previous_content)

    def save(self):
        with self.path.open('w+') as file:
            file.writelines(self.current_content)

    def close(self):
        pass


if __name__ == '__main__':
    main()
