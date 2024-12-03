import sys
from antlr4 import *
from UEFIParser import UEFIParser
from UEFILexer import UEFILexer
from graphviz import Digraph

def add_nodes_edges(graph, parent, child):
    """ Добавляет узлы и ребра в граф """
    graph.node(str(child), str(child))
    graph.edge(str(parent), str(child))

def build_graph(tree, graph=None, parent=None, seen=None):
    """ Рекурсивно строит граф из дерева разбора, избегая дублирования узлов """
    if graph is None:
        graph = Digraph()
        parent = 'root'
        graph.node(parent, 'root')
        seen = {}

    # Получаем текстовое представление узла
    node_text = tree.getText() if tree.getText() else str(tree)

    # Проверяем, был ли узел уже добавлен
    if node_text not in seen:
        # Создаем уникальный идентификатор узла
        node_id = f"{id(tree)}"  # Используем id для уникальности
        graph.node(node_id, node_text)  # Добавляем текст узла
        seen[node_text] = node_id  # Запоминаем, что этот текст уже был добавлен

        if parent is not None:
            graph.edge(parent, node_id)  # Соединяем с родителем

    else:
        node_id = seen[node_text]  # Если узел уже был добавлен, используем его id

    # Обработка детей узла
    if hasattr(tree, 'children') and tree.children:
        for child in tree.children:
            build_graph(child, graph, node_id, seen)

    return graph

def main():
    # Встраиваемый код, который вы хотите разобрать
    code = """
    #include "efi.h"

    EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
        (void)ImageHandle;
        
        SystemTable->ConOut->SetAttribute(SystemTable->ConOut, 
                EFI_TEXT_ATTR(EFI_YELLOW,EFI_GREEN)); 

        SystemTable->ConOut->ClearScreen(SystemTable->ConOut);
        
        SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Hello, World!\r\n\r\n");
        
        SystemTable->ConOut->SetAttribute(SystemTable->ConOut, 
                EFI_TEXT_ATTR(EFI_RED,EFI_BLACK));
    
        SystemTable->ConOut->OutputString(SystemTable->ConOut, 
                u"Press any key to shutdown..."); 

    
        EFI_INPUT_KEY key;
        while (SystemTable->ConIn->ReadKeyStroke(SystemTable->ConIn, &key) != EFI_SUCCESS)
            ;
        
    
        SystemTable->RuntimeServices->ResetSystem(EfiResetShutdown, EFI_SUCCESS, 0, NULL);

    
        return EFI_SUCCESS;
    }
    """

    # Используем InputStream для передачи кода
    input_stream = InputStream(code)  # Чтение кода из строки
    lexer = UEFILexer(input_stream)    # Создание лексера
    stream = CommonTokenStream(lexer)  # Создание токенов
    parser = UEFIParser(stream)         # Создание парсера
    tree = parser.compilationUnit()     # Раз
    
    # Вывод дерева разбора
    print(tree.toStringTree(recog=parser))

    # Создание графа
    graph = build_graph(tree)
    graph.render('parse_tree', format='png', cleanup=True)  # Сохранение графа в файл

if __name__ == '__main__':
    main()