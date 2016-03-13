#include <stdio.h>
#include "winnt.h"

#include "print.h"


static void Print(const char *name, uint32_t number)
{
	printf("%s: 0x%08X", name, number);
}

static void PrintFileHeaderMachine(uint16_t machine)
{
	printf(" (");
	switch (machine) {
	case IMAGE_FILE_MACHINE_UNKNOWN:
		printf("UNKNOWN");
		break;
	case IMAGE_FILE_MACHINE_I386:
		printf("I386");
		break;
	case IMAGE_FILE_MACHINE_R3000:
		printf("R3000");
		break;
	case IMAGE_FILE_MACHINE_R4000:
		printf("R4000");
		break;
	case IMAGE_FILE_MACHINE_R10000:
		printf("R10000");
		break;
	case IMAGE_FILE_MACHINE_WCEMIPSV2:
		printf("WCEMIPSV2");
		break;
	case IMAGE_FILE_MACHINE_ALPHA:
		printf("ALPHA");
		break;
	case IMAGE_FILE_MACHINE_SH3:
		printf("SH3");
		break;
	case IMAGE_FILE_MACHINE_SH3DSP:
		printf("SH3DSP");
		break;
	case IMAGE_FILE_MACHINE_SH3E:
		printf("SH3E");
		break;
	case IMAGE_FILE_MACHINE_SH4:
		printf("SH4");
		break;
	case IMAGE_FILE_MACHINE_SH5:
		printf("SH5");
		break;
	case IMAGE_FILE_MACHINE_ARM:
		printf("ARM");
		break;
	case IMAGE_FILE_MACHINE_ARMV7:
		printf("ARMV7");
		break;
	case IMAGE_FILE_MACHINE_THUMB:
		printf("THUMB");
		break;
	case IMAGE_FILE_MACHINE_AM33:
		printf("AM33");
		break;
	case IMAGE_FILE_MACHINE_POWERPC:
		printf("POWERPC");
		break;
	case IMAGE_FILE_MACHINE_POWERPCFP:
		printf("POWERPCFP");
		break;
	case IMAGE_FILE_MACHINE_IA64:
		printf("IA64");
		break;
	case IMAGE_FILE_MACHINE_MIPS16:
		printf("MIPS16");
		break;
	case IMAGE_FILE_MACHINE_ALPHA64:
		printf("ALPHA64");
		break;
	case IMAGE_FILE_MACHINE_MIPSFPU:
		printf("MIPSFPU");
		break;
	case IMAGE_FILE_MACHINE_MIPSFPU16:
		printf("MIPSFPU16");
		break;
	case IMAGE_FILE_MACHINE_TRICORE:
		printf("TRICORE");
		break;
	case IMAGE_FILE_MACHINE_CEF:
		printf("CEF");
		break;
	case IMAGE_FILE_MACHINE_EBC:
		printf("EBC");
		break;
	case IMAGE_FILE_MACHINE_AMD64:
		printf("AMD64");
		break;
	case IMAGE_FILE_MACHINE_M32R:
		printf("M32R");
		break;
	case IMAGE_FILE_MACHINE_CEE:
		printf("CEE");
		break;
	default:
		printf("invalid machine");
		break;
	}
	printf(")\n");
}

