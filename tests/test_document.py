from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch

from editor.document import Document


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


if __name__ == '__main__':
    main()
