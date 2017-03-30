# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import text.generator
    import text.editor
    import sys

    piece_of_text = text.generator.get_text()
    print(text.editor.get_printable_sentence(text.editor.get_ss_sentence(piece_of_text)).encode().decode(sys.stdout.encoding))