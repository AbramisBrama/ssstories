# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import text.generator
    import sys

    print(text.generator.get_text().encode().decode(sys.stdout.encoding))