import sys
import re
from antlr4 import *
from UEFIParser import UEFIParser
from UEFILexer import UEFILexer
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from graphviz import Digraph


class CFGBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.current_function = None
        self.last_statement = None  # Запоминаем последний оператор для связности
        self.linear_segments = []  # Линейные участки кода
        self.current_segment = []  # Текущий линейный участок
        self.statements = []  # Все операторы в коде

    def add_node(self, node_label, line, position):
        """Добавляет узел в граф, если его нет"""
        if node_label not in self.graph:
            self.graph.add_node(node_label)
            self.statements.append((node_label, line, position))  # Запоминаем узел
            self.current_segment.append((node_label, line, position))  # Добавляем в текущий участок

    def add_edge(self, from_node, to_node):
        """Добавляет направленное ребро между узлами"""
        self.graph.add_edge(from_node, to_node)

    def finalize_segment(self):
        """Сохраняет текущий линейный участок"""
        if self.current_segment:
            self.linear_segments.append(self.current_segment)
            self.current_segment = []

    def visit(self, tree):
        """Рекурсивный обход AST"""

        if isinstance(tree, UEFIParser.FunctionDeclarationContext):
            function_name = tree.getText().split('(')[0]
            self.current_function = function_name
            self.add_node(function_name, tree.start.line, tree.start.start)
            self.finalize_segment()  # Отделяем объявление функции
            self.last_statement = function_name  

            for stmt in tree.block().statement():
                self.visit(stmt)

        elif isinstance(tree, UEFIParser.StatementContext):
            statement_text = tree.getText().strip()

            # 🔴 Фильтрация `#include`, чтобы он не попадал в линейные участки
            if statement_text.startswith("#include"):
                return  # Пропускаем эту строку!

            # ✅ Исключаем объявления переменных из новых блоков
            if "EFI_INPUT_KEY" in statement_text:
                return  # Не добавляем это как отдельный участок

            # ✅ Группируем `EFI_INPUT_KEY key;` с `while`
            if "while" in statement_text:
                self.finalize_segment()

            self.add_node(statement_text, tree.start.line, tree.start.start)
            if self.last_statement:
                self.add_edge(self.last_statement, statement_text)
            self.last_statement = statement_text

        elif isinstance(tree, UEFIParser.WhileStatementContext):
            condition = tree.expression().getText()
            self.finalize_segment()  # Разделяем блок перед циклом
            self.add_node(f"while ({condition})", tree.start.line, tree.start.start)

            if self.last_statement:
                self.add_edge(self.last_statement, f"while ({condition})")

            loop_start = f"while ({condition})"
            self.last_statement = loop_start
            self.current_segment.append((loop_start, tree.start.line, tree.start.start))

            for stmt in tree.block().statement():
                self.visit(stmt)

            self.add_edge(self.last_statement, loop_start)  # Создаем зацикливание
            self.finalize_segment()

        elif hasattr(tree, 'children'):
            for child in tree.children:
                self.visit(child)

        self.finalize_segment()

    def build_adjacency_matrix(self):
        """Создает матрицу смежности"""
        nodes = list(self.graph.nodes)
        size = len(nodes)
        matrix = np.zeros((size, size), dtype=int)

        for i, from_node in enumerate(nodes):
            for j, to_node in enumerate(nodes):
                if self.graph.has_edge(from_node, to_node):
                    matrix[i][j] = 1

        return nodes, matrix

    def build_path_matrix(self, adjacency_matrix):
        """Создает матрицу путей (достижимость)"""
        size = len(adjacency_matrix)
        path_matrix = np.array(adjacency_matrix, dtype=int)

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if path_matrix[i, k] and path_matrix[k, j]:
                        path_matrix[i, j] = 1

        return path_matrix

    def visualize_cfg(self):
        """Рисует CFG с помощью networkx"""
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
        plt.title("Control Flow Graph (CFG)")   
        plt.show()

    def export_to_dot(self, filename="cfg.dot"):
        """Экспортирует CFG в DOT-формат для использования в Graphviz"""
        dot = Digraph()

        for node in self.graph.nodes:
            dot.node(node)

        for edge in self.graph.edges:
            dot.edge(edge[0], edge[1])

        dot.render(filename, format='png', cleanup=True)
        print(f"CFG сохранен как {filename}.png")

    def print_linear_segments(self):
        """Выводит линейные участки кода"""
        print("\nЛинейные участки кода:")
        for i, segment in enumerate(self.linear_segments, start=1):
            print(f"\nЛинейный участок {i}:")
            for j, (statement, line, position) in enumerate(segment, start=1):
                print(f"{j}. Узел: {statement} (строка: {line}, позиция: {position})")

    def display_matrices(self):
        """Выводит матрицу смежности и матрицу путей"""
        nodes, adjacency_matrix = self.build_adjacency_matrix()
        path_matrix = self.build_path_matrix(adjacency_matrix)

        print("\nМатрица смежности:")
        print(adjacency_matrix)

        print("\nМатрица путей:")
        print(path_matrix)

        self.plot_matrices(adjacency_matrix, path_matrix, nodes)

    def plot_matrices(self, adjacency_matrix, path_matrix, labels):
        """Отображает матрицу смежности и матрицу путей с числами (0 и 1) с увеличенным расстоянием между матрицами"""
        fig, axs = plt.subplots(1, 2, figsize=(14, 7))  # Увеличен размер графика
        fig.subplots_adjust(wspace=1.0)  # Увеличено расстояние между матрицами

        # Отображение матрицы смежности
        cax1 = axs[0].imshow(adjacency_matrix, cmap='Blues', interpolation='nearest')
        axs[0].set_title("Матрица смежности", fontsize=14)
        axs[0].set_xticks(range(len(labels)))
        axs[0].set_yticks(range(len(labels)))
        axs[0].set_xticklabels(labels, rotation=45, ha="right", fontsize=10)
        axs[0].set_yticklabels(labels, fontsize=10)

        # Добавление чисел в матрицу
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix[i])):
                axs[0].text(j, i, str(adjacency_matrix[i][j]), ha='center', va='center', color='black', fontsize=12)

        # Отображение матрицы путей
        cax2 = axs[1].imshow(path_matrix, cmap='Oranges', interpolation='nearest')
        axs[1].set_title("Матрица путей", fontsize=14)
        axs[1].set_xticks(range(len(labels)))
        axs[1].set_yticks(range(len(labels)))
        axs[1].set_xticklabels(labels, rotation=45, ha="right", fontsize=10)
        axs[1].set_yticklabels(labels, fontsize=10)

        # Добавление чисел в матрицу
        for i in range(len(path_matrix)):
            for j in range(len(path_matrix[i])):
                axs[1].text(j, i, str(path_matrix[i][j]), ha='center', va='center', color='black', fontsize=12)

        plt.tight_layout()
        plt.show()




def main():
    code = """
    #include "efi.h"

    EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
        (void)ImageHandle;

        SystemTable->ConOut->SetAttribute(SystemTable->ConOut, EFI_TEXT_ATTR(EFI_YELLOW,EFI_GREEN)); 
        SystemTable->ConOut->ClearScreen(SystemTable->ConOut);
        SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Hello, World!\r\n\r\n");
        SystemTable->ConOut->SetAttribute(SystemTable->ConOut, EFI_TEXT_ATTR(EFI_RED,EFI_BLACK));
        SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Press any key to shutdown...");

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

    cfg_builder = CFGBuilder()
    cfg_builder.visit(tree)

    cfg_builder.print_linear_segments()
    cfg_builder.display_matrices()
    cfg_builder.visualize_cfg()
    cfg_builder.export_to_dot()


if __name__ == '__main__':
    main()