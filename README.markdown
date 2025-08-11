# Word Generator

A simple Python application built with Tkinter to generate random words (12 or 24) from a `words.txt` file and copy them to the clipboard. Made with ❤️ by Ehsan.

## Features
- Select 12 or 24 random words from a provided `words.txt` file.
- Display generated words in a text area.
- Copy the generated words to the clipboard with a single click.
- Cross-platform clipboard support (Windows, macOS, Linux).

## Requirements
- Python 3.6+
- Tkinter (included with standard Python installation)
- For Linux: Install `xclip` for clipboard functionality (`sudo apt-get install xclip`)
- A `words.txt` file containing one word per line

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/3hsan1njast/word-generator.git
   cd word-generator
   ```
2. Ensure `words.txt` is in the same directory as `word_generator.py`.

## Usage
1. Run the script (or simply open the exe file):
   ```bash
   python word_generator.py
   ```
2. Select 12 or 24 words from the dropdown menu.
3. Click "Generate" to create random words.
4. Click "Copy to Clipboard" to copy the words.
5. Paste the words wherever you need them!

## Notes
- Ensure `words.txt` exists in the project directory, or the program will display an error.
- On Linux, `xclip` must be installed for clipboard functionality.
- The generated `.exe` (if created with PyInstaller) requires `words.txt` in the same directory.