static void PrintFileHeaderCharacteristics(int characteristics)
{
	printf(" (");
	if (IMAGE_FILE_RELOCS_STRIPPED & characteristics) {
		printf("RELOCS_STRIPPED ");
	}
	if (IMAGE_FILE_EXECUTABLE_IMAGE & characteristics) {
		printf("EXECUTABLE_IMAGE ");
	}
	if (IMAGE_FILE_LINE_NUMS_STRIPPED & characteristics) {
		printf("LINE_NUMS_STRIPPED ");
	}
	if (IMAGE_FILE_LOCAL_SYMS_STRIPPED & characteristics) {
		printf("LOCAL_SYMS_STRIPPED ");
	}
	if (IMAGE_FILE_AGGRESIVE_WS_TRIM & characteristics) {
		printf("AGGRESIVE_WS_TRIM ");
	}
	if (IMAGE_FILE_LARGE_ADDRESS_AWARE & characteristics) {
		printf("LARGE_ADDRESS_AWARE ");
	}
	if (IMAGE_FILE_BYTES_REVERSED_LO & characteristics) {
		printf("BYTES_REVERSED_LO ");
	}
	if (IMAGE_FILE_32BIT_MACHINE & characteristics) {
		printf("32BIT_MACHINE ");
	}
	if (IMAGE_FILE_DEBUG_STRIPPED & characteristics) {
		printf("DEBUG_STRIPPED ");
	}
	if (IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP & characteristics) {
		printf("REMOVABLE_RUN_FROM_SWAP ");
	}
	if (IMAGE_FILE_NET_RUN_FROM_SWAP & characteristics) {
		printf("NET_RUN_FROM_SWAP ");
	}
	if (IMAGE_FILE_SYSTEM & characteristics) {
		printf("SYSTEM ");
	}
	if (IMAGE_FILE_DLL & characteristics) {
		printf("DLL ");
	}
	if (IMAGE_FILE_UP_SYSTEM_ONLY & characteristics) {
		printf("UP_SYSTEM_ONLY ");
	}
	if (IMAGE_FILE_BYTES_REVERSED_HI & characteristics) {
		printf("BYTES_REVERSED_HI ");
	}
	printf(")\n");
}

static void PrintSubsystem(int subsystem)
{
	printf(" (");
	switch (subsystem) {
	case IMAGE_SUBSYSTEM_UNKNOWN:
		printf("UNKNOWN ");
		break;
	case IMAGE_SUBSYSTEM_NATIVE:
		printf("NATIVE ");
		break;
	case IMAGE_SUBSYSTEM_WINDOWS_GUI:
		printf("WINDOWS_GUI ");
		break;
	case IMAGE_SUBSYSTEM_WINDOWS_CUI:
		printf("WINDOWS_CUI ");
		break;
	case IMAGE_SUBSYSTEM_OS2_CUI:
		printf("OS2_CUI ");
		break;
	case IMAGE_SUBSYSTEM_POSIX_CUI:
		printf("POSIX_CUI ");
		break;
	case IMAGE_SUBSYSTEM_NATIVE_WINDOWS:
		printf("NATIVE_WINDOWS ");
		break;
	case IMAGE_SUBSYSTEM_WINDOWS_CE_GUI:
		printf("WINDOWS_CE_GUI ");
		break;
	case IMAGE_SUBSYSTEM_EFI_APPLICATION:
		printf("EFI_APPLICATION ");
		break;
	case IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER:
		printf("EFI_BOOT_SERVICE_DRIVER ");
		break;
	case IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER:
		printf("EFI_RUNTIME_DRIVER ");
		break;
	case IMAGE_SUBSYSTEM_EFI_ROM:
		printf("EFI_ROM ");
		break;
	case IMAGE_SUBSYSTEM_XBOX:
		printf("XBOX ");
		break;
	case IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION:
		printf("WINDOWS_BOOT_APPLICATION ");
		break;
	default:
		printf("invalid subsystem");
		break;
	}
	printf(")\n");
}

static void PrintDllCharacteristics(int dllCharacteristics)
{
	printf(" (");
	if (IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE & dllCharacteristics) {
		printf("DYNAMIC_BASE ");
	}
	if (IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY & dllCharacteristics) {
		printf("FORCE_INTEGRITY ");
	}
	if (IMAGE_DLLCHARACTERISTICS_NX_COMPAT & dllCharacteristics) {
		printf("NX_COMPAT ");
	}
	if (IMAGE_DLLCHARACTERISTICS_NO_ISOLATION & dllCharacteristics) {
		printf("NO_ISOLATION ");
	}
	if (IMAGE_DLLCHARACTERISTICS_NO_SEH & dllCharacteristics) {
		printf("NO_SEH ");
	}
	if (IMAGE_DLLCHARACTERISTICS_NO_BIND & dllCharacteristics) {
		printf("NO_BIND ");
	}
	if (IMAGE_DLLCHARACTERISTICS_APPCONTAINER & dllCharacteristics) {
		printf("APPCONTAINER ");
	}
	if (IMAGE_DLLCHARACTERISTICS_WDM_DRIVER & dllCharacteristics) {
		printf("WDM_DRIVER ");
	}
	if (IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE & dllCharacteristics) {
		printf("TERMINAL_SERVER_AWARE ");
	}
	printf(")\n");
}

