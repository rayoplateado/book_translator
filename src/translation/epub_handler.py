# src/translation/epub_handler.py

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from typing import Optional

class EPUBHandler:
    def __init__(self, universal_translator):
        self.universal_translator = universal_translator

    def process_epub(self, input_file: str, output_file: str, target_language: str, start_chapter: Optional[int] = None, end_chapter: Optional[int] = None):
        # Leer el EPUB
        book = epub.read_epub(input_file)

        # Obtener los items de tipo documento (capítulos)
        chapters = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

        # Determinar el rango de capítulos a procesar
        start = start_chapter - 1 if start_chapter else 0
        end = end_chapter if end_chapter else len(chapters)

        # Procesar solo los capítulos seleccionados
        for i, item in enumerate(chapters[start:end], start=start):
            # Extraer el contenido HTML
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text_content = soup.get_text()

            # Traducir el contenido
            translated_content = self.universal_translator.translate(text_content, target_language)

            # Imprimir la traducción en la consola
            print(f"\n--- Capítulo {i+1} traducido ---\n")
            print(translated_content)
            print("\n--- Fin del capítulo ---\n")

            # Comentado: Actualización del contenido del EPUB
            # for tag in soup.find_all(text=True):
            #     if tag.parent.name not in ['script', 'style']:
            #         tag.replace_with(translated_content)
            # item.set_content(str(soup).encode('utf-8'))

        # Comentado: Guardar el EPUB traducido
        # epub.write_epub(output_file, book)

        print("Traducción completada y mostrada en la consola.")

    def get_chapter_count(self, epub_path: str) -> int:
        book = epub.read_epub(epub_path)
        return len(list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)))
