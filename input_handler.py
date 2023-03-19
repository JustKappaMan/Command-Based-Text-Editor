import re

from document import Document


class InputHandler:
    def __init__(self, document: Document) -> None:
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
