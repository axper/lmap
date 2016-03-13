#include <string.h> // memcpy()
#include <stdlib.h> // malloc(), free(), rand()
#include <stdio.h>

#include "winnt.h"


static int Swap(unsigned char *a, unsigned char *b)
{
	void *temp = malloc(IMAGE_SIZEOF_SHORT_NAME);
	if (temp == NULL) {
		perror("Could not allocate memory");
		return 1;
	}

	memcpy(temp, a, IMAGE_SIZEOF_SHORT_NAME);
	memcpy(a, b, IMAGE_SIZEOF_SHORT_NAME);
	memcpy(b, temp, IMAGE_SIZEOF_SHORT_NAME);
	free(temp);

	return 0;
}

int Shuffle(unsigned char * arr[], int length)
{
	int random;

	int i;
	for (i = 0; i != length; i++) {
		random = rand() % (length - i);

		if (Swap(arr[ length - 1 - i ], arr[ random ])) {
			return 1;
		}
	}

	return 0;
}

