import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=''):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(content)

def setup_project():
    # Definir la estructura del proyecto
    structure = {
        'src': {
            'translation': ['__init__.py', 'translator.py', 'character_context.py', 'api_client.py'],
            'formatting': ['__init__.py', 'epub_parser.py', 'rmd_converter.py'],
            'typesetting': {
                '__init__.py': '',
                'latex_generator.py': '',
                'templates': ['book_template.tex', 'chapter_template.tex']
            },
            'utils': ['__init__.py', 'config.py', 'logger.py']
        },
        'scripts': ['translate_book.py', 'generate_pdf.R'],
        'tests': ['test_translation.py', 'test_formatting.py', 'test_typesetting.py'],
        'docs': ['README.md', 'USAGE.md', 'API.md'],
        'data': {
            'input': ['.gitkeep'],
            'output': ['.gitkeep']
        },
        'ui': ['__init__.py', 'main.py']
    }

    # Crear la estructura de directorios y archivos
    for directory, contents in structure.items():
        if isinstance(contents, dict):
            for subdir, files in contents.items():
                subdir_path = os.path.join(directory, subdir)
                create_directory(subdir_path)
                for file in files:
                    create_file(os.path.join(subdir_path, file))
        else:
            create_directory(directory)
            for file in contents:
                create_file(os.path.join(directory, file))

    # Crear archivos en la raíz del proyecto, excluyendo .gitignore
    root_files = ['requirements.txt', 'setup.py']
    for file in root_files:
        create_file(file)

    print("Estructura del proyecto creada exitosamente.")
    print("Nota: El archivo .gitignore existente no ha sido modificado.")

if __name__ == "__main__":
    setup_project()
