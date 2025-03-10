#include "efi.h"

// Глобальный указатель на EFI System Table
EFI_SYSTEM_TABLE *gSystemTable;

// Обработчик входа в функцию
void __attribute__((no_instrument_function)) __cyg_profile_func_enter(void *this_func, void *call_site) {
    if (gSystemTable) {
        gSystemTable->ConOut->OutputString(gSystemTable->ConOut, u"Function entered\r\n");
    }
}

// Обработчик выхода из функции
void __attribute__((no_instrument_function)) __cyg_profile_func_exit(void *this_func, void *call_site) {
    if (gSystemTable) {
        gSystemTable->ConOut->OutputString(gSystemTable->ConOut, u"Function exited\r\n");
    }
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
    (void)ImageHandle;
    gSystemTable = SystemTable;
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"UEFI Bootloader started.\r\n");

    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Function efi_main() entered\r\n");

    char buffer[16];
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Enter input: ");
    SystemTable->BootServices->Stall(10000000); // Задержка 2 сек

    for (int i = 0; i < 16; i++) {
        buffer[i] = 'A';
        (void)buffer;
    }

    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Press any key to exit...\r\n");

    EFI_INPUT_KEY key;
SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Press 'r' to reboot, 's' to shutdown...\r\n");

    while (1) {
        if (SystemTable->ConIn->ReadKeyStroke(SystemTable->ConIn, &key) == EFI_SUCCESS) {
            if (key.UnicodeChar == 'r' || key.UnicodeChar == 'R') {
                SystemTable->RuntimeServices->ResetSystem(EfiResetCold, EFI_SUCCESS, 0, NULL);
            } else if (key.UnicodeChar == 's' || key.UnicodeChar == 'S') {
                SystemTable->RuntimeServices->ResetSystem(EfiResetShutdown, EFI_SUCCESS, 0, NULL);
            } else {
                SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Invalid key. Press 'r' to reboot, 's' to shutdown.\r\n");
            }
        }
    }


    return EFI_SUCCESS;
}