static void PrintDataDirectory(int dataDirectory)
{
	printf(" (");
	switch (dataDirectory) {
	case IMAGE_DIRECTORY_ENTRY_EXPORT:
		printf("EXPORT ");
		break;
	case IMAGE_DIRECTORY_ENTRY_IMPORT:
		printf("IMPORT ");
		break;
	case IMAGE_DIRECTORY_ENTRY_RESOURCE:
		printf("RESOURCE ");
		break;
	case IMAGE_DIRECTORY_ENTRY_EXCEPTION:
		printf("EXCEPTION ");
		break;
	case IMAGE_DIRECTORY_ENTRY_SECURITY:
		printf("SECURITY ");
		break;
	case IMAGE_DIRECTORY_ENTRY_BASERELOC:
		printf("BASERELOC ");
		break;
	case IMAGE_DIRECTORY_ENTRY_DEBUG:
		printf("DEBUG ");
		break;
	case IMAGE_DIRECTORY_ENTRY_ARCHITECTURE:
		printf("ARCHITECTURE ");
		break;
	case IMAGE_DIRECTORY_ENTRY_GLOBALPTR:
		printf("GLOBALPTR ");
		break;
	case IMAGE_DIRECTORY_ENTRY_TLS:
		printf("TLS ");
		break;
	case IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG:
		printf("LOAD_CONFIG ");
		break;
	case IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT:
		printf("BOUND_IMPORT ");
		break;
	case IMAGE_DIRECTORY_ENTRY_IAT:
		printf("IAT ");
		break;
	case IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT:
		printf("DELAY_IMPORT ");
		break;
	case IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR:
		printf("COM_DESCRIPTOR ");
		break;
	default:
		printf("invalid data directory");
		break;
	}
	printf(")\n");
}

