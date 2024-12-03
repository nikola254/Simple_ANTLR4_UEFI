#include "efi.h"

// EFI Image Entry Point
EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
    (void)ImageHandle;	// Prevent compiler warning

    // Установка атрибутов вывода EFI_YELLOW - фоновый цвет EFI_GREEN - фон
    SystemTable->ConOut->SetAttribute(SystemTable->ConOut, 
            EFI_TEXT_ATTR(EFI_YELLOW,EFI_GREEN)); 

    // Очистка экрана (Функция очищает экран до заданного цвета фона)
    SystemTable->ConOut->ClearScreen(SystemTable->ConOut);
    // Вывод строки (Метод выводит строку на экран с использованием Unicode-символов)
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Hello, World!\r\n\r\n");
    
    // Изменение атрибутов вывода EFI_RED - фоновый цвет EFI_BLACK - фон
    SystemTable->ConOut->SetAttribute(SystemTable->ConOut, 
            EFI_TEXT_ATTR(EFI_RED,EFI_BLACK));
    // Вывод приглашения (Выводит сообщение о необходимости нажать клавишу для завершения работы.)
    SystemTable->ConOut->OutputString(SystemTable->ConOut, 
            u"Press any key to shutdown..."); 

    // Чтение клавиатурных вводов
    EFI_INPUT_KEY key;
    while (SystemTable->ConIn->ReadKeyStroke(SystemTable->ConIn, &key) != EFI_SUCCESS)
        ;
    
    // Завершение работы системы (Вызывает функцию сброса системы UEFI, которая приводит к завершению работы.)
    SystemTable->RuntimeServices->ResetSystem(EfiResetShutdown, EFI_SUCCESS, 0, NULL);

    // Возврат статуса выполнения
    return EFI_SUCCESS;
}
