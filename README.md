# 📚 BookBot

<div align="center">

A simple command-line text analysis tool that reads books and generates reports about their content.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## Results

- **Word Count Analysis** — Quickly count the total number of words in any text file
- **Letter Frequency** — Analyze and rank character occurrences throughout the document
- **No Dependencies** — Pure Python implementation with zero external dependencies

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:

```bash
git clone https://github.com/KleitonBarone/bookbot.git
cd bookbot
```

2. Add a book to analyze:

```bash
mkdir books
# Add your .txt file to the books directory
```

### Usage

Run the analysis on your book:

```bash
python main.py
```

> **Note:** By default, the program analyzes `books/frankenstein.txt`. You can modify the `path_to_file` variable in `main.py` to analyze different files.

## 📊 Sample Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The e character was found 46043 times
The t character was found 30365 times
The a character was found 26743 times
The o character was found 25225 times
The i character was found 24613 times
...
--- End report ---
```

## 🏗️ Project Structure

```
bookbot/
├── main.py          # Main application logic
├── books/           # Directory for text files to analyze
├── LICENSE          # MIT License
└── README.md        # This file
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
