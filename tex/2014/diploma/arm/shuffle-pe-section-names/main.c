#include <stdio.h>
#include <stdlib.h> // srand()
#include <time.h> // time(NULL) for srand()

#include "winnt.h"
#include "print.h"
#include "shuffle.h"


int CheckMagicDos(IMAGE_DOS_HEADER *dosHeader)
{
	if (dosHeader->e_magic != 0x5A4D) {
		return 1;
	} else {
		return 0;
	}
}

int CheckMagicPe(IMAGE_NT_HEADERS *header)
{
	if (header->Signature != 0x00004550) {
		return 1;
	} else {
		return 0;
	}
}

int ReadDosHeader(FILE *file, IMAGE_DOS_HEADER *dosHeader)
{
	if (fread(dosHeader, sizeof(IMAGE_DOS_HEADER), 1, file) != 1) {
		if (feof(file) != 0) {
			printf("Error: End of file reached when reading DOS header\n");
			return 1;
		}
		perror("Error: Could not read DOS header");
		return 2;
	}
	if (CheckMagicDos(dosHeader) != 0) {
		printf("Error: DOS magic number does not match."
		       "Either file is damaged or is not a Windows .exe\n");
		return 3;
	}

	return 0;
}

int ReadPeHeader(FILE *file, IMAGE_NT_HEADERS *header, int offset)
{
	if (fseek(file, offset, SEEK_SET) != 0) {
		perror("Error: Could not seek to e_lfanew");
		return 1;
	}

	if (fread(header, sizeof(IMAGE_NT_HEADERS), 1, file) != 1) {
		if (feof(file) != 0) {
			printf("Error: End of file reached when reading PE header\n");
			return 2;
		}
		perror("Error: Could not read PE header");
		return 3;
	}

	if (CheckMagicPe(header) != 0) {
		printf("Error: PE magic number does not match."
			   "Either file is damaged or is not a Windows .exe\n");
		return 4;
	}

	return 0;
}

int OpenFile(FILE **file, const char *filename)
{
	*file = fopen(filename, "r+");

	if (*file == NULL) {
		perror("Error: Could not open the file");
		return 1;
	}

	printf("########################################################\n");
	printf("File: %s\n", filename);

	return 0;
}

int CloseFile(FILE *file)
{
	if (fclose(file) != 0) {
		perror("Error: Could not close file");
		return 1;
	}

	return 0;
}

int ReadSections(FILE *file, IMAGE_SECTION_HEADER sections[], size_t sectionCount)
{
	if (fread(sections, sizeof(IMAGE_SECTION_HEADER), sectionCount, file) != sectionCount) {
		perror("Error: Could not read sections");
		return 1;
	}

	return 0;
}

void ReadSectionNames(IMAGE_SECTION_HEADER sections[], uint8_t **names, int sectionCount)
{
	int i;
	for (i = 0; i != sectionCount; i++) {
		names[ i ] = sections[ i ].Name;
	}
}

void PrintNames(unsigned char *names[], int sectionCount)
{
	int i;
	for (i = 0; i != sectionCount; i++) {
		printf("[%s] ", (char *)names[ i ]);
	}
	printf("\n");
}

int WriteNames(FILE *file, int offset, unsigned char **names, int sectionCount)
{
	int i;

	if (fseek(file, offset, SEEK_SET) != 0) {
		perror("Error: Could not seek to beginning of first section name");
		return 1;
	}

	for (i = 0; i != sectionCount; i++) {
		if (fwrite(names[ i ], IMAGE_SIZEOF_SHORT_NAME, 1, file) != 1) {
			if (feof(file) != 0) {
				printf("Error: End of file reached when writing section name\n");
				return 1;
			}
			perror("Error: Could not write section name");
			return 1;
		}

		if (fseek(file, sizeof(IMAGE_SECTION_HEADER) - IMAGE_SIZEOF_SHORT_NAME, SEEK_CUR) != 0) {
			perror("Error: Could not seek to beginning of a section name");
			return 1;
		}
	}

	return 0;
}

int ReadFile(FILE *file)
{
	IMAGE_DOS_HEADER dosHeader;
	IMAGE_NT_HEADERS header;
	int sectionCount;


	if (ReadDosHeader(file, &dosHeader)) {
		return 1;
	}

	if (ReadPeHeader(file, &header, dosHeader.e_lfanew)) {
		return 1;
	}

	PrintHeader(&header);


	sectionCount = header.FileHeader.NumberOfSections;
	IMAGE_SECTION_HEADER sections[ sectionCount ];

	if (ReadSections(file, sections, sectionCount)) {
		return 1;
	}

	PrintSections(sections, sectionCount);


	unsigned char *names[ sectionCount ];
	ReadSectionNames(sections, names, sectionCount);

	if (Shuffle(names, sectionCount)) {
		return 1;
	}

	printf("New order: ");
	PrintNames(names, sectionCount);

	if (WriteNames(file, dosHeader.e_lfanew + sizeof(IMAGE_NT_HEADERS), names, sectionCount)) {
		return 1;
	}

	return 0;
}

int main(int argc, char **argv)
{
	srand(time(NULL));

	if (argc < 2) {
		printf("Error: Please specify an .exe file(s)\n");
		return 1;
	}

	int i;
	for (i = 1; i != argc; i++) {
		FILE *file;

		if (OpenFile(&file, argv[ i ])) {
			return 2;
		}

		if (ReadFile(file)) {
			return 3;
		}

		if (CloseFile(file)) {
			return 4;
		}
	}

	return 0;
}
