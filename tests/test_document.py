from os import remove
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch

from editor.document import Document
from editor.exceptions import *


class TestDocument(TestCase):
    file_with_3_lines = Path('files', 'file_with_3_lines.txt')
    empty_file = Path('files', 'empty_file.txt')
    temporary_file = Path('files', 'tmp.txt')

    def test_read_lines_from_file(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n', 'Line #3'])

    def test_read_lines_from_empty_file(self):
        with patch('sys.argv', ['main.py', self.empty_file]):
            document: Document = Document()
            self.assertEqual(document.current_content, [])

    def test_count_lines_in_file(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            self.assertEqual(document.number_of_lines, 3)

    def test_count_lines_in_empty_file(self):
        with patch('sys.argv', ['main.py', self.empty_file]):
            document: Document = Document()
            self.assertEqual(document.number_of_lines, 0)

    def test_not_empty_file_is_empty(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            self.assertFalse(document.is_empty)

    def test_empty_file_is_empty(self):
        with patch('sys.argv', ['main.py', self.empty_file]):
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
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.insert_line('new line', 0)

    def test_zero_line_number_and_non_zero_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.insert_line('new line', 0, 1)

    def test_zero_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(ZeroColumnNumber):
                document.insert_line('new line', 1, 0)

    def test_too_large_line_number_on_insert(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.insert_line('new line', 42)

    def test_too_large_line_number_and_ok_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.insert_line('new line', 42, 1)

    def test_too_large_column_number_on_insert(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(TooLargeColumnNumber):
                document.insert_line('new line', 1, 42)

    def test_insert_line_specifying_line_number(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.insert_line(' is now longer', 1)
            self.assertEqual(document.current_content, ['Line #1 is now longer\n', 'Line #2\n', 'Line #3'])

    def test_insert_line_specifying_line_number_and_column_number(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.insert_line('This is the ', 1, 1)
            self.assertEqual(document.current_content, ['This is the Line #1\n', 'Line #2\n', 'Line #3'])

    def test_insert_line_not_specifying_anything(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.insert_line('Line #4')
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n', 'Line #3\n', 'Line #4'])

    def test_zero_line_number_on_delete(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.delete_line(0)

    def test_too_large_line_number_on_delete(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.delete_line(42)

    def test_delete_line(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.delete_line(3)
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n'])

    def test_first_zero_line_number_on_swap(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.swap_lines(0, 1)

    def test_second_zero_line_number_on_swap(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(ZeroLineNumber):
                document.swap_lines(1, 0)

    def test_too_large_line_number_on_swap_one(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.swap_lines(42, 1)

    def test_too_large_line_number_on_swap_two(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(TooLargeLineNumber):
                document.swap_lines(1, 42)

    def test_line_swapped_with_itself(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            with self.assertRaises(LineSwappedWithItself):
                document.swap_lines(1, 1)

    def test_swap_lines(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.swap_lines(1, 2)
            self.assertEqual(document.current_content, ['Line #2\n', 'Line #1\n', 'Line #3'])

    def test_swap_line_without_newline_at_the_end_and_normal_line(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.swap_lines(3, 1)
            self.assertEqual(document.current_content, ['Line #3\n', 'Line #2\n', 'Line #1\n'])

    def test_swap__normal_line_and_line_without_newline_at_the_end(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.swap_lines(1, 3)
            self.assertEqual(document.current_content, ['Line #3\n', 'Line #2\n', 'Line #1\n'])

    def test_undo(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.delete_line(3)
            document.undo()
            self.assertEqual(document.current_content, ['Line #1\n', 'Line #2\n', 'Line #3'])

    def test_clear(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.clear()
            self.assertEqual(document.current_content, [])

    def test_save(self):
        with open(self.temporary_file, 'w', encoding='utf-8') as f:
            f.write('Line #1\n')

        with patch('sys.argv', ['main.py', self.temporary_file]):
            document: Document = Document()
            document.insert_line('Line #2')
            document.save()
            document.close()

        try:
            with open(self.temporary_file, 'r', encoding='utf-8') as f:
                self.assertEqual(f.readlines(), ['Line #1\n', 'Line #2'])
        except AssertionError as TestFailure:
            raise TestFailure
        finally:
            remove(self.temporary_file)

    def test_close(self):
        # What can go wrong?
        self.assertTrue(True)

    def test_close_with_unsaved_changes(self):
        with patch('sys.argv', ['main.py', self.file_with_3_lines]):
            document: Document = Document()
            document.delete_line(3)
            with self.assertRaises(UnsavedChangesExist):
                document.close()


if __name__ == '__main__':
    main()