static void PrintSectionCharacteristics(int sectionCharacteristics)
{
	int unusedBytesMask = 0x00012416;
	int align = sectionCharacteristics & IMAGE_SCN_ALIGN_MASK;

	printf(" (");
	if (sectionCharacteristics & unusedBytesMask) {
		printf("WARNING: unused bytes used!");
	}

	if (IMAGE_SCN_TYPE_NO_PAD & sectionCharacteristics) {
		printf("TYPE_NO_PAD ");
	}
	if (IMAGE_SCN_CNT_CODE & sectionCharacteristics) {
		printf("CNT_CODE ");
	}
	if (IMAGE_SCN_CNT_INITIALIZED_DATA & sectionCharacteristics) {
		printf("CNT_INITIALIZED_DATA ");
	}
	if (IMAGE_SCN_CNT_UNINITIALIZED_DATA & sectionCharacteristics) {
		printf("CNT_UNINITIALIZED_DATA ");
	}
	if (IMAGE_SCN_LNK_OTHER & sectionCharacteristics) {
		printf("LNK_OTHER ");
	}
	if (IMAGE_SCN_LNK_INFO & sectionCharacteristics) {
		printf("LNK_INFO ");
	}
	if (IMAGE_SCN_LNK_REMOVE & sectionCharacteristics) {
		printf("LNK_REMOVE ");
	}
	if (IMAGE_SCN_LNK_COMDAT & sectionCharacteristics) {
		printf("LNK_COMDAT ");
	}
	if (IMAGE_SCN_NO_DEFER_SPEC_EXC & sectionCharacteristics) {
		printf("NO_DEFER_SPEC_EXC ");
	}
	if (IMAGE_SCN_GPREL & sectionCharacteristics) {
		printf("GPREL ");
	}
	if (IMAGE_SCN_MEM_FARDATA & sectionCharacteristics) {
		printf("MEM_FARDATA ");
	}
	if (IMAGE_SCN_MEM_PURGEABLE & sectionCharacteristics) {
		printf("MEM_PURGEABLE ");
	}
	if (IMAGE_SCN_MEM_16BIT & sectionCharacteristics) {
		printf("MEM_16BIT ");
	}
	if (IMAGE_SCN_MEM_LOCKED & sectionCharacteristics) {
		printf("MEM_LOCKED ");
	}
	if (IMAGE_SCN_MEM_PRELOAD & sectionCharacteristics) {
		printf("MEM_PRELOAD ");
	}
	if (IMAGE_SCN_LNK_NRELOC_OVFL & sectionCharacteristics) {
		printf("LNK_NRELOC_OVFL ");
	}
	if (IMAGE_SCN_MEM_DISCARDABLE & sectionCharacteristics) {
		printf("MEM_DISCARDABLE ");
	}
	if (IMAGE_SCN_MEM_NOT_CACHED & sectionCharacteristics) {
		printf("MEM_NOT_CACHED ");
	}
	if (IMAGE_SCN_MEM_NOT_PAGED & sectionCharacteristics) {
		printf("MEM_NOT_PAGED ");
	}
	if (IMAGE_SCN_MEM_SHARED & sectionCharacteristics) {
		printf("MEM_SHARED ");
	}
	if (IMAGE_SCN_MEM_EXECUTE & sectionCharacteristics) {
		printf("MEM_EXECUTE ");
	}
	if (IMAGE_SCN_MEM_READ & sectionCharacteristics) {
		printf("MEM_READ ");
	}
	if (IMAGE_SCN_MEM_WRITE & sectionCharacteristics) {
		printf("MEM_WRITE ");
	}
	if (IMAGE_SCN_SCALE_INDEX & sectionCharacteristics) {
		printf("SCALE_INDEX ");
	}

	switch (align) {
	case IMAGE_SCN_ALIGN_1BYTES:
		printf("ALIGN_1BYTES ");
		break;
	case IMAGE_SCN_ALIGN_2BYTES:
		printf("ALIGN_2BYTES ");
		break;
	case IMAGE_SCN_ALIGN_4BYTES:
		printf("ALIGN_4BYTES ");
		break;
	case IMAGE_SCN_ALIGN_8BYTES:
		printf("ALIGN_8BYTES ");
		break;
	case IMAGE_SCN_ALIGN_16BYTES:
		printf("ALIGN_16BYTES ");
		break;
	case IMAGE_SCN_ALIGN_32BYTES:
		printf("ALIGN_32BYTES ");
		break;
	case IMAGE_SCN_ALIGN_64BYTES:
		printf("ALIGN_64BYTES ");
		break;
	case IMAGE_SCN_ALIGN_128BYTES:
		printf("ALIGN_128BYTES ");
		break;
	case IMAGE_SCN_ALIGN_256BYTES:
		printf("ALIGN_256BYTES ");
		break;
	case IMAGE_SCN_ALIGN_512BYTES:
		printf("ALIGN_512BYTES ");
		break;
	case IMAGE_SCN_ALIGN_1024BYTES:
		printf("ALIGN_1024BYTES ");
		break;
	case IMAGE_SCN_ALIGN_2048BYTES:
		printf("ALIGN_2048BYTES ");
		break;
	case IMAGE_SCN_ALIGN_4096BYTES:
		printf("ALIGN_4096BYTES ");
		break;
	case IMAGE_SCN_ALIGN_8192BYTES:
		printf("ALIGN_8192BYTES ");
		break;
	default:
		printf("invalid alignment");
		break;
	}
	printf(")\n");
}

