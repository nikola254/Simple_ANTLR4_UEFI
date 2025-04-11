#include "efi.h"

EFI_STATUS EFIAPI bootkit_hook(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
    TRACE_ENTER("bootkit_hook");
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Hook triggered: System compromised!\r\n");
    TRACE_EXIT("bootkit_hook");
    return EFI_SUCCESS;
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE ImageHandle, EFI_SYSTEM_TABLE *SystemTable) {
    TRACE_ENTER("efi_main");
    (void)ImageHandle;

    TRACE_ENTER("SetAttribute_YELLOW_GREEN");
    SystemTable->ConOut->SetAttribute(SystemTable->ConOut, EFI_TEXT_ATTR(EFI_YELLOW, EFI_GREEN));
    TRACE_EXIT("SetAttribute_YELLOW_GREEN");

    TRACE_ENTER("ClearScreen");
    SystemTable->ConOut->ClearScreen(SystemTable->ConOut);
    TRACE_EXIT("ClearScreen");

    TRACE_ENTER("OutputString_Hello");
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Hello, World!\r\n\r\n");
    TRACE_EXIT("OutputString_Hello");

    TRACE_ENTER("SetAttribute_RED_BLACK");
    SystemTable->ConOut->SetAttribute(SystemTable->ConOut, EFI_TEXT_ATTR(EFI_RED, EFI_BLACK));
    TRACE_EXIT("SetAttribute_RED_BLACK");

    TRACE_ENTER("OutputString_PressKey");
    SystemTable->ConOut->OutputString(SystemTable->ConOut, u"Press any key to shutdown...");
    TRACE_EXIT("OutputString_PressKey");

    EFI_INPUT_KEY key;
    TRACE_ENTER("WaitForKey");
    while (SystemTable->ConIn->ReadKeyStroke(SystemTable->ConIn, &key) != EFI_SUCCESS)
        ;
    TRACE_EXIT("WaitForKey");

    TRACE_ENTER("ConditionalBranch");
    if (key.ScanCode == 0xFF) {
        TRACE_ENTER("bootkit_hook_call");
        bootkit_hook(ImageHandle, SystemTable);
        TRACE_EXIT("bootkit_hook_call");
    } else {
        TRACE_ENTER("ResetSystem_call");
        SystemTable->RuntimeServices->ResetSystem(EfiResetShutdown, EFI_SUCCESS, 0, NULL);
        TRACE_EXIT("ResetSystem_call");
    }
    TRACE_EXIT("ConditionalBranch");

    TRACE_EXIT("efi_main");
    return EFI_SUCCESS;
}
