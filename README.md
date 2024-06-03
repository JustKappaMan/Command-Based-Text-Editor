# Command Based Text Editor
![MIT License](https://img.shields.io/github/license/JustKappaMan/Command-Based-Text-Editor)
![Code style: black](https://img.shields.io/badge/code%20style-black-black)
![Coverage (87%)](https://img.shields.io/badge/coverage-87%25-brightgreen)

Edit text files with CLI using a set of commands.

## Usage
* Open the file you want to edit: `python3` `main.py` `file.txt`
* Use the following set of commands:
  * `insert` `"text"` — append the text to the end of the file
  * `insert` `line_number` `"text"` — append the text to the end of the line
  * `insert` `line_number` `column_number` `"text"` — insert the text at the given position
  * `delete` `line_number` — delete the line
  * `swap` `line1_number` `line2_number` — swap the lines
  * `undo` — undo the last command
  * `clear` — clear the file
  * `save` — save the file
  * `close` — close the editor

## License
This project is licensed under the MIT License.
