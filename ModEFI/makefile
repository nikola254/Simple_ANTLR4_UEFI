gcc:
	X86_64-w64-mingw32-gcc efi.c \
	-std=c17 \
	-Wall \
	-Wextra \
	-Wpedantic \
	-mno-red-zone \
	-ffreestanding \
	-fshort-wchar \
	-finstrument-functions \
	-nostdlib \
	-Wl,--subsystem,10 \
	-e efi_main \
	-o BOOTX64.EFI
