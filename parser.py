import sys
import re
from antlr4 import *
from UEFIParser import UEFIParser
from UEFILexer import UEFILexer
from graphviz import Digraph
import matplotlib.pyplot as plt
import numpy as np


class LinearSegmentFinder:
    def __init__(self): 
        self.linear_segments = []  # Список для хранения линейных участков
        self.current_segment = []   # Текущий линейный участок
        self.statements = []        # Список для хранения узлов
        self.adjacency_matrix = []  # Матрица смежности
        self.variable_declarations = {'key': 1}  # Словарь для хранения объявленных переменных
        self.header_segments = []    # Список для хранения заголовков
        self.statm = set() # Список для хранения операторов

    def print_slices(self):
        # print("Слайды класса LinearSegmentFinder:")
        # print("-" * 40)
        # print("1. linear_segments: ", self.linear_segments)
        # print("   (Список для хранения линейных участков)")
        print("3. statements: ", self.statm)
        # print("   (Список для хранения операторов)")
        # print("5. variable_declarations: ", self.variable_declarations)
        # print("   (Словарь для хранения объявленных переменных)")
        # print("-" * 40)
    
    def add_statement(self, statement, line, char_position):
        # Разбиваем оператор на отдельные части
        # statements = self.split_statements(statement)
        # for stmt in statements:
            # Добавляем узел в список узлов
            self.statements.append(statement)  
            # print(f"Добавлено в список узлов: {statement} (строка: {line}, позиция: {char_position})")  # Вывод в консоль

            # Добавляем узел в текущий линейный участок
            self.current_segment.append((statement, line, char_position))
    
    def add_stat(self, statem, line, char_position):
        statm = self.split_statements(statem)
        for stmt in statm:
            # Фильтруем ключевые слова
            if stmt not in {'NULL', '0'}:  # Добавьте другие ключевые слова, если необходимо
                self.statm.add(stmt)  # Используем множество для уникальности
                # print(f"Добавлено в список операторов: {stmt} (строка: {line}, позиция: {char_position})")
    
    def split_statements(self, statement):
        unique_parts = set()  # Используем множество для уникальности
        pattern = r'(\w+|\w+\s*->\s*\w+|\w+\s*\(.*?\))'
        statem = re.sub(r'u?\'[^\']*\'|u?"[^"]*"', '', statement)
        
        # Игнорируем строки с директивами #include
        if '#include' in statem:
            return []  # Возвращаем пустой список, если есть директива #include
        
        matches = re.findall(pattern, statem)
        
        for match in matches:
            cleaned_match = re.sub(r'[()]', '', match).strip()
            
            # Удаляем 'key' из 'EFI_INPUT_KEYkey'
            if cleaned_match.startswith('EFI_INPUT_KEY'):
                cleaned_match = cleaned_match.replace('key', '', 1)  # Удаляем только первое вхождение 'key'
            
            # Фильтруем ключевые слова
            if cleaned_match not in {'NULL', '0'}:  # Добавьте другие ключевые слова, если необходимо
                unique_parts.add(cleaned_match)
        
        return list(unique_parts)  # Преобразуем множество обратно в список

    def finalize_segment(self):
        if self.current_segment:
            if self.header_segments:  # Если это заголовок
                # print("Завершен линейный участок заголовка:")
                # for idx, (stmt, line, char_pos) in enumerate(self.header_segments):
                #     print(f"{idx + 1} узел: {stmt} (строка: {line}, позиция: {char_pos})")
                self.header_segments = []  # Сброс заголовков
            # else:  # Если это линейный участок функции
                # print("Завершен линейный участок функции:")
                # for idx, (stmt, line, char_pos) in enumerate(self.current_segment):
                #     print(f"{idx + 1}: {stmt} (строка: {line}, позиция: {char_pos})")
            self.linear_segments.append(self.current_segment)
            self.current_segment = []
            
    def visit(self, tree):
        if isinstance(tree, UEFIParser.VariableDeclarationContext):
            # Обработка объявления переменной
            line = tree.start.line
            declaration = tree.getText()
            var_name = self.extract_variable_name(declaration)
            if var_name:
                self.variable_declarations[var_name] = line  # Сохраняем имя переменной и строку
                # print(f"Объявлена переменная: {var_name} (строка: {line})")  # Вывод в консоль
        elif isinstance(tree, UEFIParser.StatementContext):
            line = tree.start.line
            char_position = tree.start.start
            self.add_statement(tree.getText(), line, char_position)
            self.add_stat(tree.getText(), line, char_position)
        elif isinstance(tree, UEFIParser.WhileStatementContext):
            self.finalize_segment()  # Завершаем текущий линейный участок
            # print(f"Обработка цикла while: {tree.getText()} (строка: {tree.start.line}, позиция: {tree.start.start})")  # Вывод в консоль
            for stmt in tree.block().statement():
                self.visit(stmt)
            self.finalize_segment()  # Завершаем линейный участок цикла
        elif isinstance(tree, UEFIParser.FunctionDeclarationContext):
            self.finalize_segment()  # Завершаем текущий линейный участок
            # print(f"Обработка функции: {tree.getText()} (строка: {tree.start.line}, позиция: {tree.start.start})")  # Вывод в консоль
            for stmt in tree.block().statement():
                self.visit(stmt)
            self.finalize_segment()  # Завершаем линейный участок функции
        elif hasattr(tree, 'children'):
            for child in tree.children:
                self.visit(child)
    
    def extract_variable_name(self, declaration):
        # Извлечение имени переменной из строки объявления
        # Например, для "EFI_INPUT_KEY key;" нужно получить "key"
        match = re.search(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*;', declaration)
        return match.group(1) if match else None
    
    def find_dependencies(self):
        dependencies = {}
        for statement in self.statements:
            parts = statement.split('->')
            for part in parts:
                part = part.strip()
                if part in self.statm:
                    if part not in dependencies:
                        dependencies[part] = []
                    dependencies[part].append(statement)
        # print(dependencies)
        return dependencies
            
    def build_adjacency_matrix(self):
        dependencies = self.find_dependencies()
        operators = list(self.statm)
        size = len(operators)
        
        # Инициализация матрицы смежности
        self.adjacency_matrix = [[0] * size for _ in range(size)]
        
        # Заполнение матрицы смежности на основе зависимостей
        for i, operator in enumerate(operators):
            if operator in dependencies:
                for dependent_statement in dependencies[operator]:
                    for j, dep_operator in enumerate(operators):
                        if dep_operator in dependent_statement:
                            self.adjacency_matrix[i][j] = 1  # Устанавливаем связь

        # Вывод матрицы смежности для проверки
        print("Матрица смежности:")
        for row in self.adjacency_matrix:
            print(row)
                    
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

def build_path_matrix(adjacency_matrix):
    n = len(adjacency_matrix)
    path_matrix = [[0] * n for _ in range(n)]

    # Инициализация матрицы путей на основе матрицы смежности
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                path_matrix[i][j] = 1  # Прямой путь существует
        path_matrix[i][i] = 1  # Путь к самому себе

    # Используем алгоритм Флойда-Уоршелла для нахождения всех путей
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if path_matrix[i][k] and path_matrix[k][j]:
                    path_matrix[i][j] = 1  # Путь существует через k

    return path_matrix


def plot_adjacency_matrix(matrix):
    matrix = np.array(matrix, dtype=np.float32)
    plt.figure(figsize=(10, 8))
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title('Матрица смежности')
    plt.xlabel('Операторы')
    plt.ylabel('Операторы')
    plt.xticks(ticks=np.arange(len(matrix)), labels=np.arange(len(matrix)))
    plt.yticks(ticks=np.arange(len(matrix)), labels=np.arange(len(matrix)))
    plt.show()

def plot_matrices(adjacency_matrix, path_matrix, statements):
    # Преобразуем входные данные в массивы NumPy, если они списки
    adjacency_matrix = np.array(adjacency_matrix)
    path_matrix = np.array(path_matrix)

    # Извлекаем уникальные операторы для меток
    operators = list(statements)  # Используем переданные операторы как метки

    fig, axs = plt.subplots(1, 2, figsize=(10, 10))

    # Отображение матрицы смежности
    cax1 = axs[0].imshow(adjacency_matrix, cmap='hot', interpolation='nearest')
    axs[0].set_title('Матрица смежности')
    axs[0].set_xticks(ticks=np.arange(len(adjacency_matrix)))
    axs[0].set_yticks(ticks=np.arange(len(adjacency_matrix)))
    axs[0].set_xticklabels(operators, rotation=45, ha='right')  # Используем названия операторов
    axs[0].set_yticklabels(operators)

    # Добавляем текстовые метки (0 и 1) в матрицу смежности
    for i in range(adjacency_matrix.shape[0]):
        for j in range(adjacency_matrix.shape[1]):
            axs[0].text(j, i, int(adjacency_matrix[i, j]), ha='center', va='center', color='green')

    # Отображение матрицы путей
    cax2 = axs[1].imshow(path_matrix, cmap='hot', interpolation='nearest')
    axs[1].set_title('Матрица путей')
    axs[1].set_xticks(ticks=np.arange(len(path_matrix)))
    axs[1].set_yticks(ticks=np.arange(len(path_matrix)))
    axs[1].set_xticklabels(operators, rotation=45, ha='right')  # Используем названия операторов
    axs[1].set_yticklabels(operators)

    # Добавляем текстовые метки (0 и 1) в матрицу путей
    for i in range(path_matrix.shape[0]):
        for j in range(path_matrix.shape[1]):
            axs[1].text(j, i, int(path_matrix[i, j]), ha='center', va='center', color='blue')

    plt.tight_layout()
    plt.show()
    
def main():
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

    input_stream = InputStream(code)
    lexer = UEFILexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = UEFIParser(stream)
    tree = parser.compilationUnit()

    # Создаем экземпляр LinearSegmentFinder и обрабатываем дерево
    finder = LinearSegmentFinder()
    finder.visit(tree)

    print("\nВсе найденные линейные участки:")
    for i, segment in enumerate(finder.linear_segments, start=1):
        print(f"Линейный участок {i}:")
        node_counter = 1
        for line, line_num, char_pos in segment:
            print(f"{node_counter}.Узел:  {line} (строка: {line_num}, позиция: {char_pos})")
            node_counter += 1
    
            
    # Пример вызова метода для построения матрицы смежности
    finder.build_adjacency_matrix()
    finder.print_slices()
    # print("Матрица смежности:")
    # for row in finder.adjacency_matrix:
    # plot_adjacency_matrix(finder.adjacency_matrix)
    
    path_matrix = build_path_matrix(finder.adjacency_matrix)
    # plot_adjacency_matrix(path_matrix)
    # print("Матрица путей:")
    # for row in path_matrix:
    #     print(row)
    plot_matrices(finder.adjacency_matrix, path_matrix, finder.statm)
    
    
if __name__ == '__main__':
    main()