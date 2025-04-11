from antlr4 import *
from efi_instrumLexer import efi_instrumLexer
from efi_instrumParser import efi_instrumParser
import sys

def tree_to_dot(tree, parser):
    dot_lines = []
    dot_lines.append("digraph ParseTree {")
    dot_lines.append("  node [shape=box, fontname=\"Arial\"];")
    
    counter = 0
    # Определяем функцию-обход с использованием nonlocal-счётчика
    def visit(node, parent_id=None):
        nonlocal counter
        current_id = counter
        counter += 1
        # Получаем текст узла, экранируем кавычки
        label = node.getText().replace('"', '\\"')
        dot_lines.append(f'  node{current_id} [label="{label}"];')
        if parent_id is not None:
            dot_lines.append(f'  node{parent_id} -> node{current_id};')
        # Рекурсивно обходим всех детей
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            visit(child, current_id)
    visit(tree)
    dot_lines.append("}")
    return "\n".join(dot_lines)

def main():
    # Используем входной файл (например, 1.txt)
    input_stream = FileStream(sys.argv[1], encoding="utf-8")
    lexer = efi_instrumLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = efi_instrumParser(stream)
    tree = parser.start()
    
    dot = tree_to_dot(tree, parser)
    with open("tree.dot", "w", encoding="utf-8") as f:
        f.write(dot)
    print("DOT-файл сохранён как tree.dot")
    
if __name__ == '__main__':
    main()
