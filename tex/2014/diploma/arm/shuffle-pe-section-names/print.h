#ifndef PRINT_H
#define PRINT_H

#include "winnt.h"

void PrintHeader(IMAGE_NT_HEADERS *header);
void PrintSections(IMAGE_SECTION_HEADER *sections, int sectionCount);

#endif // PRINT_H
