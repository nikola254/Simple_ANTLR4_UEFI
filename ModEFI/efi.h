#ifndef EFI_H
#define EFI_H

#include <stdint.h>
#include <stddef.h> // NULL

#ifndef _UCHAR_H
typedef uint_least16_t char16_t;
#endif

// Common UEFI Data Types
typedef uint16_t    UINT16;
typedef uint32_t    UINT32;
typedef uint64_t    UINT64;
typedef uint64_t    UINTN;
typedef char16_t    CHAR16;
typedef void        VOID;

typedef UINTN       EFI_STATUS;
typedef VOID*       EFI_HANDLE;

#define IN
#define OUT
#define OPTIONAL
#define CONST const

#define EFIAPI __attribute__((ms_abi))
#define EFI_SUCCESS 0

// Определение EFI_TABLE_HEADER должно быть ПЕРЕД его использованием
typedef struct {
    UINT64  Signature;
    UINT32  Revision;
    UINT32  HeaderSize;
    UINT32  CRC32;
    UINT32  Reserved;
} EFI_TABLE_HEADER;

typedef struct EFI_SIMPLE_TEXT_INPUT_PROTOCOL EFI_SIMPLE_TEXT_INPUT_PROTOCOL;
typedef struct EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL;
typedef struct EFI_RUNTIME_SERVICES EFI_RUNTIME_SERVICES;
typedef struct EFI_BOOT_SERVICES EFI_BOOT_SERVICES;

// EFI Simple Text Input Protocol
typedef struct {
    UINT16  ScanCode;
    CHAR16  UnicodeChar;
} EFI_INPUT_KEY;

typedef EFI_STATUS (EFIAPI *EFI_INPUT_READ_KEY) (
    IN EFI_SIMPLE_TEXT_INPUT_PROTOCOL  *This, 
    OUT EFI_INPUT_KEY                   *Key
);

struct EFI_SIMPLE_TEXT_INPUT_PROTOCOL {
    void*               Reset;
    EFI_INPUT_READ_KEY  ReadKeyStroke;
    void*               WaitForKey;
};

// EFI Simple Text Output Protocol
typedef EFI_STATUS (EFIAPI *EFI_TEXT_STRING) (
    IN EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *This,
    IN CHAR16                          *String
);

typedef EFI_STATUS (EFIAPI *EFI_TEXT_SET_ATTRIBUTE) (
    IN EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *This,
    IN UINTN                           Attribute
);

typedef EFI_STATUS (EFIAPI *EFI_TEXT_CLEAR_SCREEN) (
    IN EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *This
);

struct EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL {
    void*                           Reset;
    EFI_TEXT_STRING                 OutputString;
    void*                           TestString;
    void*                           QueryMode;
    void*                           SetMode;
    EFI_TEXT_SET_ATTRIBUTE          SetAttribute;
    EFI_TEXT_CLEAR_SCREEN           ClearScreen;
    void*                           SetCursorPosition;
    void*                           EnableCursor;
    void*                           Mode;
};

// EFI Reset System
typedef enum {
    EfiResetCold,
    EfiResetWarm,
    EfiResetShutdown,
    EfiResetPlatformSpecific
} EFI_RESET_TYPE;

typedef VOID (EFIAPI *EFI_RESET_SYSTEM) (
   IN EFI_RESET_TYPE ResetType,      
   IN EFI_STATUS     ResetStatus,   
   IN UINTN          DataSize,     
   IN VOID           *ResetData OPTIONAL
);

// EFI Runtime Services
struct EFI_RUNTIME_SERVICES {
    EFI_TABLE_HEADER Hdr;
    void* GetTime;
    void* SetTime;
    void* GetWakeupTime;
    void* SetWakeupTime;
    void* SetVirtualAddressMap;
    void* ConvertPointer;
    void* GetVariable;
    void* GetNextVariableName;
    void* SetVariable;
    void* GetNextHighMonotonicCount;
    EFI_RESET_SYSTEM ResetSystem;
    void* UpdateCapsule;
    void* QueryCapsuleCapabilities;
    void* QueryVariableInfo;
};

// EFI Boot Services
typedef EFI_STATUS (EFIAPI *EFI_BOOT_SERVICES_STALL)(UINTN Microseconds);

struct EFI_BOOT_SERVICES {
    EFI_TABLE_HEADER Hdr;
    EFI_BOOT_SERVICES_STALL Stall;
    void* ExitBootServices;
    void* AllocatePool;
    void* FreePool;
    void* CreateEvent;
    void* SetTimer;
    void* WaitForEvent;
    void* SignalEvent;
    void* CloseEvent;
    void* InstallProtocolInterface;
    void* ReinstallProtocolInterface;
    void* UninstallProtocolInterface;
    void* HandleProtocol;
    void* RegisterProtocolNotify;
    void* LocateHandle;
    void* LocateDevicePath;
    void* InstallConfigurationTable;
    void* LoadImage;
    void* StartImage;
    void* Exit;
    void* UnloadImage;
};

// EFI System Table
typedef struct {
    EFI_TABLE_HEADER                Hdr;
    void*                           FirmwareVendor;
    UINT32                          FirmwareRevision;
    void*                           ConsoleInHandle;
    EFI_SIMPLE_TEXT_INPUT_PROTOCOL 	*ConIn;
    void*                           ConsoleOutHandle;
    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *ConOut;
    void*                           StandardErrorHandle;
    void*                           StdErr;
    EFI_RUNTIME_SERVICES            *RuntimeServices;
    EFI_BOOT_SERVICES               *BootServices;
    UINTN                           NumberOfTableEntries;
    void*                           ConfigurationTable;
} EFI_SYSTEM_TABLE;

#endif // EFI_H
