from antlr4 import *
from UEFIParser import UEFIParser
from UEFIListener import UEFIListener
from UEFILexer import UEFILexer

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
    input_stream = InputStream(code)
    lexer = UEFILexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = UEFIParser(token_stream)

    # Получаем корень дерева разбора
    tree = parser.compilationUnit()

    # Создаем и регистрируем слушателя
    listener = UEFIListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()