import re

# Исходный код UEFI
uefi_code = """
EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
    (void)ImageHandle;
    SystemTable->ConOut->SetAttribute(SystemTable->ConOut, EFI_TEXT_ATTR(EFI_YELLOW,EFI_GREEN)); 
    SystemTable->ConOut->ClearScreen(SystemTable->ConOut);
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Hello, World!\\r\\n\\r\\n");
    SystemTable->ConOut->SetAttribute(SystemTable->ConOut, EFI_TEXT_ATTR(EFI_RED,EFI_BLACK));
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Press any key to shutdown...");
    EFI_INPUT_KEY key;
    while (SystemTable->ConIn->ReadKeyStroke(SystemTable->ConIn, &key) != EFI_SUCCESS)
        ;
    SystemTable->RuntimeServices->ResetSystem(EfiResetShutdown, EFI_SUCCESS, 0, NULL);
    return EFI_SUCCESS;
}
"""

# 1. Извлекаем вызовы функций (но исключаем сам `efi_main`)
function_calls = re.findall(r'\b([A-Za-z_]+)\s*\(', uefi_code)
function_calls = sorted(set(filter(lambda f: f != "efi_main" and not f.startswith("EFI_"), function_calls)))

# 2. Убираем зарезервированные слова (`while` → `loop_while`)
function_calls = ["loop_while" if f == "while" else f for f in function_calls]

# 3. Создаём ANTLR-грамматику
antlr_grammar = "grammar CallTree;\n\n"

# Основное правило (efi_main без дублирования)
calls_rule = " ".join([f"ENTER_{call} {call} EXIT_{call}" for call in function_calls])
antlr_grammar += f"start : efi_main ;\n\n"
antlr_grammar += f"efi_main : ENTER_efi_main {calls_rule} EXIT_efi_main ;\n\n"

# Генерируем правила для вызванных функций
defined_functions = set()
for call in function_calls:
    if call not in defined_functions:
        antlr_grammar += f"{call} : ENTER_{call} EXIT_{call} ;\n"
        defined_functions.add(call)

# Добавляем ENTER и EXIT (без дублирующихся правил)
antlr_grammar += "\n// ENTER и EXIT события\n"
antlr_grammar += "ENTER_efi_main : '[ENTER] efi_main';\n"
antlr_grammar += "EXIT_efi_main : '[EXIT] efi_main';\n"

for call in defined_functions:
    antlr_grammar += f"ENTER_{call} : '[ENTER] {call}';\n"
    antlr_grammar += f"EXIT_{call} : '[EXIT] {call}';\n"

# Записываем исправленную грамматику в файл
with open("CallTree.g4", "w") as f:
    f.write(antlr_grammar)

print("ANTLR-грамматика без дублирования `efi_main` успешно сгенерирована!")
