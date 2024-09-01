# Book Translation and Typesetting Project

## Overview

This project is an automated system for translating and typesetting books. It uses the Anthropic API for translation and maintains context-awareness for character consistency across different languages. The system is designed to be book-agnostic, allowing for easy adaptation to various literary works.

## Features

- Automated translation using the Anthropic API
- Character context management for consistent translations
- EPUB parsing and RMD conversion
- PDF generation using R and LaTeX
- Command-line interface for easy use

## Project Structure

```
book_translator/
│
├── src/
│   ├── translation/
│   │   ├── __init__.py
│   │   ├── translator.py
│   │   ├── character_context.py
│   │   └── api_client.py
│   │
│   ├── formatting/
│   │   ├── __init__.py
│   │   ├── epub_parser.py
│   │   └── rmd_converter.py
│   │
│   ├── typesetting/
│   │   ├── __init__.py
│   │   ├── latex_generator.py
│   │   └── templates/
│   │       ├── book_template.tex
│   │       └── chapter_template.tex
│   │
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
│
├── scripts/
│   ├── translate_book.py
│   ├── generate_pdf.R
│   └── manage_characters.py
│
├── tests/
│   ├── test_translation.py
│   ├── test_formatting.py
│   └── test_typesetting.py
│
├── docs/
│   ├── README.md
│   ├── USAGE.md
│   └── API.md
│
├── data/
│   ├── input/
│   └── output/
│
├── ui/  # For future implementation of user interface
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt
├── setup.py
├── .gitignore
├── .env
└── characters.json
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/book-translator.git
   cd book-translator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Anthropic API key:
   Create a `.env` file in the root directory and add your API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

5. Prepare your `characters.json` file:
   Create a JSON file with character information. Use the provided `manage_characters.py` script to add or modify characters.

## Usage

### Managing Characters

To add or list characters:

```
python scripts/manage_characters.py --add --name "Character Name" --gender "Gender" --description "Description" --role "Role" --file "characters.json"
python scripts/manage_characters.py --list --file "characters.json"
```

### Translating a Book

To translate a book:

```
python scripts/translate_book.py --input input.txt --output output.txt --target-language es --characters-file characters.json
```

### Generating PDF

(Instructions for using the R script to generate PDF will be added here)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Anthropic for providing the translation API
- (Add any other acknowledgments here)
