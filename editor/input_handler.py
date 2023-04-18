import re
import sys

from editor.document import Document
from editor.exceptions import *


class InputHandler:
    def __init__(self) -> None:
        try:
            self.document: Document = Document()
        except (WrongNumberOfCommandLineArgs, PathDoesNotExist, PathIsNotFilepath) as e:
            sys.exit(e)

        self.user_input = None

    def start(self):
        while True:
            self.user_input = input('>>> ')

            try:
                if m := re.match(r'insert(?: (\d+))?(?: (\d+))? \"(.+)\"$', self.user_input):
                    match len(args := [x for x in m.groups() if x is not None]):
                        case 1:
                            self.document.insert_line(text=args[0])
                            continue
                        case 2:
                            self.document.insert_line(line_number=int(args[0]), text=args[1])
                            continue
                        case 3:
                            self.document.insert_line(line_number=int(args[0]), column_number=int(args[1]),
                                                      text=args[2])
                            continue
                elif m := re.match(r'delete (\d+)$', self.user_input):
                    self.document.delete_line(line_number=int(m.group(1)))
                    continue
                elif m := re.match(r'swap (\d+) (\d+)$', self.user_input):
                    if len(args := [x for x in m.groups() if x is not None]) == 2:
                        self.document.swap_lines(int(args[0]), int(args[1]))
                        continue
            except (ZeroLineNumber, TooLargeLineNumber,
                    ZeroColumnNumber, TooLargeColumnNumber,
                    LineSwappedWithItself) as e:
                print(f'{e}')
                continue

            if self.user_input == 'undo':
                self.document.undo()
            elif self.user_input == 'clear':
                self.document.clear()
            elif self.user_input == 'save':
                self.document.save()
            elif self.user_input == 'close':
                try:
                    self.document.close()
                except UnsavedChangesExist as e:
                    if input(f'{e}').lower() == 'y':
                        sys.exit(0)
                    else:
                        continue
                else:
                    sys.exit(0)
            else:
                print('Error! Unknown command.')
