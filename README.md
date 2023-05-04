# Command Based Text Editor
![MIT License](https://img.shields.io/github/license/JustKappaMan/Command-Based-Text-Editor)
![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)
![Coverage (65%)](https://img.shields.io/badge/coverage-65%25-orange)

Edit text files with CLI using a set of commands.
## Usage
* Open the file you want to edit: `python` `main.py` `file.txt`
* Use the following set of commands:
  * `insert` `"text"` — appends the text to the end of the file
  * `insert` `line_number` `"text"` — appends the text to the end of the line
  * `insert` `line_number` `column_number` `"text"` — inserts the text at given position
  * `delete` `line_number` — deletes the line
  * `swap` `line1_number` `line2_number` — swaps the lines
  * `undo` — undoes the last command
  * `clear` — clears the file
  * `save` — saves the file
  * `close` — closes the editor
## License
This project is licensed under the MIT License.