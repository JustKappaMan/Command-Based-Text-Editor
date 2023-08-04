# Command Based Text Editor
![MIT License](https://img.shields.io/github/license/JustKappaMan/Command-Based-Text-Editor)
![Code style: black](https://img.shields.io/badge/code%20style-black-black)
![Coverage (87%)](https://img.shields.io/badge/coverage-87%25-brightgreen)

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
## Credits
Big thanks to:
* [JetBrains](https://www.jetbrains.com/community/opensource) for Open Source development license