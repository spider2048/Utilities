CC := gcc
CFLAGS := -I /usr/include/python3.11/ -L /usr/lib/python3.11/config-3.11-x86_64-linux-gnu -l python3.11 --shared -fPIC

build:
	cython local.py -3 -o local.c
	$(CC) $(CFLAGS) local.c -o local.so
	strip -s local.so
	rm local.c