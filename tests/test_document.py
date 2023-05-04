from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch

from editor.document import Document
from editor.exceptions import *


class TestDocument(TestCase):
    def test_read_lines_from_file(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n', 'Line #3'])

    def test_read_lines_from_empty_file(self):
        with patch('sys.argv', ['main.py', Path('files', 'empty_file.txt')]):
            document: Document = Document()
            self.assertEqual(document.current_content, [])

    def test_count_lines_in_file(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            self.assertEqual(document.number_of_lines, 3)

    def test_count_lines_in_empty_file(self):
        with patch('sys.argv', ['main.py', Path('files', 'empty_file.txt')]):
            document: Document = Document()
            self.assertEqual(document.number_of_lines, 0)

    def test_not_empty_file_is_empty(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            self.assertFalse(document.is_empty)

    def test_empty_file_is_empty(self):
        with patch('sys.argv', ['main.py', Path('files', 'empty_file.txt')]):
            document: Document = Document()
            self.assertTrue(document.is_empty)

    def test_wrong_number_of_command_line_args(self):
        with patch('sys.argv', ['main.py']):
            self.assertRaises(WrongNumberOfCommandLineArgs, Document)

    def test_path_does_not_exist(self):
        with patch('sys.argv', ['main.py', Path('files', 'not_existing_file.txt')]):
            self.assertRaises(PathDoesNotExist, Document)

    def test_path_is_not_filepath(self):
        with patch('sys.argv', ['main.py', Path('files')]):
            self.assertRaises(PathIsNotFilepath, Document)

    def test_zero_line_number_on_insert(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.insert_line('new line', line_number=0)

    def test_zero_line_number_and_non_zero_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.insert_line('new line', line_number=0, column_number=1)

    def test_zero_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(ZeroColumnNumber):
                document.insert_line('new line', line_number=1, column_number=0)

    def test_too_large_line_number_on_insert(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.insert_line('new line', line_number=42)

    def test_too_large_line_number_and_ok_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.insert_line('new line', line_number=42, column_number=1)

    def test_too_large_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(TooLargeColumnNumber):
                document.insert_line('new line', line_number=1, column_number=42)

    def test_insert_line_specifying_line_number(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            document.insert_line(' is now longer', line_number=1)
            self.assertEqual(document.current_content, ['Line #1 is now longer\n', 'Line #2\n', 'Line #3'])

    def test_insert_line_specifying_line_number_and_column_number(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            document.insert_line('This is the ', line_number=1, column_number=1)
            self.assertEqual(document.current_content, ['This is the Line #1\n', 'Line #2\n', 'Line #3'])

    def test_insert_line_not_specifying_anything(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            document.insert_line('Line #4')
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n', 'Line #3\n', 'Line #4'])

    def test_zero_line_number_on_delete(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.delete_line(0)

    def test_too_large_line_number_on_delete(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.delete_line(42)

    def test_delete_line(self):
        with patch('sys.argv', ['main.py', Path('files', 'file_with_3_lines.txt')]):
            document: Document = Document()
            document.delete_line(3)
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n'])


if __name__ == '__main__':
    main()