void PrintHeader(IMAGE_NT_HEADERS *header)
{
	int i;

	//printf("\tSignature:\n");
	//Print("Signature", header->Signature);

	printf("\tFileHeader:");
	Print("\nMachine", header->FileHeader.Machine);
	PrintFileHeaderMachine(header->FileHeader.Machine);
	Print("NumberOfSections", header->FileHeader.NumberOfSections);
	Print("\nTimeDateStamp", header->FileHeader.TimeDateStamp);
	Print("\nPointerToSymbolTable", header->FileHeader.PointerToSymbolTable);
	Print("\nNumberOfSymbols", header->FileHeader.NumberOfSymbols);
	Print("\nSizeOfOptionalHeader", header->FileHeader.SizeOfOptionalHeader);
	Print("\nCharacteristics", header->FileHeader.Characteristics);
	PrintFileHeaderCharacteristics(header->FileHeader.Characteristics);

	printf("\tOptionalHeader:");
	Print("\nMagic", header->OptionalHeader.Magic);
	Print("\nMajorLinkerVersion", header->OptionalHeader.MajorLinkerVersion);
	Print("\nMinorLinkerVersion", header->OptionalHeader.MinorLinkerVersion);
	Print("\nSizeOfCode", header->OptionalHeader.SizeOfCode);
	Print("\nSizeOfInitializedData", header->OptionalHeader.SizeOfInitializedData);
	Print("\nSizeOfUninitializedData", header->OptionalHeader.SizeOfUninitializedData);
	Print("\nAddressOfEntryPoint", header->OptionalHeader.AddressOfEntryPoint);
	Print("\nBaseOfCode", header->OptionalHeader.BaseOfCode);
	Print("\nBaseOfData", header->OptionalHeader.BaseOfData);
	Print("\nImageBase", header->OptionalHeader.ImageBase);
	Print("\nSectionAlignment", header->OptionalHeader.SectionAlignment);
	Print("\nFileAlignment", header->OptionalHeader.FileAlignment);
	Print("\nMajorOperatingSystemVersion", header->OptionalHeader.MajorOperatingSystemVersion);
	Print("\nMinorOperatingSystemVersion", header->OptionalHeader.MinorOperatingSystemVersion);
	Print("\nMajorImageVersion", header->OptionalHeader.MajorImageVersion);
	Print("\nMinorImageVersion", header->OptionalHeader.MinorImageVersion);
	Print("\nMajorSubsystemVersion", header->OptionalHeader.MajorSubsystemVersion);
	Print("\nMinorSubsystemVersion", header->OptionalHeader.MinorSubsystemVersion);
	Print("\nWin32VersionValue", header->OptionalHeader.Win32VersionValue);
	Print("\nSizeOfImage", header->OptionalHeader.SizeOfImage);
	Print("\nSizeOfHeaders", header->OptionalHeader.SizeOfHeaders);
	Print("\nCheckSum", header->OptionalHeader.CheckSum);
	Print("\nSubsystem", header->OptionalHeader.Subsystem);
	PrintSubsystem(header->OptionalHeader.Subsystem);
	Print("DllCharacteristics", header->OptionalHeader.DllCharacteristics);
	PrintDllCharacteristics(header->OptionalHeader.DllCharacteristics);
	Print("SizeOfStackReserve", header->OptionalHeader.SizeOfStackReserve);
	Print("\nSizeOfStackCommit", header->OptionalHeader.SizeOfStackCommit);
	Print("\nSizeOfHeapReserve", header->OptionalHeader.SizeOfHeapReserve);
	Print("\nSizeOfHeapCommit", header->OptionalHeader.SizeOfHeapCommit);
	Print("\nLoaderFlags", header->OptionalHeader.LoaderFlags);
	Print("\nNumberOfRvaAndSizes", header->OptionalHeader.NumberOfRvaAndSizes);
	printf("\n");

	for (i = 0; i != IMAGE_NUMBEROF_DIRECTORY_ENTRIES; i++) {
		if (header->OptionalHeader.DataDirectory[ i ].VirtualAddress != 0 ||
			header->OptionalHeader.DataDirectory[ i ].Size != 0) {

			printf("\tDataDirectory %d:", i);
			PrintDataDirectory(i);
			Print("Addr", header->OptionalHeader.DataDirectory[ i ].VirtualAddress);
			Print("  Size", header->OptionalHeader.DataDirectory[ i ].Size);
			printf("\n");
		}
	}
}

static void PrintSection(IMAGE_SECTION_HEADER *section)
{
	printf("Name: %.8s", (char *)section->Name);
	Print("\nVirtualAddress", section->VirtualAddress);
	Print("\nSizeOfRawData", section->SizeOfRawData);
	Print("\nPointerToRawData", section->PointerToRawData);
	Print("\nPointerToRelocations", section->PointerToRelocations);
	Print("\nPointerToLinenumbers", section->PointerToLinenumbers);
	Print("\nNumberOfRelocations", section->NumberOfRelocations);
	Print("\nNumberOfLinenumbers", section->NumberOfLinenumbers);
	Print("\nCharacteristics", section->Characteristics);
	PrintSectionCharacteristics(section->Characteristics);
}

void PrintSections(IMAGE_SECTION_HEADER *sections, int sectionCount)
{
	int i;
	for (i = 0; i != sectionCount; i++) {
		printf("\tSection %d:\n", i);
		PrintSection(&sections[ i ]);
	}
}

