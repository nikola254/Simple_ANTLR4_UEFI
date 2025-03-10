# -*- coding: utf-8 -*-
import os
import subprocess
from antlr4 import *
from newCallTreeLexer import newCallTreeLexer
from newCallTreeParser import newCallTreeParser
from antlr4.tree.Trees import Trees

antlr_jar = "C:/antlr/antlr-4.9.2-complete.jar"  # Укажите свой путь к ANTLR
grammar_file = "UEFI.g4"

# ✅ Компиляция ANTLR-грамматики
def compile_antlr():
    print("🔄 Компиляция ANTLR-грамматики...")
    subprocess.run(f'java -jar {antlr_jar} -Dlanguage=Python3 {grammar_file}', shell=True)

# ✅ Разбор UEFI-кода
def parse_uefi_code(code):
    input_stream = InputStream(code)
    lexer = newCallTreeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = newCallTreeParser(stream)
    tree = parser.start()

    # Разбираем дерево
    functions, call_tree = extract_call_tree(tree, parser)
    generate_antlr_grammar(functions, call_tree)
    
def extract_function_calls(func_context, parser):
    calls = []
    for i in range(func_context.getChildCount()):
        child = func_context.getChild(i)
        if isinstance(child, parser.functionCall().__class__):  # ✅ Исправленный вариант
            calls.append(child.getChild(0).getText())  # Имя вызванной функции
    return calls


# ✅ Извлекаем дерево вызовов с ENTER и EXIT
def extract_call_tree(tree, parser):
    functions = []
    call_tree = {}

    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        if isinstance(child, newCallTreeParser.FunctionCallContext):
            func_name = child.getChild(0).getChild(1).getText()
            functions.append(func_name)
            call_tree[func_name] = extract_function_calls(child, parser)

    return functions, call_tree



# ✅ Генерируем грамматику вызовов ANTLR
def generate_antlr_grammar(functions, call_tree):
    grammar_lines = [
        "grammar CallTree;",
        "start : efi_main ;"
    ]

    for func in functions:
        call_list = call_tree.get(func)
        call_sequence = " ".join([f"ENTER_{c} {c} EXIT_{c}" for c in call_list]) if call_list else ""
        grammar_lines.append(f"{func} : ENTER_{func} {call_sequence} EXIT_{func} ;")

    grammar_lines.append("\n// Вход и выход")
    for func in functions:
        grammar_lines.append(f'ENTER_{func} : "[ENTER] {func}";')
        grammar_lines.append(f'EXIT_{func} : "[EXIT] {func}";')

    grammar_text = "\n".join(grammar_lines)

    # ✅ Сохраняем грамматику в файл
    with open("CallTree.g4", "w", encoding="utf-8") as f:
        f.write(grammar_text)

    print("\n🔹 Сгенерированная грамматика вызовов ANTLR:\n")
    print(grammar_text)

# ✅ Главная функция
if __name__ == "__main__":
    compile_antlr()

    # 📂 Исходный UEFI-код
    uefi_code = """
    #include "efi.h"

    EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
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

    parse_uefi_code(uefi_code)
