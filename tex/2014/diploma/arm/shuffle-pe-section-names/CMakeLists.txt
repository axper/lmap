cmake_minimum_required (VERSION 2.6)
project (program)

set (EXTRA_LIBS )

add_executable (program main.c print.c shuffle.c)
target_link_libraries (program ${EXTRA_LIBS})
